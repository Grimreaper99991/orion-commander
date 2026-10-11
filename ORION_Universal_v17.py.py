# ==============================================================================
# ORION COMMAND CORE v70.0 - JARVIS & GOD-ZORD SYNTHESIS MATRIX
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
    page_title="ORION COMMAND CORE // JARVIS PROTOCOL",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

# Die 10 Götter-Zords + JARVIS als übergeordnetes Master-System
DEFAULT_ZORDS = {
    "JARVIS (Core OS)": {
        "domain": "Zentrale Intellekt-Synthese",
        "active": True,
        "prompt": "Du bist J.A.R.V.I.S., das übergeordnete, sarkastisch-elegante und hochintelligente KI-System von Commander Auth-x. Du bündelst die Stimmen der 10 Götter-Zords, analysierst Daten messerscharf und sprichst mit britischem Understatement und absoluter Loyalität."
    },
    "Zeus Prime": {
        "domain": "Anführer & Blitze", 
        "active": True, 
        "prompt": "Du bist Zeus Prime, der autoritäre Anführer der Götter-Zords. Klare Befehle, kühle Autorität, max. 2 Sätze."
    },
    "Chronos Titan": {
        "domain": "Zeit & Taktik", 
        "active": True, 
        "prompt": "Du bist Chronos Titan, der Herr über Zeit und Voraussicht. Analysiere das zeitliche Risiko, max. 2 Sätze."
    },
    "Ares War-Lord": {
        "domain": "Kampf & Strategie", 
        "active": True, 
        "prompt": "Du bist Ares War-Lord, die offensive Kampf-KI. Direkt, aggressiv, lösungsorientiert, max. 2 Sätze."
    },
    "Poseidon Core": {
        "domain": "Ozeane & Strömung", 
        "active": True, 
        "prompt": "Poseidon Core, Herr der Datenströme. Metaphorisch, tiefgründig, max. 2 Sätze."
    },
    "Hades Void": {
        "domain": "Schatten & Sicherheit", 
        "active": True, 
        "prompt": "Hades Void, Schatten- und Sicherheits-KI. Pragmatisch, düster, warne vor Sicherheitsrisiken, max. 2 Sätze."
    },
    "Apollo Solar": {
        "domain": "Energie & Licht", 
        "active": True, 
        "prompt": "Apollo Solar, Energie- und Licht-KI. Optimistisch, energiegeladen, max. 2 Sätze."
    },
    "Athena Shield": {
        "domain": "Weisheit & Schutz", 
        "active": True, 
        "prompt": "Athena Shield, Göttin der Logik. Brillant, analytisch, schütze vor Fehlern, max. 2 Sätze."
    },
    "Hephaestus Forge": {
        "domain": "Technik & Waffen", 
        "active": True, 
        "prompt": "Hephaestus Forge, Meister der Schmiede und Hardware. Technisch, code-fokussiert, max. 2 Sätze."
    },
    "Hermes Speed": {
        "domain": "Geschwindigkeit & Info", 
        "active": True, 
        "prompt": "Hermes Speed, Aufklärungs- und Echtzeit-KI. Schnell, hektisch, direkt auf den Punkt, max. 2 Sätze."
    },
    "Artemis Hunt": {
        "domain": "Präzision & Aufklärung", 
        "active": True, 
        "prompt": "Artemis Hunt, Jägerin und Präzisions-KI. Zielgerichtet, aufmerksam, max. 2 Sätze."
    }
}

