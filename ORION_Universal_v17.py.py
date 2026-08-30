# ==============================================================================
# ORION COMMAND CORE v30.0 (TRUE ABSOLUTE LAYER OVERLAY)
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
    """Konvertiert lokales Bild in Base64 für direkte HTML-Einbindung"""
    if os.path.exists(image_path):
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

# CSS für echte Layer-Überlagerung
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    * { font-family: 'JetBrains Mono', monospace !important; }
    .stApp { background-color: #040404; color: #FFFFFF; }
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    
    /* Der Wrapper setzt den Bild-Hintergrund */
    .overlay-wrapper {
        position: relative;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .overlay-wrapper img {
        width: 100%;
        display: block;
    }

    /* Unsichtbare Klickzone direkt auf dem Bild */
    .click-zone {
        position: absolute;
        cursor: pointer;
        z-index: 999;
        /* Zum Ausrichten: leicht rot einfärben / gestrichelt anzeigen */
        border: 1px dashed rgba(0, 255, 0, 0.4);
        background: rgba(0, 255, 0, 0.05);
    }
    
    .click-zone:hover {
        border: 2px solid #00FF00;
        background: rgba(0, 255, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN OVERLAY
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img_path = get_asset_path("Frame 0.jpg")
    img_b64 = get_base64_image(img_path) if img_path else ""
    
    # HTML Layout: Bild + Eingabefeld & Button im selben Div-Container
    st.markdown(f"""
    <div class="overlay-wrapper">
        <img src="data:image/jpeg;base64,{img_b64}">
    </div>
    """, unsafe_allow_html=True)
    
    # Streamlit Widgets über Spalten direkt platzieren
    col1, col2 = st.columns([1.2, 1])
    with col2:
        st.markdown("<div style='margin-top: -35%; position: relative; z-index: 1000;'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Passwort...", key="pwd_input")
        if st.button("ENTER CORE", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA HUB (Dashboard Klickzone direkt im Bild)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img_path = get_asset_path("Frame 1.jpg")
    img_b64 = get_base64_image(img_path) if img_path else ""
    
    # Dashboard Klickzone über Prozentwerte (top%, left%, width%, height%)
    st.markdown(f"""
    <div class="overlay-wrapper">
        <img src="data:image/jpeg;base64,{img_b64}">
        <a href="javascript:void(0);" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue'}, '*'});">
            <div class="click-zone" style="top: 70%; left: 8%; width: 22%; height: 10%;"></div>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Ausweich-Button direkt auf der Höhenaustausch-Ebene
    c1, c2 = st.columns([0.4, 1])
    with c1:
        st.markdown("<div style='margin-top: -15%; position: relative; z-index: 1000;'>", unsafe_allow_html=True)
        if st.button("➔ DASHBOARD ÖFFNEN", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD SEKTOREN
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img_path = get_asset_path("Frame 2.jpg")
    img_b64 = get_base64_image(img_path) if img_path else ""
    
    st.markdown(f"""
    <div class="overlay-wrapper">
        <img src="data:image/jpeg;base64,{img_b64}">
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div style='margin-top: -40%; position: relative; z-index: 1000;'>", unsafe_allow_html=True)
        if st.button("➔ Zord Crew", use_container_width=True): navigate_to("frame_3")
        if st.button("➔ Zeus Details", use_container_width=True): navigate_to("frame_4")
        if st.button("➔ Funkraum", use_container_width=True): navigate_to("frame_5")
        if st.button("➔ Ghost Room Simulator", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: SEKTOR RÄUME
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_num = st.session_state.current_frame.split("_")[1]
    img_path = get_asset_path(f"Frame {frame_num}.jpg")
    img_b64 = get_base64_image(img_path) if img_path else ""
    
    st.markdown(f"""
    <div class="overlay-wrapper">
        <img src="data:image/jpeg;base64,{img_b64}">
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([0.4, 1])
    with col1:
        st.markdown("<div style='margin-top: -12%; position: relative; z-index: 1000;'>", unsafe_allow_html=True)
        if st.button("↩ Zurück Zur Navigation", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
