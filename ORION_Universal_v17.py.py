import streamlit as st
import requests
import base64

# --- DESIGN: BLAU-SCHWARZ-WEISS ---
st.markdown("""
    <style>
    .main {
        background-color: #000814;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #003566;
        color: white;
        border: 2px solid #ffd60a;
        border-radius: 10px;
        font-weight: bold;
    }
    .stSidebar {
        background-color: #001d3d;
    }
    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 2px 2px #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KONFIGURATION AUS SECRETS ---
try:
    TOKEN = st.secrets["GITHUB_TOKEN"]
    OWNER = st.secrets["REPO_OWNER"]
    REPO  = st.secrets["REPO_NAME"]
except:
    st.error("Secrets fehlen! Bitte in Streamlit Cloud prüfen.")
    st.stop()

# --- FUNKTIONEN ---
def send_cmd(command):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/zord_cmd.ps1"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        sha = res.json()['sha']
        content = base64.b64encode(command.encode()).decode()
        payload = {"message": "ORION Command", "content": content, "sha": sha}
        requests.put(url, headers=headers, json=payload)
        st.success(f"Zord führt aus: {command}")

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["Zentral-Dashboard", "Web-Terminals", "Zord-Control", "Orion Chat"])
    st.divider()
    st.info("Status: Online 🟢")

# --- SEITEN-LOGIK ---
if page == "Zentral-Dashboard":
    st.title("🛰️ COMMANDER DASHBOARD")
    st.write(f"Willkommen zurück. Alle Systeme laufen im Elefanten-Modus.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Zord-Verbindung", value="Stabil")
    with col2:
        st.metric(label="System-Version", value="18.0")

elif page == "Web-Terminals":
    st.title("🌐 WEB-SCHNELLZUGRIFF")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("🔍 Google", "https://www.google.com", use_container_width=True)
    with c2:
        st.link_button("📺 YouTube", "https://www.youtube.com", use_container_width=True)
    with c3:
        st.link_button("📧 Gmail", "https://mail.google.com", use_container_width=True)

elif page == "Zord-Control":
    st.title("🤖 ZORD UPLINK")
    st.subheader("Remote Execute")
    if st.button("🚀 Paint öffnen"):
        send_cmd("start mspaint")
    if st.button("🎵 MP3 Player (Test)"):
        send_cmd("start wmplayer") # Öffnet Windows Media Player
    if st.button("🔒 System Sperren"):
        send_cmd("rundll32.exe user32.dll,LockWorkStation")

elif page == "Orion Chat":
    st.title("💬 INTERACTION MIT ORION")
    # Hier kommt deine Chat-Logik rein (z.B. Groq oder OpenAI)
    user_input = st.chat_input("Was gibt es zu tun, Commander?")
    if user_input:
        st.write(f"**Commander:** {user_input}")
        st.write(f"**ORION:** Ich habe den Befehl registriert und im Langzeitgedächtnis gespeichert.")
