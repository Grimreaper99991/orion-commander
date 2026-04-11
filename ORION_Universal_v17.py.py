import streamlit as st
from groq import Groq
import os

# --- ORION DESIGN: DEEP SPACE CONTRAST ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="centered")

st.markdown("""
    <style>
    /* 1. Hintergrund: Absolut Schwarz */
    .stApp {
        background-color: #000000 !important;
    }

    /* 2. Chat-Container: Dunkles Grau/Braun zur Abhebung */
    [data-testid="stChatMessage"] {
        background-color: #1a1a1a !important; 
        border: 1px solid #333333;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    /* 3. SCHRIFT-UPGRADE: Knallweiß für User UND Orion */
    /* Dies erzwingt Weiß für alle Textelemente im Chat */
    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] span, 
    [data-testid="stChatMessage"] div {
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important; /* Etwas dicker für bessere Kanten */
        opacity: 1 !important;
    }

    /* 4. Titel und Header */
    h1, h2, h3 {
        color: #FF0000 !important; /* Dein Signal-Rot */
        text-shadow: none !important;
    }

    /* 5. Eingabefeld Kontrast */
    .stChatFloatingInputContainer {
        background-color: #000000 !important;
    }
    
    textarea {
        color: #FFFFFF !important;
        background-color: #1a1a1a !important;
    }

    /* Sidebar Fix */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM LOGIK ---
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except Exception:
    st.error("Fehler: API Key 'Orions Power' fehlt in den Secrets!")
    st.stop()

st.title("🪐 ORION COMMANDER")

# Gedächtnis
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist ORION. Antworte klar und deutlich. Dein Commander ist grimreaper99991."}
    ]

# Verlauf anzeigen
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Befehl eingeben..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Das neue, aktive Triebwerk
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
            st.error(f"Systemfehler: {e}")

# Sidebar
if st.sidebar.button("System-Reset"):
    st.session_state.messages = [st.session_state.messages[0]]
    st.rerun()
