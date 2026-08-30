# ==============================================================================
# ORION COMMAND CORE v31.0 (FIXED SYNTAX & TRUE HTML ABSOLUTE OVERLAY)
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ASSETS PATH: assets/Frame 0.jpg bis Frame 6.jpg
# ==============================================================================

import streamlit as st
import os
import base64

st.set_page_config(
    page_title="ORION BASE COMMANDER",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

def get_asset_path(filename):
    paths = [f"assets/{filename}", f"assets/{filename.lower()}", f"assets/{filename.replace(' ', '_')}"]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# Styling für 1:1 echte Layer-Überlagerung
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    * { font-family: 'JetBrains Mono', monospace !important; }
    .stApp { background-color: #040404; color: #FFFFFF; }
    .block-container { padding: 1rem !important; max-width: 1000px !important; }
    
    /* Container hält das Bild als Basis */
    .overlay-container {
        position: relative;
        width: 100%;
        display: inline-block;
    }
    
    .overlay-container img {
        width: 100%;
        display: block;
        border-radius: 8px;
    }

    /* Streamlit Eingabefelder / Buttons Anpassung */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 2px solid #00FF00 !important;
        border-radius: 4px !important;
    }

    .stButton > button {
        background-color: rgba(0, 255, 0, 0.15) !important;
        color: #00FF00 !important;
        border: 1px dashed #00FF00 !important;
        font-weight: bold !important;
        height: 100% !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #00FF00;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN OVERLAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img_path = get_asset_path("Frame 0.jpg")
    img_b64 = get_base64_image(img_path)
    
    if img_b64:
        st.markdown(f'<div class="overlay-container"><img src="data:image/jpeg;base64,{img_b64}"></div>', unsafe_allow_html=True)
    elif img_path:
        st.image(img_path, use_container_width=True)

    # Positionierung direkt über Spalten-Offset IN DAS BILD
    col1, col2 = st.columns([1.1, 0.9])
    with col2:
        st.markdown("<div style='margin-top: -35%; position: relative; z-index: 999;'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Passwort eingeben...", key="pwd_input")
        if st.button("ENTER CORE", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA HUB (Dashboard Button Hotspot)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img_path = get_asset_path("Frame 1.jpg")
    img_b64 = get_base64_image(img_path)
    
    if img_b64:
        st.markdown(f'<div class="overlay-container"><img src="data:image/jpeg;base64,{img_b64}"></div>', unsafe_allow_html=True)
    elif img_path:
        st.image(img_path, use_container_width=True)

    c1, c2, c3 = st.columns([0.4, 0.5, 1.1])
    with c1:
        st.markdown("<div style='margin-top: -22%; position: relative; z-index: 999; height: 50px;'>", unsafe_allow_html=True)
        if st.button("➔ DASHBOARD", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD SEKTOREN
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img_path = get_asset_path("Frame 2.jpg")
    img_b64 = get_base64_image(img_path)
    
    if img_b64:
        st.markdown(f'<div class="overlay-container"><img src="data:image/jpeg;base64,{img_b64}"></div>', unsafe_allow_html=True)
    elif img_path:
        st.image(img_path, use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div style='margin-top: -42%; position: relative; z-index: 999;'>", unsafe_allow_html=True)
        if st.button("➔ Zord Crew", use_container_width=True): navigate_to("frame_3")
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        if st.button("➔ Zeus Details", use_container_width=True): navigate_to("frame_4")
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        if st.button("➔ Funkraum", use_container_width=True): navigate_to("frame_5")
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        if st.button("➔ Ghost Room Simulator", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME (Zurück-Button Overlay)
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_num = st.session_state.current_frame.split("_")[1]
    img_path = get_asset_path(f"Frame {frame_num}.jpg")
    img_b64 = get_base64_image(img_path)
    
    if img_b64:
        st.markdown(f'<div class="overlay-container"><img src="data:image/jpeg;base64,{img_b64}"></div>', unsafe_allow_html=True)
    elif img_path:
        st.image(img_path, use_container_width=True)

    col1, col2 = st.columns([0.4, 1])
    with col1:
        st.markdown("<div style='margin-top: -15%; position: relative; z-index: 999;'>", unsafe_allow_html=True)
        if st.button("↩ Zurück", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
