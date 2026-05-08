import streamlit as st
import requests
import base64

# --- MASTER DESIGN v18.3 (Blau-Schwarz-Weiss & High-Visibility Fix) ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="wide")

st.markdown("""
    <style>
    /* Hintergrund */
    .main {
        background-color: #000814;
        color: #ffffff;
    }
    /* HIGH VISIBILITY FIX: Erzwingt Weiß für ALLE Textelemente */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span, .stMarkdown div {
        color: #ffffff !important;
        text-shadow: 1px 1px 2px #000000;
    }
    /* Buttons */
    .stButton>button {
        background-color: #003566;
        color: #ffffff !important;
        border: 2px solid #0077b6;
        border-radius: 12px;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }
    /* Sidebar Fix */
    [data-testid="stSidebar"] {
        background-color: #001d3d;
        border-right: 2px solid #003566;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }
    /* Chat Fix */
    .stChatMessage {
        background-color: #001d3d;
        border-radius: 10px;
        border: 1px solid #003566;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM-KERN ---
try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_OWNER   = st.secrets["REPO_OWNER"]
    REPO_NAME    = st.secrets["REPO_NAME"]
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    FILE_PATH    = "zord_cmd.ps1"
except Exception as e:
    st.error(f"❌ Fehler: {e}")
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
            requests.put(api_url, headers=headers, json=payload)
            st.success(f"✅ Zord-Uplink aktiv: {command}")
    except:
        st.error("💥 Uplink Fehlgeschlagen")

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["🛰️ Dashboard", "🌐 Web-Terminals", "🤖 Zord-Control", "💬 Orion Chat"])
    st.divider()
    st.write("Status: Online 🟢")

# --- SEITEN-LOGIK ---
if page == "🛰️ Dashboard":
    st.title("🛰️ COMMANDER ZENTRALE")
    st.info("Systeme laufen im Elefanten-Modus. Lesbarkeit optimiert.")

elif page == "🌐 Web-Terminals":
    st.title("🌐 WEB-SCHNELLZUGRIFF")
    c1, c2, c3 = st.columns(3)
    with c1: st.link_button("🔍 Google", "https://www.google.com", use_container_width=True)
    with c2: st.link_button("📺 YouTube", "https://www.youtube.com", use_container_width=True)
    with c3: st.link_button("📧 Gmail", "https://mail.google.com", use_container_width=True)

elif page == "🤖 Zord-Control":
    st.title("🤖 ZORD-REMOTE")
    if st.button("🚀 Paint starten", use_container_width=True): send_to_zord("start mspaint")
    if st.button("🔒 PC Sperren", use_container_width=True): send_to_zord("rundll32.exe user32.dll,LockWorkStation")

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
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Du bist ORION, die loyale KI des Commanders. Antworte immer in Weiß und sei schlagfertig."}] + st.session_state.messages
            )
            full_res = response.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error(f"Fehler: {e}")
