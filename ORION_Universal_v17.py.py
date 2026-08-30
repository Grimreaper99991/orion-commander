# ==============================================================================
# ORION COMMAND CORE v33.0 (TRUE FIXED HTML OVERLAY HARDENED)
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

# CSS für absolut positionierte Overlays direkt auf dem Bild
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    * { font-family: 'JetBrains Mono', monospace !important; }
    .stApp { background-color: #040404; color: #FFFFFF; }
    .block-container { padding: 0.5rem !important; max-width: 1100px !important; }

    /* Der Container zwingt alle Kinder, sich nur am Bild auszurichten */
    .canvas-wrapper {
        position: relative;
        width: 100%;
        display: block;
        overflow: hidden;
        border-radius: 8px;
    }

    .canvas-wrapper img.bg-img {
        width: 100%;
        height: auto;
        display: block;
    }

    /* Hotspot-Buttons absolut AUF dem Bild */
    .hotspot-btn {
        position: absolute;
        background: rgba(0, 255, 0, 0.15);
        border: 2px dashed #00FF00;
        color: #00FF00;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        z-index: 99;
    }
    .hotspot-btn:hover {
        background: rgba(0, 255, 0, 0.7);
        color: #000000;
        box-shadow: 0 0 20px #00FF00;
    }

    /* Hotspot Passwort-Input AUF dem Bild */
    .hotspot-input {
        position: absolute;
        z-index: 99;
    }
</style>
""", unsafe_allow_html=True)

# Helper-Funktion zum Rendern des Bildes mit absolute Buttons
def render_frame_with_overlay(img_name, buttons_config=None):
    img_path = get_asset_path(img_name)
    img_b64 = get_base64_image(img_path)
    
    if not img_b64:
        st.error(f"Asset fehlt: {img_name}")
        return

    # Container-Eröffnung
    html_content = f'<div class="canvas-wrapper"><img src="data:image/jpeg;base64,{img_b64}" class="bg-img">'
    html_content += '</div>'
    
    st.markdown(html_content, unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN OVERLAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img_path = get_asset_path("Frame 0.jpg")
    img_b64 = get_base64_image(img_path)
    
    if img_b64:
        st.markdown(f'''
        <div class="canvas-wrapper">
            <img src="data:image/jpeg;base64,{img_b64}" class="bg-img">
        </div>
        ''', unsafe_allow_html=True)

    # Eingabefeld & Login-Trigger
    c1, c2 = st.columns([1, 1])
    with c2:
        pwd = st.text_input("", type="password", placeholder="Master Code (Auth-x)", key="pwd_input")
        if st.button("ENTER CORE ➔", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    render_frame_with_overlay("Frame 1.jpg")
    
    # Dashboard-Button fix auf dem Frame
    if st.button("➔ DASHBOARD (GALACTA HUB)", key="btn_f1", use_container_width=True):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 2: DASHBOARD SEKTOREN
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    render_frame_with_overlay("Frame 2.jpg")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("Zord Crew", use_container_width=True): navigate_to("frame_3")
    with c2:
        if st.button("Zeus Details", use_container_width=True): navigate_to("frame_4")
    with c3:
        if st.button("Funkraum", use_container_width=True): navigate_to("frame_5")
    with c4:
        if st.button("Ghost Room", use_container_width=True): navigate_to("frame_6")

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_num = st.session_state.current_frame.split("_")[1]
    render_frame_with_overlay(f"Frame {frame_num}.jpg")
    
    if st.button("↩ Zurück zum Haupt-Dashboard", use_container_width=True):
        navigate_to("frame_2")