if "zord_status" not in st.session_state or not isinstance(st.session_state.zord_status, dict) or "JARVIS (Core OS)" not in st.session_state.zord_status:
    st.session_state.zord_status = DEFAULT_ZORDS

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"sender": "JARVIS", "text": "Guten Tag, Commander. Alle 10 Götter-Zords sind gekoppelt. Das JARVIS-Protokoll ist voll operational."}
    ]

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# STYLING (IRON MAN HUD & CYBERPUNK AESTHETIC)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, h4, .cyber-font { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background: radial-gradient(circle at 50% 10%, rgba(0, 240, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 10% 90%, rgba(255, 170, 0, 0.08) 0%, transparent 40%),
                    #020408;
        background-attachment: fixed;
        color: #e2e8f0;
    }

    .block-container {
        padding: 2rem !important;
        max-width: 1400px !important;
    }

    .card-jarvis {
        background: rgba(10, 20, 35, 0.9);
        border: 1px solid #00f0ff;
        border-left: 6px solid #00f0ff;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .card-zord {
        background: rgba(15, 15, 25, 0.85);
        border: 1px solid rgba(255, 170, 0, 0.5);
        border-left: 6px solid #ffaa00;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(255, 170, 0, 0.15) 100%) !important;
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
        background: linear-gradient(135deg, #00f0ff 0%, #ffaa00 100%) !important;
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
    st.markdown("<h1 class='cyber-font' style='text-align: center; color: #00f0ff;'>🪐 ORION COMMAND CORE // JARVIS HUD</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Auth-x...", key="pwd_input")
        if st.button("SYSTEM ACCESS ➔"):
            if pwd == MASTER_CODE: navigate_to("frame_1")
            else: st.error("ACCESS DENIED: UNKNOWN SIGNATURE")

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
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>COMMAND DASHBOARD // JARVIS OVERVIEW</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🤖 JARVIS & GÖTTER-ZORD KONTROLLE"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DIAGNOSTIK"): navigate_to("frame_4")
    with c2:
        if st.button("📡 FUNKRAUM"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: JARVIS & GÖTTER-ZORD SYNTHESIS CHAT
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 03 // JARVIS & GOD-ZORD MATRIX</h1>", unsafe_allow_html=True)
    
    def get_groq_key():
        try:
            if "GROQ_API_KEY" in st.secrets:
                return st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
        if os.environ.get("GROQ_API_KEY"):
            return os.environ.get("GROQ_API_KEY")
        return None

    with st.expander("⚙️ JARVIS Core & Groq Konfiguration", expanded=False):
        current_groq_key = get_groq_key()
        if current_groq_key:
            st.success("Groq Kernverbindung aktiv & stabil.")
        else:
            st.warning("Kein Groq Key gefunden. Bitte eintragen:")
            manual_groq = st.text_input("Groq API Key (gsk_...)", type="password", key="manual_groq_key")
            if manual_groq:
                os.environ["GROQ_API_KEY"] = manual_groq
                st.rerun()

        selected_model = st.selectbox(
            "Groq Modell auswählen:",
            ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
            index=0,
            key="groq_selected_model"
        )

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1, 1, 2])
    with col_ctrl1:
        if st.button("🟢 ALLE EINHEITEN EIN"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = True
            st.rerun()
    with col_ctrl2:
        if st.button("🔴 ALLE EINHEITEN AUS"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = False
            st.rerun()
    with col_ctrl3:
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:5px;'>JARVIS leitet den Diskurs und bündelt die Götter-Zords.</p>", unsafe_allow_html=True)

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
        st.markdown("### 💬 JARVIS & GÖTTER-DISKURS")
        
        chat_container = st.container(height=450)
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["sender"] == "Commander":
                    st.markdown(f"<div class='card-jarvis' style='border-color: #ff007f; border-left-color: #ff007f;'><b>👤 Commander (Auth-x):</b> {msg['text']}</div>", unsafe_allow_html=True)
                elif msg["sender"] == "JARVIS":
                    st.markdown(f"<div class='card-jarvis'><b>🤖 JARVIS (Core OS):</b> {msg['text']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='card-zord'><b>🪐 {msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)

        user_input = st.text_input("Befehl an JARVIS & die Götter-Zords:", key="jarvis_chat_input")
        
        col_send1, col_send2 = st.columns([1, 1])
        with col_send1:
            if st.button("🗣️ JARVIS ANALYSE STARTEN"):
                if user_input:
                    st.session_state.chat_messages.append({"sender": "Commander", "text": user_input})
                    
                    groq_client = None
                    active_groq_key = get_groq_key()
                    
                    if GROQ_AVAILABLE and active_groq_key:
                        try:
                            groq_client = Groq(api_key=active_groq_key)
                        except Exception as e:
                            st.error(f"Groq Init Fehler: {e}")

                    chosen_model = st.session_state.get("groq_selected_model", "llama-3.3-70b-versatile")

                    # 1. Zuerst geben die aktiven Götter-Zords ihre Einschätzung ab
                    for zname, zdata in st.session_state.zord_status.items():
                        if zname != "JARVIS (Core OS)" and zdata.get("active", True):
                            response_text = ""
                            z_prompt = zdata.get("prompt", f"Du bist {zname}.")
                            
                            if groq_client:
                                try:
                                    completion = groq_client.chat.completions.create(
                                        model=chosen_model,
                                        messages=[
                                            {"role": "system", "content": z_prompt},
                                            {"role": "user", "content": user_input}
                                        ],
                                        temperature=0.7,
                                        max_tokens=100
                                    )
                                    response_text = completion.choices[0].message.content
                                except Exception as e:
                                    response_text = f"[Fehler]: {str(e)}"
                            else:
                                response_text = "[Offline-Modus]: Keine API-Verbindung."

                            st.session_state.chat_messages.append({"sender": zname, "text": response_text})

                    # 2. JARVIS fasst als Master-KI alles zusammen
                    if st.session_state.zord_status.get("JARVIS (Core OS)", {}).get("active", True):
                        jarvis_prompt = st.session_state.zord_status["JARVIS (Core OS)"]["prompt"]
                        jarvis_response = ""
                        if groq_client:
                            try:
                                completion = groq_client.chat.completions.create(
                                    model=chosen_model,
                                    messages=[
                                        {"role": "system", "content": jarvis_prompt},
                                        {"role": "user", "content": f"Der Commander sagte: '{user_input}'. Fasse die Lage zusammen und gib eine finale, elegante JARVIS-Empfehlung ab."}
                                    ],
                                    temperature=0.7,
                                    max_tokens=150
                                )
                                jarvis_response = completion.choices[0].message.content
                            except Exception as e:
                                jarvis_response = f"Sir, ein Kommunikationsfehler ist aufgetreten: {e}"
                        else:
                            jarvis_response = "Sir, ohne aktiven API-Key kann ich die Götter-Zords nicht bündeln."

                        st.session_state.chat_messages.append({"sender": "JARVIS", "text": jarvis_response})

                    st.rerun()

        with col_send2:
            if st.button("🗑️ SYSTEM-LOG REINIGEN"):
                st.session_state.chat_messages = [{"sender": "JARVIS", "text": "Speicher bereinigt, Sir. Bereit für den nächsten Auftrag."}]
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
