# ==============================================================================
# ORION COMMAND CORE v26.0 (1:1 FIGMA PIXEL OVERLAY)
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ASSETS PATH: assets/Frame 0.jpg bis Frame 6.jpg
# ==============================================================================

import streamlit as st
import os

st.set_page_config(
    page_title="ORION BASE COMMANDER",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# GLOBAL STYLES & OVERLAY CANVAS LOGIC
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }
    
    /* Haupt-Canvas Container (Skaliert exakt mit dem Bild) */
    .figma-canvas {
        position: relative;
        width: 100%;
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .figma-bg {
        width: 100%;
        display: block;
        border-radius: 8px;
    }

    /* Unsichtbare / Neon-Interaktive Klickzonen */
    .overlay-btn {
        position: absolute;
        z-index: 10;
    }

    /* Streamlit Input Styling Transparenz Anpassung */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 4px !important;
    }
    
    /* Streamlit Custom Transparent Overlay Buttons */
    .stButton > button {
        background-color: rgba(0, 255, 0, 0.2) !important;
        color: #00FF00 !important;
        border: 2px solid #00FF00 !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #00FF00;
    }
</style>
""", unsafe_allow_html=True)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

def get_asset_path(filename):
    paths = [f"assets/{filename}", f"assets/{filename.lower()}", f"assets/{filename.replace(' ', '_')}"]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

# ==============================================================================
# FRAME 0: LOGIN OVERLAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img = get_asset_path("Frame 0.jpg")
    
    st.markdown("<div class='figma-canvas'>", unsafe_allow_html=True)
    if img:
        st.image(img, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Eingabefeld & Enter Button exakt auf die weißen Felder positioniert
    col1, col2 = st.columns([1.2, 1])
    with col2:
        st.markdown("<div style='margin-top: -300px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Password...", key="login_pwd")
        if st.button("ENTER CORE", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA MAIN HUB (Dashboard Button exakt über der grünen Fläche)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img = get_asset_path("Frame 1.jpg")
    
    st.markdown("<div class='figma-canvas'>", unsafe_allow_html=True)
    if img:
        st.image(img, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Der Klick-Button legt sich genau über den neongrünen Dashboard-Button
    c1, c2, c3 = st.columns([0.45, 0.45, 1])
    with c1:
        st.markdown("<div style='margin-top: -240px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("DASHBOARD ➔", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img = get_asset_path("Frame 2.jpg")
    
    st.markdown("<div class='figma-canvas'>", unsafe_allow_html=True)
    if img:
        st.image(img, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Positionierung direkt auf der Klick-Liste des Dashboards
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("<div style='margin-top: -220px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("➔ Zord Crew", use_container_width=True): navigate_to("frame_3")
        if st.button("➔ Zeus Details", use_container_width=True): navigate_to("frame_4")
        if st.button("➔ Funkraum", use_container_width=True): navigate_to("frame_5")
        if st.button("➔ Ghost Room Simulator", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME (Zurück-Button exakt über Text)
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_id = st.session_state.current_frame
    frame_num = frame_id.split("_")[1]
    img = get_asset_path(f"Frame {frame_num}.jpg")
    
    st.markdown("<div class='figma-canvas'>", unsafe_allow_html=True)
    if img:
        st.image(img, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Zurück-Button wird im unteren Drittel direkt über deinen Figma-Text gelegt
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("<div style='margin-top: -140px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("↩ Zurück Zur Navigation", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
