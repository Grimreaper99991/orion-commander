# ==============================================================================
# ORION COMMAND CORE v25.0 (ABSOLUTE OVERLAY POSITIONING)
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

# Custom Styling für absolute Positionierung über den Bildern
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }
    
    /* Frame Container mit relativem Layout für Layer-Positionierung */
    .frame-container {
        position: relative;
        width: 100%;
        max-width: 1100px;
        margin: 0 auto;
    }
    
    .frame-bg {
        width: 100%;
        display: block;
        border-radius: 8px;
    }

    /* Style für Overlay-Buttons (Sci-Fi Look) */
    .stButton > button {
        background-color: rgba(0, 255, 0, 0.15) !important;
        color: #00FF00 !important;
        border: 2px solid #00FF00 !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        transition: all 0.2s ease;
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
    }
    .stButton > button:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00FF00;
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
# FRAME 0: LOGIN (Eingabefeld & Enter-Button exakt rechts positioniert)
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    img = get_asset_path("Frame 0.jpg")
    
    if img:
        st.image(img, use_container_width=True)
    
    # Positionierung über Spalten genau auf dem Feld aus Screenshot Frame 0
    col_left, col_right = st.columns([1.3, 1])
    with col_right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        pwd = st.text_input("", type="password", placeholder="Enter Password", key="login_pwd")
        if st.button("Enter", use_container_width=True):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED")

# ==============================================================================
# FRAME 1: GALACTA (Dashboard-Button exakt über dem grünen Feld)
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    img = get_asset_path("Frame 1.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    col1, col2, col3 = st.columns([0.4, 0.6, 1])
    with col1:
        # Erzeugt den Klick-Button direkt an der Stelle deines grünen Figma-Buttons
        if st.button("➔ Dashboard Öffnen", use_container_width=True):
            navigate_to("frame_2")

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION (Sektor-Auswahl)
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    img = get_asset_path("Frame 2.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    st.markdown("### 🎯 Sektor Ansteuern:")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("[-Zord Crew]", use_container_width=True): navigate_to("frame_3")
    with c2:
        if st.button("[-Zeus Details]", use_container_width=True): navigate_to("frame_4")
    with c3:
        if st.button("[-Funkraum]", use_container_width=True): navigate_to("frame_5")
    with c4:
        if st.button("[-Ghost Simulator]", use_container_width=True): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: ZORD CREW
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    img = get_asset_path("Frame 3.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    if st.button("↩ Zurück Zur Navigation"):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 4: ZEUS DETAILS
# ==============================================================================
elif st.session_state.current_frame == "frame_4":
    img = get_asset_path("Frame 4.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    if st.button("↩ Zurück Zur Navigation"):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 5: FUNKRAUM
# ==============================================================================
elif st.session_state.current_frame == "frame_5":
    img = get_asset_path("Frame 5.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    if st.button("↩ Zurück Zur Navigation"):
        navigate_to("frame_2")

# ==============================================================================
# FRAME 6: GHOST GAME SIMULATOR
# ==============================================================================
elif st.session_state.current_frame == "frame_6":
    img = get_asset_path("Frame 6.jpg")
    if img:
        st.image(img, use_container_width=True)
        
    if st.button("↩ Zurück Zur Navigation"):
        navigate_to("frame_2")
