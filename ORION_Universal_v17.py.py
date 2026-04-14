import streamlit as st
from groq import Groq

# --- ORION CLOUD COMMANDER v18.5 ---
st.set_page_config(page_title="ORION CLOUD", page_icon="🪐", layout="centered")

# Design: Deep Space Black (Optimiert für OLED-Handys & Kontrast)
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    [data-testid="stChatMessage"] {
        background-color: #111111 !important; 
        border: 1px solid #333333;
        border-radius: 15px;
        margin-bottom: 15px;
    }
    /* Knallweiße Schrift für User und Orion */
    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] span {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
    }
    /* Status-Anzeigen */
    [data-testid="stMetricValue"] { color: #FFFFFF !important; }
    [data-testid="stMetricLabel"] { color: #FF0000 !important; }
    /* Eingabefeld fix für Mobile */
    .stChatFloatingInputContainer { background-color: #000000 !important; }
    .stButton>button { background-color: #1a1a1a; color: white; border: 1px solid #FF0000; }
    </style>
    """, unsafe_allow_html=True)

# --- CLOUD API LOGIK ---
try:
    # Nutzt NUR die Cloud-Secrets von GitHub/Streamlit
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except Exception as e:
    st.error("⚠️ Cloud-Verbindungsfehler: Überprüfe 'Orions Power' in den Streamlit Secrets!")
    st.stop()

# --- DASHBOARD ---
st.title("🪐 ORION CLOUD")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="System", value="ONLINE", delta="Cloud-Mode")
with col2:
    st.metric(label="Gedächtnis", value="ELEFANT 1.0", delta="Aktiv")

st.markdown("---")

# --- CHAT GEDÄCHTNIS ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist ORION, die mobile Zentrale von Commander superman9999. Antworte kurz, präzise und hilf beim Coden."}
    ]

# Verlauf anzeigen
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Befehlseingabe
if prompt := st.chat_input("Befehl senden..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        full_res = ""
        placeholder = st.empty()
        
        # Das stärkste Triebwerk llama-3.3-70b
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

# Reset in der Seitenleiste
if st.sidebar.button("System-Reset"):
    st.session_state.messages = [st.session_state.messages[0]]
    st.rerun()
