# ==============================================================================
# ORION COMMAND CORE v24.0 (FIGMA UI-DESIGN MATCH)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# FIGMA STYLES: Technos & JetBrains Mono Vibe // Custom Color Palette
# ==============================================================================

import streamlit as st
import datetime
import os
try:
    from groq import Groq
except ImportError:
    st.error("Bitte füge 'groq' zu deiner requirements.txt hinzu!")

# 1. STREAMLIT CONFIG & DESIGN SYSTEM
st.set_page_config(
    page_title="ORION BASE COMMANDER",
    page_icon="🪐",
    layout="wide"
)

# Custom CSS basierend auf deinen Figma Frame-Farben und -Shapes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #111111 !important; border-right: 2px solid #262626; }
    
    /* Cyber Card Base Container */
    .cyber-frame {
        background-color: #111111;
        border: 2px solid #262626;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.8);
    }
    
    /* Buttons im Cut-Corner Sci-Fi Style */
    .stButton > button {
        background-color: #262626 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        border-radius: 4px !important;
        font-weight: bold !important;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 10px #00FF00;
    }

    /* Zord Specific Colors */
    .z-zeus { color: #eab308; font-weight: bold; }
    .z-shadow { color: #95C5F4; font-weight: bold; }
    .z-medusa { color: #10b981; font-weight: bold; }
    .z-storm { color: #06b6d4; font-weight: bold; }
    .z-grimreaper { color: #dc2626; font-weight: bold; }
    .z-light { color: #FFFFFF; font-weight: bold; }
    .z-titan { color: #f97316; font-weight: bold; }
    .z-spider { color: #2563eb; font-weight: bold; }
    .z-orion { color: #00FF00; font-weight: bold; }
    .z-ghost { color: #a855f7; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# API KEY SETUP
primary_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
groq_client = Groq(api_key=primary_key) if primary_key else None

# SESSION STATES (NAVIGATION)
if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"  # Startet bei Frame 0 (Login Gate)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

MASTER_CODE = "Auth-x"

# ZORD DEFINITIONS
ZORDS = {
    "zeus": {"name": "ZEUS", "class": "z-zeus", "desc": "Quantum Code Core"},
    "shadow": {"name": "SHADOW", "class": "z-shadow", "desc": "Security Hub"},
    "medusa": {"name": "MEDUSA", "class": "z-medusa", "desc": "UI/UX Vision"},
    "storm": {"name": "STORM", "class": "z-storm", "desc": "Real-Time Signal"},
    "grimreaper": {"name": "GRIMREAPER", "class": "z-grimreaper", "desc": "Executioner Engine"},
    "light": {"name": "LIGHT", "class": "z-light", "desc": "Logic Core"},
    "titan": {"name": "TITAN", "class": "z-titan", "desc": "Prompt Craft"},
    "spider": {"name": "SPIDER", "class": "z-spider", "desc": "Crawler Scan"},
    "orion": {"name": "ORION", "class": "z-orion", "desc": "Prime Core"},
    "ghost": {"name": "GHOST", "class": "z-ghost", "desc": "Game Simulator"}
}

# HELPER SWITCH FRAME
def navigate_to(frame_id):
    st.session_state.current_frame = frame_id
    st.rerun()

# ==============================================================================
# FRAME 0: LOGIN GATEWAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://i.imgur.com/v8tT9Yf.png", use_container_width=True, caption="BIKER CORE") # Stilisierter Biker
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #00FF00;'>Hello !</h2>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #00FF00; margin-top:-20px;'>Welcome To Orions Base</h1>", unsafe_allow_html=True)
        
        pwd = st.text_input("Enter Password", type="password", key="gate_pwd")
        if st.button("Enter", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")

# ==============================================================================
# FRAME 1: GALACTA MAIN HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    col_left, col_right = st.columns([1, 2])
    with col_left:
        st.markdown("<h2 style='color: #95C5F4;'>GALACTA</h2>", unsafe_allow_html=True)
        st.caption("Welcome to Orions Base")
        st.write("The mission of Sci-Fi World is to teach and inspire people. Species of all ages with an uplifting vision of the future.")
        
        if st.button("Dashboard", use_container_width=True):
            navigate_to("frame_2")
            
    with col_right:
        st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #95C5F4;'>EXLAR HUB</h3>", unsafe_allow_html=True)
        st.write("Base Status: ONLINE // Zords Ready: 10/10")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 style='color: #00FF00;'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF00;'>Navigation Vom Dashboard</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
    if st.button("➔ Zord Crew", use_container_width=True): navigate_to("frame_3")
    if st.button("➔ Zeus Details", use_container_width=True): navigate_to("frame_4")
    if st.button("➔ Funkraum", use_container_width=True): navigate_to("frame_5")
    if st.button("➔ Ghost Room Simulator", use_container_width=True): navigate_to("frame_6")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3: ZORD CREW
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 style='color: #00FF00;'>zord crew</h1>", unsafe_allow_html=True)
    
    col_list, col_vis = st.columns([2, 1])
    with col_list:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<span class='z-zeus'>zeus</span> - Code Core", unsafe_allow_html=True)
            st.markdown("<span class='z-medusa'>medusa</span> - UI/UX Vision", unsafe_allow_html=True)
            st.markdown("<span class='z-grimreaper'>grimreaper</span> - Code Cleaner", unsafe_allow_html=True)
            st.markdown("<span class='z-titan'>titan</span> - Prompt Craft", unsafe_allow_html=True)
            st.markdown("<span class='z-orion'>orion</span> - Main AI", unsafe_allow_html=True)
        with c2:
            st.markdown("<span class='z-shadow'>shadow</span> - Security", unsafe_allow_html=True)
            st.markdown("<span class='z-storm'>storm</span> - Audio Signal", unsafe_allow_html=True)
            st.markdown("<span class='z-light'>light</span> - Knowledge Base", unsafe_allow_html=True)
            st.markdown("<span class='z-spider'>spider</span> - Crawler", unsafe_allow_html=True)
            st.markdown("<span class='z-ghost'>ghost</span> - Gaming Build", unsafe_allow_html=True)
    
    st.br = st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Zurück Zur Navigation"): navigate_to("frame_2")

# ==============================================================================
# FRAME 4: ZEUS DETAILS
# ==============================================================================
elif st.session_state.current_frame == "frame_4":
    st.markdown("<h1 style='color: #00FF00;'>Zeus Details</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
    st.info("⚡ ZEUS QUANTUM TERMINAL: Bereit für Python-Code-Generierung & Refactoring.")
    st.text_area("Zeus Code-Terminal Input:", key="zeus_in")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Zurück Zur Navigation"): navigate_to("frame_2")

# ==============================================================================
# FRAME 5: FUNKRAUM
# ==============================================================================
elif st.session_state.current_frame == "frame_5":
    st.markdown("<h1 style='color: #00FF00;'>Funkraum</h1>", unsafe_allow_html=True)
    st.caption("Kommunikations Zentrale")
    
    st.audio_input("Funkspruch absetzen:")
    
    if st.button("Zurück Zur Navigation"): navigate_to("frame_2")

# ==============================================================================
# FRAME 6: GHOST GAME SIMULATOR
# ==============================================================================
elif st.session_state.current_frame == "frame_6":
    st.markdown("<h1 style='color: #00FF00;'>Ghost Game Simulator</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cyber-frame'>", unsafe_allow_html=True)
    st.write("🟣 GHOST ZORD: ARPG Build-Optimizer & Loot-Strategie geladen.")
    st.text_input("Gegenstand / Skill / Build eingeben:")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Zurück Zur Navigation"): navigate_to("frame_2")
