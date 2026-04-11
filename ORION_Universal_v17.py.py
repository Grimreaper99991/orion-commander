import streamlit as st
import os
import json
from groq import Groq
import pathlib

# --- 1. PFAD-ZENTRALE ---
ROOT_DIR = pathlib.Path(__file__).parent.absolute()
BASE_DIR = os.path.join(ROOT_DIR, "ORION_CORE")
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
MEMORY_FILE = os.path.join(BASE_DIR, "universal_memory.json")

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: pass
    return {"wissen": [], "einstellungen": {"farbe": "#FF0000"}}

def save_mem(content):
    data = load_memory()
    if content and content not in data["wissen"]:
        data["wissen"].append(content)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    return False

# --- 2. HYBRID-APP DESIGN (Handy-Optimierung) ---
st.set_page_config(page_title="ORION MOBILE", layout="wide")

# Hier ballern wir das Design rein, damit es wie eine App wirkt
st.markdown("""
    <style>
    /* Handy-Optimierung */
    [data-testid="stSidebar"] { min-width: 250px; max-width: 250px; }
    .main .block-container { padding: 1rem; }
    .stChatFloatingInputContainer { bottom: 20px; }
    /* Roter "Commander" Style */
    .stApp { border-top: 6px solid #FF0000; background-color: #0e1117; }
    h1, h2, h3 { color: #FF0000 !important; }
    </style>
    """, unsafe_allow_html=True)

# API-Brücke
api_key = os.getenv("Orions Power")
client = Groq(api_key=api_key) if api_key else None

# --- 3. MOBILE NAVIGATION ---
st.sidebar.title("🪐 ORION MOBILE")
# Auf dem Handy ist ein kompaktes Menü besser
menu = st.sidebar.selectbox("Kommando-Ebene", ["Chat", "Gedächtnis", "System"])

# --- 4. LOGIK ---
mem_data = load_memory()

if menu == "Chat":
    st.subheader("🛡️ Strategischer Dialog")
    if "messages" not in st.session_state: st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Befehle?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        ctx = "\n".join(mem_data["wissen"][-5:])
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": f"Du bist ORION. Wissen: {ctx}"}] + st.session_state.messages
            ).choices[0].message.content
            
            with st.chat_message("assistant"): st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})
            
            if st.button("🐘 Ins Gehirn kopieren"):
                if save_mem(res):
                    st.success("Universal gespeichert!")
        except Exception as e:
            st.error(f"Fehler: {e}")

elif menu == "Gedächtnis":
    st.subheader("🐘 Archiv")
    for i, w in enumerate(reversed(mem_data["wissen"])):
        st.info(f"{w}")

elif menu == "System":
    st.write(f"Online auf: {os.getenv('COMPUTERNAME')}")
    if st.button("Logout / Reset"):
        st.session_state.messages = []
        st.rerun()