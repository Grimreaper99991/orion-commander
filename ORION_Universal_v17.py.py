# ==============================================================================
# ORION COMMAND CORE v55.1 - GOD ZORD MULTI-AGENT CHAT MATRIX (FIXED)
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ==============================================================================

import streamlit as st
import os

st.set_page_config(
    page_title="ORION COMMAND CORE",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

# Initialisierung der 10 Götter-Zords & Chat-Historie
if "zord_status" not in st.session_state:
    st.session_state.zord_status = {
        "Zeus Prime": {"domain": "Anführer & Blitze", "active": True, "style": "Autoritär und entscheidend"},
        "Chronos Titan": {"domain": "Zeit & Taktik", "active": True, "style": "Analytisch und vorausschauend"},
        "Ares War-Lord": {"domain": "Kampf & Strategie", "active": True, "style": "Aggressiv und direkt"},
        "Poseidon Core": {"domain": "Ozeane & Strömung", "active": True, "style": "Tiefgründig und unberechenbar"},
        "Hades Void": {"domain": "Schatten & Geheimnisse", "active": True, "style": "Düster und pragmatisch"},
        "Apollo Solar": {"domain": "Energie & Licht", "active": True, "style": "Strahlend und optimistisch"},
        "Athena Shield": {"domain": "Weisheit & Schutz", "active": True, "style": "Klug und taktvoll"},
        "Hephaestus Forge": {"domain": "Technik & Waffen", "active": True, "style": "Technisch und handwerklich"},
        "Hermes Speed": {"domain": "Geschwindigkeit & Info", "active": True, "style": "Schnell und hektisch"},
        "Artemis Hunt": {"domain": "Präzision & Aufklärung", "active": True, "style": "Wachsam und präzise"}
    }

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"sender": "System", "text": "ORION Götter-Zord Matrix online. Alle Einheiten bereit für den kollektiven Diskurs."}
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

    .card-cyan {
        background: rgba(10, 25, 41, 0.85);
        border: 1px solid #00f0ff;
        border-left: 5px solid #00f0ff;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.15);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
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

    .stTextInput input {
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
        if st.button("🪐 ZORD CREW & GÖTTER-CHAT"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DETAILS"): navigate_to("frame_4")
    with c2:
        if st.button("📡 FUNKRAUM"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: DIE 10 GÖTTER-ZORDS + MULTI-AGENTEN CHAT
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 03 // GÖTTER-ZORD MATRIX & CHAT</h1>", unsafe_allow_html=True)
    
    # Steuerung: Alle ein- oder ausschalten
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
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:5px;'>Aktiviere Einheiten, um ihre Meinungen einzuholen.</p>", unsafe_allow_html=True)

    st.markdown("---")
    
    # Layout: Links die Zord-Schalter, Rechts der Götter-Chat
    col_zords, col_chat = st.columns([1, 1.8])

    with col_zords:
        st.markdown("### 🤖 EINHEITEN STATUS")
        for zname, zdata in st.session_state.zord_status.items():
            sub_c1, sub_c2 = st.columns([3, 1])
            with sub_c1:
                status_color = "badge-cyan" if zdata["active"] else "badge-gold"
                status_text = "AKTIV" if zdata["active"] else "OFF"
                st.markdown(f"**{zname}** <span class='{status_color}'>{status_text}</span><br><span style='font-size:0.75rem; color:#8ab4f8;'>Domäne: {zdata['domain']}</span>", unsafe_allow_html=True)
            with sub_c2:
                btn_label = "🔌" if zdata["active"] else "⚡"
                if st.button(btn_label, key=f"toggle_{zname}"):
                    st.session_state.zord_status[zname]["active"] = not zdata["active"]
                    st.rerun()

    with col_chat:
        st.markdown("### 💬 GÖTTER-DISKURS CHAT")
        
        chat_container = st.container(height=400)
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["sender"] == "Commander":
                    st.markdown(f"<div class='card-chat' style='border-color: #ff007f;'><b>👤 Commander (Du):</b> {msg['text']}</div>", unsafe_allow_html=True)
                elif msg["sender"] == "System":
                    st.markdown(f"<div class='card-chat' style='border-color: #ffaa00;'><b>⚙️ System:</b> {msg['text']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='card-chat'><b>🪐 {msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)

        user_input = st.text_input("Befehl oder Frage an die Götter-Zords:", key="zord_chat_input")
        
        col_send1, col_send2 = st.columns([1, 1])
        with col_send1:
            if st.button("🗣️ MEINUNGEN EINHOLEN"):
                if user_input:
                    st.session_state.chat_messages.append({"sender": "Commander", "text": user_input})
                    
                    for zname, zdata in st.session_state.zord_status.items():
                        if zdata["active"]:
                            response_text = f"Analysiere Anweisung '{user_input}' durch das Prisma von {zdata['domain']}. Unsere Protokolle stehen bereit!"
                            if "Zeus" in zname:
                                response_text = f"Als Anführer befehle ich: Wir setzen '{user_input}' mit voller Härte und Priorität um!"
                            elif "Ares" in zname:
                                response_text = f"Hervorragend! '{user_input}' klingt nach Kampf. Lasst uns angreifen!"
                            elif "Chronos" in zname:
                                response_text = f"Zeitlich gesehen müssen wir bei '{user_input}' exakt vorausplanen. Keine Fehler."
                            elif "Hephaestus" in zname:
                                response_text = f"Die Technik für '{user_input}' wird umgehend in der Schmiede vorbereitet."
                            
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
