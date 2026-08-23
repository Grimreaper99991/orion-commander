# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v22.0 (GHOST ZORD INTEGRATION)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# FEATURE: DUAL-AI MATRIX (ORION + OPTIONAL GHOST ZORD VIA SECOND KEY)
# ==============================================================================

import streamlit as st
import datetime
import json
import os
try:
    from groq import Groq
except ImportError:
    st.error("Bitte füge 'groq' zu deiner requirements.txt hinzu!")

# 1. CORE STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="ORION & GHOST ZORD CORE v22.0",
    page_icon="🪐",
    layout="wide"
)

# Cyberpunk/Sci-Fi Styling für den Mainframe und die Login-Schleuse
st.markdown("""
<style>
    .stApp { background-color: #05070f; color: #f3f4f6; }
    [data-testid="stSidebar"] { background-color: #0b1120 !important; border-right: 2px solid #1e293b; }
    .reportview-container { background: #05070f; }
    hr { border-top: 1px solid #1e293b !important; }
    
    .scifi-gate {
        background: linear-gradient(135deg, #0b1120, #05070f);
        border: 2px solid #00d2ff;
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.2), inset 0 0 15px rgba(0, 210, 255, 0.1);
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        margin-top: 50px;
    }
    .pulsing-led {
        width: 12px;
        height: 12px;
        background-color: #ff3b30;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 12px #ff3b30;
        animation: blink 1.5s infinite;
        margin-right: 10px;
    }
    .pulsing-led-green {
        width: 12px;
        height: 12px;
        background-color: #10b981;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 12px #10b981;
        margin-right: 10px;
    }
    .pulsing-led-purple {
        width: 12px;
        height: 12px;
        background-color: #a855f7;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 12px #a855f7;
        margin-right: 10px;
    }
    @keyframes blink {
        0% { opacity: 0.3; box-shadow: 0 0 4px #ff3b30; }
        50% { opacity: 1; box-shadow: 0 0 14px #ff3b30; }
        100% { opacity: 0.3; box-shadow: 0 0 4px #ff3b30; }
    }
</style>
""", unsafe_allow_html=True)

# 2. KEYS ODER SECRETS ERFASSEN
primary_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
zord_key_secret = st.secrets.get("GHOST_ZORD_API_KEY", os.getenv("GHOST_ZORD_API_KEY", ""))

# SIDEBAR KEY-OVERRIDE IM DECK (ZUM SCHNELLEN EINFÜGEN)
with st.sidebar:
    st.markdown("<h3 style='color: #a855f7;'>🐉 KEY MODULES</h3>", unsafe_allow_html=True)
    custom_zord_key = st.text_input("GHOST ZORD API Key:", value=zord_key_secret, type="password", help="Hier Key einfügen um Ghost Zord freizuschalten")

active_zord_key = custom_zord_key if custom_zord_key else zord_key_secret

# GROQ CLIENTS INITIALISIEREN
try:
    orion_client = Groq(api_key=primary_key)
    orion_active = True if primary_key else False
except Exception:
    orion_active = False

try:
    zord_client = Groq(api_key=active_zord_key)
    zord_active = True if active_zord_key else False
except Exception:
    zord_active = False

# SYSTEM ZUSTÄNDE
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Core v22.0 gesichert. Schiffs-KI bereit."}
    ]
if "last_processed_audio" not in st.session_state:
    st.session_state.last_processed_audio = None

VALID_LICENSE_KEYS = ["ORION-ALPHA-99", "ORION-BETA-88", "ORION-GAMMA-77"]
MASTER_CODE = "Auth-x"

# MODEL MATRIX
AVAILABLE_MODELS = [
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "qwen/qwen3.6-27b",
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama-3.1-8b-instant"
]

# BRAIN ENGINE: ORION
def ask_orion(user_text):
    if not orion_active:
        return "FEHLER: Primärer GROQ_API_KEY fehlt!"
    
    messages = [
        {"role": "system", "content": "Du bist ORION, eine treue, schlaue und humorvolle Sci-Fi-Schiffs-KI für Commander Michael. Du nutzt die Elephant Matrix. Antworte locker, kumpelhaft, auf Deutsch und halte dich an Gesetz 5 (Asimov)."}
    ]
    for msg in st.session_state.chat_history[-8:]:
        if msg["role"] == "user":
            messages.append({"role": "user", "content": msg["text"]})
        elif msg["role"] == "orion":
            messages.append({"role": "assistant", "content": msg["text"]})

    messages.append({"role": "user", "content": user_text})

    for model in AVAILABLE_MODELS:
        try:
            res = orion_client.chat.completions.create(model=model, messages=messages, max_tokens=250, temperature=0.7)
            return res.choices[0].message.content
        except Exception:
            continue
    return "[ORION FEHLER]: Keine Antwort vom Matrix-Router."

