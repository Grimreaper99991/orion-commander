import streamlit as st
from groq import Groq

# --- ORION OS v19.5: MULTI-TOOL DASHBOARD ---
st.set_page_config(page_title="ORION OS", page_icon="🪐", layout="wide")

# --- CYBER-TECH DESIGN (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 2px solid #FF0000; }
    p, span, label { color: #FFFFFF !important; font-family: 'Courier New', monospace; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { color: #FF0000 !important; }
    .stButton>button { width: 100%; background-color: #1a1a1a; color: #FF0000; border: 1px solid #FF0000; }
    .stButton>button:hover { background-color: #FF0000; color: #FFFFFF; box-shadow: 0 0 10px #FF0000; }
    /* Styling für Notizblock */
    .stTextArea textarea { background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #333333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- API INITIALISIERUNG ---
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except:
    st.error("⚠️ System-Error: API-Key fehlt!")
    st.stop()

# --- NAVIGATION (SIDEBAR) ---
with st.sidebar:
    st.title("🪐 ORION OS")
    st.markdown("---")
    # Erweiterte Navigation
    page = st.radio("ZENTRALE", [
        "🏠 CORE CHAT", 
        "📝 NOTIZBLOCK", 
        "🎵 MEDIA PLAYER", 
        "🌐 WEB-LINKS",
        "📊 SYSTEM STATUS"
    ])
    st.markdown("---")
    
    st.subheader("⚡ QUICK ACTIONS")
    if st.button("🧹 Reset Chat"):
        st.session_state.messages = [{"role": "system", "content": "ORION OS v19.5 Online."}]
        st.rerun()

# --- LOGIK DER SEITEN ---

if page == "🏠 CORE CHAT":
    st.title("🪐 CORE COMMAND")
    # Metric Bar
    c1, c2, c3 = st.columns(3)
    c1.metric("STATUS", "ONLINE")
    c2.metric("USER", "superman9999")
    c3.metric("OS", "v19.5")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "Bereit für Befehle, Commander."}]

    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Befehl..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            full_res = ""
            placeholder = st.empty()
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True
            )
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    full_res += chunk.choices[0].delta.content
                    placeholder.markdown(full_res + "▌")
            placeholder.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

elif page == "📝 NOTIZBLOCK":
    st.header("📝 Digitaler Notizblock")
    if "user_notes" not in st.session_state:
        st.session_state.user_notes = ""
    
    # Textbereich für Notizen
    notes = st.text_area("Deine Gedanken / Entwürfe:", value=st.session_state.user_notes, height=400)
    st.session_state.user_notes = notes
    st.success("Notizen werden automatisch in der Sitzung gespeichert!")

elif page == "🎵 MEDIA PLAYER":
    st.header("🎵 Media Player")
    st.info("Du kannst hier MP3-Dateien oder URLs abspielen.")
    # Beispiel für eine hochgeladene Datei oder URL
    audio_url = st.text_input("Audio-URL eingeben (MP3):", placeholder="https://www.beispiel.de/musik.mp3")
    if audio_url:
        st.audio(audio_url)
    st.markdown("---")
    st.write("Lokale MP3-Dateien können direkt hier hochgeladen werden:")
    uploaded_file = st.file_uploader("Datei wählen", type=["mp3"])
    if uploaded_file is not None:
        st.audio(uploaded_file)

elif page == "🌐 WEB-LINKS":
    st.header("🌐 Schnell-Verknüpfungen")
    st.write("Hier sind deine direkten Tunnel ins Netz:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.link_button("🔍 Google Suche", "https://www.google.com")
        st.link_button("📺 YouTube", "https://www.youtube.com")
    with col_b:
        st.link_button("📧 Gmail", "https://mail.google.com")
        st.link_button("🐙 GitHub", "https://github.com")
    
    st.markdown("---")
    st.info("Hinweis: Echte Browser-Fenster innerhalb der App werden oft von Google/YouTube aus Sicherheitsgründen blockiert. Die Link-Buttons öffnen sie direkt in einem neuen Tab – so wie es am Handy am besten funktioniert.")

elif page == "📊 SYSTEM STATUS":
    st.header("⚙️ Diagnose")
    st.progress(100, text="Cloud-Verbindung stabil")
    st.json({"Build": "19.5", "Mobile-Optimized": True, "Audio-Engine": "Streamlit Native"})
