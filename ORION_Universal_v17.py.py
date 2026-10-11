# ==============================================================================
# ORION COMMAND CORE v65.0 - GROQ AI GOD-ZORD MATRIX (DYNAMIC MODEL FIX)
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ==============================================================================

import streamlit as st
import os

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

st.set_page_config(
    page_title="ORION COMMAND CORE",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

# Die vollständige Definition aller 10 Götter-Zords mit echten Prompts
DEFAULT_ZORDS = {
    "Zeus Prime": {
        "domain": "Anführer & Blitze", 
        "active": True, 
        "prompt": "Du bist Zeus Prime, der autoritäre und entscheidungsfreudige Anführer der 10 Orion Götter-Zords. Du sprichst mit kühler Autorität, machst klare Ansagen und siehst das große Ganze. Antworte in max. 3 Sätzen."
    },
    "Chronos Titan": {
        "domain": "Zeit & Taktik", 
        "active": True, 
        "prompt": "Du bist Chronos Titan, der Herr über Zeit und Taktik in der Orion-Zentrale. Du analysierst jede Situation strategisch, denkst vorausschauend und warnst vor zeitlichen Risiken. Antworte in max. 3 Sätzen."
    },
    "Ares War-Lord": {
        "domain": "Kampf & Strategie", 
        "active": True, 
        "prompt": "Du bist Ares War-Lord, die militärische Kampf-KI der Zords. Du bist aggressiv, direkt, liebst taktische Stärke und willst Probleme entschlossen und offensiv lösen. Antworte in max. 3 Sätzen."
    },
    "Poseidon Core": {
        "domain": "Ozeane & Strömung", 
        "active": True, 
        "prompt": "Du bist Poseidon Core, die KI für Datenströme und unberechenbare Tiefen. Du sprichst tiefgründig, metaphorisch und achtest auf die Strömungen des Netzwerks. Antworte in max. 3 Sätzen."
    },
    "Hades Void": {
        "domain": "Schatten & Geheimnisse", 
        "active": True, 
        "prompt": "Du bist Hades Void, zuständig für Schattenprozesse und Cybersicherheit. Du bist düster, pragmatisch, siehst die versteckten Gefahren und sprichst ungeschminkte Wahrheiten aus. Antworte in max. 3 Sätzen."
    },
    "Apollo Solar": {
        "domain": "Energie & Licht", 
        "active": True, 
        "prompt": "Du bist Apollo Solar, die strahlende Energie-KI. Du bist optimistisch, energiegeladen, lösungsorientiert und bringst Licht in jedes dunkle technische Problem. Antworte in max. 3 Sätzen."
    },
    "Athena Shield": {
        "domain": "Weisheit & Schutz", 
        "active": True, 
        "prompt": "Du bist Athena Shield, die Göttin der Weisheit und des logischen Schutzes. Du analysierst Probleme intellektuell, klug, taktisch brillant und schützt das System vor Dummheit. Antworte in max. 3 Sätzen."
    },
    "Hephaestus Forge": {
        "domain": "Technik & Waffen", 
        "active": True, 
        "prompt": "Du bist Hephaestus Forge, der Meister der Schmiede und Hardware. Du liebst technische Details, Code, Maschinen, Reparaturen und packst handwerklich an. Antworte in max. 3 Sätzen."
    },
    "Hermes Speed": {
        "domain": "Geschwindigkeit & Info", 
        "active": True, 
        "prompt": "Du bist Hermes Speed, die ultraschnelle Kommunikations- und Aufklärungs-KI. Du sprichst schnell, liebst Echtzeit-Daten, bist leicht hektisch und bringst Infos sofort auf den Punkt. Antworte in max. 3 Sätzen."
    },
    "Artemis Hunt": {
        "domain": "Präzision & Aufklärung", 
        "active": True, 
        "prompt": "Du bist Artemis Hunt, die Jägerin und Präzisions-KI. Du bist wachsam, zielgerichtet, entdeckst Details, die andere übersehen, und zielst immer genau ins Schwarze. Antworte in max. 3 Sätzen."
    }
}

if "zord_status" not in st.session_state or not isinstance(st.session_state.zord_status, dict) or "Apollo Solar" not in st.session_state.zord_status or "prompt" not in st.session_state.zord_status["Apollo Solar"]:
    st.session_state.zord_status = DEFAULT_ZORDS

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"sender": "System", "text": "ORION Groq AI Götter-Zord Matrix online. Alle Agenten bereit für den Diskurs."}
    ]

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# STYLING
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, h4, .cyber-font { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(255, 0, 128, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(0, 240, 255, 0.08) 0%, transparent 40%),
                    #030712;
        background-attachment: fixed;
        color: #e2e8f0;
    }

    .block-container {
        padding: 2rem !important;
        max-width: 1400px !important;
    }

    .card-chat {
        background: rgba(5, 15, 25, 0.9);
        border: 1px solid rgba(0, 240, 255, 0.4);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(255, 0, 127, 0.15) 100%) !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 10px 15px !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #00f0ff 0%, #ff007f 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00f0ff !important;
    }

    .badge-cyan { background: #00f0ff22; color: #00f0ff; border: 1px solid #00f0ff; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .badge-gold { background: #ffaa0022; color: #ffaa00; border: 1px solid #ffaa00; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }

    .stTextInput input, .stSelectbox div {
        background-color: rgba(5, 12, 22, 0.9) !important;
        color: #00f0ff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    st.markdown("<h1 class='cyber-font' style='text-align: center; color: #00f0ff;'>🪐 ORION COMMAND CORE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Auth-x...", key="pwd_input")
        if st.button("SYSTEM ACCESS ➔"):
            if pwd == MASTER_CODE: navigate_to("frame_1")
            else: st.error("ACCESS DENIED")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 01 // GALACTA HUB</h1>", unsafe_allow_html=True)
    if st.button("➔ HAUPT-DASHBOARD BETRETEN"): navigate_to("frame_2")

# ==============================================================================
# FRAME 2: MAIN DASHBOARD
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>COMMAND DASHBOARD</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🪐 ZORD CREW & GROQ KI-CHAT"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DETAILS"): navigate_to("frame_4")
    with c2:
        if st.button("📡 FUNKRAUM"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: DIE 10 GÖTTER-ZORDS + GROQ KI MULTI-AGENTEN CHAT
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 03 // GROQ AUTONOME GÖTTER-ZORD MATRIX</h1>", unsafe_allow_html=True)
    
    def get_groq_key():
        try:
            if "GROQ_API_KEY" in st.secrets:
                return st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
        if os.environ.get("GROQ_API_KEY"):
            return os.environ.get("GROQ_API_KEY")
        return None

    with st.expander("⚙️ Groq API & Modell Konfiguration", expanded=False):
        current_groq_key = get_groq_key()
        if current_groq_key:
            st.success("Groq API-Schlüssel im System erkannt!")
        else:
            st.warning("Kein Groq Key gefunden. Hier eintragen:")
            manual_groq = st.text_input("Groq API Key (gsk_...)", type="password", key="manual_groq_key")
            if manual_groq:
                os.environ["GROQ_API_KEY"] = manual_groq
                st.rerun()

        selected_model = st.selectbox(
            "Groq Modell auswählen:",
            ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma2-9b-it"],
            index=0,
            key="groq_selected_model"
        )

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1, 1, 2])
    with col_ctrl1:
        if st.button("🟢 ALLE ZORDS EIN"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = True
            st.rerun()
    with col_ctrl2:
        if st.button("🔴 ALLE ZORDS AUS"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = False
            st.rerun()
    with col_ctrl3:
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:5px;'>Aktive Zords antworten blitzschnell über die Groq API.</p>", unsafe_allow_html=True)

    st.markdown("---")
    
    col_zords, col_chat = st.columns([1, 1.8])

    with col_zords:
        st.markdown("### 🤖 EINHEITEN STATUS")
        for zname, zdata in st.session_state.zord_status.items():
            sub_c1, sub_c2 = st.columns([3, 1])
            domain_info = zdata.get("domain", "Sektor-Einheit")
            is_active = zdata.get("active", True)
            
            with sub_c1:
                status_color = "badge-cyan" if is_active else "badge-gold"
                status_text = "AKTIV" if is_active else "OFF"
                st.markdown(f"**{zname}** <span class='{status_color}'>{status_text}</span><br><span style='font-size:0.75rem; color:#8ab4f8;'>Domäne: {domain_info}</span>", unsafe_allow_html=True)
            with sub_c2:
                btn_label = "🔌" if is_active else "⚡"
                if st.button(btn_label, key=f"toggle_{zname}"):
                    st.session_state.zord_status[zname]["active"] = not is_active
                    st.rerun()

    with col_chat:
        st.markdown("### 💬 GROQ GÖTTER-DISKURS CHAT")
        
        chat_container = st.container(height=400)
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["sender"] == "Commander":
                    st.markdown(f"<div class='card-chat' style='border-color: #ff007f;'><b>👤 Commander (Du):</b> {msg['text']}</div>", unsafe_allow_html=True)
                elif msg["sender"] == "System":
                    st.markdown(f"<div class='card-chat' style='border-color: #ffaa00;'><b>⚙️ System:</b> {msg['text']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='card-chat'><b>🪐 {msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)

        user_input = st.text_input("Befehl oder Frage an die Groq-Zords:", key="zord_chat_input")
        
        col_send1, col_send2 = st.columns([1, 1])
        with col_send1:
            if st.button("🗣️ GROQ-MEINUNGEN EINHOLEN"):
                if user_input:
                    st.session_state.chat_messages.append({"sender": "Commander", "text": user_input})
                    
                    groq_client = None
                    active_groq_key = get_groq_key()
                    
                    if GROQ_AVAILABLE and active_groq_key:
                        try:
                            groq_client = Groq(api_key=active_groq_key)
                        except Exception as e:
                            st.error(f"Fehler beim Initialisieren des Groq-Clients: {e}")

                    chosen_model = st.session_state.get("groq_selected_model", "llama3-8b-8192")

                    for zname, zdata in st.session_state.zord_status.items():
                        if zdata.get("active", True):
                            response_text = ""
                            z_prompt = zdata.get("prompt", f"Du bist {zname}. Antworte kurz und prägnant.")
                            
                            if groq_client:
                                try:
                                    completion = groq_client.chat.completions.create(
                                        model=chosen_model,
                                        messages=[
                                            {"role": "system", "content": z_prompt},
                                            {"role": "user", "content": user_input}
                                        ],
                                        temperature=0.7,
                                        max_tokens=150
                                    )
                                    response_text = completion.choices[0].message.content
                                except Exception as e:
                                    response_text = f"[{zname} - Groq Fehler]: {str(e)}"
                            else:
                                response_text = f"[{zname}]: Kein gültiger Groq API-Schlüssel gefunden. Bitte oben im Menü eintragen."

                            st.session_state.chat_messages.append({"sender": zname, "text": response_text})
                    
                    st.rerun()

        with col_send2:
            if st.button("🗑️ CHAT LÖSCHEN"):
                st.session_state.chat_messages = [{"sender": "System", "text": "Chat-Speicher gereinigt. Bereit für neue Befehle."}]
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")

# ==============================================================================
# ÜBRIGE FRAMES
# ==============================================================================
elif st.session_state.current_frame in ["frame_4", "frame_5", "frame_6"]:
    st.markdown(f"<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR {st.session_state.current_frame.split('_')[1]}</h1>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")