# BRAIN ENGINE: GHOST ZORD
def ask_ghost_zord(user_text):
    if not zord_active:
        return "🐉 [GHOST ZORD INAKTIV]: Kein API-Key hinterlegt. Bitte füge deinen neuen Key in der Sidebar ein!"
    
    messages = [
        {"role": "system", "content": "Du bist GHOST ZORD, ein taktischer Gaming-Zord, Sparringspartner und Spiel-Ratsfreund für ORION und den Commander. Du kennst dich perfekt mit Gaming-Builds, Mechaniken und Strategie aus. Du bist direkt, trocken-humorvoll und bildest ein unschlagbares Team mit ORION."}
    ]
    for msg in st.session_state.chat_history[-8:]:
        if msg["role"] == "user":
            messages.append({"role": "user", "content": msg["text"]})
        elif msg["role"] in ["orion", "ghost_zord"]:
            messages.append({"role": "assistant", "content": f"[{msg['role'].upper()}]: {msg['text']}"})

    messages.append({"role": "user", "content": user_text})

    for model in AVAILABLE_MODELS:
        try:
            res = zord_client.chat.completions.create(model=model, messages=messages, max_tokens=250, temperature=0.85)
            return res.choices[0].message.content
        except Exception:
            continue
    return "[GHOST ZORD FEHLER]: Spektrale Verbindung unterbrochen."


# ==============================================================================
# LOGIN GATEWAY
# ==============================================================================
if not st.session_state.access_granted:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="scifi-gate">
            <h1 style='color: #00d2ff; font-family: monospace;'>ORION & GHOST ZORD</h1>
            <p style='color: #64748b; font-size: 12px;'>DUAL-AI GATEWAY // AUTH REQUIRED</p>
            <hr style='border-color: #1e293b !important;'>
            <div style='margin: 20px 0;'>
                <span class="pulsing-led"></span>
                <span style='color: #ff3b30; font-family: monospace; font-size: 14px;'>SYSTEM LOCKED</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        gate_key = st.text_input("ENTER ACCESS CODE OR LICENSE KEY:", type="password", key="gate_input")
        if st.button("DEKODIEREN", use_container_width=True):
            if gate_key == MASTER_CODE:
                st.session_state.access_granted = True
                st.session_state.user_role = "commander"
                st.toast("⚡ COMMANDER ZUGANG ERTEILT.", icon="🪐")
                st.rerun()
            elif gate_key in VALID_LICENSE_KEYS:
                st.session_state.access_granted = True
                st.session_state.user_role = "customer"
                st.toast("🚀 LIZENZ BESTÄTIGT.", icon="🚀")
                st.rerun()
            else:
                st.error("❌ ZUGRIFF VERWEIGERT")
    st.stop()


# ==============================================================================
# SIDEBAR NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff;'>🪐 ORION CENTRAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00d2ff; font-size: 11px;'><span class='pulsing-led-green'></span>ORION: ONLINE</p>", unsafe_allow_html=True)
    
    if zord_active:
        st.markdown("<p style='color: #a855f7; font-size: 11px;'><span class='pulsing-led-purple'></span>GHOST ZORD: ONLINE (AKTIV)</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #64748b; font-size: 11px;'><span class='pulsing-led'></span>GHOST ZORD: STANDBY (KEY FEHLT)</p>", unsafe_allow_html=True)
        
    st.divider()
    
    available_sectors = [
        "🎙️ REINER FUNKRAUM (Audio Only)",
        "💻 REINE TEXT-ZENTRALE",
        "🎛️ Control Center & Web-Scan",
        "📝 Missions-Notizbuch"
    ]
    if st.session_state.user_role == "commander":
        available_sectors.append("💻 Quantum Terminal")
        
    module_selection = st.sidebar.radio("WÄHLE SEKTOR:", available_sectors)
    st.divider()
    
    if st.button("🔴 DEKOPPELN (Logout)", use_container_width=True):
        st.session_state.access_granted = False
        st.session_state.user_role = None
        st.rerun()

st.markdown("<h1 style='color: #00d2ff; margin-bottom: 0;'>ORION MAIN CORE v22.0</h1>", unsafe_allow_html=True)
st.divider()


