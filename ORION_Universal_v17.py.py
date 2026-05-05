import streamlit as st
from groq import Groq

# --- ORION OS v19.6: ZORD COMMANDER ENGINE ---
st.set_page_config(page_title="ORION OS ZORD", page_icon="🪐", layout="wide")

# --- CYBER-TECH DESIGN (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 2px solid #FF0000; }
    p, span, label { color: #FFFFFF !important; font-family: 'Courier New', monospace; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] { color: #FF0000 !important; }
    .stButton>button { width: 100%; background-color: #1a1a1a; color: #FF0000; border: 1px solid #FF0000; }
    .stButton>button:hover { background-color: #FF0000; color: #FFFFFF; box-shadow: 0 0 10px #FF0000; }
    .stTextArea textarea { background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #333333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- API INITIALISIERUNG ---
try:
    api_key = st.secrets["Orions Power"]
    client = Groq(api_key=api_key)
except:
    st.error("⚠️ API-Key fehlt!")
    st.stop()

# --- INITIALISIERUNG DES ZORD-COMMAND-PUFFERS ---
if "zord_commands" not in st.session_state:
    st.session_state.zord_commands = []

# --- NAVIGATION ---
with st.sidebar:
    st.title("🪐 ORION OS ZORD")
    page = st.radio("ZENTRALE", ["🏠 CORE CHAT", "📝 NAZ COMMANDER", "🌐 WEB-LINKS"])
    st.markdown("---")
    # Status des Zords
    if st.session_state.zord_commands:
        st.error(f"ZORD: {len(st.session_state.zord_commands)} Befehle wartend...")
    else:
        st.success("ZORD: Standby.")

# --- CORE CHAT (Unverändert) ---
if page == "🏠 CORE CHAT":
    st.title("🪐 CORE COMMAND")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "Zord Commander v19.6 Online."}]
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
    if prompt := st.chat_input("Befehl..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        # (Groq API Aufruf wie zuvor...)

# --- NEU: NAZ COMMANDER MODUL ---
elif page == "📝 NAZ COMMANDER":
    st.header("🤖 Nano-Assistenz-Zord Control")
    st.write("Erstelle Befehle für deinen lokalen PC-Zord.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. KI-Befehl generieren")
        user_intent = st.text_input("Was soll der Zord tun?", placeholder="z.B. 'Öffne Steam und Discord'")
        
        if st.button("Generate Zord Code"):
            if user_intent and client:
                # Wir bitten die KI, nur den PowerShell-Befehl auszugeben
                task_prompt = f"""Erzeuge einen PowerShell-Einzeiler (one-liner) für folgende Aktion: '{user_intent}'. Antworte NUR mit dem Code, keine Erklärungen."""
                try:
                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant", # Schnellstes Modell für Code
                        messages=[{"role": "user", "content": task_prompt}],
                        temperature=0.1
                    )
                    generated_code = completion.choices[0].message.content.strip()
                    st.session_state.current_zord_code = generated_code
                    st.success("Code generiert!")
                except Exception as e:
                    st.error(f"Error: {e}")

        # Code-Vorschau und Bestätigung
        if "current_zord_code" in st.session_state:
            st.code(st.session_state.current_zord_code, language="powershell")
            if st.button("Befehl an Zord senden"):
                # Befehl in den Puffer pushen
                st.session_state.zord_commands.append(st.session_state.current_zord_code)
                del st.session_state.current_zord_code
                st.rerun()

    with col2:
        st.subheader("2. Zord Befehls-Warteschlange")
        if st.session_state.zord_commands:
            for i, cmd in enumerate(st.session_state.zord_commands):
                st.code(f"{i+1}: {cmd}", language="powershell")
            if st.button("Warteschlange leeren"):
                st.session_state.zord_commands = []
                st.rerun()
        else:
            st.write("Keine Befehle wartend.")

    st.markdown("---")
    st.write("### Wie du den Zord lokal aktivierst:")
    st.info("Kopiere den untenstehenden PowerShell-Code und speichere ihn als `NAZ.ps1` auf deinem PC Desktop. Führe ihn dann mit Rechtsklick -> 'Run with PowerShell' aus.")
    
    # Der lokale Zord-Agent (PowerShell)
    zord_agent_code = f"""# --- ORION NAZ (Nano-Assistenz-Zord) Agent v1.0 ---
Write-Host "ZORD Agent ONLINE - Höre auf Befehle aus der Cloud..." -ForegroundColor Green

# HINWEIS: Für die echte Cloud-Anbindung müssen wir hier einen GitHub API Call einbauen.
# Im Moment ist dies ein Demo-Skelett, das lokal simuliert, wie er Befehle abruft.
Write-Host "Simuliere Standby. Für die echte Verbindung brauchen wir Phase 2." -ForegroundColor Yellow
Start-Sleep -Seconds 10
"""
    st.code(zord_agent_code, language="powershell")

elif page == "🌐 WEB-LINKS":
    st.header("🌐 Schnell-Verknüpfungen")
    st.link_button("🔍 Google Suche", "https://www.google.com")
    st.link_button("📺 YouTube", "https://www.youtube.com")
