import datetime
from datetime import timezone
import requests
import streamlit as st

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Orion.Ai | 10 Götter ZordNet",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
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
# 2. DIE 10 GÖTTER-ZORDS (ROLLEN & SYSTEM-PROMPTS)
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
# 3. SESSION STATE INITIALIZATION
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
if "elephant_memory" not in st.session_state:
    st.session_state.elephant_memory = [
        "Master Code: Auth-x aktiv",
        "Haupt-Architekt: Michael Gautschi",
        "Asimov Gesetz 5: Nur Michael darf Code-Änderungen vornehmen.",
        "System-Standard: Elephant Memory aktiviert.",
    ]

# ---------------------------------------------------------
# 4. GUMROAD LICENSE VALIDATION SYSTEM (OHNE PRODUCT-ID-ZWANG)
# ---------------------------------------------------------
def _detect_duration_from_purchase(purchase: dict):
    """Ermittelt Laufzeit & Tier automatisch ohne fest hinterlegte Product IDs."""
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

    # Creator- / Test-Keys sofort durchlassen
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
# 5. AUTOMATISCHE API-ERKENNUNG & MULTI-API ABFRAGE FÜR ALLE 10 ZORDS
# ---------------------------------------------------------
def _collect_secret_values(obj, prefix="", out=None):
    """Sammelt alle Strings aus flachen und verschachtelten Secrets ein."""
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


def _build_api_targets():
    """Baut aus allen hinterlegten API-Keys in st.secrets eine Liste nutzbarer API-Ziele."""
    all_secrets = _collect_secret_values(dict(st.secrets))

    # Alles einsammeln, was nach API-Key / Token / Secret aussieht
    candidate_keys = []
    for k, v in all_secrets.items():
        kl = k.lower()
        if any(word in kl for word in ("key", "token", "api")) and not any(
            skip in kl for skip in ("url", "model", "endpoint", "base", "gumroad")
        ):
            candidate_keys.append((k, v))

    # Bevorzugte Key-Namen nach vorne sortieren
    priority = ("openai", "llm", "gemini", "google", "openrouter", "groq", "mistral", "deepseek")
    candidate_keys.sort(
        key=lambda item: next(
            (i for i, p in enumerate(priority) if p in item[0].lower()),
            len(priority),
        )
    )

    default_base_url = (
        all_secrets.get("LLM_BASE_URL")
        or all_secrets.get("OPENAI_BASE_URL")
        or all_secrets.get("BASE_URL")
        or ""
    )
    default_model = (
        all_secrets.get("LLM_MODEL")
        or all_secrets.get("OPENAI_MODEL")
        or all_secrets.get("MODEL")
        or ""
    )

    targets = []
    for key_name, api_key in candidate_keys:
        kl = key_name.lower()
        is_gemini = "gemini" in kl or "google" in kl or api_key.startswith("AIza")
        is_openrouter = "openrouter" in kl or api_key.startswith("sk-or-")
        is_groq = "groq" in kl or api_key.startswith("gsk_")

        if default_base_url:
            base_url = default_base_url
        elif is_gemini:
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
        elif is_openrouter:
            base_url = "https://openrouter.ai/api/v1"
        elif is_groq:
            base_url = "https://api.groq.com/openai/v1"
        else:
            base_url = "https://api.openai.com/v1"

        if default_model:
            model = default_model
        elif is_gemini:
            model = "gemini-2.5-flash"
        elif is_openrouter:
            model = "openai/gpt-4o-mini"
        elif is_groq:
            model = "llama-3.3-70b-versatile"
        else:
            model = "gpt-4o-mini"

        targets.append(
            {
                "name": key_name,
                "api_key": api_key,
                "base_url": str(base_url).rstrip("/"),
                "model": str(model),
            }
        )

    return targets


