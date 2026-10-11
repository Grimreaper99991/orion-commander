# ==============================================================================
# ORION COMMAND CORE v50.0 - GOD ZORD COMMAND NETWORK
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX
# ==============================================================================

import streamlit as st
import os

st.set_page_config(
    page_title="ORION COMMAND CORE",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

# Initialisierung der 10 Götter-Zords Status-Matrix
if "zord_status" not in st.session_state:
    st.session_state.zord_status = {
        f"Zord 0{i+1}" if i+1 < 10 else f"Zord {i+1}": {
            "name": name,
            "status": "BEREIT",
            "power": 100,
            "mode": "STANDBY"
        } for i, name in enumerate([
            "Zeus Prime", "Chronos Titan", "Ares War-Lord", "Poseidon Core", 
            "Hades Void", "Apollo Solar", "Athena Shield", "Hephaestus Forge", 
            "Hermes Speed", "Artemis Hunt"
        ])
    }

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
# STYLING (HIGH-TECH CYBERPUNK)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, h4, .cyber-font { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(255, 0, 128, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(0, 240, 255, 0.08) 0%, transparent 40%),
                    #030712;
        background-attachment: fixed;
        color: #e2e8f0;
    }

    .block-container {
        padding: 2rem !important;
        max-width: 1400px !important;
    }

    .card-cyan {
        background: rgba(10, 25, 41, 0.8);
        border: 1px solid #00f0ff;
        border-left: 5px solid #00f0ff;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .card-gold {
        background: rgba(30, 25, 10, 0.8);
        border: 1px solid #ffaa00;
        border-left: 5px solid #ffaa00;
        box-shadow: 0 0 15px rgba(255, 170, 0, 0.2);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(255, 0, 127, 0.15) 100%) !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 10px 15px !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #00f0ff 0%, #ff007f 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00f0ff !important;
    }

    .badge-cyan { background: #00f0ff22; color: #00f0ff; border: 1px solid #00f0ff; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .badge-gold { background: #ffaa0022; color: #ffaa00; border: 1px solid #ffaa00; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .badge-green { background: #00ff8822; color: #00ff88; border: 1px solid #00ff88; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .badge-red { background: #ff005522; color: #ff0055; border: 1px solid #ff0055; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }

    .stTextInput input {
        background-color: rgba(5, 12, 22, 0.9) !important;
        color: #00f0ff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    st.markdown("<h1 class='cyber-font' style='text-align: center; color: #00f0ff;'>🪐 ORION COMMAND CORE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Auth-x...", key="pwd_input")
        if st.button("SYSTEM ACCESS ➔"):
            if pwd == MASTER_CODE: navigate_to("frame_1")
            else: st.error("ACCESS DENIED")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 01 // GALACTA HUB</h1>", unsafe_allow_html=True)
    if st.button("➔ HAUPT-DASHBOARD BETRETEN"): navigate_to("frame_2")

# ==============================================================================
# FRAME 2: MAIN DASHBOARD
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>COMMAND DASHBOARD</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🪐 ZORD CREW (10 GÖTTER-ZORDS)"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DETAILS"): navigate_to("frame_4")
    with c2:
        if st.button("📡 FUNKRAUM"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: DIE 10 GÖTTER-ZORDS STEUERUNG
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 03 // 10 GÖTTER-ZORD CREW</h1>", unsafe_allow_html=True)
    
    # GLOBAL COMMAND CONTROL (ALLE ZORDS SAMMELN)
    st.markdown("""
    <div class='card-gold'>
        <h3 class='cyber-font' style='color: #ffaa00; margin:0;'>⚡ GLOBAL ZORD COMMAND CONTROL</h3>
        <p style='font-size:0.85rem; color:#cbd5e1;'>Steuere alle 10 Einheiten gleichzeitig oder löse die Haupt-Sync aus.</p>
    </div>
    """, unsafe_allow_html=True)

    gc1, gc2, gc3, gc4 = st.columns(4)
    with gc1:
        if st.button("🔥 ALL ZORDS: FULL POWER"):
            for zid in st.session_state.zord_status:
                st.session_state.zord_status[zid]["power"] = 100
                st.session_state.zord_status[zid]["mode"] = "ATTACK"
                st.session_state.zord_status[zid]["status"] = "MAX POWER"
            st.success("ALLE ZORDS AUF MAXIMALER LEISTUNG!")
            st.rerun()

    with gc2:
        if st.button("🛡️ ALL ZORDS: SHIELD MODE"):
            for zid in st.session_state.zord_status:
                st.session_state.zord_status[zid]["mode"] = "DEFENSE"
                st.session_state.zord_status[zid]["status"] = "SHIELD UP"
            st.info("SCHUTZSCHILDE FÜR ALLE ZORDS AKTIVIERT!")
            st.rerun()

    with gc3:
        if st.button("💤 ALL ZORDS: STANDBY"):
            for zid in st.session_state.zord_status:
                st.session_state.zord_status[zid]["mode"] = "STANDBY"
                st.session_state.zord_status[zid]["status"] = "BEREIT"
            st.warning("ALLE ZORDS IM STANDBY-MODUS.")
            st.rerun()

    with gc4:
        if st.button("👑 MEGA-FORMATION"):
            for zid in st.session_state.zord_status:
                st.session_state.zord_status[zid]["mode"] = "FUSED"
                st.session_state.zord_status[zid]["status"] = "TITAN GOD COMBINED"
            st.error("⚡ GÖTTER-ZORD MEGA-FORMATION GEKOPPELT!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 🤖 EINZEL-ZORD STEUERUNG")

    # GRID MIT ALLEN 10 ZORDS
    zord_items = list(st.session_state.zord_status.items())
    
    # Render in 2 Fünfer-Reihen
    for row in range(2):
        cols = st.columns(5)
        for idx in range(5):
            z_idx = row * 5 + idx
            zid, data = zord_items[z_idx]
            
            with cols[idx]:
                mode_color = "badge-green" if data["mode"] == "ATTACK" else "badge-cyan" if data["mode"] == "DEFENSE" else "badge-gold" if data["mode"] == "STANDBY" else "badge-red"
                
                st.markdown(f"""
                <div class='card-cyan' style='padding: 12px;'>
                    <span class='{mode_color}'>{zid}</span>
                    <h4 class='cyber-font' style='color: #00f0ff; margin: 8px 0 2px 0; font-size: 0.95rem;'>{data['name']}</h4>
                    <p style='font-size: 0.75rem; margin: 0;'>Status: <strong>{data['status']}</strong></p>
                    <p style='font-size: 0.75rem; margin: 0;'>Power: {data['power']}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    if st.button("⚡", key=f"pwr_{zid}", help="Power Up"):
                        st.session_state.zord_status[zid]["power"] = min(100, data["power"] + 10)
                        st.rerun()
                with c_btn2:
                    if st.button("🔄", key=f"mode_{zid}", help="Modus wechseln"):
                        next_mode = "ATTACK" if data["mode"] == "STANDBY" else "DEFENSE" if data["mode"] == "ATTACK" else "STANDBY"
                        st.session_state.zord_status[zid]["mode"] = next_mode
                        st.session_state.zord_status[zid]["status"] = f"MODUS: {next_mode}"
                        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")

# ==============================================================================
# ÜBRIGE FRAMES
# ==============================================================================
elif st.session_state.current_frame in ["frame_4", "frame_5", "frame_6"]:
    st.markdown(f"<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR {st.session_state.current_frame.split('_')[1]}</h1>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")
