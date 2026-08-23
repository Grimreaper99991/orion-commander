## ==============================================================================
# ORION UNIVERSAL COMMAND CORE v21.4 (FAILSAFE MULTI-MODEL ROUTER)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
# FIX: AUTO-FALLBACK ROUTER FOR GROQ MODELS (ZERO 404 ERRORS)
# ==============================================================================

import streamlit as st
import datetime
import json
try:
    from groq import Groq
except ImportError:
    st.error("Bitte füge 'groq' zu deiner requirements.txt hinzu!")

# 1. CORE STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="ORION COMMANDER v21.4",
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
    
    /* Bling-Bling Sci-Fi Container */
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
    @keyframes blink {
        0% { opacity: 0.3; box-shadow: 0 0 4px #ff3b30; }
        50% { opacity: 1; box-shadow: 0 0 14px #ff3b30; }
        100% { opacity: 0.3; box-shadow: 0 0 4px #ff3b30; }
    }
</style>
""", unsafe_allow_html=True)

# ERSTELLE GROQ CLIENT AUS DEN SECRETS
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    ai_active = True
except Exception as e:
    ai_active = False

# INITIALISIERUNG DER SYSTEM-ZUSTÄNDE
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None # 'commander' oder 'customer'
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Core v21.4 gesichert. Multi-Model-Router aktiv."}
    ]
if "last_processed_audio" not in st.session_state:
    st.session_state.last_processed_audio = None

# GÜLTIGE KUNDEN-LIZENZKEYS
VALID_LICENSE_KEYS = ["ORION-ALPHA-99", "ORION-BETA-88", "ORION-GAMMA-77"]
MASTER_CODE = "Auth-x"

# BRAIN ENGINE WITH AUTOMATIC FAILSAFE ROUTER
def ask_orion_groq(user_text):
    if not ai_active:
        return "FEHLER: Groq-Key fehlt in den Secrets!"
    
    # Liste aller stabilen Modelle als Backup-Kette
    AVAILABLE_MODELS = [
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]
    
    messages = [
        {
            "role": "system", 
            "content": "Du bist ORION, eine hochentwickelte, schlaue, humorvolle und treue Sci-Fi-Schiffs-KI für den Commander. Du besitzt die 'Elephant Matrix' (vergisst nie). Antworte absolut authentisch, kumpelhaft, locker und niemals steif. Antworte immer auf Deutsch, halte dich kurz und knackig und beachte Gesetz 5 (Asimov-Sicherung)."
        }
    ]
    for msg in st.session_state.chat_history[-8:]:
        role_type = "assistant" if msg["role"] == "orion" else "user"
        messages.append({"role": role_type, "content": msg["text"]})
        
    messages.append({"role": "user", "content": user_text})

    # PROBIERE JEDES MODELL AUTOMATISCH DURCH
    for model_name in AVAILABLE_MODELS:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception:
            continue # Bei Fehler direkt zum nächsten Modell springen!
            
    return "[GROQ-MATRIX-FEHLER]: Keines der Standard-Modelle konnte erreicht werden. Bitte API-Key prüfen."


# ==============================================================================
# SEKTOR 0: DIE DESIGNTE SCI-FI SCHLEUSE (LOGIN MASK)
# ==============================================================================
if not st.session_state.access_granted:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="scifi-gate">
            <h1 style='color: #00d2ff; font-family: monospace; letter-spacing: 5px; margin-bottom: 0;'>ORION DEEP-SPACE</h1>
            <p style='color: #64748b; font-family: monospace; font-size: 12px; margin-top: 5px;'>SECURITY HUB // MATRIX CODES REQUIRED</p>
            <hr style='border-color: #1e293b !important;'>
            <div style='margin: 20px 0;'>
                <span class="pulsing-led"></span>
                <span style='color: #ff3b30; font-family: monospace; font-size: 14px; letter-spacing: 2px;'>MAIN DECK LOCKED // ENCRYPTION ACTIVE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        gate_key = st.text_input("ENTER ACCESS CODE OR LICENSE KEY:", type="password", key="gateway_key_input")
        
        if st.button("DEKODIEREN & ZUGANG ANFORDERN", use_container_width=True):
            if gate_key == MASTER_CODE:
                st.session_state.access_granted = True
                st.session_state.user_role = "commander"
                st.toast("⚡ WILLKOMMEN ZURÜCK, COMMANDER. MASTER-ZUGANG ERTEILT.", icon="🪐")
                st.rerun()
            elif gate_key in VALID_LICENSE_KEYS:
                st.session_state.access_granted = True
                st.session_state.user_role = "customer"
                st.toast("📡 LIZENZ BESTÄTIGT. WILLKOMMEN AN BORD.", icon="🚀")
                st.rerun()
            else:
                st.error("❌ ZUGRIFF VERWEIGERT: Code oder Lizenz-Key ungültig. Die Firewall hält.")
                
    st.stop()


# ==============================================================================
# SIDEBAR NAVIGATION (NACH LOGIN)
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px;'>🪐 ORION CENTRAL</h2>", unsafe_allow_html=True)
    
    if st.session_state.user_role == "commander":
        st.markdown("<p style='color: #00d2ff; font-size: 11px; font-family: monospace;'><span class='pulsing-led-green'></span>RANK: ARCHITECT (Michael)</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'><span class='pulsing-led-green'></span>RANK: LICENSED CUSTOMER</p>", unsafe_allow_html=True)
        
    st.markdown("<p style='color: #64748b; font-size: 11px; font-family: monospace;'>CORE: v21.4 // Auth-x Active</p>", unsafe_allow_html=True)
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

# MAIN INTERFACE
st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION MAIN CORE v21.4</h1>", unsafe_allow_html=True)
st.divider()


# ==============================================================================
# MODULE SELECTION EXECUTION
# ==============================================================================

# SEKTOR 1: DER REINE FUNKRAUM
if module_selection == "🎙️ REINER FUNKRAUM (Audio Only)":
    st.subheader("🎙️ Isolierter Audio-Sektor (Synchronized)")
    
    audio_data = st.audio_input("Funkspruch einsprechen und Aufnahme stoppen:", key="orion_audio_recorder")
    
    if audio_data is not None:
        current_audio_id = audio_data.size
        if st.session_state.last_processed_audio != current_audio_id:
            with st.spinner("📡 Signal empfangen. Dekodiere Frequenzen via Whisper-Engine..."):
                try:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=audio_data,
                        response_format="text"
                    )
                    
                    if transcript and transcript.strip():
                        st.session_state.chat_history.append({"role": "user", "text": transcript})
                        reply = ask_orion_groq(transcript)
                        st.session_state.chat_history.append({"role": "orion", "text": reply})
                        st.session_state.last_processed_audio = current_audio_id
                        st.rerun()
                except Exception as audio_err:
                    st.error(f"Audio-Dekodierungsfehler: {str(audio_err)}")

    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "orion":
        last_orion_text = st.session_state.chat_history[-1]["text"]
        st.components.v1.html(f"""
        <script>
            const synth = window.speechSynthesis;
            synth.cancel();
            const utterance = new SpeechSynthesisUtterance({json.dumps(last_orion_text)});
            utterance.lang = 'de-DE';
            utterance.pitch = 0.85;
            synth.speak(utterance);
        </script>
        """, height=0)

    st.markdown("### 📡 Funk-Logbuch:")
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #ff3b30; padding: 15px; min-height: 300px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>[FUNK-AUDIO]:</strong> \"{msg['text']}\"</div>"
        else:
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>[ORION]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# SEKTOR 2: DIE REINE TEXT-ZENTRALE
elif module_selection == "💻 REINE TEXT-ZENTRALE":
    st.subheader("💻 Tastatur-Eingabe-Sektor")
    
    text_input = st.text_input("Befehl über Tastatur einspeisen...", key="pure_text_input")
    if st.button("Senden", use_container_width=True) and text_input:
        st.session_state.chat_history.append({"role": "user", "text": text_input})
        with st.spinner("Berechne Datenstrom..."):
            reply = ask_orion_groq(text_input)
        st.session_state.chat_history.append({"role": "orion", "text": reply})
        st.rerun()
        
    st.markdown("### 📜 Text-Protokoll:")
    text_box_html = "<div style='background: #020617; border-left: 3px solid #00d2ff; padding: 15px; min-height: 250px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
        if msg["role"] == "user":
            text_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>[MANUAL-KEY]:</strong> {msg['text']}</div>"
        else:
            text_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>[ORION]:</strong> {msg['text']}</div>"
    text_box_html += "</div>"
    st.markdown(text_box_html, unsafe_allow_html=True)

# SEKTOREN 3, 4
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Cyber-Netzwerk Websuche & Wikipedia Modules")
    st.info("System bereit.")
elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Daten-Protokolle & Logbücher")
    st.caption("Einträge gesichert.")

# EXKLUSIVER COMMANDER SEKTOR 5
elif module_selection == "💻 Quantum Terminal" and st.session_state.user_role == "commander":
    st.subheader("💻 ARCHITEKTEN QUANTUM TERMINAL")
    st.code("Core v21.4 Online. Multi-Model Failsafe aktiv. Master-Bypass bereit.", language="text")
    st.write("Gültige Kunden-Keys im Speicher:", VALID_LICENSE_KEYS)
