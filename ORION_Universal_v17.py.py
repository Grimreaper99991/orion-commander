# ==============================================================================
# ORION COMMAND CORE v29.0 (PURE HTML/CSS HOTSPOT OVERLAY)
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

# Custom Styling: Unsichtbare Hotspot-Buttons absolut über dem Hintergrundbild
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }

    /* Standard Streamlit Padding entfernen für exakte Positionierung */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 1000px !important;
    }

    /* Der Rahmen, der das Hintergrundbild enthält */
    .canvas-card {
        position: relative;
        width: 100%;
        /* Seitenverhältnis deines Figma-Frames (Höhe / Breite) */
        padding-top: 56.25%; /* 16:9 Standard. Falls deine Figma-Bilder höher sind, passe % an */
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center top;
        border-radius: 8px;
        overflow: hidden;
    }

    /* Unsichtbare Klickzonen */
    .hotspot-btn .stButton > button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        width: 100% !important;
        height: 100% !important;
        cursor: pointer !important;
    }

    /* Optional: Beim Drüberfahren zeigt ein grüner Schein die Klickzone */
    .hotspot-btn .stButton > button:hover {
        background-color: rgba(0, 255, 0, 0.15) !important;
        border: 1px dashed #00FF00 !important;
    }

    /* Transparente Passwort-Eingabe direkt im Feld */
    .pw-overlay input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 2px solid #00FF00 !important;
        border-radius: 4px !important;
        height: 40px !important;
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
    
    # 1. Bild als Hintergrund rendern
    if img:
        st.markdown(f'<div class="canvas-card" style="background-image: url(\'app/static/{img}\');">', unsafe_allow_html=True)
        # Notfalls direktes Bild laden falls Static Pfad in Streamlit Cloud abweicht
        st.image(img, use_container_width=True)
    
    # 2. Eingabefeld & Enter Button über Prozentwerte direkt platzieren
    col1, col2 = st.columns([1.2, 1])
    with col2:
        st.markdown("<div style='margin-top: -280px;' class='pw-overlay'>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Passwort...", key="login_pwd")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 10px; height: 45px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("LOGIN_SUBMIT", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 1: GALACTA HUB (Dashboard Button Hotspot)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img = get_asset_path("Frame 1.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    # Unsichtbarer Button exakt auf deinem gezeichneten Dashboard-Button
    # Passe 'margin-top' und die Spaltenbreite an, bis er genau deckungsgleich ist
    c1, c2, c3 = st.columns([0.35, 0.3, 1.35])
    with c1:
        st.markdown("<div style='margin-top: -180px; height: 60px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("DASHBOARD_HOTSPOT", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION (Sektor Klick-Felder)
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img = get_asset_path("Frame 2.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    col1, col2 = st.columns([1, 1])
    with col1:
        # Zord Crew Hotspot
        st.markdown("<div style='margin-top: -260px; height: 45px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("HS_ZORD", use_container_width=True): navigate_to("frame_3")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Zeus Hotspot
        st.markdown("<div style='margin-top: 15px; height: 45px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("HS_ZEUS", use_container_width=True): navigate_to("frame_4")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Funkraum Hotspot
        st.markdown("<div style='margin-top: 15px; height: 45px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("HS_FUNK", use_container_width=True): navigate_to("frame_5")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Ghost Simulator Hotspot
        st.markdown("<div style='margin-top: 15px; height: 45px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("HS_GHOST", use_container_width=True): navigate_to("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3, 4, 5, 6: ZURÜCK-BUTTON HOTSPOT
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_id = st.session_state.current_frame
    frame_num = frame_id.split("_")[1]
    img = get_asset_path(f"Frame {frame_num}.jpg")
    
    if img:
        st.image(img, use_container_width=True)
        
    col1, col2 = st.columns([0.4, 1.6])
    with col1:
        st.markdown("<div style='margin-top: -120px; height: 50px;' class='hotspot-btn'>", unsafe_allow_html=True)
        if st.button("HS_BACK", use_container_width=True):
            navigate_to("frame_2")
        st.markdown("</div>", unsafe_allow_html=True)