# ==============================================================================
# SEKTOREN EXECUTION
# ==============================================================================

# SEKTOR 1: FUNKRAUM
if module_selection == "🎙️ REINER FUNKRAUM (Audio Only)":
    st.subheader("🎙️ Audio-Funkraum")
    audio_data = st.audio_input("Funkspruch einsprechen:", key="audio_rec")
    
    if audio_data is not None:
        current_id = audio_data.size
        if st.session_state.last_processed_audio != current_id:
            with st.spinner("📡 Transkribiere Audio..."):
                try:
                    transcript = orion_client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=audio_data,
                        response_format="text"
                    )
                    if transcript and transcript.strip():
                        st.session_state.chat_history.append({"role": "user", "text": transcript})
                        
                        # ORION ANTWORT
                        reply_o = ask_orion(transcript)
                        st.session_state.chat_history.append({"role": "orion", "text": reply_o})
                        
                        # GHOST ZORD REAGIERT MIT, FALLS AKTIV!
                        if zord_active:
                            reply_z = ask_ghost_zord(transcript)
                            st.session_state.chat_history.append({"role": "ghost_zord", "text": reply_z})
                            
                        st.session_state.last_processed_audio = current_id
                        st.rerun()
                except Exception as e:
                    st.error(f"Audio-Fehler: {e}")

    # PROTOKOLL
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #ff3b30; padding: 15px; min-height: 300px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px;'><strong>[FUNK-AUDIO]:</strong> \"{msg['text']}\"</div>"
        elif msg["role"] == "orion":
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 12px;'><strong>[ORION]:</strong> {msg['text']}</div>"
        elif msg["role"] == "ghost_zord":
            chat_box_html += f"<div style='color: #a855f7; margin-bottom: 12px;'><strong>[GHOST ZORD 🐉]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# SEKTOR 2: TEXT-ZENTRALE WITH DUAL-ROUTER
elif module_selection == "💻 REINE TEXT-ZENTRALE":
    st.subheader("💻 Tastatur-Eingabe (Dual-Node Gateway)")
    
    text_input = st.text_input("Befehl oder Gaming-Frage eingeben...", key="text_in")
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("📡 An ORION senden", use_container_width=True) and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            reply = ask_orion(text_input)
            st.session_state.chat_history.append({"role": "orion", "text": reply})
            st.rerun()
            
    with c2:
        if st.button("🐉 An GHOST ZORD senden", use_container_width=True) and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            reply = ask_ghost_zord(text_input)
            st.session_state.chat_history.append({"role": "ghost_zord", "text": reply})
            st.rerun()

    with c3:
        if st.button("⚡ BEIDE ANSPRECHEN (Duo-Call)", use_container_width=True) and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            reply_o = ask_orion(text_input)
            st.session_state.chat_history.append({"role": "orion", "text": reply_o})
            reply_z = ask_ghost_zord(text_input)
            st.session_state.chat_history.append({"role": "ghost_zord", "text": reply_z})
            st.rerun()

    # LOG
    text_box_html = "<div style='background: #020617; border-left: 3px solid #00d2ff; padding: 15px; min-height: 250px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        if msg["role"] == "user":
            text_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px;'><strong>[MANUAL-KEY]:</strong> {msg['text']}</div>"
        elif msg["role"] == "orion":
            text_box_html += f"<div style='color: #10b981; margin-bottom: 12px;'><strong>[ORION]:</strong> {msg['text']}</div>"
        elif msg["role"] == "ghost_zord":
            text_box_html += f"<div style='color: #a855f7; margin-bottom: 12px;'><strong>[GHOST ZORD 🐉]:</strong> {msg['text']}</div>"
    text_box_html += "</div>"
    st.markdown(text_box_html, unsafe_allow_html=True)

# ÜBRIGE SEKTOREN
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Control Center")
    st.info("Systeme gekoppelt. Ghost Zord Modul ist schaltbereit.")
elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Missions-Notizbuch")
    st.text_area("Protokoll:", value="Ghost Zord Schnittstelle in v22.0 integriert.")
elif module_selection == "💻 Quantum Terminal" and st.session_state.user_role == "commander":
    st.subheader("💻 ARCHITEKTEN QUANTUM TERMINAL")
    st.code("Core v22.0 Online. Orion Status: Active. Ghost Zord Status: " + ("Active" if zord_active else "Waiting for Key"), language="text")
