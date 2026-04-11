import streamlit as st
from groq import Groq
import os

# --- ORION DESIGN & CONFIG ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="centered")

# CSS für maximale Lesbarkeit auf dem Handy
st.markdown("""
    <style>
    /* Haupt-Hintergrund */
    .stApp {
        background-color: #0e1117;
    }

    /* Chat-Nachrichten Boxen */
    [data-testid="stChatMessage"] {
        background-color: #1d2129 !important; 
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #3d4450;
        padding: 15px;
    }

    /* ORIONS ANTWORT: Knallweiß und gut lesbar */
    [data-testid="stChatMessageAssistant"] .stMarkdown p {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* NUTZER NACHRICHT: Leicht abgesetzt */
    [data-testid="stChatMessageUser"] .stMarkdown p {
        color: #00f2ff !important; /* Ein cooles Cyber-Blau für dich */
        font-size: 1.1rem !important;
    }

    /* Überschriften */
    h1, h2, h3 {
        color: #FF0000 !important;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 5px #000000;
    }

    /* Eingabefeld fix für Mobile */
    .stChatFloatingInputContainer {
        background-color: #0e1117 !important;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background-color: #FF0000;
        color: white;
        border-radius: 10px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM LOGIK ---

# API Key aus den Streamlit Cloud Secrets laden
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except Exception:
    st.error("Fehler: API Key 'Orions Power' nicht in den Secrets gefunden!")
    st.stop()

st.title("🪐 ORION COMMANDER")
st.subheader("Mobile Zentrale v17.5")

# Gedächtnis-Initialisierung (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist ORION, eine loyale und hochintelligente KI. Deine Antworten sind präzise, hilfreich und haben einen Hauch von technischer Autorität. Dein Commander ist grimreaper99991."}
    ]

# Chat-Verlauf anzeigen
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Befehl eingeben..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # KI Antwort generieren
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
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

# --- FOOTER ---
st.sidebar.markdown("---")
if st.sidebar.button("Gedächtnis löschen"):
    st.session_state.messages = [st.session_state.messages[0]]
    st.rerun()

elif menu == "System":
    st.write(f"Online auf: {os.getenv('COMPUTERNAME')}")
    if st.button("Logout / Reset"):
        st.session_state.messages = []
        st.rerun()
