import streamlit as st
import os

# 1. PAGE SETUP
st.set_page_config(page_title="ORION BASE COMMANDER", layout="wide")

# 2. EXACT FIGMA CSS (Clip-Paths, Colors, Typography)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * { font-family: 'JetBrains Mono', monospace !important; }
    
    .stApp { background-color: #040404; color: #FFFFFF; }
    
    /* Sci-Fi Container Form mit abgeschnittenen Ecken (Frame-Shape) */
    .f-container {
        background-color: #111111;
        border: 2px solid #262626;
        clip-path: polygon(0 0, 85% 0, 100% 15%, 100% 100%, 15% 100%, 0 85%);
        padding: 30px;
        position: relative;
        min-height: 550px;
    }
    
    /* Grüner Custom Dashboard Button */
    .btn-green button {
        background-color: #00FF00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 10px 20px !important;
        box-shadow: 0 0 10px #00FF00;
    }
    
    /* Zurück-Button Style */
    .btn-return button {
        background-color: transparent !important;
        color: #00FF00 !important;
        border: none !important;
        font-size: 16px !important;
        text-align: left !important;
    }
    .btn-return button:hover {
        text-shadow: 0 0 8px #00FF00;
    }

    /* Zord Crew Farben */
    .z-zeus { color: #eab308; }
    .z-shadow { color: #95C5F4; }
    .z-medusa { color: #10b981; }
    .z-storm { color: #06b6d4; }
    .z-grimreaper { color: #dc2626; }
    .z-light { color: #FFFFFF; }
    .z-titan { color: #f97316; }
    .z-spider { color: #2563eb; }
    .z-orion { color: #00FF00; }
    .z-ghost { color: #a855f7; }
</style>
""", unsafe_allow_html=True)

# 3. STATE MANAGEMENT
if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

def goto(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# FRAME 0: LOGIN
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    col1, col2 = st.columns([1, 1])
    with col1:
        if os.path.exists("assets/biker.jpg"):
            st.image("assets/biker.jpg", use_container_width=True)
        else:
            st.write("🖼️ [Biker Bild]")
    with col2:
        st.markdown("<h2 style='color: #00FF00;'>Hello !</h2>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #00FF00;'>Welcome To Orions Base</h1>", unsafe_allow_html=True)
        pwd = st.text_input("Enter Password", type="password")
        if st.button("Enter"):
            if pwd == "Auth-x":
                goto("frame_1")

# ==============================================================================
# FRAME 1: GALACTA MAIN DECK
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("""
        <h1 style='color: #95C5F4; font-size: 40px;'>GALACTA</h1>
        <p style='color: #BABABA;'>Welcome to Orions Base</p>
        <p style='color: #BABABA; max-width: 450px;'>
        The mission of Sci-Fi World is to teach and inspire people, 
        Species of all ages with an uplifting vision of the future.<br><br>
        We aren't just any artificial brain—it actually functions like the human brain.
        </p>
    """, unsafe_allow_html=True)
    
    # NUR DIESER BUTTON FÜHRT ZUR NAVI
    st.markdown("<div class='btn-green'>", unsafe_allow_html=True)
    if st.button("Dashboard"):
        goto("frame_2")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 2: DASHBOARD NAVIGATION
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 style='color: #00FF00; font-size: 50px;'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF00;'>Navigation Vom Dashboard</p>", unsafe_allow_html=True)
    st.write("---")
    
    col_nav, _ = st.columns([2, 1])
    with col_nav:
        st.markdown("<div class='btn-return'>", unsafe_allow_html=True)
        if st.button("- Zord Crew"): goto("frame_3")
        if st.button("- Zeus Details"): goto("frame_4")
        if st.button("- Funkraum"): goto("frame_5")
        if st.button("- Ghost Room Simulator"): goto("frame_6")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 3: ZORD CREW
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 style='color: #00FF00;'>zord crew</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <h3><span class='z-zeus'>zeus</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='z-shadow'>shadow</span></h3>
            <h3><span class='z-medusa'>medusa</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='z-storm'>storm</span></h3>
            <h3><span class='z-grimreaper'>grimreaper</span> <span class='z-light'>light</span></h3>
            <h3><span class='z-titan'>titan</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='z-spider'>spider</span></h3>
            <h3><span class='z-orion'>orion</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class='z-ghost'>ghost</span></h3>
        """, unsafe_allow_html=True)
    with col2:
        if os.path.exists("assets/mecha.jpg"):
            st.image("assets/mecha.jpg", width=200)
            
    st.markdown("<br><br><div class='btn-return'>", unsafe_allow_html=True)
    if st.button("Zurück Zur Navigation"): goto("frame_2")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 4: ZEUS DETAILS
# ==============================================================================
elif st.session_state.current_frame == "frame_4":
    st.markdown("<h1 style='color: #00FF00;'>Zeus Details</h1>", unsafe_allow_html=True)
    
    # Hier kommt später dein Chat/Code Kasten rein
    st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='btn-return'>", unsafe_allow_html=True)
    if st.button("Zurück Zur Navigation"): goto("frame_2")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 5: FUNKRAUM
# ==============================================================================
elif st.session_state.current_frame == "frame_5":
    st.markdown("<h1 style='color: #00FF00;'>Funkraum</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF00;'>Kommunikations Zentrale</p>", unsafe_allow_html=True)
    
    # Gelber Kasten aus deinem Figma Design
    st.markdown("<div style='background-color: #FFFF00; height: 150px; border-radius: 4px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<br><div class='btn-return'>", unsafe_allow_html=True)
    if st.button("Zurück Zur Navigation"): goto("frame_2")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# FRAME 6: GHOST GAME SIMULATOR
# ==============================================================================
elif st.session_state.current_frame == "frame_6":
    if os.path.exists("assets/ghost.jpg"):
        st.image("assets/ghost.jpg", width=150)
    st.markdown("<h1 style='color: #00FF00;'>Ghost Game Simulator</h1>", unsafe_allow_html=True)
    
    # Hellblaues Kasten-Element aus deinem Figma Design
    st.markdown("<div style='background-color: #95C5F4; height: 120px; border-radius: 4px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<br><div class='btn-return'>", unsafe_allow_html=True)
    if st.button("Zurück Zur Navigation"): goto("frame_2")
    st.markdown("</div>", unsafe_allow_html=True)
