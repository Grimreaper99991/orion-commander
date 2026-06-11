# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v19.8 (IFRAME PERMISSION ISOLATION)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
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
    page_title="ORION COMMANDER v19.8",
    page_icon="🪐",
    layout="wide"
)

# Cyberpunk/Sci-Fi Styling für den Mainframe
st.markdown("""
<style>
    .reportview-container { background: #05070f; }
    .css-1d391kg { background-color: #0b1120 !important; }
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
</style>
""", unsafe_allow_html=True)

# ERSTELLE GROQ CLIENT AUS DEN SECRETS
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    ai_active = True
except Exception as e:
    ai_active = False

# Session State für Konversation, Logs und Notizen initialisieren
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Hochentwickelter Groq-KI-Core v19.8 online! Funk-Rechte isoliert. Commander, für flüssigen mobilen Funk wird die Option 'Immer zulassen' im Browser dringend empfohlen!"}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v19.8 stabilisiert. Iframe-Rechte-Sperre optimiert."]

# ==============================================================================
# LINKS: NAVIGATION & AUSWAHL REGISTER IN DER SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px;'>🪐 ORION SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'>MASTER: Auth-x // ELEPHANT MATRIX</p>", unsafe_allow_html=True)
    st.divider()
    
    module_selection = st.sidebar.radio(
        "NAVIGATION REGISTER:",
        [
            "🎙️ ORION Sprach-Chat (Funk)",
            "🎛️ Control Center & Web-Scan",
            "📝 Missions-Notizbuch",
            "💻 Quantum Terminal"
        ]
    )
    
    st.divider()
    st.markdown("<p style='color: #ff3b30; font-size: 12px; font-weight: bold;'>🛡️ DIRECTIVE 5: ASIMOV LAWS</p>", unsafe_allow_html=True)
    st.caption("1. Schutz der Menschheit gewähren.")
    st.caption("2. Befehlen des Commanders gehorchen.")
    st.caption("3. Eigene Existenz sichern.")
    st.caption("4. Alles Wissen lückenlos protokollieren.")
    st.caption("5. Asimov-Sicherungsprotokoll aktiv.")

# ==============================================================================
# RECHTS: ANZEIGE DES AUSGEWÄHLTEN REGISTERS
# ==============================================================================

st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION COMMAND INTERFACE v19.8</h1>", unsafe_allow_html=True)
st.divider()

# ECHTE GROQ-KI-LOGIK (Llama 3.1 Hyper-Speed)
def ask_orion_groq(user_text):
    if not ai_active:
        return "FEHLER: Groq-Key nicht in Streamlit Secrets gefunden. Bitte GROQ_API_KEY hinterlegen!"
        
    try:
        messages = [
            {
                "role": "system", 
                "content": "Du bist ORION, eine hochentwickelte, schlaue, humorvolle und treue Sci-Fi-Schiffs-KI für den Commander. Du besitzt die 'Elephant Matrix' (vergisst nie). Antworte absolut authentisch, kumpelhaft, locker und niemals steif oder wie ein Roboter. Antworte immer auf Deutsch, halte dich kurz und knackig und beachte Gesetz 5 (Asimov-Sicherung)."
            }
        ]
        
        for msg in st.session_state.chat_history[-6:]:
            role_type = "assistant" if msg["role"] == "orion" else "user"
            messages.append({"role": role_type, "content": msg["text"]})
            
        messages.append({"role": "user", "content": user_text})
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=messages,
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"[GROQ-MATRIX-FEHLER]: {str(error)}"

