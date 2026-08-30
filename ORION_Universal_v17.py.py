# ==============================================================================
# ORION COMMAND CORE v28.0 (PIXEL-PERFECT PERCENTAGE OVERLAYS)
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

# Custom Styling für 1:1 absolute Prozent-Overlay-Positionierung
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }

    /* Canvas Wrapper */
    .canvas-container {
        position: relative;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }

    .canvas-image {
        width: 100%;
        display: block;
    }

    /* Absoluter Layer über dem Bild */
    .overlay-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Lässt Klicks durch wo keine Buttons sind */
    }

    /* Einzelne Hotspots Klickbar machen */
    .hotspot {
        position: absolute;
        pointer-events: auto;
    }

    /* Unsichtbare Buttons */
    .ghost-btn .stButton > button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        width: 100% !important;
        height: 100% !important;
        min-height: 45px !important;
        cursor: pointer !important;
    }
    
    .ghost-btn .stButton > button:hover {
        border: 2px dashed #00FF00 !important;
        background-color: rgba(0, 255, 0, 0.1) !important;
    }

    /* Transparente Eingabefelder */
    .pw-input input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 1px solid #00FF00 !important;
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
# FRAME 0: LOGIN OVERLAY (Passwortfeld & Enter Button genau im Feld)
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img = get_asset_path("Frame 0.jpg")
    
    # Anpassen der Prozentwerte (top/left/width) falls es auf deiner Auflösung abweicht
    st.markdown(f"""
    <div class="canvas-container">
        <img src="app/static/{img}" class="canvas-image" fallback="{img}">
    </div>
    """, unsafe_allow_html=True)
    
    # Falls st.image bevorzugt wird für GitHub Streamlit Cloud:
    if img:
        st.image(img, use_container_width=True)
        
    col1, col2 = st.columns([1.1, 1])
    with col2:
        st.markdown("<div style='margin-top: -340px;' class='pw-input'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Passwort eingeben...", key="login_pwd")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 10px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("ENTER_LOGIN", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED: Ungültiger Code!")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA (Dashboard Button exakt auf der grünen Schaltfläche)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img = get_asset_path("Frame 1.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    c1, c2, c3 = st.columns([0.4, 0.5, 1.1])
    with c1:
        st.markdown("<div style='margin-top: -260px; height: 60px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("GHOST_DASH", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION (Sektor-Klickzonen direkt auf den Zeilen)
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img = get_asset_path("Frame 2.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div style='margin-top: -280px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("GO_ZORD_CREW", use_container_width=True): navigate_to("frame_3")
        st.markdown("</div><div style='margin-top: 10px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("GO_ZEUS", use_container_width=True): navigate_to("frame_4")
        st.markdown("</div><div style='margin-top: 10px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("GO_FUNK", use_container_width=True): navigate_to("frame_5")
        st.markdown("</div><div style='margin-top: 10px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("GO_GHOST", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME (Zurück-Button)
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_id = st.session_state.current_frame
    frame_num = frame_id.split("_")[1]
    img = get_asset_path(f"Frame {frame_num}.jpg")
    
    if img:
        st.image(img, use_container_width=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div style='margin-top: -150px; height: 50px;' class='ghost-btn'>", unsafe_allow_html=True)
        if st.button("RETURN_NAV", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