def _query_openai_compatible(target: dict, messages: list) -> str:
    resp = requests.post(
        f"{target['base_url']}/chat/completions",
        headers={
            "Authorization": f"Bearer {target['api_key']}",
            "Content-Type": "application/json",
        },
        json={
            "model": target["model"],
            "messages": messages,
            "temperature": 0.7,
        },
        timeout=35,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()


def call_llm_for_zord(zord_name: str, prompt: str) -> str:
    zord_info = ZORD_ROSTER[zord_name]
    targets = _build_api_targets()

    if not targets:
        return (
            f"[{zord_name} | Keine API-Keys erkannt]\n"
            f"Es wurden in `st.secrets` keine API-Keys gefunden. Trage z. B. `OPENAI_API_KEY` oder `GEMINI_API_KEY` ein."
        )

    recent_memory = "\n".join(f"- {m}" for m in st.session_state.elephant_memory[-20:])
    recent_chat = []
    for agent, user_msg, ai_msg in st.session_state.chat_history[-6:]:
        recent_chat.append({"role": "user", "content": f"({agent}) {user_msg}"})
        recent_chat.append({"role": "assistant", "content": ai_msg})

    system_content = (
        f"{zord_info['system']}\n\n"
        f"Aktuelles Elephant Memory (Kontext & bisherige Ereignisse):\n{recent_memory}"
    )

    messages = [{"role": "system", "content": system_content}]
    messages.extend(recent_chat)
    messages.append({"role": "user", "content": prompt})

    errors = []
    for target in targets:
        try:
            return _query_openai_compatible(target, messages)
        except Exception as e:
            errors.append(f"{target['name']} ({target['model']}): {type(e).__name__}: {e}")

    joined_errors = "\n- ".join(errors)
    return f"[{zord_name} | Alle API-Versuche fehlgeschlagen]\n- {joined_errors}"


class ZordNetEngine:
    @staticmethod
    def process_request(agent_name: str, prompt: str) -> str:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.elephant_memory.append(f"[{timestamp}] [{agent_name}] Nutzereingabe: {prompt}")

        reply = call_llm_for_zord(agent_name, prompt)

        short_reply = reply.replace("\n", " ")[:180]
        st.session_state.elephant_memory.append(f"[{timestamp}] [{agent_name}] Antwort: {short_reply}")
        return reply


# ---------------------------------------------------------
# 6. USER INTERFACE (LOGIN & DASHBOARD)
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

    targets = _build_api_targets()
    if targets:
        api_names = ", ".join(f"{t['name']} ({t['model']})" for t in targets)
        api_status = f"AKTIV [{len(targets)} APIs: {api_names}]"
    else:
        api_status = "KEINE API GEFUNDEN"

    st.markdown(
        f"""
    <div class="status-card">
        <b>Status:</b> <span style="color:#00ff66;">ONLINE</span> |
        <b>Pass Tier:</b> {st.session_state.pass_tier} |
        <b>Gültig für:</b> {remaining_str} |
        <b>APIs:</b> {api_status} |
        <b>Auth-X Master:</b> Michael Gautschi
    </div>
    """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.header("🐘 Elephant Memory")
        st.caption("Protokoll & Kontext für alle 10 Zords")
        for mem in reversed(st.session_state.elephant_memory[-25:]):
            st.markdown(f"- {mem}")

        st.divider()
        if st.button("Abmelden / Lock System"):
            st.session_state.authenticated = False
            st.rerun()

    # Grid für alle 10 Götter-Zords (5 pro Reihe)
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

    if st.button("Befehl Ausführen ⚡"):
        if user_prompt.strip():
            with st.spinner(f"{selected_agent} denkt nach..."):
                output = ZordNetEngine.process_request(selected_agent, user_prompt.strip())
            st.session_state.chat_history.append((selected_agent, user_prompt.strip(), output))
        else:
            st.warning("Bitte gib einen Befehl oder eine Frage ein.")

    st.subheader("📜 Terminal Output & Logs")
    for agent, req, res in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(f"**[{agent}]** {req}")
        with st.chat_message("assistant"):
            st.markdown(res)
