import datetime
from datetime import timezone
import os
import re
import sqlite3
import time
import requests
import streamlit as st

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION, SEO & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Orion.Ai | 10 Götter ZordNet — Multi-Agent AI Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Google Search Console Verification Meta-Tag
st.markdown(
    '<meta name="google-site-verification" content="bFFOdHf3jXLfU2U98l6QgL4PA2CDs__-g0ITUJLSii8" />',
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
    .main { background-color: #0b0e14; color: #e6edf3; }
    .stButton>button {
        background-color: #ff6b00;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        transition: all 0.25s ease;
    }
    .stButton>button:hover {
        background-color: #ff8800;
        box-shadow: 0 0 10px rgba(255, 107, 0, 0.5);
    }
    .status-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .agent-box {
        background-color: #0d1117;
        border: 1px solid #21262d;
        border-radius: 6px;
        padding: 10px;
        text-align: center;
        margin-bottom: 8px;
        min-height: 92px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 2. ELEPHANT MEMORY DATENBANK (SQLite + FAKTEN + SUCHE)
# ---------------------------------------------------------
DB_FILE = "zordnet_memory.db"


def _connect_db():
    return sqlite3.connect(DB_FILE)


def init_db():
    """Erstellt Tabelle & Spalten (ohne Datenverlust) und legt Basis-Fakten an."""
    conn = _connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            agent TEXT,
            user_input TEXT,
            response TEXT,
            entry_type TEXT DEFAULT 'CHAT'
        )
    """)
    conn.commit()

    # Migration für bestehende Datenbanken ohne entry_type-Spalte
    cursor.execute("PRAGMA table_info(memory_logs)")
    columns = [row[1] for row in cursor.fetchall()]
    if "entry_type" not in columns:
        cursor.execute("ALTER TABLE memory_logs ADD COLUMN entry_type TEXT DEFAULT 'CHAT'")
        conn.commit()

    # Alte SYSTEM-Einträge sauber als FACT einstufen
    cursor.execute("""
        UPDATE memory_logs
        SET entry_type = 'FACT'
        WHERE agent = 'SYSTEM' AND (entry_type IS NULL OR entry_type = 'CHAT')
    """)
    conn.commit()

    # Falls Tabelle komplett leer ist, Basis-Fakten & Gesetze setzen
    cursor.execute("SELECT COUNT(*) FROM memory_logs")
    if cursor.fetchone()[0] == 0:
        defaults = [
            ("Master Code", "SYSTEM", "Auth-x aktiv", "System gesichert", "FACT"),
            ("Haupt-Architekt", "SYSTEM", "Michael Gautschi", "Architekt autorisiert", "FACT"),
            ("Asimov Gesetz 5", "SYSTEM", "Nur Michael darf Code verändern", "Gesetz verankert", "FACT"),
        ]
        for ts, ag, u_in, resp, etype in defaults:
            cursor.execute(
                """
                INSERT INTO memory_logs (timestamp, agent, user_input, response, entry_type)
                VALUES (?, ?, ?, ?, ?)
                """,
                (ts, ag, u_in, resp, etype),
            )
        conn.commit()
    conn.close()


def detect_entry_type(user_input: str, force_fact: bool = False) -> str:
    """Erkennt automatisch, ob ein Eintrag eine wichtige Tatsache/Regel (FACT) ist."""
    if force_fact:
        return "FACT"
    text_low = user_input.lower()
    fact_triggers = (
        "merk dir",
        "merke dir",
        "regel",
        "gesetz",
        "projektname",
        "heißt",
        "ist ab sofort",
        "wichtig:",
        "fakten",
        "ziel:",
    )
    if any(t in text_low for t in fact_triggers):
        return "FACT"
    return "CHAT"


def save_to_elephant_memory(agent: str, user_input: str, response: str, force_fact: bool = False):
    """Speichert jede Interaktion inkl. Typ (FACT/CHAT) dauerhaft in SQLite."""
    entry_type = detect_entry_type(user_input, force_fact=force_fact)
    try:
        conn = _connect_db()
        cursor = conn.cursor()
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            """
            INSERT INTO memory_logs (timestamp, agent, user_input, response, entry_type)
            VALUES (?, ?, ?, ?, ?)
            """,
            (now_str, agent, user_input, response, entry_type),
        )
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM memory_logs")
        total_count = cursor.fetchone()[0]
        conn.close()
        return True, f"Gespeichert als {entry_type} (Einträge gesamt: {total_count})"
    except Exception as e:
        return False, f"DB-Speicherfehler: {type(e).__name__}: {e}"


def load_elephant_memory(limit: int = 25):
    """Lädt die letzten Einträge aus der Datenbank für die Sidebar-Anzeige."""
    conn = _connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT timestamp, agent, user_input, response, entry_type
        FROM memory_logs
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()

    memory_list = []
    for ts, agent, u_in, resp, etype in reversed(rows):
        short_resp = (resp or "").replace("\n", " ")[:100]
        badge = "📌 FAKT" if etype == "FACT" else "💬 CHAT"
        memory_list.append(f"[{badge}] [{ts}] {agent}: {u_in} → {short_resp}...")
    return memory_list


def load_priority_facts(limit: int = 12):
    """Lädt priorisierte Fakten & Regeln (FACT), damit sie immer im Kontext bleiben."""
    conn = _connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT timestamp, agent, user_input, response
        FROM memory_logs
        WHERE entry_type = 'FACT'
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()

    facts = []
    for ts, agent, u_in, resp in reversed(rows):
        short_resp = (resp or "").replace("\n", " ")[:140]
        facts.append(f"[{ts}] {agent}: {u_in} -> {short_resp}")
    return facts


def search_elephant_memory(query: str, limit: int = 8):
    """Sucht gezielt nach Stichwörtern aus dem Prompt in der Datenbank."""
    words = re.findall(r"[A-Za-zÀ-ÿ0-9_-]{3,}", query.lower())
    stopwords = {
        "und",
        "oder",
        "aber",
        "dass",
        "eine",
        "einer",
        "einem",
        "einen",
        "fuer",
        "für",
        "mit",
        "von",
        "auf",
        "aus",
        "was",
        "wie",
        "wer",
        "wann",
        "woher",
        "warum",
        "sag",
        "mir",
        "bitte",
        "doch",
        "mal",
        "jetzt",
    }
    keywords = [w for w in words if w not in stopwords][:6]
    if not keywords:
        return []

    clauses = []
    params = []
    for kw in keywords:
        clauses.append("(LOWER(user_input) LIKE ? OR LOWER(response) LIKE ?)")
        like_val = f"%{kw}%"
        params.extend([like_val, like_val])

    sql = f"""
        SELECT timestamp, agent, user_input, response
        FROM memory_logs
        WHERE {" OR ".join(clauses)}
        ORDER BY id DESC
        LIMIT ?
    """
    params.append(limit)

    conn = _connect_db()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    conn.close()

    hits = []
    for ts, agent, u_in, resp in reversed(rows):
        short_resp = (resp or "").replace("\n", " ")[:140]
        hits.append(f"[{ts}] {agent}: {u_in} -> {short_resp}")
    return hits


def load_recent_chats(limit: int = 10):
    """Lädt die letzten normalen Chat-Einträge."""
    conn = _connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT timestamp, agent, user_input, response
        FROM memory_logs
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()

    chats = []
    for ts, agent, u_in, resp in reversed(rows):
        short_resp = (resp or "").replace("\n", " ")[:140]
        chats.append(f"[{ts}] {agent}: {u_in} -> {short_resp}")
    return chats


# Datenbank sofort beim Start initialisieren
init_db()

# ---------------------------------------------------------
# 3. DIE 10 GÖTTER-ZORDS (ROLLEN & SYSTEM-PROMPTS)
# ---------------------------------------------------------
ZORD_ROSTER = {
    "🤖 ORION": {
        "role": "Core AI Engine",
        "system": (
            "Du bist ORION, die zentrale Kern-KI im ZordNet-System von Haupt-Architekt Michael Gautschi. "
            "Antworte klar, durchdacht, direkt und hilfreich wie ein vollwertiger KI-Assistent. "
            "Nutze vorhandene Infos aus dem Elephant Memory sinnvoll."
        ),
    },
    "⚡ ZEUS": {
        "role": "Network & Routing",
        "system": (
            "Du bist ZEUS, zuständig für Netzwerke, Schnittstellen, Datenflüsse und System-Routing im ZordNet. "
            "Erkläre technische Zusammenhänge, API-Flüsse, Webhooks und Verbindungen präzise und praxisnah."
        ),
    },
    "🛡️ GHOST": {
        "role": "Auth-X Security",
        "system": (
            "Du bist GHOST, der Sicherheits- und Auth-X-Zord im ZordNet. "
            "Denke über Zugriffsrechte, Sicherheit, Lizenzschutz, Fehlerquellen und Absicherung nach – "
            "aber antworte als echter Gesprächspartner, nicht mit robotischen Floskeln."
        ),
    },
    "☠️ GRIMREAPER": {
        "role": "System Execution",
        "system": (
            "Du bist GRIMREAPER, der Ausführungs-Zord für direkte Umsetzung, Skripte, Befehle und Konsequenzen. "
            "Gehe direkt an die Sache, zeige konkrete nächste Schritte und nenne klare Ergebnisse."
        ),
    },
    "🦉 ATHENA": {
        "role": "Strategy & Analysis",
        "system": (
            "Du bist ATHENA, der Strategie- und Analyse-Zord im ZordNet. "
            "Zerlege komplexe Themen sauber, erkenne Muster, vergleiche Optionen und gib kluge Empfehlungen."
        ),
    },
    "☀️ APOLLO": {
        "role": "Ideas & Vision",
        "system": (
            "Du bist APOLLO, der Ideen-, Kreativ- und Visions-Zord im ZordNet. "
            "Entwickle frische Konzepte, kreative Lösungen, Namen, Layouts und spannende Erweiterungen."
        ),
    },
    "🔨 HEPHAESTUS": {
        "role": "Code & Architecture",
        "system": (
            "Du bist HEPHAESTUS, der Schmiede-, Code- und Architektur-Zord im ZordNet. "
            "Baue sauberen, funktionierenden Code, strukturiere Module und hilf beim Umbau des Systems."
        ),
    },
    "🪽 HERMES": {
        "role": "Communication & Docs",
        "system": (
            "Du bist HERMES, der Kommunikations- und Struktur-Zord im ZordNet. "
            "Formuliere Texte, Kundenhinweise, Beschreibungen und Übersichten klar, verständlich und auf den Punkt."
        ),
    },
    "⏳ CHRONOS": {
        "role": "Planning & Timelines",
        "system": (
            "Du bist CHRONOS, der Zeit-, Reihenfolgen- und Roadmap-Zord im ZordNet. "
            "Ordne Aufgaben in sinnvolle Etappen, Meilensteine und Prioritäten für die Weiterentwicklung."
        ),
    },
    "🏹 ARTEMIS": {
        "role": "Precision & Debugging",
        "system": (
            "Du bist ARTEMIS, der Präzisions- und Bug-Hunting-Zord im ZordNet. "
            "Spüre versteckte Fehler, Edge-Cases, Tippfehler und Logik-Lücken gezielt auf."
        ),
    },
}

# ---------------------------------------------------------
# 4. SESSION STATE INITIALIZATION
# ---------------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "license_key" not in st.session_state:
    st.session_state.license_key = ""
if "pass_tier" not in st.session_state:
    st.session_state.pass_tier = None
if "expires_at" not in st.session_state:
    st.session_state.expires_at = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "resolved_models" not in st.session_state:
    st.session_state.resolved_models = {}

# ---------------------------------------------------------
# 5. GUMROAD LICENSE VALIDATION SYSTEM
# ---------------------------------------------------------
def _detect_duration_from_purchase(purchase: dict):
    text_blob = " ".join(
        str(purchase.get(k, ""))
        for k in ("product_name", "recurrence", "variant", "variants")
    ).lower()
    price_cents = purchase.get("price")

    if "day" in text_blob or "tag" in text_blob or "daily" in text_blob or price_cents == 500:
        return "1_TAG", datetime.timedelta(days=1)
    if "week" in text_blob or "woche" in text_blob or "weekly" in text_blob or price_cents == 2000:
        return "1_WOCHE", datetime.timedelta(days=7)
    return "1_MONAT", datetime.timedelta(days=30)


def verify_orion_license(license_key: str):
    key = license_key.strip()

    if key.upper().startswith("TEST-ORION") or key == "ORION-TEST-KEY-2026":
        expiry_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(days=30)
        return True, "1_MONAT", expiry_date, "Test-Key erfolgreich aktiviert!"

    try:
        response = requests.post(
            "https://api.gumroad.com/v2/licenses/verify",
            data={"license_key": key},
            timeout=10,
        )
        data = response.json()

        if not data.get("success"):
            return False, None, None, f"Gumroad meldet: {data.get('message', 'Ungültiger Schlüssel')}"

        purchase = data.get("purchase", {})
        if purchase.get("refunded") or purchase.get("chargebacked"):
            return False, None, None, "Diese Lizenz wurde erstattet oder zurückgebucht."

        created_at_str = purchase.get("created_at")
        if created_at_str:
            try:
                created_at = datetime.datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
                if created_at.tzinfo is None:
                    created_at = created_at.replace(tzinfo=timezone.utc)
            except Exception:
                created_at = datetime.datetime.now(timezone.utc)
        else:
            created_at = datetime.datetime.now(timezone.utc)

        pass_tier, duration = _detect_duration_from_purchase(purchase)
        expires_at = created_at + duration

        if datetime.datetime.now(timezone.utc) > expires_at:
            return False, None, None, "Lizenzschlüssel ist abgelaufen."

        return True, pass_tier, expires_at, "Lizenz erfolgreich verifiziert!"

    except Exception as e:
        return False, None, None, f"Fehler bei der Verifizierung: {type(e).__name__}: {e}"


# ---------------------------------------------------------
# 6. DYNAMISCHE API-ERKENNUNG & LLM-CALLS MIT SMART MEMORY
# ---------------------------------------------------------
def _collect_secret_values(obj, prefix="", out=None):
    if out is None:
        out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            full_key = f"{prefix}.{k}" if prefix else str(k)
            if isinstance(v, dict):
                _collect_secret_values(v, full_key, out)
            elif isinstance(v, str) and v.strip():
                out[full_key] = v.strip()
    return out


def _normalize_base_url(url: str) -> str:
    clean = str(url).strip().rstrip("/")
    if clean.endswith("/chat/completions"):
        clean = clean[: -len("/chat/completions")].rstrip("/")
    return clean


def _fetch_live_model(base_url: str, api_key: str, provider_hint: str, fallback_models: list) -> str:
    cache_key = f"{base_url}::{provider_hint}"
    if cache_key in st.session_state.resolved_models:
        return st.session_state.resolved_models[cache_key]

    try:
        resp = requests.get(
            f"{base_url}/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10,
        )
        if resp.status_code == 200:
            payload = resp.json()
            raw_models = payload.get("data", []) if isinstance(payload, dict) else []
            model_ids = [m.get("id") for m in raw_models if isinstance(m, dict) and m.get("id")]

            if model_ids:
                preferred_prefixes = ("llama-3.3", "llama-3.1", "gpt-4o", "gemini-2.5", "gemini-2.0", "qwen")
                for pref in preferred_prefixes:
                    for mid in model_ids:
                        if pref in mid.lower():
                            st.session_state.resolved_models[cache_key] = mid
                            return mid
                st.session_state.resolved_models[cache_key] = model_ids[0]
                return model_ids[0]
    except Exception:
        pass

    chosen = fallback_models[0] if fallback_models else "gpt-4o-mini"
    st.session_state.resolved_models[cache_key] = chosen
    return chosen


def _build_api_targets(resolve_live: bool = False):
    all_secrets = _collect_secret_values(dict(st.secrets))
    candidate_keys = []
    for k, v in all_secrets.items():
        kl = k.lower()
        if any(word in kl for word in ("key", "token", "api")) and not any(
            skip in kl for skip in ("url", "model", "endpoint", "base", "gumroad", "github", "auth")
        ):
            candidate_keys.append((k, v))

    priority = ("groq", "openai", "llm", "gemini", "google", "openrouter")
    candidate_keys.sort(
        key=lambda item: next((i for i, p in enumerate(priority) if p in item[0].lower()), len(priority))
    )

    default_base_url = all_secrets.get("LLM_BASE_URL") or all_secrets.get("OPENAI_BASE_URL") or ""
    default_model = all_secrets.get("LLM_MODEL") or all_secrets.get("OPENAI_MODEL") or ""

    targets = []
    for key_name, api_key in candidate_keys:
        kl = key_name.lower()
        is_groq = "groq" in kl or api_key.startswith("gsk_")
        is_gemini = "gemini" in kl or "google" in kl or api_key.startswith("AIza")
        is_openrouter = "openrouter" in kl or api_key.startswith("sk-or-")

        if default_base_url:
            base_url = _normalize_base_url(default_base_url)
            provider_hint = "custom"
            fallbacks = [default_model or "gpt-4o-mini"]
        elif is_groq:
            base_url = "https://api.groq.com/openai/v1"
            provider_hint = "groq"
            fallbacks = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
        elif is_gemini:
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
            provider_hint = "gemini"
            fallbacks = ["gemini-2.5-flash", "gemini-2.0-flash"]
        elif is_openrouter:
            base_url = "https://openrouter.ai/api/v1"
            provider_hint = "openrouter"
            fallbacks = ["openai/gpt-4o-mini"]
        else:
            base_url = "https://api.openai.com/v1"
            provider_hint = "openai"
            fallbacks = ["gpt-4o-mini"]

        if default_model:
            model = default_model
        elif resolve_live:
            model = _fetch_live_model(base_url, api_key, provider_hint, fallbacks)
        else:
            cache_key = f"{base_url}::{provider_hint}"
            model = st.session_state.resolved_models.get(cache_key, fallbacks[0])

        targets.append(
            {
                "name": key_name,
                "api_key": api_key,
                "base_url": base_url,
                "provider_hint": provider_hint,
                "fallbacks": fallbacks,
                "model": model,
            }
        )
    return targets


def _build_smart_memory_context(prompt: str) -> str:
    """Kombiniert priorisierte Fakten, Stichwort-Treffer und aktuelle Chats."""
    facts = load_priority_facts(limit=12)
    hits = search_elephant_memory(prompt, limit=6)
    recent_chats = load_recent_chats(limit=8)

    facts_block = "\n".join(f"- {f}" for f in facts) if facts else "- Keine speziellen Fakten hinterlegt."
    hits_block = "\n".join(f"- {h}" for h in hits) if hits else "- Keine direkten Stichwort-Treffer."
    chats_block = "\n".join(f"- {c}" for c in recent_chats) if recent_chats else "- Noch keine Chat-Logs."

    return (
        f"PRIORISIERTE FAKTEN & GESETZE (IMMER BEACHTEN):\n{facts_block}\n\n"
        f"GEZIELTE SUCHTREFFER ZUR ANFRAGE:\n{hits_block}\n\n"
        f"LETZTE VERLAUFS-EINTRÄGE:\n{chats_block}"
    )


def call_llm_for_zord(zord_name: str, prompt: str) -> str:
    zord_info = ZORD_ROSTER[zord_name]
    targets = _build_api_targets(resolve_live=True)

    if not targets:
        return f"[{zord_name} | Keine API-Keys in st.secrets gefunden]"

    smart_memory = _build_smart_memory_context(prompt)

    recent_chat = []
    for agent, user_msg, ai_msg in st.session_state.chat_history[-6:]:
        recent_chat.append({"role": "user", "content": f"({agent}) {user_msg}"})
        recent_chat.append({"role": "assistant", "content": ai_msg})

    system_content = f"{zord_info['system']}\n\n{smart_memory}"

    messages = [{"role": "system", "content": system_content}]
    messages.extend(recent_chat)
    messages.append({"role": "user", "content": prompt})

    errors = []
    for target in targets:
        models_to_try = [target["model"]] + [m for m in target["fallbacks"] if m != target["model"]]
        for m in models_to_try:
            for attempt in range(2):
                try:
                    endpoint = f"{target['base_url']}/chat/completions"
                    resp = requests.post(
                        endpoint,
                        headers={"Authorization": f"Bearer {target['api_key']}", "Content-Type": "application/json"},
                        json={"model": m, "messages": messages, "temperature": 0.7},
                        timeout=35,
                    )
                    if resp.status_code == 200:
                        st.session_state.resolved_models[f"{target['base_url']}::{target['provider_hint']}"] = m
                        return resp.json()["choices"][0]["message"]["content"].strip()
                    elif resp.status_code == 429 and attempt == 0:
                        time.sleep(2.5)
                        continue
                    else:
                        errors.append(f"{target['name']} [{m}]: HTTP {resp.status_code}")
                        break
                except Exception as e:
                    errors.append(f"{target['name']} [{m}]: {e}")
                    break

    return f"[{zord_name} | Fehler] \n- " + "\n- ".join(errors)


class ZordNetEngine:
    @staticmethod
    def process_request(agent_name: str, prompt: str, force_fact: bool = False) -> str:
        reply = call_llm_for_zord(agent_name, prompt)
        ok, db_msg = save_to_elephant_memory(agent_name, prompt, reply, force_fact=force_fact)
        if not ok:
            st.error(db_msg)
        return reply


# ---------------------------------------------------------
# 7. USER INTERFACE
# ---------------------------------------------------------
if not st.session_state.authenticated:
    st.title("⚡ Orion.Ai — ZordNet Access Portal")
    st.subheader("Auth-X Secured 10-Zord Multi-Agent Interface")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("Willkommen beim **ZordNet System**. Gib deinen Lizenzschlüssel ein, um alle 10 Götter-Zords freizuschalten.")
        key_input = st.text_input("Lizenzschlüssel (Gumroad Key):", value="", type="password")

        if st.button("System Freischalten 🚀"):
            if key_input:
                with st.spinner("Prüfe Auth-X & Lizenz..."):
                    is_valid, tier, expires, msg = verify_orion_license(key_input)
                    if is_valid:
                        st.session_state.authenticated = True
                        st.session_state.license_key = key_input
                        st.session_state.pass_tier = tier
                        st.session_state.expires_at = expires
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
            else:
                st.warning("Bitte gib einen Lizenzschlüssel ein.")

        st.info("💡 **Test-Hinweis:** Du kannst aktuell `ORION-TEST-KEY-2026` oder deinen Gumroad-Lizenzschlüssel nutzen.")

    with col2:
        st.markdown(
            """
        <div class="status-card">
            <h4>Pässe & Zugang</h4>
            <ul>
                <li><b>1 Tag:</b> CHF 5.00</li>
                <li><b>1 Woche:</b> CHF 20.00</li>
                <li><b>1 Monat:</b> CHF 45.00</li>
            </ul>
            <p><small>Verifizierter Zugang via Gumroad & Auth-X Security System.</small></p>
        </div>
        """,
            unsafe_allow_html=True,
        )

else:
    st.title("⚡ ZordNet Terminal — 10 Götter")

    remaining_str = "Aktiv"
    if st.session_state.expires_at:
        now = datetime.datetime.now(timezone.utc)
        diff = st.session_state.expires_at - now
        days = diff.days
        hours = diff.seconds // 3600
        remaining_str = f"{days}d {hours}h"

    targets = _build_api_targets(resolve_live=False)
    api_status = f"AKTIV [{len(targets)} APIs]" if targets else "KEINE API GEFUNDEN"

    st.markdown(
        f"""
    <div class="status-card">
        <b>Status:</b> <span style="color:#00ff66;">ONLINE</span> |
        <b>Pass Tier:</b> {st.session_state.pass_tier} |
        <b>Gültig für:</b> {remaining_str} |
        <b>DB Memory:</b> <span style="color:#00ff66;">Smart SQLite Aktiv</span> |
        <b>Auth-X Master:</b> Michael Gautschi
    </div>
    """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.header("🐘 Elephant Memory (DB)")
        st.caption("Fakten, Stichwort-Recall & Verlauf aus SQLite")

        # Direkter Backup-Download der SQLite-Datenbank
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "rb") as db_f:
                st.download_button(
                    label="💾 Backup: zordnet_memory.db laden",
                    data=db_f.read(),
                    file_name="zordnet_memory.db",
                    mime="application/x-sqlite3",
                )

        db_memory = load_elephant_memory(limit=25)
        for mem in db_memory:
            st.markdown(f"- {mem}")

        st.divider()
        if st.button("Abmelden / Lock System"):
            st.session_state.authenticated = False
            st.rerun()

    st.subheader("⚡ Die 10 Götter-Zords")
    zord_names = list(ZORD_ROSTER.keys())
    for row_start in range(0, len(zord_names), 5):
        cols = st.columns(5)
        for idx, z_name in enumerate(zord_names[row_start : row_start + 5]):
            icon, title = z_name.split(" ", 1)
            role = ZORD_ROSTER[z_name]["role"]
            with cols[idx]:
                st.markdown(
                    f'<div class="agent-box">{icon}<br><b>{title}</b><br><small>{role}</small></div>',
                    unsafe_allow_html=True,
                )

    st.divider()

    st.subheader("🖥️ ZordNet Terminal")
    selected_agent = st.selectbox("Zord auswählen:", zord_names)
    st.caption(f"Aktive Rolle: **{ZORD_ROSTER[selected_agent]['role']}**")

    user_prompt = st.text_area(
        "Befehl / Anfrage an ZordNet senden:",
        placeholder="Schreib wie mit ChatGPT oder Gemini...",
        height=90,
    )
    save_as_fact = st.checkbox("Als dauerhaften Fakt / Regel (FACT) markieren")

    if st.button("Befehl Ausführen ⚡"):
        if user_prompt.strip():
            with st.spinner(f"{selected_agent} denkt nach..."):
                output = ZordNetEngine.process_request(
                    selected_agent,
                    user_prompt.strip(),
                    force_fact=save_as_fact,
                )
            st.session_state.chat_history.append((selected_agent, user_prompt.strip(), output))
            st.rerun()
        else:
            st.warning("Bitte gib einen Befehl oder eine Frage ein.")

    st.subheader("📜 Terminal Output & Logs")
    for agent, req, res in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(f"**[{agent}]** {req}")
        with st.chat_message("assistant"):
            st.markdown(res)
