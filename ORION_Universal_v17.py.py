import streamlit as st
import requests
import base64

# --- MASTER DESIGN v18.4 (Cloud-Notes & High-Contrast Fix) ---
st.set_page_config(page_title="ORION COMMANDER", page_icon="🪐", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000814; color: #ffffff; }
    
    /* Globaler Text-Fix für maximale Lesbarkeit */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span, label, .stSelectbox label {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000;
        font-weight: 500;
    }

    /* Sidebar Navigation Weiss-Fix */
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .stRadio label {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        text-shadow: 2px 2px 4px #000000 !important;
    }

    .stButton>button {
        background-color: #003566;
        color: #ffffff !important;
        border: 2px solid #0077b6;
        border-radius: 12px;
        text-shadow: 1px 1px 2px #000000;
    }

    [data-testid="stSidebar"] { background-color: #001d3d; border-right: 2px solid #003566; }
    .stChatMessage { background-color: #001d3d; border: 1px solid #003566; }
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

# --- GITHUB CLOUD STORAGE FUNKTIONEN ---
def manage_github_file(file_name, content=None, mode="read"):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    
    res = requests.get(url, headers=headers)
    sha = res.json()['sha'] if res.status_code == 200 else None

    if mode == "read":
        if res.status_code == 200:
            return base64.b64decode(res.json()['content']).decode("utf-8")
        return ""
    elif mode == "write":
        content_b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        payload = {"message": f"ORION Update {file_name}", "content": content_b64}
        if sha: payload["sha"] = sha
        requests.put(url, headers=headers, json=payload)
        return True

# --- ZORD UPLINK ---
def send_to_zord(command):
    manage_github_file("zord_cmd.ps1", command, mode="write")
    st.success(f"✅ Zord-Uplink: {command}")

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION MENU")
    page = st.radio("Navigation", ["🛰️ Dashboard", "🌐 Web-Terminals", "📝 Cloud-Notizen", "🤖 Zord-Control", "💬 Orion Chat"])
    st.divider()
    st.write("Status: Online 🟢")

# --- SEITE: DASHBOARD ---
if page == "🛰️ Dashboard":
    st.title("🛰️ COMMANDER ZENTRALE")
    st.info("Willkommen zurück. Alle Navigations-Elemente sind nun auf High-Contrast Weiß gestellt.")

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
    st.subheader("Deine Notizen auf GitHub")
    
    # Laden
    current_notes = manage_github_file("notizen.txt", mode="read")
    new_notes = st.text_area("Schreibe hier deine Gedanken...", value=current_notes, height=300)
    
    if st.button("💾 In Cloud speichern"):
        if manage_github_file("notizen.txt", content=new_notes, mode="write"):
            st.success("Notizen sicher in der Cloud verwahrt! (GitHub)")

# --- SEITE: ZORD-CONTROL ---
elif page == "🤖 Zord-Control":
    st.title("🤖 ZORD-REMOTE")
    if st.button("🚀 Paint starten"): send_to_zord("start mspaint")
    if st.button("🔒 PC Sperren"): send_to_zord("rundll32.exe user32.dll,LockWorkStation")

# --- SEITE: ORION CHAT ---
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
                messages=[{"role": "system", "content": "Du bist ORION. Sei schlagfertig und loyal."}] + st.session_state.messages
            )
            full_res = response.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error(f"Fehler: {e}")
