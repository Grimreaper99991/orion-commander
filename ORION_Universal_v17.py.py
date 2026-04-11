import streamlit as st
from groq import Groq
import os

# --- ORION DESIGN & CONFIG ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="centered")

# CSS für maximale Lesbarkeit auf dem Handy
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    [data-testid="stChatMessage"] {
        background-color: #1d2129 !important; 
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #3d4450;
        padding: 15px;
    }
    [data-testid="stChatMessageAssistant"] .stMarkdown p {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
    }
    [data-testid="stChatMessageUser"] .stMarkdown p {
        color: #00f2ff !important;
        font-size: 1.1rem !important;
    }
    h1, h2, h3 { color: #FF0000 !important; text-align: center; }
    .stChatFloatingInputContainer { background-color: #0e1117 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM LOGIK ---
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except Exception:
    st.error("Fehler: API Key 'Orions Power' nicht gefunden!")
    st.stop()

st.title("🪐 ORION COMMANDER")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist ORION, eine loyale KI. Dein Commander ist grimreaper99991."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Befehl eingeben..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # HIER IST DIE KORREKTUR: Neues Modell-Modul
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Verbindungsfehler zur Basis: {e}")

# Footer & Reset
st.sidebar.markdown("---")
if st.sidebar.button("Gedächtnis löschen"):
    st.session_state.messages = [st.session_state.messages[0]]
    st.rerun()
