import streamlit as st
import requests
import base64

# --- MASTER DESIGN v18.6 (Total Visibility & Deep-Chat-Fix) ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="wide")

st.markdown("""
    <style>
    /* Hintergrund der Hauptseite */
    .main { background-color: #000814; color: #ffffff !important; }
    
    /* 1. SIDEBAR WEISS-FIX: Alles in der Sidebar muss weiß sein */
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        text-shadow: 1px 1px 2px #000000 !important;
    }

    /* 2. CHAT WEISS-FIX: Erzwingt Weiß für alle Nachrichten-Inhalte */
    [data-testid="stChatMessage"] * {
        color: #ffffff !important;
        text-shadow: 1px 1px 2px #000000 !important;
    }
    
    /* Spezifisch für den Text innerhalb der Chat-Blasen */
    .stChatMessage [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }

    /* 3. ALLGEMEINER TEXT-FIX: Falls irgendwo noch Schwarz auftaucht */
    .stMarkdown p, .stMarkdown li, .stMarkdown span {
        color: #ffffff !important;
    }

    /* Buttons Design */
    .stButton>button {
        background-color: #003566;
        color: #ffffff !important;
        border: 2px solid #0077b6;
        border-radius: 12px;
        text-shadow: 1px 1px 2px #000000;
    }

    /* Sidebar-Bereich & Chat-Blasen Hintergrund */
    [data-testid="stSidebar"] { background-color: #001d3d; border-right: 2px solid #003566; }
    .stChatMessage { background-color: #001d3d !important; border: 1px solid #003566 !important; }
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

# --- GITHUB CLOUD STORAGE ---
def manage_github_file(file_name, content=None, mode="read"):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=headers)
    sha = res.json()['sha'] if res.status_code == 200 else None
    if mode == "read":
        return base64.b64decode(res.json()['content']).decode("utf-8") if res.status_code == 200 else ""
    elif mode == "write":
        content_b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        payload = {"message": f"ORION Update {file_name}", "content": content_b64}
        if sha: payload["sha"] = sha
        requests.put(url, headers=headers, json=payload)
        return True

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["🛰️ Dashboard", "🌐 Web-Terminals", "📝 Cloud-Notizen", "🤖 Zord-Control", "💬 Orion Chat"])
    st.divider()
    st.write("Status: Online 🟢")

# --- SEITEN-LOGIK ---
if page == "🛰️ Dashboard":
    st.title("🛰️ COMMANDER ZENTRALE")
    st.info("System-Update v18.6: Deep-Chat-Visibility-Fix aktiviert.")

elif page == "🌐 Web-Terminals":
    st.title("🌐 WEB-SCHNELLZUGRIFF")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.link_button("🔍 Google", "https://www.google.com", use_container_width=True)
    with c2: st.link_button("📺 YouTube", "https://www.youtube.com", use_container_width=True)
    with c3: st.link_button("📧 Gmail", "https://mail.google.com", use_container_width=True)
    with c4: st.link_button("💻 Chip.de", "https://www.chip.de", use_container_width=True)

elif page == "📝 Cloud-Notizen":
    st.title("📝 ORION CLOUD-STORAGE")
    current_notes = manage_github_file("notizen.txt", mode="read")
    new_notes = st.text_area("Schreibe hier deine Gedanken...", value=current_notes, height=300)
    if st.button("💾 In Cloud speichern"):
        if manage_github_file("notizen.txt", content=new_notes, mode="write"):
            st.success("Notizen sicher auf GitHub verwahrt!")

elif page == "🤖 Zord-Control":
    st.title("🤖 ZORD-REMOTE")
    if st.button("🚀 Paint starten"): manage_github_file("zord_cmd.ps1", "start mspaint", mode="write")
    if st.button("🔒 PC Sperren"): manage_github_file("zord_cmd.ps1", "rundll32.exe user32.dll,LockWorkStation", mode="write")

elif page == "💬 Orion Chat":
    st.title("💬 INTERACTION MIT ORION")
    if "messages" not in st.session_state: st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if prompt := st.chat_input("Befehl..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        try:
            from groq import Groq
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Du bist ORION. Sei schlagfertig und loyal. Antworte immer so, dass der Commander dich perfekt lesen kann."}] + st.session_state.messages
            )
            full_res = response.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error(f"Fehler: {e}")
