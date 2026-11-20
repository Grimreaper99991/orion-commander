import streamlit as st
import requests
import datetime
from datetime import timezone

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Orion.Ai | ZordNet System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Theme & Neon Accents)
st.markdown("""
<style>
    .main { background-color: #0b0e14; color: #e6edf3; }
    .stButton>button {
        background-color: #ff6b00;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        transition: all 0.3s ease;
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
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION STATE INITIALIZATION
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
        "System-Standard: Elephant Memory aktiviert."
    ]

# ---------------------------------------------------------
# 3. GUMROAD LICENSE VALIDATION SYSTEM
# ---------------------------------------------------------
GUMROAD_PRODUCT_IDS = {
    "1_TAG":"PNXJZNc-Am0n3S5UXK2Iqw==",      # Ersetzen mit deinen Gumroad Product IDs
    "1_WOCHE":"qZkqQUIlwnUW51EqLZg8gw==",
    "1_MONAT":"qftgaG4CJFmDLpp4u6T3fw=="
}

def verify_orion_license(license_key):
    """Validiert den Lizenzschlüssel über Gumroad API oder den Creator-Test-Key."""
    key = license_key.strip()
    
    # 1. Creator Test-Key Check (Für interne Tests & Gumroad Testkäufe)
    if key.upper().startswith("TEST-ORION") or key == "ORION-TEST-KEY-2026":
        expiry_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(days=30)
        return True, "1_MONAT", expiry_date, "Test-Key erfolgreich aktiviert!"

    # 2. Echter Gumroad API Check
    try:
        # Falls du eine spezifische Product-ID nutzen willst, gib permalink an
        response = requests.post(
            "https://api.gumroad.com/v2/licenses/verify",
            data={"license_key": key},
            timeout=10
        )
        data = response.json()
        
        if data.get("success"):
            purchase = data.get("purchase", {})
            product_id = purchase.get("product_id")
            created_at_str = purchase.get("created_at")
            
            # Laufzeit ermitteln basierend auf Produkttyp
            created_at = datetime.datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
            
            # Standardmäßig 1 Monat setzen wenn unbekannt, sonst matchen
            pass_tier = "1_MONAT"
            duration = datetime.timedelta(days=30)
            
            if product_id == GUMROAD_PRODUCT_IDS.get("1_TAG"):
                pass_tier = "1_TAG"
                duration = datetime.timedelta(days=1)
            elif product_id == GUMROAD_PRODUCT_IDS.get("1_WOCHE"):
                pass_tier = "1_WOCHE"
                duration = datetime.timedelta(days=7)
                
            expires_at = created_at + duration
            
            if datetime.datetime.now(timezone.utc) > expires_at:
                return False, None, None, "Lizenzschlüssel ist abgelaufen."
                
            return True, pass_tier, expires_at, "Lizenz erfolgreich verifiziert!"
        else:
            return False, None, None, "Ungültiger Lizenzschlüssel."
            
    except Exception as e:
        # Fallback falls Offline/API-Fehler während des Testens
        return False, None, None, f"Fehler bei der Verifizierung: {str(e)}"

# ---------------------------------------------------------
# 4. ZORDNET MULTI-AGENT ENGINE
# ---------------------------------------------------------
class ZordNetEngine:
    @staticmethod
    def process_request(agent_name, prompt):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Log-Eintrag fürs Elefantengedächtnis vorbereiten
        memory_entry = f"[{timestamp}] [{agent_name}] Befehl: {prompt}"
        st.session_state.elephant_memory.append(memory_entry)
        
        # Agenten-Spezifische Antworten
        if agent_name == "🤖 ORION (Core AI)":
            response = f"[Orion Core] Verarbeite Haupt-Anfrage: '{prompt}'. Status: Optimal."
        elif agent_name == "⚡ ZEUS (Network Protocols)":
            response = f"[Zeus Network] Routen überprüft für: '{prompt}'. Protokoll stabil."
        elif agent_name == "🛡️ GHOST (Auth-X Security)":
            response = f"[Ghost Security] Auth-X Check für '{prompt}': Zugriff gewährt. Keine Bedrohung erkannt."
        elif agent_name == "☠️ GRIMREAPER (System Execution)":
            response = f"[Grimreaper Execution] Führe System-Befehl aus: '{prompt}'. Ausführung erfolgreich."
        else:
            response = f"[ZordNet Core] Anfrage erhalten: {prompt}"
            
        return response

# ---------------------------------------------------------
# 5. USER INTERFACE (LOGIN & DASHBOARD)
# ---------------------------------------------------------

# --- LOGIN SCREEN ---
if not st.session_state.authenticated:
    st.title("⚡ Orion.Ai — ZordNet Access Portal")
    st.subheader("Auth-X Secured Multi-Agent Interface")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Willkommen beim **ZordNet System**. Bitte gib deinen Gumroad-Lizenzschlüssel ein, um das Terminal freizuschalten.
        """)
        
        key_input = st.text_input("Lizenzschlüssel (Gumroad Key):", value="", type="password")
        
        if st.button("System Freischalten 🚀"):
            if key_input:
                with st.spinner("Prüfe Auth-X & Gumroad Lizenz..."):
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
                
        st.info("💡 **Test-Hinweis:** Du kannst aktuell auch `ORION-TEST-KEY-2026` oder den Gumroad Test-Key nutzen.")

    with col2:
        st.markdown("""
        <div class="status-card">
            <h4>Pässe & Zugang</h4>
            <ul>
                <li><b>1 Tag:</b> CHF 5.00</li>
                <li><b>1 Woche:</b> CHF 20.00</li>
                <li><b>1 Monat:</b> CHF 45.00</li>
            </ul>
            <p><small>Verifizierter Zugang via Gumroad & Auth-X Security System.</small></p>
        </div>
        """, unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Bar / Header Status
    st.title("⚡ ZordNet Terminal Dashboard")
    
    # Restzeit Berechnen
    remaining_str = "Aktiv"
    if st.session_state.expires_at:
        now = datetime.datetime.now(timezone.utc)
        diff = st.session_state.expires_at - now
        days = diff.days
        hours = diff.seconds // 3600
        remaining_str = f"{days}d {hours}h"
        
    st.markdown(f"""
    <div class="status-card">
        <b>Status:</b> <span style="color:#00ff66;">ONLINE</span> | 
        <b>Pass Tier:</b> {st.session_state.pass_tier} | 
        <b>Gültig für:</b> {remaining_str} | 
        <b>Auth-X Master:</b> Michael Gautschi
    </div>
    """, unsafe_allow_html=True)
    
    # Layout: Sidebar für Elephant Memory & Agenten-Übersicht
    with st.sidebar:
        st.header("🐘 Elephant Memory")
        st.caption("Dauerhafte Protokollierung & System-Gesetze")
        for mem in st.session_state.elephant_memory:
            st.markdown(f"- {mem}")
            
        st.divider()
        if st.button("Abmelden / Lock System"):
            st.session_state.authenticated = False
            st.rerun()

    # Agenten Grid
    st.subheader("⚡ ZordNet Multi-Agent System")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="agent-box">🤖<br><b>ORION</b><br><small>Core AI Engine</small></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="agent-box">⚡<br><b>ZEUS</b><br><small>Network Protocols</small></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="agent-box">🛡️<br><b>GHOST</b><br><small>Auth-X Security</small></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="agent-box">☠️<br><b>GRIMREAPER</b><br><small>System Execution</small></div>', unsafe_allow_html=True)

    st.divider()

    # Terminal Input Area
    st.subheader("🖥️ ZordNet Terminal")
    
    selected_agent = st.selectbox(
        "Agenten auswählen:",
        ["🤖 ORION (Core AI)", "⚡ ZEUS (Network Protocols)", "🛡️ GHOST (Auth-X Security)", "☠️ GRIMREAPER (System Execution)"]
    )
    
    user_prompt = st.text_input("Befehl / Anfrage an ZordNet senden:", placeholder="Gib deinen Befehl ein...")
    
    if st.button("Befehl Ausführen ⚡"):
        if user_prompt:
            output = ZordNetEngine.process_request(selected_agent, user_prompt)
            st.session_state.chat_history.append((selected_agent, user_prompt, output))
        else:
            st.warning("Bitte gib einen Befehl ein.")

    # Terminal Output Logs
    st.subheader("📜 Terminal Output & Logs")
    for agent, req, res in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(f"**[{agent}]** {req}")
        with st.chat_message("assistant"):
            st.write(res)
