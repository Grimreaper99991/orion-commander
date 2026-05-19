import streamlit as st
import requests
import base64
from datetime import datetime
import time

# --- MASTER DESIGN v18.8 (Sternen-Avatar & Status Engine) ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000814; color: #ffffff !important; }
    [data-testid="stSidebar"] * { color: #ffffff !important; text-shadow: 1px 1px 2px #000; }
    [data-testid="stChatMessage"] * { color: #ffffff !important; }
    .stButton>button { background-color: #003566; color: #ffffff !important; border: 2px solid #0077b6; border-radius: 12px; }
    [data-testid="stSidebar"] { background-color: #001d3d; border-right: 2px solid #003566; }
    .stChatMessage { background-color: #001d3d !important; border: 1px solid #003566 !important; }
    
    /* STYLING FÜR DEN STERNEN-AVATAR */
    .avatar-box {
        border: 2px solid #0077b6;
        border-radius: 20px;
        background: radial-gradient(circle, #001d3d 0%, #000814 100%);
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 15px #0077b6;
    }
    .star-animation {
        font-size: 50px;
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(0.9); opacity: 0.6; }
        100% { transform: scale(1.1); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM-KERN ---
try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_OWNER   = st.secrets["REPO_OWNER"]
    REPO_NAME    = st.secrets["REPO_NAME"]
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception as e:
    st.error(f"Sicherheits-Fehler: {e}")
    st.stop()

# --- GITHUB ENGINE ---
def manage_github_file(file_name, content=None, mode="read", append=False):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=headers)
    sha = res.json()['sha'] if res.status_code == 200 else None
    if mode == "read":
        return base64.b64decode(res.json()['content']).decode("utf-8") if res.status_code == 200 else ""
    elif mode == "write":
        if append:
            old_content = manage_github_file(file_name, mode="read")
            content = old_content + "\n" + content
        content_b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        payload = {"message": f"ORION Update: {file_name}", "content": content_b64}
        if sha: payload["sha"] = sha
        requests.put(url, headers=headers, json=payload)
        return True

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    manage_github_file("security_log.txt", f"[{timestamp}] {action}", mode="write", append=True)

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["🛰️ Dashboard", "🌐 Web-Terminals", "📝 Cloud-Notizen", "🤖 Zord-Control", "🛡️ Sicherheit", "💬 Orion Chat"])
    st.divider()
    st.write("Status: Online 🟢")

# --- SEITE: DASHBOARD ---
if page == "🛰️ Dashboard":
    st.title("🛰️ COMMANDER ZENTRALE")
    
    # Avatar Anzeige im Dashboard (Ruhezustand)
    st.markdown("""
    <div class="avatar-box">
        <div class="star-animation">✨ 🌌 👤 🌌 ✨</div>
        <h3 style="color: #00b4d8;">ORION AVATAR: STEHT / BEREIT</h3>
        <p style="color: #ffffff;">Blauer Sternen-Körper stabilisiert. Warte auf Befehle des Commanders.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Systeme laufen optimal. Keine Bedrohungen erkannt.")

# --- SEITE: WEB-TERMINALS ---
elif page == "🌐 Web-Terminals":
    st.title("🌐 WEB-SCHNELLZUGRIFF")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.link_button("🔍 Google", "https://www.google.com", use_container_width=True)
    with c2: st.link_button("📺 YouTube", "https://www.youtube.com", use_container_width=True)
    with c3: st.link_button("📧 Gmail", "https://mail.google.com", use_container_width=True)
    with c4: st.link_button("💻 Chip.de", "https://www.chip.de", use_container_width=True)

# --- SEITE: CLOUD-NOTIZEN ---
elif page == "📝 Cloud-Notizen":
    st.title("📝 ORION CLOUD-STORAGE")
    current_notes = manage_github_file("notizen.txt", mode="read")
    new_notes = st.text_area("Notizblock", value=current_notes, height=300)
    if st.button("💾 Speichern"):
        manage_github_file("notizen.txt", new_notes, mode="write")
        st.success("Gespeichert.")

# --- SEITE: ZORD-CONTROL ---
elif page == "🤖 Zord-Control":
    st.title("🤖 ZORD-REMOTE")
    
    # Avatar agiert
    if st.button("🚀 Paint starten"): 
        st.markdown('<div class="avatar-box">🏃‍♂️💨 <i>Avatar läuft los, um Zord zu aktivieren...</i></div>', unsafe_allow_html=True)
        manage_github_file("zord_cmd.ps1", "start mspaint", mode="write")
        log_action("Start Paint")
        
    if st.button("🔒 PC Sperren"): 
        manage_github_file("zord_cmd.ps1", "rundll32.exe user32.dll,LockWorkStation", mode="write")
        log_action("Lock Workstation")

# --- SEITE: SICHERHEIT ---
elif page == "🛡️ Sicherheit":
    st.title("🛡️ SYSTEM-PROTOKOLL")
    logs = manage_github_file("security_log.txt", mode="read")
    st.text_area("Protokoll-Einträge", value=logs, height=400, disabled=True)
    if st.button("🗑️ Log löschen"):
        manage_github_file("security_log.txt", "--- NEUES PROTOKOLL GESTARTET ---", mode="write")
        st.rerun()

# --- SEITE: CHAT ---
elif page == "💬 Orion Chat":
    st.title("💬 INTERACTION")
    
    # Zustand: Denken / Verarbeiten
    avatar_placeholder = st.empty()
    avatar_placeholder.markdown("""
    <div class="avatar-box">
        <div class="star-animation">🌌 🧠 🌌</div>
        <h4 style="color: #00b4d8;">ORION STATUS: SITZT UND DENKT NACH</h4>
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
        
    if prompt := st.chat_input("Befehl..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Visuelles Feedback: KI arbeitet hart
        avatar_placeholder.markdown("""
        <div class="avatar-box">
            <div class="star-animation">✨🌀👤🌀✨</div>
            <h4 style="color: #ffb703;">ORION RECHNET / GENERIERT ANTWORT...</h4>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            from groq import Groq
            client = Groq(api_key=GROQ_API_KEY)
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Du bist ORION. Sei loyal."}] + st.session_state.messages
            )
            full_res = res.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
            
            # Nach der Antwort wieder in den normalen Denk-Modus
            avatar_placeholder.markdown("""
            <div class="avatar-box">
                <div class="star-animation">🌌 👤 🌌</div>
                <h4 style="color: #00b4d8;">ORION STATUS: SITZT UND WARTET</h4>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e: 
            st.error(f"Fehler: {e}")
