# ==============================================================================
# ORION COMMAND CORE v24.0 (EXACT FIGMA 1:1 EXECUTION)
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# ASSETS PATH: assets/Frame 0.jpg - Frame 7.jpg
# ==============================================================================

import streamlit as st
import os

# 1. PAGE SETUP & GLOBAL STYLES
st.set_page_config(
    page_title="ORION BASE COMMANDER",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling für JetBrains Mono / Technos Vibe & Cyberpunk UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { 
        background-color: #040404; 
        color: #FFFFFF; 
    }
    
    /* Buttons im Neongrün Sci-Fi Look */
    .stButton > button {
        background-color: #262626 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        border-radius: 4px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #00FF00;
    }

    /* Zord Crew Custom Font Colors */
    .z-zeus { color: #eab308; font-weight: bold; font-size: 22px; }
    .z-shadow { color: #95C5F4; font-weight: bold; font-size: 22px; }
    .z-medusa { color: #10b981; font-weight: bold; font-size: 22px; }
    .z-storm { color: #06b6d4; font-weight: bold; font-size: 22px; }
    .z-grimreaper { color: #dc2626; font-weight: bold; font-size: 22px; }
    .z-light { color: #FFFFFF; font-weight: bold; font-size: 22px; }
    .z-titan { color: #f97316; font-weight: bold; font-size: 22px; }
    .z-spider { color: #2563eb; font-weight: bold; font-size: 22px; }
    .z-orion { color: #00FF00; font-weight: bold; font-size: 22px; }
    .z-ghost { color: #a855f7; font-weight: bold; font-size: 22px; }
    
    /* Input Styling */
    .stTextInput input {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #262626 !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. SESSION STATE MANAGEMENT
if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

def load_asset(filename):
    """Sicherer Bildlader für GitHub Assets"""
    paths = [
        f"assets/{filename}",
        f"assets/{filename.lower()}",
        f"assets/{filename.replace(' ', '_')}"
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

# ==============================================================================
# FRAME 0: LOGIN GATEWAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img_path = load_asset("Frame 0.jpg")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        if img_path:
            st.image(img_path, use_container_width=True)
        else:
            st.info("🖼️ assets/Frame 0.jpg geladen")
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #00FF00;'>Hello !</h2>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #00FF00; margin-top:-20px;'>Welcome To Orions Base</h1>", unsafe_allow_html=True)
        
        pwd = st.text_input("Enter Password", type="password", key="login_pwd")
        if st.button("Enter", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED: Ungültiger Master Code!")

# ==============================================================================
# FRAME 1: GALACTA MAIN HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img_path = load_asset("Frame 1.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    # NUR DIESER BUTTON FÜHRT ZUR DASHBOARD NAVIGATION (FRAME 2)
    if st.button("➔ Zum Dashboard", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img_path = load_asset("Frame 2.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<h2 style='color: #00FF00;'>Sektor-Auswahl</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Zord Crew", use_container_width=True): navigate_to("frame_3")
    with col2:
        if st.button("Zeus Details", use_container_width=True): navigate_to("frame_4")
    with col3:
        if st.button("Funkraum", use_container_width=True): navigate_to("frame_5")
    with col4:
        if st.button("Ghost Room Simulator", use_container_width=True): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: ZORD CREW
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    img_path = load_asset("Frame 3.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ Zurück Zur Navigation", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 4: ZEUS DETAILS
# ==============================================================================
elif st.session_state.current_frame == "frame_4":
    img_path = load_asset("Frame 4.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ Zurück Zur Navigation", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 5: FUNKRAUM
# ==============================================================================
elif st.session_state.current_frame == "frame_5":
    img_path = load_asset("Frame 5.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ Zurück Zur Navigation", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 6: GHOST GAME SIMULATOR
# ==============================================================================
elif st.session_state.current_frame == "frame_6":
    img_path = load_asset("Frame 6.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ Zurück Zur Navigation", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 7: DESIGN SYSTEM & PALETTE
# ==============================================================================
elif st.session_state.current_frame == "frame_7":
    img_path = load_asset("Frame 7.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ Zurück Zur Navigation", use_container_width=True):
        navigate_to("frame_2")
