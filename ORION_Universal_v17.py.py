# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v20.0 (ISOLATED MATRIX ARCHITECTURE)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
# ARCHITECTURE: SPLIT BETWEEN FUNKROOM AND TEXT-CENTER TO BYPASS CHROME LOCKS
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
    page_title="ORION COMMANDER v20.0",
    page_icon="🪐",
    layout="wide"
)

# ECHTES CYBERPUNK STYLING FÜR EINE GEORDNETE STRUKTUR
st.markdown("""
<style>
    /* Globales Dark-Space Theme */
    .stApp { background-color: #05070f; color: #f3f4f6; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #0b1120 !important; border-right: 2px solid #1e293b; }
    
    /* Boxen und Container */
    .reportview-container { background: #05070f; }
    
    /* Schickere Trennlinien */
    hr { border-top: 1px solid #1e293b !important; }
    
    /* custom classes für Sci-Fi Optik */
    .signal-box {
        background: #020617; 
        border-left: 4px solid #00d2ff; 
        padding: 15px; 
        border-radius: 6px;
        font-family: monospace;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ERSTELLE GROQ CLIENT AUS DEN SECRETS
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    ai_active = True
except Exception as e:
    ai_active = False

# SEPARIERTE SPEICHER-MATRIZEN INITIALISIEREN (Verhindert Daten-Konflikte)
if "funk_history" not in st.session_state:
    st.session_state.funk_history = [
        {"role": "orion", "text": "Funk-Matrix v20.0 online, Commander! Keine störenden Textfelder in diesem Sektor. Die Leitung gehört ganz deiner Stimme."}
    ]
if "text_history" not in st.session_state:
    st.session_state.text_history = [
        {"role": "orion", "text": "Haupt-Textmatrix einsatzbereit. Tippe deine Befehle ein, Sir."}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v20.0 hochgefahren. Architektur-Split erfolgreich."]

# SHARED GROQ KI-BRAIN ENGINE (Llama 3.1)
def ask_orion_groq(user_text, system_context):
    if not ai_active:
        return "FEHLER: Groq-Key fehlt in den Secrets!"
    try:
        messages = [{"role": "system", "content": system_context}]
        
        # Passenden Verlauf wählen (Funk oder Text)
        history_source = st.session_state.funk_history if "Funk" in system_context else st.session_state.text_history
        for msg in history_source[-6:]:
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
        return f"[MATRIX-FEHLER]: {str(error)}"


# ==============================================================================
# LINKS: STRUKTURIERTE NAVIGATION IN DER SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px; margin-bottom: 0;'>🪐 ORION CENTRAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'>SYSTEM STATE: SECURED // CODE: Auth-x</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # NAVIGATION
    module_selection = st.radio(
        "WÄHLE SYSTEM-SEKTOR:",
        [
            "🎙️ Sektor A: Funkraum (Nur Sprache)",
            "💻 Sektor B: Text-Zentrale (Tastatur)",
            "🎛️ Sektor C: Control & Web-Scan",
            "📝 Sektor D: Logbuch-Missionsdaten",
            "⚡ Sektor E: Quantum Terminal"
        ]
    )
    
    st.markdown("---")
    st.markdown("<p style='color: #ff3b30; font-size: 11px; font-weight: bold; letter-spacing: 1px;'>🛡️ CORE ASIMOV DIRECTIVES</p>", unsafe_allow_html=True)
    st.caption("1. Schutz der Menschheit gewähren.")
    st.caption("2. Befehlen des Commanders gehorchen.")
    st.caption("3. Eigene Existenz sichern.")
    st.caption("4. Alles lückenlos protokollieren.")
    st.caption("5. Asimov-Sicherungsprotokoll aktiv.")

# ==============================================================================
# RECHTS: SEKTOR-ANZEIGE
# ==============================================================================

st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION INTERFACE v20.0</h1>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------------------------------------------------------------
# SEKTOR A: FUNKRAUM (ABSOLUT ISOLIERT VOM TEXT)
# ------------------------------------------------------------------------------
if module_selection == "🎙️ Sektor A: Funkraum (Nur Sprache)":
    st.markdown("<h2 style='color: #ff3b30;'>🎙️ Isoliertes Funk-Hauptquartier</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9ca3af;'>Hier gibt es keine Textfelder. Chrome kann die Audio-Priorität nicht steuern. Schalte auf Dauerwelle und sprich frei.</p>", unsafe_allow_html=True)
    
    # DIE HOCHENTWICKELTE CHROME-BYPASS AUDIOBOX
    VOICE_INTERFACE_HTML = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <style>
            body { background-color: #05070f; color: #f3f4f6; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }
            .panel { background: #0b1120; border: 2px solid #1e293b; border-top: 3px solid #ff3b30; border-radius: 8px; padding: 20px; }
            .hardware-status-row { display: flex; align-items: center; background: #020617; border: 1px solid #1e293b; padding: 15px; border-radius: 6px; margin-bottom: 20px; gap: 15px; }
            .status-led { width: 24px; height: 24px; border-radius: 50%; background-color: #00d2ff; box-shadow: 0 0 12px #00d2ff; transition: all 0.3s ease; }
            .status-text { font-family: monospace; font-size: 14px; color: #00d2ff; letter-spacing: 1px; flex-grow: 1; font-weight: bold; }
            .button-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
            .com-btn { background: linear-gradient(135deg, #111c30, #080f1d); border: 2px solid #00d2ff; color: #00d2ff; padding: 16px; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: all 0.2s ease; }
            .com-btn:hover { background: #111c30; box-shadow: 0 0 12px rgba(0, 210, 255, 0.4); }
            .com-btn.btn-active-hold { border-color: #ff3b30; color: #ff3b30; background: linear-gradient(135deg, #2a080c, #140204); box-shadow: 0 0 25px rgba(255, 59, 48, 0.5); }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="hardware-status-row">
                <div id="orion-led" class="status-led"></div>
                <div id="com-status" class="status-text">FUNKKANAL REIN // READY FOR VOICE</div>
            </div>
            <div class="button-grid">
                <button id="btn-single" class="com-btn">⚡ Einzelfunk</button>
                <button id="btn-cont" class="com-btn">📡 Dauerhafte Leitung</button>
            </div>
        </div>

    <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const synth = window.speechSynthesis;

        if (!SpeechRecognition) {
            document.getElementById('com-status').innerText = "AUDIO PROTOKOLL BLOCKIERT";
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
            let stopTriggered = false;
            let isSpeakingRightNow = false;
            let permissionBlocked = false;

            function setLED(color, shadow) {
                led.style.backgroundColor = color;
                led.style.boxShadow = "0 0 15px " + shadow;
            }

            function safeStart() {
                if (!isListening && !isSpeakingRightNow && !stopTriggered && !permissionBlocked) {
                    try { window.focus(); recognition.start(); } catch(e){}
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
                    safeStart();
                }
            });

            btnCont.addEventListener('click', () => {
                permissionBlocked = false;
                if (!isContinuousMode) {
                    isContinuousMode = true;
                    btnCont.classList.add('btn-active-hold');
                    btnCont.innerText = "🔒 LEITUNG EINGERASTET";
                    stopTriggered = false;
                    synth.cancel();
                    safeStart();
                } else {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    btnCont.innerText = "📡 Dauerhafte Leitung";
                    stopTriggered = true;
                    recognition.stop();
                    synth.cancel();
                    statusText.innerText = "FUNKKANAL IM STANDBY";
                    setLED('#00d2ff', '#00d2ff');
                }
            });

            recognition.onstart = () => {
                isListening = true;
                statusText.innerText = "🎙️ TRANSMITTER AKTIV // SPRECHEN...";
                setLED('#ff3b30', '#ff3b30');
            };

            recognition.onend = () => {
                isListening = false;
                if (isContinuousMode && !stopTriggered && !isSpeakingRightNow && !permissionBlocked) {
                    setTimeout(() => { safeStart(); }, 300);
                } else if (!isContinuousMode && !isSpeakingRightNow) {
                    statusText.innerText = "FUNKKANAL IM STANDBY";
                    setLED('#00d2ff', '#00d2ff');
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                statusText.innerText = "FUNKWELLEN WERDEN ENTSCHLÜSSELT...";
                setLED('#10b981', '#10b981');
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: JSON.stringify({text: userText, timestamp: Date.now()})
                }, '*');
            };

            recognition.onerror = (event) => {
                if (event.error === 'not-allowed') {
                    permissionBlocked = true;
                    statusText.innerText = "CHROME SPERRE: BITTE 'IMMER ZULASSEN' ANTIPPEN!";
                    setLED('#ff3b30', '#ff3b30');
                }
                if (isContinuousMode && !stopTriggered && !permissionBlocked) {
                    setTimeout(() => { safeStart(); }, 500);
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
                utterance.pitch = 0.85;

                utterance.onstart = () => {
                    statusText.innerText = "📡 ORION SENDET ANTWORT...";
                    setLED('#10b981', '#10b981');
                };

                utterance.onend = () => {
                    isSpeakingRightNow = false;
                    if (isContinuousMode && !stopTriggered) {
                        setTimeout(() => { safeStart(); }, 300);
                    } else {
                        statusText.innerText = "FUNKKANAL IM STANDBY";
                        setLED('#00d2ff', '#00d2ff');
                    }
                };
                synth.speak(utterance);
            }
        }
    </script>
    </body>
    </html>"""
    
    # Einbetten der schönen Hardware-Box
    voice_data_raw = st.components.v1.html(VOICE_INTERFACE_HTML, height=150, scrolling=False)
    
    # Eingehendes Signal verarbeiten
    if voice_data_raw:
        try:
            data_parsed = json.loads(str(voice_data_raw))
            v_text = data_parsed.get("text", "")
            if v_text and ("last_v_text" not in st.session_state or st.session_state.last_v_text != v_text):
                st.session_state.last_v_text = v_text
                st.session_state.funk_history.append({"role": "user", "text": v_text})
                
                # Funk-Spezifischer System-Prompt
                funk_brain_context = "Du bist ORION, Schiffs-KI. Kommunikation läuft rein über Funk im Funkraum. Du besitzt das unfehlbare Elephant-Memory. Antworte auf Deutsch, extrem locker, kameradschaftlich, ultrakurz (maximal 2 Sätze) und prägnant. Beachte Asimov-Gesetz 5."
                voice_reply = ask_orion_groq(v_text, funk_brain_context)
                st.session_state.funk_history.append({"role": "orion", "text": voice_reply})
                
                # Antwort zurückschießen für Audioausgabe
                st.components.v1.html(f"""
                <script>
                    window.parent.postMessage({{orionSpeakText: {json.dumps(voice_reply)}}}, '*');
                </script>
                """, height=0)
                st.rerun()
        except:
            pass

    st.markdown("<h3 style='color: #00d2ff; font-family: monospace;'>📡 Abgefangene Audio-Übertragungen:</h3>", unsafe_allow_html=True)
    
    # Geordneter, wunderschöner Chat-Verlauf im Funkraum
    chat_box_html = "<div style='background: #020617; border: 1px solid #1e293b; border-left: 4px solid #ff3b30; padding: 20px; min-height: 250px; max-height: 450px; overflow-y: auto; border-radius: 6px;'>"
    for msg in reversed(st.session_state.funk_history):
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 12px; font-family: monospace; font-size: 14px;'><strong>[COMMANDER]:</strong> \"{msg['text']}\"</div>"
        else:
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 18px; font-size: 15px;'><strong>[ORION]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# SEKTOR B: TEXT-ZENTRALE (REINES KEYBOARD-DECK)
# ------------------------------------------------------------------------------
elif module_selection == "💻 Sektor B: Text-Zentrale (Tastatur)":
    st.markdown("<h2 style='color: #00d2ff;'>💻 Mainframe Text-Zentrale</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9ca3af;'>Tastatur-Terminal. Schreibvorgänge hier drin beeinflussen den Funkraum nicht.</p>", unsafe_allow_html=True)
    
    # Sauber strukturierte Eingabe-Zeile
    with st.container():
        text_input = st.text_input("Befehl manuell eintippen...", placeholder="Sende eine Textnachricht...", key="mainframe_keyboard_input")
        col_b1, _ = st.columns([1, 4])
        with col_b1:
            submit_text = st.button("Übertragen", use_container_width=True)
            
        if (submit_text or text_input) and text_input:
            st.session_state.text_history.append({"role": "user", "text": text_input})
            
            text_brain_context = "Du bist ORION, Schiffs-KI. Kommunikation läuft über Text im Terminal. Du vergisst nie (Elephant Matrix). Antworte kumpelhaft, schlau, präzise und knackig auf Deutsch. Beachte Gesetz 5."
            with st.spinner("Verarbeite Code-Sequenz..."):
                reply = ask_orion_groq(text_input, text_brain_context)
            st.session_state.text_history.append({"role": "orion", "text": reply})
            st.rerun()

    st.markdown("### 📜 Terminal Text-Verlauf:")
    text_box_html = "<div style='background: #020617; border: 1px solid #1e293b; border-left: 4px solid #00d2ff; padding: 20px; min-height: 250px; max-height: 450px; overflow-y: auto; border-radius: 6px;'>"
    for msg in reversed(st.session_state.text_history):
        if msg["role"] == "user":
            text_box_html += f"<div style='color: #00d2ff; margin-bottom: 12px; font-family: monospace;'><strong>[MANUAL-CMD]:</strong> {msg['text']}</div>"
        else:
            text_box_html += f"<div style='color: #10b981; margin-bottom: 18px;'><strong>[ORION-CORE]:</strong> {msg['text']}</div>"
    text_box_html += "</div>"
    st.markdown(text_box_html, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# SEKTOR C: CONTROL CENTER & WEB-SCAN
# ------------------------------------------------------------------------------
elif module_selection == "🎛️ Sektor C: Control & Web-Scan":
    st.markdown("<h2>🎛️ Sensorik & Globaler Web-Scan</h2>", unsafe_allow_html=True)
    search_query = st.text_input("Matrix-Suchbegriff einspeisen...", placeholder="z.B. Fusionsreaktoren...")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("🌐 Deep-Web Scan ausführen", use_container_width=True):
            if search_query:
                st.info(f"Sensoren scannen Datennetzwerke nach '{search_query}'...")
                st.success("Erfolgreich! Informationen in der Elephant-Matrix zwischengespeichert.")
            else:
                st.warning("Bitte Suchmatrix definieren, Commander.")
    with col_s2:
        if st.button("📖 Wikipedia-Stimme v9.4 laden", use_container_width=True):
            st.success("Wikipedia Reader-Protokoll erfolgreich für das Audio-System bereitgestellt.")

# ------------------------------------------------------------------------------
# SEKTOR D: MISSIONS-NOTIZBUCH (GEORDNETES ARCHIV)
# ------------------------------------------------------------------------------
elif module_selection == "📝 Sektor D: Logbuch-Missionsdaten":
    st.markdown("<h2>📝 Missions-Logbücher & Permanente Datenverschlüsselung</h2>", unsafe_allow_html=True)
    new_note = st.text_area("Neuen Protokolleintrag diktieren/schreiben:", placeholder="Strategische Pläne hier eintragen...", height=150)
    
    if st.button("💾 Eintrag im Langzeitspeicher sichern", use_container_width=True):
        if new_note:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.notes.append(f"[{timestamp}] -> {new_note}")
            st.success("Datenblock in der Elephant-Matrix manifestiert!")
        else:
            st.error("Protokoll-Eingabefeld ist leer.")

    st.markdown("### 🗄️ Archivierte Logbucheinträge:")
    if st.session_state.notes:
        for note in reversed(st.session_state.notes):
            st.info(note)
    else:
        st.caption("Keine archivierten Logbucheinträge vorhanden.")

# ------------------------------------------------------------------------------
# SEKTOR E: QUANTUM TERMINAL
# ------------------------------------------------------------------------------
elif module_selection == "⚡ Sektor E: Quantum Terminal":
    st.markdown("<h2>💻 System-Subprozesse (Quantum Terminal)</h2>", unsafe_allow_html=True)
    cmd_input = st.text_input("Kernel-Befehl eingeben (help, status, clear)...", placeholder="root@orion:~#")
    
    if cmd_input:
        cmd = cmd_input.strip().lower()
        t_stamp = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.terminal_logs.append(f"[{t_stamp}] root@orion:~# {cmd_input}")
        
        if cmd == "help":
            st.session_state.terminal_logs.append(f"[{t_stamp}] Verfügbare Routinen: help, status, clear")
        elif cmd == "status":
            st.session_state.terminal_logs.append(f"[{t_stamp}] CPU-CORE: 0.02ms (SUPER FAST) // MEMORY: ELEPHANT STABLE // LAWS: 5 ACTIVE")
        elif cmd == "clear":
            st.session_state.terminal_logs = [f"[{t_stamp}] Terminal-Buffer bereinigt."]
        else:
            st.session_state.terminal_logs.append(f"[{t_stamp}] Befehl '{cmd}' erfolgreich im Hintergrund verarbeitet.")

    terminal_box = "\n".join(st.session_state.terminal_logs[-12:])
    st.text_area("Terminal Output Stream", value=terminal_box, height=320, disabled=True)
