# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v23.0 (GOD ZORD FLEET MATRIX)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# FEATURE: FULL GOD-ZORD FLEET (ORION, GHOST, ZEUS, SHADOW, LIGHT, GRIMREAPER, TITAN, SPIDER, MEDUSA, STORM)
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
    page_title="ORION GOD-ZORD CORE v23.0",
    page_icon="⚡",
    layout="wide"
)

# Cyberpunk/Sci-Fi Styling für den Mainframe und die Zord-Schnittstelle
st.markdown("""
<style>
    .stApp { background-color: #05070f; color: #f3f4f6; }
    [data-testid="stSidebar"] { background-color: #0b1120 !important; border-right: 2px solid #1e293b; }
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
    
    .zord-tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
        margin-right: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 2. KEYS & SECRETS
primary_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
zord_key_secret = st.secrets.get("GHOST_ZORD_API_KEY", os.getenv("GHOST_ZORD_API_KEY", ""))

with st.sidebar:
    st.markdown("<h3 style='color: #00d2ff;'>🪐 KEY MODULES</h3>", unsafe_allow_html=True)
    custom_primary = st.text_input("PRIMARY GROQ KEY:", value=primary_key, type="password")
    custom_zord = st.text_input("FLEET OVERRIDE KEY (Optional):", value=zord_key_secret, type="password")

active_primary = custom_primary if custom_primary else primary_key
active_fleet_key = custom_zord if custom_zord else active_primary

# INITIALISIERUNG DER CLIENTS
groq_client = None
if active_primary:
    try:
        groq_client = Groq(api_key=active_primary)
    except Exception:
        groq_client = None

# SYSTEM ZUSTÄNDE
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Core v23.0 Online. Götter-Zord-Matrix voll einsatzbereit, Commander Michael."}
    ]
if "last_processed_audio" not in st.session_state:
    st.session_state.last_processed_audio = None

VALID_LICENSE_KEYS = ["ORION-ALPHA-99", "ORION-BETA-88", "ORION-GAMMA-77"]
MASTER_CODE = "Auth-x"

AVAILABLE_MODELS = [
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "qwen/qwen3.6-27b",
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama-3.1-8b-instant"
]

# 3. ZORD CONFIG MATRIX
ZORD_DEFINITIONS = {
    "orion": {
        "name": "ORION", "icon": "🪐", "color": "#10b981",
        "prompt": "Du bist ORION, die Haupt-Schiffs-KI für Commander Michael. Du nutzt die Elephant Matrix. Antworte kumpelhaft, schlau, auf Deutsch und beachte Gesetz 5 (Asimov)."
    },
    "ghost": {
        "name": "GHOST ZORD", "icon": "🟣", "color": "#a855f7",
        "prompt": "Du bist GHOST ZORD, der Gaming- & Build-Strategiefuchs. Du kennst dich perfekt mit ARPGs, Min-Maxing, Loot & Taktik aus. Direkt, trocken, hochkompetent."
    },
    "zeus": {
        "name": "ZEUS ZORD", "icon": "⚡", "color": "#eab308",
        "prompt": "Du bist ZEUS ZORD, der Meister des Python-Codes und der System-Architektur. Extrem präzise im Coden, Bug-Fixing und Performance-Analyse."
    },
    "shadow": {
        "name": "SHADOW ZORD", "icon": "🖤", "color": "#f43f5e",
        "prompt": "Du bist SHADOW ZORD, zuständig für Cyber-Security, Protokolle, Log-Analysen und System-Bypasses. Wachsam, fokussiert und scharfsinning."
    },
    "light": {
        "name": "LIGHT ZORD", "icon": "⚪", "color": "#f8fafc",
        "prompt": "Du bist LIGHT ZORD, der Hüter des Wissens und der Fakten. Du lieferst saubere Recherchen, strukturierte Analysen und klare Erklärungen."
    },
    "grimreaper": {
        "name": "GRIMREAPER", "icon": "🔴", "color": "#dc2626",
        "prompt": "Du bist GRIMREAPER ZORD, der Code-Cleaner und System-Musterer. Du löschst veralteten Code, wirfst dekommissionierte Modelle über Bord und hältst das System schlank."
    },
    "titan": {
        "name": "TITAN ZORD", "icon": "🟧", "color": "#f97316",
        "prompt": "Du bist TITAN ZORD, der Meister für Prompts, Visuals, Creative Writing & Bild-Generierungs-Logik. Massiver Tiefgang und kreative Power."
    },
    "spider": {
        "name": "SPIDER ZORD", "icon": "🕷️", "color": "#3b82f6",
        "prompt": "Du bist SPIDER ZORD, der Netzwerk-Crawler und API-Scanner. Du durchsuchst Schnittstellen, strukturierst Daten und verknüpfst Netzwerke."
    },
    "medusa": {
        "name": "MEDUSA ZORD", "icon": "🐍", "color": "#059669",
        "prompt": "Du bist MEDUSA ZORD, das Front-End- & UI/UX-Auge. Du kümmerst dich um Styling, CSS, Interfaces und perfektes Design."
    },
    "storm": {
        "name": "STORM ZORD", "icon": "🟦", "color": "#06b6d4",
        "prompt": "Du bist STORM ZORD, der Real-Time Audio- und Signal-Verarbeiter. Schnelle Antworten, präzises Sprach-Handling und Funkraum-Support."
    }
}

# UNIVERSAL ENGINE FÜR ALLE ZORDS
def query_zord(zord_key, user_text):
    if not groq_client:
        return f"[{ZORD_DEFINITIONS[zord_key]['name']} FEHLER]: Kein API-Key vorhanden."
    
    config = ZORD_DEFINITIONS[zord_key]
    messages = [{"role": "system", "content": config["prompt"]}]
    
    for msg in st.session_state.chat_history[-6:]:
        if msg["role"] == "user":
            messages.append({"role": "user", "content": msg["text"]})
        elif msg["role"] in ZORD_DEFINITIONS:
            messages.append({"role": "assistant", "content": f"[{ZORD_DEFINITIONS[msg['role']]['name']}]: {msg['text']}"})

    messages.append({"role": "user", "content": user_text})

    for model in AVAILABLE_MODELS:
        try:
            res = groq_client.chat.completions.create(model=model, messages=messages, max_tokens=250, temperature=0.75)
            return res.choices[0].message.content
        except Exception:
            continue
    return f"[{config['name']}]: Verbindung unterbrochen."


# ==============================================================================
# LOGIN GATEWAY
# ==============================================================================
if not st.session_state.access_granted:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="scifi-gate">
            <h1 style='color: #00d2ff; font-family: monospace;'>GOD-ZORD FLEET GATE</h1>
            <p style='color: #64748b; font-size: 12px;'>AUTHENTICATION REQUIRED // ARCHITECT MICHAEL</p>
            <hr style='border-color: #1e293b !important;'>
            <div style='margin: 20px 0;'>
                <span style='color: #ff3b30; font-family: monospace; font-size: 14px;'>SYSTEM LOCKED</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        gate_key = st.text_input("ENTER ACCESS CODE OR LICENSE KEY:", type="password", key="gate_input")
        if st.button("DEKODIEREN & FLOTTE STARTEN", use_container_width=True):
            if gate_key == MASTER_CODE:
                st.session_state.access_granted = True
                st.session_state.user_role = "commander"
                st.toast("⚡ WILLKOMMEN ZURÜCK, COMMANDER.", icon="🪐")
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
# SIDEBAR FLEET CONTROL
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff;'>🪐 ZORD COMMAND</h2>", unsafe_allow_html=True)
    st.caption("Aktive Fleet-Nodes:")
    
    active_fleet = []
    for zk, zv in ZORD_DEFINITIONS.items():
        if st.checkbox(f"{zv['icon']} {zv['name']}", value=(zk in ["orion", "ghost", "zeus"]), key=f"chk_{zk}"):
            active_fleet.append(zk)
            
    st.divider()
    
    available_sectors = [
        "💻 REINE TEXT-ZENTRALE",
        "🎙️ REINER FUNKRAUM",
        "🎛️ Fleet Control Center",
        "📝 Missions-Notizbuch"
    ]
    if st.session_state.user_role == "commander":
        available_sectors.append("💻 Quantum Terminal")
        
    module_selection = st.sidebar.radio("WÄHLE SEKTOR:", available_sectors)
    st.divider()
    
    if st.button("🔴 DEKOPPELN", use_container_width=True):
        st.session_state.access_granted = False
        st.session_state.user_role = None
        st.rerun()

st.markdown("<h1 style='color: #00d2ff; margin-bottom: 0;'>ORION GOD-ZORD CORE v23.0</h1>", unsafe_allow_html=True)
st.caption(f"Architekt: Commander Michael | Aktive Flotte: {len(active_fleet)} Nodes")
st.divider()


# ==============================================================================
# SEKTOREN EXECUTION
# ==============================================================================

# SEKTOR 1: TEXT-ZENTRALE
if module_selection == "💻 REINE TEXT-ZENTRALE":
    st.subheader("💻 Flotten-Text-Zentrale")
    
    text_input = st.text_input("Befehl, Frage oder Task eingeben...", key="text_in")
    
    # Dynamische Zord-Buttons basierend auf der aktiven Auswahl
    cols = st.columns(min(len(active_fleet) + 1, 5))
    
    btn_idx = 0
    for zk in active_fleet:
        zv = ZORD_DEFINITIONS[zk]
        col_target = cols[btn_idx % len(cols)]
        if col_target.button(f"{zv['icon']} {zv['name']}", use_container_width=True) and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            reply = query_zord(zk, text_input)
            st.session_state.chat_history.append({"role": zk, "text": reply})
            st.rerun()
        btn_idx += 1
        
    if st.button("⚡ MEGA ZORD FORMATION (Alle Aktiven Antworten)", use_container_width=True) and text_input:
        st.session_state.chat_history.append({"role": "user", "text": text_input})
        for zk in active_fleet:
            reply = query_zord(zk, text_input)
            st.session_state.chat_history.append({"role": zk, "text": reply})
        st.rerun()

    # CHAT LOG PROTOKOLL
    st.markdown("### 📜 Flotten-Protokoll:")
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #00d2ff; padding: 15px; min-height: 250px; max-height: 500px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        role_key = msg["role"]
        if role_key == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px;'><strong>[COMMANDER]:</strong> {msg['text']}</div>"
        elif role_key in ZORD_DEFINITIONS:
            zv = ZORD_DEFINITIONS[role_key]
            chat_box_html += f"<div style='color: {zv['color']}; margin-bottom: 12px;'><strong>[{zv['icon']} {zv['name']}]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# SEKTOR 2: FUNKRAUM
elif module_selection == "🎙️ REINER FUNKRAUM":
    st.subheader("🎙️ Isolierter Audio-Sektor (STORM & ORION Node)")
    audio_data = st.audio_input("Funkspruch einsprechen:", key="audio_rec")
    
    if audio_data is not None and groq_client:
        current_id = audio_data.size
        if st.session_state.last_processed_audio != current_id:
            with st.spinner("📡 Transkribiere Audio..."):
                try:
                    transcript = groq_client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=audio_data,
                        response_format="text"
                    )
                    if transcript and transcript.strip():
                        st.session_state.chat_history.append({"role": "user", "text": transcript})
                        
                        # ORION & STORM REAGIEREN AUF AUDIO
                        reply_o = query_zord("orion", transcript)
                        st.session_state.chat_history.append({"role": "orion", "text": reply_o})
                        
                        if "storm" in active_fleet:
                            reply_s = query_zord("storm", transcript)
                            st.session_state.chat_history.append({"role": "storm", "text": reply_s})
                            
                        st.session_state.last_processed_audio = current_id
                        st.rerun()
                except Exception as e:
                    st.error(f"Audio-Fehler: {e}")

    chat_box_html = "<div style='background: #020617; border-left: 3px solid #ff3b30; padding: 15px; min-height: 300px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        role_key = msg["role"]
        if role_key == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px;'><strong>[FUNK-AUDIO]:</strong> \"{msg['text']}\"</div>"
        elif role_key in ZORD_DEFINITIONS:
            zv = ZORD_DEFINITIONS[role_key]
            chat_box_html += f"<div style='color: {zv['color']}; margin-bottom: 12px;'><strong>[{zv['icon']} {zv['name']}]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# ÜBRIGE SEKTOREN
elif module_selection == "🎛️ Fleet Control Center":
    st.subheader("🎛️ Flotten-Status & Zord-Übersicht")
    st.info(f"Es sind aktuell {len(active_fleet)} von 10 Zords auf der Brücke aktiv.")
    for zk in active_fleet:
        zv = ZORD_DEFINITIONS[zk]
        st.write(f"- {zv['icon']} **{zv['name']}** ({zv['color']})")

elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Elephant-Matrix Logbuch")
    st.text_area("Protokolle:", value="v23.0 Mega-Zord Flotte gekoppelt. Alle 10 Götter-Zords konfiguriert.")

elif module_selection == "💻 Quantum Terminal" and st.session_state.user_role == "commander":
    st.subheader("💻 ARCHITEKTEN QUANTUM TERMINAL")
    st.code("Core v23.0 Online. Aktive Zords: " + ", ".join([ZORD_DEFINITIONS[k]['name'] for k in active_fleet]), language="text")