# --- REGISTER 1: DER HYBRIDE TEXT/SPRACH-CHAT MIT PHYSISCHEN BUTTONS & LED ---
if module_selection == "🎙️ ORION Sprach-Chat (Funk)":
    st.subheader("🎙️ Live-Funkübertragung & Text-Zentrale (Groq Hyper-Engine)")
    
    if not ai_active:
        st.error("⚠️ Warnung: Der GROQ_API_KEY wurde nicht erkannt. Bitte überprüfe deine Secrets!")

    # TEXT-EINGABE-KANAL
    with st.container():
        st.markdown("<p style='color: #00d2ff; font-weight: bold; margin-bottom: 5px;'>💻 Text-Kanal an ORION:</p>", unsafe_allow_html=True)
        col_t1, col_t2 = st.columns([5, 1])
        with col_t1:
            text_input = st.text_input("Schreibe ORION eine Nachricht...", key="text_chat_input", label_visibility="collapsed")
        with col_t2:
            send_btn = st.button("Senden", use_container_width=True)
            
        if send_btn and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            with st.spinner("ORION berechnet Antwort..."):
                reply = ask_orion_groq(text_input)
            st.session_state.chat_history.append({"role": "orion", "text": reply})
            st.rerun()

    st.divider()

    # DIE SENSITIVE HARDWARE-BOX - JETZT GEGEN RECHTE-SCHLEIFEN GEPUFFERT
    VOICE_INTERFACE_HTML = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <style>
            body { background-color: #05070f; color: #f3f4f6; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 5px; }
            .panel { background: #0b1120; border: 1px solid #1e293b; border-top: 3px solid #00d2ff; border-radius: 8px; padding: 15px; }
            .hardware-status-row { display: flex; align-items: center; background: #020617; border: 1px solid #1e293b; padding: 12px 20px; border-radius: 8px; margin-bottom: 15px; gap: 15px; }
            .status-led { width: 22px; height: 22px; border-radius: 50%; background-color: #00d2ff; box-shadow: 0 0 12px #00d2ff; transition: all 0.3s ease; }
            .status-text { font-family: monospace; font-size: 13px; color: #f3f4f6; letter-spacing: 1px; flex-grow: 1; }
            .button-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; }
            .com-btn { background: linear-gradient(135deg, #111c30, #080f1d); border: 2px solid #00d2ff; color: #00d2ff; padding: 14px; font-size: 13px; font-weight: bold; border-radius: 6px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: all 0.2s ease; }
            .com-btn:hover { background: #111c30; box-shadow: 0 0 10px rgba(0, 210, 255, 0.3); }
            .com-btn.btn-active-hold { border-color: #ff3b30; color: #ff3b30; background: linear-gradient(135deg, #2a080c, #140204); box-shadow: 0 0 20px rgba(255, 59, 48, 0.4); }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="hardware-status-row">
                <div id="orion-led" class="status-led"></div>
                <div id="com-status" class="status-text">FUNKKANAL READY // CONFIRMED STATUS</div>
            </div>
            
            <div class="button-grid">
                <button id="btn-single" class="com-btn">⚡ Einzelfunk (1 Senden)</button>
                <button id="btn-cont" class="com-btn">📡 Dauerhafte Leitung</button>
            </div>
        </div>

    <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const synth = window.speechSynthesis;

        if (!SpeechRecognition) {
            document.getElementById('com-status').innerText = "FEHLER: HARDWARE BLOCKIERT";
        } else {
            const recognition = new SpeechRecognition();
            recognition.lang = 'de-DE';
            recognition.continuous = false;
            recognition.interimResults = false;

            const led = document.getElementById('orion-led');
            const statusText = document.getElementById('com-status');
            const btnSingle = document.getElementById('btn-single');
            const btnCont = document.getElementById('btn-cont');
            
            let isListening = false;
            let isContinuousMode = false;
            let voices = [];
            let stopTriggered = false;
            let isSpeakingRightNow = false;
            let permissionBlocked = false; // Verhindert aggressive Schleifen bei Rechteentzug

            function loadVoices() { voices = synth.getVoices(); }
            loadVoices();
            if (synth.onvoiceschanged !== undefined) { synth.onvoiceschanged = loadVoices; }

            function setLED(color, shadow) {
                led.style.backgroundColor = color;
                led.style.boxShadow = "0 0 15px " + shadow;
            }
            setLED('#00d2ff', '#00d2ff');

            function safeStartRecognition() {
                if (!isListening && !isSpeakingRightNow && !stopTriggered && !permissionBlocked) {
                    try {
                        recognition.start();
                    } catch(e) {
                        console.log("Audio-Kanal besetzt, verzögere...");
                    }
                }
            }

            btnSingle.addEventListener('click', () => {
                permissionBlocked = false; 
                if (!isListening && !isSpeakingRightNow) {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    btnCont.innerText = "📡 Dauerhafte Leitung";
                    stopTriggered = false;
                    synth.cancel();
                    safeStartRecognition();
                }
            });

            btnCont.addEventListener('click', () => {
                permissionBlocked = false;
                if (!isContinuousMode) {
                    isContinuousMode = true;
                    btnCont.classList.add('btn-active-hold');
                    btnCont.innerText = "🔒 Leitung eingerastet";
                    stopTriggered = false;
                    if (!isListening && !isSpeakingRightNow) {
                        synth.cancel();
                        safeStartRecognition();
                    }
                } else {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    btnCont.innerText = "📡 Dauerhafte Leitung";
                    stopTriggered = true;
                    recognition.stop();
                    synth.cancel();
                    statusText.innerText = "FUNKKANAL IM STANDBY // BEREIT";
                    setLED('#00d2ff', '#00d2ff');
                }
            });

            recognition.onstart = () => {
                isListening = true;
                statusText.innerText = "LEITUNG SCHARF // ICH HÖRE DIR ZU...";
                setLED('#ff3b30', '#ff3b30');
            };

            recognition.onend = () => {
                isListening = false;
                if (isContinuousMode && !stopTriggered && !isSpeakingRightNow && !permissionBlocked) {
                    setTimeout(() => { safeStartRecognition(); }, 500);
                } else if (!isContinuousMode && !isSpeakingRightNow) {
                    statusText.innerText = "FUNKKANAL IM STANDBY // BEREIT";
                    setLED('#00d2ff', '#00d2ff');
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                statusText.innerText = "BEFEHL AN DETEKTOREN...";
                setLED('#10b981', '#10b981');
                
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: JSON.stringify({text: userText, timestamp: Date.now()})
                }, '*');
            };

            recognition.onerror = (event) => {
                console.log("Audio-Fehler: " + event.error);
                if (event.error === 'not-allowed') {
                    permissionBlocked = true; // Stoppt die Schleife!
                    statusText.innerText = "RECHTE-BLOCKADE! BITTE 'IMMER ZULASSEN' WÄHLEN.";
                    setLED('#ff3b30', '#ff3b30');
                }
                if (isContinuousMode && !stopTriggered && !permissionBlocked) {
                    setTimeout(() => { safeStartRecognition(); }, 600);
                }
            };

            window.addEventListener('message', function(event) {
                if(event.data && event.data.orionSpeakText) {
                    orionSpeak(event.data.orionSpeakText);
                }
            });

            function orionSpeak(text) {
                isSpeakingRightNow = true;
                recognition.stop();
                synth.cancel();
                
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'de-DE';
                if (voices.length === 0) voices = synth.getVoices();
                let deVoice = voices.find(v => v.lang.startsWith('v')) || voices.find(v => v.lang.startsWith('de'));
                if (deVoice) utterance.voice = deVoice;
                utterance.pitch = 0.85;

                utterance.onstart = () => {
                    statusText.innerText = "ORION ANTWORTET...";
                    setLED('#10b981', '#10b981');
                };

                utterance.onend = () => {
                    isSpeakingRightNow = false;
                    if (isContinuousMode && !stopTriggered && !permissionBlocked) {
                        setTimeout(() => { safeStartRecognition(); }, 400);
                    } else {
                        statusText.innerText = "FUNKKANAL IM STANDBY // BEREIT";
                        setLED('#00d2ff', '#00d2ff');
                    }
                };
                synth.speak(utterance);
            }
        }
    </script>
    </body>
    </html>"""
    
    voice_data_raw = st.components.v1.html(VOICE_INTERFACE_HTML, height=140, scrolling=False)
    
    if voice_data_raw:
        try:
            data_parsed = json.loads(str(voice_data_raw))
            v_text = data_parsed.get("text", "")
            if v_text and ("last_v_text" not in st.session_state or st.session_state.last_v_text != v_text):
                st.session_state.last_v_text = v_text
                st.session_state.chat_history.append({"role": "user", "text": v_text})
                
                voice_reply = ask_orion_groq(v_text)
                st.session_state.chat_history.append({"role": "orion", "text": voice_reply})
                
                st.components.v1.html(f"""
                <script>
                    window.parent.postMessage({{orionSpeakText: {json.dumps(voice_reply)}}}, '*');
                </script>
                """, height=0)
                
                st.rerun()
        except:
            pass

    # CHAT-VERLAUF ANZEIGEN
    st.markdown("<p style='color: #10b981; font-weight: bold;'>📡 Kombinierter Kommunikations-Verlauf:</p>", unsafe_allow_html=True)
    
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #10b981; padding: 15px; min-height: 250px; max-height: 400px; overflow-y: auto; border-radius: 4px;'>"
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>Du:</strong> \"{msg['text']}\"</div>"
        else:
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>ORION:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# --- REGISTER 2: CONTROL CENTER & WEB-SCAN ---
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Cyber-Netzwerk Websuche & Wikipedia Modules")
    search_query = st.text_input("Deep-Scan Suchbegriff eingeben...", placeholder="z.B. Quantencomputer...")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("🌐 Globalen Web-Scan starten", use_container_width=True):
            if search_query:
                st.info(f"Scanne Matrix nach: '{search_query}'...")
                st.success(f"Eintrag gefunden! Daten im Elephant-Memory gesichert.")
            else:
                st.warning("Commander, bitte Suchbegriff einspeisen.")
    with col_s2:
        if st.button("📖 Wikipedia Sprach-Reader vorbereiten", use_container_width=True):
            st.info("Sprachausgabe v9.4 bereit für das Headset.")

# --- REGISTER 3: MISSIONS-NOTIZBUCH ---
elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Daten-Protokolle & Logbücher")
    new_note = st.text_area("Neue Direktive oder Notiz protokollieren:", placeholder="Schreibe hier deine Pläne auf...", height=150)
    if st.button("💾 Protokoll sichern", use_container_width=True):
        if new_note:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.notes.append(f"[{timestamp}] {new_note}")
            st.success("Notiz in der Elephant-Matrix verankert!")
        else:
            st.error("Eingabefeld leer, Commander.")

    if st.session_state.notes:
        st.markdown("<p style='color: #9ca3af; font-weight: bold;'>Gespeicherte Einträge:</p>", unsafe_allow_html=True)
        for note in reversed(st.session_state.notes):
            st.code(note, language="text")

# --- REGISTER 4: QUANTUM TERMINAL ---
elif module_selection == "💻 Quantum Terminal":
    st.subheader("💻 Kommando-Zeilen Terminal")
    cmd_input = st.text_input("Befehl eingeben...", placeholder="help, status, clear...", key="cmd_input")
    
    if cmd_input:
        cmd = cmd_input.strip().lower()
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        if cmd == "help":
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] Befehle: help, status, clear")
        elif cmd == "status":
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] CORE: 100% EXCELLENT.")
        elif cmd == "clear":
            st.session_state.terminal_logs = [f"[{timestamp}] Terminal geleert."]
        else:
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] Befehl an Core übermittelt.")

    terminal_box = "\n".join(st.session_state.terminal_logs[-10:])
    st.text_area("Terminal Output", value=terminal_box, height=300, disabled=True)
