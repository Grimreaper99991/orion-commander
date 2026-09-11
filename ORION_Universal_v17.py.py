# ==============================================================================
# ORION COMMAND CORE v35.0 - NATIVE CYBERPUNK INTERFACE
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
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

# Hilfsfunktionen für Bildpfade & Base64
def get_asset_path(filename):
    paths = [f"assets/{filename}", f"assets/{filename.lower()}", f"assets/{filename.replace(' ', '_')}"]
    for p in paths:
        if os.path.exists(p):
            return p
    return None

def get_base64_image(image_path):
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# CYBERPUNK / SCI-FI CSS THEME
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    /* Grund-Styling */
    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, .cyber-title { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background-color: #03070d;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 255, 170, 0.05) 0%, transparent 60%),
            linear-gradient(rgba(0, 255, 170, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 170, 0.03) 1px, transparent 1px);
        background-size: 100% 100%, 30px 30px, 30px 30px;
        color: #e0f0ff;
    }

    .block-container {
        padding: 2rem !important;
        max-width: 1200px !important;
    }

    /* Sci-Fi Glasmorphismus Cards */
    .cyber-card {
        background: rgba(10, 20, 30, 0.75);
        border: 1px solid rgba(0, 255, 170, 0.3);
        box-shadow: 0 0 15px rgba(0, 255, 170, 0.1), inset 0 0 15px rgba(0, 255, 170, 0.05);
        border-radius: 8px;
        padding: 20px;
        backdrop-filter: blur(8px);
        margin-bottom: 20px;
        position: relative;
    }
    
    .cyber-card::before {
        content: '';
        position: absolute;
        top: -1px; left: -1px;
        width: 10px; height: 10px;
        border-top: 2px solid #00ffaa;
        border-left: 2px solid #00ffaa;
    }

    /* Cyberpunk Buttons */
    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 255, 170, 0.1) 0%, rgba(0, 150, 255, 0.1) 100%) !important;
        color: #00ffaa !important;
        border: 1px solid #00ffaa !important;
        box-shadow: 0 0 10px rgba(0, 255, 170, 0.2) !important;
        border-radius: 4px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: #00ffaa !important;
        color: #03070d !important;
        box-shadow: 0 0 25px #00ffaa, 0 0 10px #00ffaa !important;
        transform: translateY(-2px);
    }

    /* Eingabefeld (Passwort) */
    .stTextInput input {
        background-color: rgba(5, 15, 25, 0.8) !important;
        color: #00ffaa !important;
        border: 1px solid rgba(0, 255, 170, 0.5) !important;
        border-radius: 4px !important;
        padding: 10px !important;
        font-size: 1.1rem !important;
    }
    .stTextInput input:focus {
        border-color: #00ffaa !important;
        box-shadow: 0 0 15px rgba(0, 255, 170, 0.4) !important;
    }

    /* Status Badges */
    .status-online {
        color: #00ffaa;
        text-shadow: 0 0 8px #00ffaa;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: CYBER TERMINAL LOGIN
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    st.markdown("<h1 class='cyber-title' style='text-align: center; color: #00ffaa; margin-bottom: 30px;'>🪐 ORION BASE COMMANDER</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        img_path = get_asset_path("Frame 0.jpg")
        if img_path:
            st.image(img_path, use_container_width=True)
        else:
            st.markdown("""
            <div class='cyber-card' style='height: 300px; display: flex; align-items: center; justify-content: center;'>
                <p style='color: #00ffaa;'>SYSTEM READY // WAITING FOR AUTHENTICATION</p>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.markdown("""
        <div class='cyber-card'>
            <h3 class='cyber-title' style='color: #00ffaa; margin-top: 0;'>SECURITY CHECK</h3>
            <p style='font-size: 0.9rem; color: #8ab4f8;'>Bitte Autorisierungscode eingeben, um Zugriff auf die Untergeschosse zu erhalten.</p>
        </div>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Code eingeben...", key="pwd_input")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("SYSTEM INITIALISIEREN ➔"):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED // UNGÜLTIGER MASTER CODE")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("<h1 class='cyber-title' style='color: #00ffaa;'>SEKTOR 01 // GALACTA HUB</h1>", unsafe_allow_html=True)
    
    img_path = get_asset_path("Frame 1.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.markdown("""
        <div class='cyber-card'>
            <h4>SYSTEM STATUS</h4>
            <p>Kern: <span class='status-online'>ONLINE</span></p>
            <p>Sicherheit: LEVEL 5</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='cyber-card'>
            <h4>STATION DATA</h4>
            <p>Orion Base Sub-Level 4</p>
            <p>Verbindung: Verschlüsselt</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➔ HAUPT-DASHBOARD ÖFFNEN"):
            navigate_to("frame_2")

# ==============================================================================
# FRAME 2: MAIN DASHBOARD
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 class='cyber-title' style='color: #00ffaa;'>COMMAND DASHBOARD</h1>", unsafe_allow_html=True)
    
    img_path = get_asset_path("Frame 2.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🛠️ SCHNELLZUGRIFF SEKTOREN")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🪐 ZORD CREW (FRAME 3)"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DETAILS (FRAME 4)"): navigate_to("frame_4")
    with col2:
        if st.button("📡 FUNKRAUM (FRAME 5)"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM SIMULATOR (FRAME 6)"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3 BSI 6: SEKTOR RÄUME
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    frame_names = {
        "frame_3": "ZORD CREW",
        "frame_4": "ZEUS DETAILS",
        "frame_5": "FUNKRAUM",
        "frame_6": "GHOST ROOM SIMULATOR"
    }
    
    f_key = st.session_state.current_frame
    f_num = f_key.split("_")[1]
    
    st.markdown(f"<h1 class='cyber-title' style='color: #00ffaa;'>SEKTOR {f_num} // {frame_names[f_key]}</h1>", unsafe_allow_html=True)
    
    img_path = get_asset_path(f"Frame {f_num}.jpg")
    if img_path:
        st.image(img_path, use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("↩ ZURÜCK ZUM DASHBOARD"):
            navigate_to("frame_2")
    with col2:
        st.markdown(f"""
        <div class='cyber-card'>
            <p style='margin: 0;'>Aktiver Raum: <strong>{frame_names[f_key]}</strong> | Datenstrom stabil.</p>
        </div>
        """, unsafe_allow_html=True)
