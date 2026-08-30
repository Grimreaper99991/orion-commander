# ==============================================================================
# ORION COMMAND CORE v27.0 (INVISIBLE GHOST OVERLAYS)
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

# Custom Styling: Unsichtbare Buttons & Transparente Eingabefelder
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }

    /* UNSICHTBARE GHOST-BUTTONS OVERLAY */
    .stButton > button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        height: 50px !important;
        cursor: pointer !important;
    }
    
    /* Beim Darüberfahren ein dezent leuchtender Rahmen für Feedback */
    .stButton > button:hover {
        border: 2px dashed #00FF00 !important;
        background-color: rgba(0, 255, 0, 0.08) !important;
    }

    /* Passwort-Feld transparent & exakt angepasst */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.85) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 4px !important;
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
    if img:
        st.image(img, use_container_width=True)
    
    col1, col2 = st.columns([1.3, 1])
    with col2:
        st.markdown("<div style='margin-top: -300px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Password...", key="login_pwd")
        st.markdown("<div style='margin-top: 15px;'>", unsafe_allow_html=True)
        if st.button("ENTER", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")
        st.markdown("</div></div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA MAIN HUB (Unsichtbarer Button über dem Dashboard-Feld)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img = get_asset_path("Frame 1.jpg")
    if img:
        st.image(img, use_container_width=True)
    
    c1, c2, c3 = st.columns([0.45, 0.45, 1])
    with c1:
        st.markdown("<div style='margin-top: -245px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("GHOST_DASHBOARD", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION (Unsichtbare Navigations-Klickzonen)
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img = get_asset_path("Frame 2.jpg")
    if img:
        st.image(img, use_container_width=True)
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("<div style='margin-top: -220px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("BTN_ZORD_CREW", use_container_width=True): navigate_to("frame_3")
        if st.button("BTN_ZEUS", use_container_width=True): navigate_to("frame_4")
        if st.button("BTN_FUNK", use_container_width=True): navigate_to("frame_5")
        if st.button("BTN_GHOST", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME (Unsichtbarer Zurück-Button über Text)
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_id = st.session_state.current_frame
    frame_num = frame_id.split("_")[1]
    img = get_asset_path(f"Frame {frame_num}.jpg")
    
    if img:
        st.image(img, use_container_width=True)
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("<div style='margin-top: -140px; position: relative; z-index: 99;'>", unsafe_allow_html=True)
        if st.button("BTN_RETURN", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
