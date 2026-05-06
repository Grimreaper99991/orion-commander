import streamlit as st
import requests
import base64

# --- MASTER DESIGN v18.2 (Blau-Schwarz-Weiss) ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #000814;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #003566;
        color: #ffffff;
        border: 2px solid #0077b6;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
        text-shadow: 1px 1px 2px #000000;
    }
    .stButton>button:hover {
        border-color: #ffffff;
        box-shadow: 0px 0px 15px #0077b6;
    }
    [data-testid="stSidebar"] {
        background-color: #001d3d;
        border-right: 2px solid #003566;
    }
    h1, h2, h3, p, label {
        color: #ffffff !important;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
    }
    .stChatMessage {
        background-color: #001d3d;
        border-radius: 10px;
        border: 1px solid #003566;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM-KERN (Secrets) ---
try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_OWNER   = st.secrets["REPO_OWNER"]
    REPO_NAME    = st.secrets["REPO_NAME"]
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    FILE_PATH    = "zord_cmd.ps1"
except Exception as e:
    st.error(f"❌ Red Skull Sabotage: {e}")
    st.stop()

# --- FUNKTION: ZORD UPLINK ---
def send_to_zord(command):
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    try:
        res = requests.get(api_url, headers=headers)
        if res.status_code == 200:
            sha = res.json()['sha']
            content_b64 = base64.b64encode(command.encode("utf-8")).decode("utf-8")
            payload = {"message": f"ORION Command: {command}", "content": content_b64, "sha": sha}
            put_res = requests.put(api_url, headers=headers, json=payload)
            if put_res.status_code == 200:
                st.success(f"✅ Zord-Uplink aktiv: {command}")
                return True
    except Exception as e:
        st.error(f"💥 Fehler: {e}")
    return False

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["🛰️ Dashboard", "🌐 Web-Terminals", "🤖 Zord-Control", "💬 Orion Chat"])
    st.divider()
    st.write("Status: Online 🟢")

# --- SEITE: DASHBOARD ---
if page == "🛰️ Dashboard":
    st.title("🛰️ COMMANDER ZENTRALE")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Zord Status", "Stabil")
    with col2: st.metric("Netzwerk", "Verschlüsselt")
    with col3: st.metric("KI-Kern", "Bereit")
    st.info("Systeme laufen im Elefanten-Modus. Keine Vorkommnisse.")

# --- SEITE: WEB-TERMINALS ---
elif page == "🌐 Web-Terminals":
    st.title("🌐 WEB-SCHNELLZUGRIFF")
    c1, c2, c3 = st.columns(3)
    with c1: st.link_button("🔍 Google", "https://www.google.com", use_container_width=True)
    with c2: st.link_button("📺 YouTube", "https://www.youtube.com", use_container_width=True)
    with c3: st.link_button("📧 Gmail", "https://mail.google.com", use_container_width=True)

# --- SEITE: ZORD-CONTROL ---
elif page == "🤖 Zord-Control":
    st.title("🤖 ZORD-REMOTE")
    colA, colB = st.columns(2)
    with colA:
        if st.button("🚀 Paint starten", use_container_width=True): send_to_zord("start mspaint")
        if st.button("🎵 MP3 Player öffnen", use_container_width=True): send_to_zord("start wmplayer")
    with colB:
        if st.button("🔒 PC Sperren", use_container_width=True): send_to_zord("rundll32.exe user32.dll,LockWorkStation")
        if st.button("📝 Notepad öffnen", use_container_width=True): send_to_zord("start notepad")

# --- SEITE: ORION CHAT ---
elif page == "💬 Orion Chat":
    st.title("💬 INTERACTION MIT ORION")
    if "messages" not in st.session_state: st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if prompt := st.chat_input("Befehl an ORION..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        try:
            from groq import Groq
            client = Groq(api_key=GROQ_API_KEY)
            # AKTUALISIERTES MODELL HIER: llama-3.3-70b-versatile
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Du bist ORION, die loyale KI des Commanders. Du hast ein Elefanten-Gedächtnis."}] + st.session_state.messages
            )
            full_res = response.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error(f"Red Skull hat das Sprachmodul manipuliert: {e}")
