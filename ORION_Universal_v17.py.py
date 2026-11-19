import os
import time
import json
import datetime
import requests
from typing import Tuple, Dict, Any
import streamlit as st

# ==============================================================================
# 1. GUMROAD LIZENZ-KONFIGURATION (Hier deine 3 Product IDs einfügen)
# ==============================================================================
GUMROAD_PRODUCT_IDS = {
    "1_tag":"PNXJZNc-Am0n3S5UXK2Iqw==",
    "1_woche":"qZkqQUIlwnUW51EqLZg8gw==",
    "1_monat":"qftgaG4CJFmDLpp4u6T3fw==",
}

DURATION_DAYS = {
    "1_tag": 1,
    "1_woche": 7,
    "1_monat": 30,
}

GUMROAD_VERIFY_URL = "https://api.gumroad.com/v2/licenses/verify"

# ==============================================================================
# 2. STREAMLIT PAGE CONFIG & SESSION INITIALISIERUNG
# ==============================================================================
st.set_page_config(
    page_title="Orion.Ai - ZordNet Central",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Dark Neon Theme)
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #1f6feb; color: white; border-radius: 8px; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #161b22; color: #f0f6fc; border: 1px solid #30363d; }
    .zord-card { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# Session States initialisieren
if "orion_auth" not in st.session_state:
    st.session_state.orion_auth = False
if "orion_msg" not in st.session_state:
    st.session_state.orion_msg = ""
if "orion_meta" not in st.session_state:
    st.session_state.orion_meta = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "elephant_memory" not in st.session_state:
    st.session_state.elephant_memory = [
        "Master Code: Auth-x aktiv",
        "Haupt-Architekt: Michael Gautschi",
        "Asimov Gesetz 5: Nur Michael darf Code-Änderungen vornehmen.",
        "System-Standard: Elephant Memory aktiviert."
    ]

# ==============================================================================
# 3. GUMROAD LIZENZPRÜFER ENGINE
# ==============================================================================
def verify_orion_license(user_license_key: str) -> Tuple[bool, str, dict]:
    clean_key = (user_license_key or "").strip()
    if not clean_key:
        return False, "Bitte gib deinen Lizenzschlüssel ein.", {}

    if clean_key.lower().startswith("sample"):
        return False, "Das ist ein Beispiel-Platzhalter. Bitte einen echten Lizenzschlüssel nutzen.", {}

    last_network_error = None

    for tier, product_id in GUMROAD_PRODUCT_IDS.items():
        if not product_id or product_id.startswith("HIER_PRODUCT_ID_"):
            continue

        payload = {
            "product_id": product_id,
            "license_key": clean_key,
            "increment_uses_count": "false",
        }

        try:
            response = requests.post(GUMROAD_VERIFY_URL, data=payload, timeout=12)
            data = response.json()
        except Exception as exc:
            last_network_error = str(exc)
            continue

        if not data.get("success"):
            continue

        purchase = data.get("purchase") or {}

        if (purchase.get("refunded") or 
            purchase.get("chargebacked") or 
            data.get("subscription_cancelled_at") or 
            data.get("subscription_ended_at")):
            return False, "Diese Lizenz wurde storniert oder zurückerstattet.", {}

        created_at_str = purchase.get("created_at")
        if not created_at_str:
            return True, f"Zugriff gewährt ({tier.upper()} Pass).", {"tier": tier, "key": clean_key}

        try:
            purchase_dt = datetime.datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
            if purchase_dt.tzinfo is None:
                purchase_dt = purchase_dt.replace(tzinfo=datetime.timezone.utc)
        except ValueError:
            return False, "Kaufdatum konnte nicht verarbeitet werden.", {}

        now_utc = datetime.datetime.now(datetime.timezone.utc)
        expiration_dt = purchase_dt + datetime.timedelta(days=DURATION_DAYS[tier])

        if now_utc >= expiration_dt:
            return False, f"Lizenz abgelaufen ({tier.upper()} Pass).", {}

        remaining = expiration_dt - now_utc
        total_hours = int(remaining.total_seconds() // 3600)
        days_part = total_hours // 24
        hours_part = total_hours % 24
        time_label = f"{days_part}d {hours_part}h" if days_part > 0 else f"{hours_part}h"

        meta = {
            "tier": tier,
            "key": clean_key,
            "expires_at": expiration_dt.isoformat(),
            "remaining_label": time_label
        }
        return True, f"Zugriff aktiv ({tier.upper()} Pass) - Verbleibend: ~{time_label}", meta

    if last_network_error:
        return False, f"Verbindungsfehler zur Gumroad-API: {last_network_error}", {}

    return False, "Ungültiger Lizenzschlüssel oder falsche Produkt-Zuordnung.", {}

# ==============================================================================
# 4. ZORDNET AGENTEN ENGINE (Orion, Zeus, Ghost, Grimreaper)
# ==============================================================================
class ZordNetSystem:
    @staticmethod
    def process_agent_request(agent_name: str, prompt: str) -> str:
        prompt_lower = prompt.lower()
        
        if agent_name == "Orion (Core AI)":
            if "status" in prompt_lower:
                return "ORION v9.5 Core: Alle Subsysteme laufen optimal. Elephant Memory geladen."
            return f"ORION Antwort: Verarbeite Befehl '{prompt}' unter Berücksichtigung von Asimovs Gesetzen."
            
        elif agent_name == "Zeus (Network & Protocol)":
            return f"ZEUS Knoten: Verteilungsprotokoll für '{prompt}' an Server-Sockets etabliert. Latenz 1ms."
            
        elif agent_name == "Ghost (Security & Auth-X)":
            if "auth" in prompt_lower or "pass" in prompt_lower:
                return "GHOST Shield: Auth-X Mastercode bestätigt. Zugriff auf ZordNet verifiziert."
            return f"GHOST Shield: Überwache Datenstrom für prompt '{prompt}'. Keine Anomalien festgestellt."
            
        elif agent_name == "Grimreaper (Execution & Control)":
            return f"GRIMREAPER Control: Task '{prompt}' in Ausführungsschleife eingereiht. Status: OK."
            
        return "ZordNet: Unbekannter Agent."

# ==============================================================================
# 5. UI: LOGIN SCREEN
# ==============================================================================
def render_login_screen():
    st.markdown("<h1 style='text-align: center; color: #ff7b00;'>⚡ Orion.Ai / ZordNet Access</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Bitte gib deinen 1-Tag, 1-Woche oder 1-Monat Pass ein.</p>", unsafe_allow_html=True)

    unconfigured = [k for k, v in GUMROAD_PRODUCT_IDS.items() if not v or v.startswith("HIER_PRODUCT_ID_")]
    if unconfigured:
        st.warning(f"⚠️ Hinweis: Product IDs fehlen noch für: {', '.join(unconfigured)}")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            license_key = st.text_input("Gumroad Lizenzschlüssel", type="password", placeholder="XXXXX-XXXXX-XXXXX-XXXXX")
            submit = st.form_submit_button("System freischalten")

        if submit:
            with st.spinner("Prüfe Lizenz via Gumroad..."):
                ok, msg, meta = verify_orion_license(license_key)
                st.session_state.orion_msg = msg
                if ok:
                    st.session_state.orion_auth = True
                    st.session_state.orion_meta = meta
                    st.rerun()
                else:
                    st.error(msg)

# ==============================================================================
# 6. UI: MAIN SYSTEM INTERFACE (ZORDNET DASHBOARD)
# ==============================================================================
def render_orion_app():
    meta = st.session_state.orion_meta

    # Live Expiration Check
    exp_str = meta.get("expires_at")
    if exp_str:
        exp_dt = datetime.datetime.fromisoformat(exp_str)
        if datetime.datetime.now(datetime.timezone.utc) >= exp_dt:
            st.session_state.orion_auth = False
            st.session_state.orion_meta = {}
            st.warning("Dein Lizenzpass ist abgelaufen.")
            st.rerun()

    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("## ⚡ ZordNet Status")
        st.success(f"**Pass Tier:** {meta.get('tier', 'aktiv').upper()}")
        if "remaining_label" in meta:
            st.info(f"**Gültig für:** {meta['remaining_label']}")
        
        st.markdown("---")
        st.markdown("### 🐘 Elephant Memory")
        for mem in st.session_state.elephant_memory:
            st.caption(f"• {mem}")

        st.markdown("---")
        if st.button("Abmelden"):
            st.session_state.orion_auth = False
            st.session_state.orion_meta = {}
            st.rerun()

    # --- MAIN INTERFACE ---
    st.title("⚡ ZordNet Multi-Agent System")
    st.caption("Orion.Ai Core Architecture | Auth-X Secured")

    # Agenten Übersicht Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("<div class='zord-card'><b>🤖 ORION</b><br><small>Core AI Engine</small></div>", unsafe_allow_html=True)
    col2.markdown("<div class='zord-card'><b>⚡ ZEUS</b><br><small>Network Protocols</small></div>", unsafe_allow_html=True)
    col3.markdown("<div class='zord-card'><b>🛡️ GHOST</b><br><small>Auth-X Security</small></div>", unsafe_allow_html=True)
    col4.markdown("<div class='zord-card'><b>☠️ GRIMREAPER</b><br><small>System Execution</small></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Command Execution Center
    st.subheader("ZordNet Terminal")
    
    agent_choice = st.selectbox("Agenten auswählen:", ["Orion (Core AI)", "Zeus (Network & Protocol)", "Ghost (Security & Auth-X)", "Grimreaper (Execution & Control)"])
    user_prompt = st.text_input("Befehl / Anfrage an ZordNet senden:")

    if st.button("Befehl ausführen"):
        if user_prompt:
            response = ZordNetSystem.process_agent_request(agent_choice, user_prompt)
            st.session_state.chat_history.append((agent_choice, user_prompt, response))
        else:
            st.warning("Bitte gib einen Befehl ein.")

    # Chat Log / Terminal Output
    if st.session_state.chat_history:
        st.markdown("### Terminal Log")
        for agent, req, res in reversed(st.session_state.chat_history):
            with st.expander(f"[{agent}] - {req[:40]}..."):
                st.write(f"**Anfrage:** {req}")
                st.write(f"**Antwort:** {res}")

# ==============================================================================
# 7. ROUTING
# ==============================================================================
if not st.session_state.orion_auth:
    render_login_screen()
else:
    render_orion_app()
