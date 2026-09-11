# ==============================================================================
# ORION COMMAND CORE v40.0 - PURE CYBERPUNK WEB INTERFACE
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ==============================================================================

import streamlit as st

st.set_page_config(
    page_title="ORION COMMAND CORE",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# PURE SCI-FI / CYBERPUNK STYLING (Hologramm & Terminal Look)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=JetBrains+Mono:wght@400;600&display=swap');

    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, h4, .cyber-font { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background-color: #020509;
        background-image: 
            linear-gradient(rgba(0, 255, 128, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 128, 0.02) 1px, transparent 1px);
        background-size: 20px 20px;
        color: #c0d0e0;
    }

    .block-container {
        padding: 2.5rem !important;
        max-width: 1300px !important;
    }

    /* Cyber Card / Paneele */
    .cyber-box {
        background: rgba(5, 12, 22, 0.85);
        border: 1px solid rgba(0, 255, 128, 0.3);
        box-shadow: 0 0 20px rgba(0, 255, 128, 0.08), inset 0 0 15px rgba(0, 255, 128, 0.03);
        border-radius: 6px;
        padding: 25px;
        position: relative;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    
    .cyber-box::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 12px; height: 12px;
        border-top: 2px solid #00ff80;
        border-left: 2px solid #00ff80;
    }
    
    .cyber-box::after {
        content: '';
        position: absolute;
        bottom: 0; right: 0;
        width: 12px; height: 12px;
        border-bottom: 2px solid #00ff80;
        border-right: 2px solid #00ff80;
    }

    /* Leuchtende Cyber Buttons */
    .stButton > button {
        background: rgba(0, 255, 128, 0.08) !important;
        color: #00ff80 !important;
        border: 1px solid #00ff80 !important;
        border-radius: 4px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        padding: 14px 24px !important;
        width: 100% !important;
        transition: all 0.25s ease-in-out !important;
        text-transform: uppercase;
        box-shadow: 0 0 10px rgba(0, 255, 128, 0.15);
    }

    .stButton > button:hover {
        background: #00ff80 !important;
        color: #020509 !important;
        box-shadow: 0 0 25px #00ff80, 0 0 10px #00ff80 !important;
        transform: translateY(-2px);
    }

    /* Input Felder */
    .stTextInput input {
        background-color: rgba(2, 8, 15, 0.9) !important;
        color: #00ff80 !important;
        border: 1px solid rgba(0, 255, 128, 0.5) !important;
        border-radius: 4px !important;
        padding: 12px !important;
        font-size: 1.2rem !important;
        letter-spacing: 2px;
    }
    .stTextInput input:focus {
        border-color: #00ff80 !important;
        box-shadow: 0 0 15px rgba(0, 255, 128, 0.4) !important;
    }

    .status-badge {
        display: inline-block;
        padding: 4px 10px;
        background: rgba(0, 255, 128, 0.1);
        border: 1px solid #00ff80;
        color: #00ff80;
        font-size: 0.8rem;
        border-radius: 3px;
        text-shadow: 0 0 5px #00ff80;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: SECURE LOGIN TERMINAL
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        st.markdown("""
        <div class="cyber-box" style="text-align: center;">
            <h2 class="cyber-font" style="color: #00ff80; margin-bottom: 5px;">ORION CORE</h2>
            <p style="font-size: 0.85rem; color: #7090b0; letter-spacing: 1px;">SYSTEM ACCESS PROTOCOL V4.0</p>
            <div style="margin: 20px 0;"><span class="status-badge">SECURITY LEVEL 5</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Auth-x...", key="pwd_input")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("SYSTEM STARTEN"):
            if pwd == MASTER_CODE:
                navigate_to("frame_1")
            else:
                st.error("ACCESS DENIED // UNGÜLTIGER CODE")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("""
    <div class="cyber-box">
        <h1 class="cyber-font" style="color: #00ff80; margin: 0;">SEKTOR 01 // GALACTA HUB</h1>
        <p style="color: #7090b0; margin-top: 5px;">Zentrale Navigations- und Überwachungsschnittstelle</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="cyber-box">
            <h3 class="cyber-font" style="color: #fff;">TELEMETRIE & DIAGNOSE</h3>
            <p>Kern-Status: <span style="color: #00ff80; font-weight: bold;">STABIL</span></p>
            <p>Memory-Matrix: <span style="color: #00ff80; font-weight: bold;">ELEPHANT ACTIVE</span></p>
            <p>Verschlüsselung: <span style="color: #00ff80; font-weight: bold;">AKTIV (Auth-x)</span></p>
            <br>
            <p style="font-size: 0.9rem; color: #80a0c0;">Alle Sub-Sektionen sind voll funktionsfähig. Bereit für den Übergang in das Haupt-Dashboard.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("ZUM DASHBOARD ➔"):
            navigate_to("frame_2")

# ==============================================================================
# FRAME 2: MAIN COMMAND DASHBOARD
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("""
    <div class="cyber-box">
        <h1 class="cyber-font" style="color: #00ff80; margin: 0;">COMMAND DASHBOARD</h1>
        <p style="color: #7090b0; margin-top: 5px;">Wähle einen Sektor für den Zugriff auf die Sub-Systeme.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="cyber-box">
            <h4 class="cyber-font" style="color: #00ff80;">🪐 ZORD CREW</h4>
            <p style="font-size: 0.9rem; color: #80a0c0;">Verwaltung und Status der autonomen Agenten-Einheiten.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SEKTOR 3 ÖFFNEN"): navigate_to("frame_3")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cyber-box">
            <h4 class="cyber-font" style="color: #00ff80;">⚡ ZEUS DETAILS</h4>
            <p style="font-size: 0.9rem; color: #80a0c0;">Client-Architektur, Kommunikationsprotokolle und Logfiles.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SEKTOR 4 ÖFFNEN"): navigate_to("frame_4")

    with col2:
        st.markdown("""
        <div class="cyber-box">
            <h4 class="cyber-font" style="color: #00ff80;">📡 FUNKRAUM</h4>
            <p style="font-size: 0.9rem; color: #80a0c0;">Interne Frequenzen, Sprach-Synthese und Kanalüberwachung.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SEKTOR 5 ÖFFNEN"): navigate_to("frame_5")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cyber-box">
            <h4 class="cyber-font" style="color: #00ff80;">👻 GHOST ROOM SIMULATOR</h4>
            <p style="font-size: 0.9rem; color: #80a0c0;">Schattenprozesse, Simulationen und Ghost-Node Logs.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("SEKTOR 6 ÖFFNEN"): navigate_to("frame_6")

# ==============================================================================
# FRAMES 3 BIS 6: SEKTOR RÄUME
# ==============================================================================
elif st.session_state.current_frame in ["frame_3", "frame_4", "frame_5", "frame_6"]:
    sector_data = {
        "frame_3": {"title": "ZORD CREW", "icon": "🪐", "desc": "Agenten-Netzwerk aktiv. Alle Protokolle laufen fehlerfrei."},
        "frame_4": {"title": "ZEUS DETAILS", "icon": "⚡", "desc": "Client-Verbindungen und Socket-Status im grünen Bereich."},
        "frame_5": {"title": "FUNKRAUM", "icon": "📡", "desc": "Audio-Streams und Sprach-Schnittstellen bereit."},
        "frame_6": {"title": "GHOST ROOM SIMULATOR", "icon": "👻", "desc": "Ghost-Prozess läuft isoliert im Hintergrund."}
    }
    
    current_f = st.session_state.current_frame
    info = sector_data[current_f]
    
    st.markdown(f"""
    <div class="cyber-box">
        <h1 class="cyber-font" style="color: #00ff80; margin: 0;">{info['icon']} {info['title']}</h1>
        <p style="color: #7090b0; margin-top: 5px;">{info['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("↩ ZURÜCK ZUM DASHBOARD"):
            navigate_to("frame_2")
    with col2:
        st.markdown("""
        <div class="cyber-box">
            <h4 class="cyber-font" style="color: #fff;">DIAGNOSE MELDUNG</h4>
            <p style="font-size: 0.9rem; color: #00ff80;">Sub-System läuft stabil. Keine Anomalien im Datenstrom festgestellt.</p>
        </div>
        """, unsafe_allow_html=True)
