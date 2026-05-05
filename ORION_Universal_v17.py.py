import streamlit as st
from groq import Groq

# --- ORION OS v19: COMMANDER DASHBOARD ---
st.set_page_config(page_title="ORION OS", page_icon="🪐", layout="wide")

# --- CYBER-TECH DESIGN (CSS) ---
st.markdown("""
    <style>
    /* Haupt-Hintergrund */
    .stApp { background-color: #000000 !important; }
    
    /* Glas-Effekt für Navigation & Chat */
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 2px solid #FF0000;
    }
    
    /* Kacheln & Chat-Bubbles */
    [data-testid="stChatMessage"] {
        background-color: rgba(26, 26, 26, 0.8) !important; 
        border: 1px solid #333333;
        border-left: 5px solid #FF0000;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    /* Schrift-Styling */
    p, span, label { color: #FFFFFF !important; font-family: 'Courier New', monospace; }
    
    /* Metrics / Dashboard-Kacheln */
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { color: #FF0000 !important; text-transform: uppercase; }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a;
        color: #FF0000;
        border: 1px solid #FF0000;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #FF0000; color: #FFFFFF; box-shadow: 0 0 10px #FF0000; }
    </style>
    """, unsafe_allow_html=True)

# --- CLOUD API INITIALISIERUNG ---
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except Exception:
    st.error("⚠️ System-Error: 'Orions Power' Secret fehlt!")
    st.stop()

# --- NAVIGATION (SIDEBAR) ---
with st.sidebar:
    st.title("🪐 ORION OS")
    st.markdown("---")
    page = st.radio("NAVIGATION", ["🏠 CORE CHAT", "📊 SYSTEM STATUS", "📂 ARCHIVE"])
    st.markdown("---")
    
    st.subheader("⚡ QUICK ACTIONS")
    if st.button("📝 Analyse Code"):
        st.session_state.temp_prompt = "Bitte analysiere meinen aktuellen Code."
    if st.button("🧹 Clear Logs"):
        st.session_state.messages = [{"role": "system", "content": "Du bist ORION OS. Status: Bereit."}]
        st.rerun()

# --- HAUPT-DASHBOARD ---
if page == "🏠 CORE CHAT":
    # Obere Status-Leiste
    col1, col2, col3 = st.columns(3)
    col1.metric("OS-STATUS", "ONLINE", "v19.0")
    col2.metric("CONNECTION", "ENCRYPTED", "⚡ Groq")
    col3.metric("MEMORY", "ELEPHANT", "Active")
    
    st.markdown("---")

    # Chat-Historie
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "Willkommen im Core, Commander superman9999. Wie gehen wir vor?"}]

    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Input-Logik
    prompt = st.chat_input("Befehl eingeben...")
    if "temp_prompt" in st.session_state:
        prompt = st.session_state.temp_prompt
        del st.session_state.temp_prompt

    if prompt:
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

elif page == "📊 SYSTEM STATUS":
    st.header("⚙️ System-Diagnose")
    st.write("Alle Triebwerke laufen im optimalen Bereich.")
    st.progress(100, text="Cloud-Sync abgeschlossen")
    st.json({"Model": "Llama-3.3-70B", "Provider": "Groq", "User": "superman9999", "Memory-Mode": "Elephant"})

elif page == "📂 ARCHIVE":
    st.header("📂 Daten-Archiv")
    st.info("Hier werden zukünftige Protokolle und deine Schreiben (z.B. für den Klientenrat) abgelegt.")
    st.code("Speisesaal-Optimierung v1.0 - STATUS: Entwurf")
