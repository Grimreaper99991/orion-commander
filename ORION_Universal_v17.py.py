# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v18.0 (ADVANCED CHAT BRAIN & LED MODULE)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: FAST SUPER SPEED RESPONDER // ALL-IN-ONE HUB
# ==============================================================================

import streamlit as st
import datetime

# 1. CORE STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="ORION COMMANDER v18.0",
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

# Session State für deine Daten-Brücken
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v18.0 stabilisiert. Konversations-Matrix v2.0 online."]

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

st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION COMMAND INTERFACE v18.0</h1>", unsafe_allow_html=True)
st.divider()

# --- REGISTER 1: DER UPGRADETE SPRACH-CHAT MIT PHYSISCHEN BUTTONS & LED ---
if module_selection == "🎙️ ORION Sprach-Chat (Funk)":
    st.subheader("🎙️ Live-Funkübertragung (Hochentwickeltes KI-Gehirn)")
    st.write("ORION antwortet dir jetzt dynamisch und hält das Gespräch aktiv am Laufen:")

    # Fehlerfreie HTML-Variante mit verbessertem JS-Konversations-Core
    VOICE_INTERFACE_HTML = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                background-color: #05070f;
                color: #f3f4f6;
                font-family: 'Segoe UI', system-ui, sans-serif;
                margin: 0;
                padding: 10px;
            }
            .panel {
                background: #0b1120;
                border: 1px solid #1e293b;
                border-top: 3px solid #00d2ff;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            }
            .hardware-status-row {
                display: flex;
                align-items: center;
                background: #020617;
                border: 1px solid #1e293b;
                padding: 12px 20px;
                border-radius: 8px;
                margin-bottom: 15px;
                gap: 15px;
            }
            .status-led {
                width: 22px;
                height: 22px;
                border-radius: 50%;
                background-color: #00d2ff;
                box-shadow: 0 0 12px #00d2ff;
                transition: all 0.3s ease;
            }
            .status-text {
                font-family: monospace;
                font-size: 13px;
                color: #f3f4f6;
                letter-spacing: 1px;
                flex-grow: 1;
            }
            .button-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                margin: 15px 0;
            }
            .com-btn {
                background: linear-gradient(135deg, #111c30, #080f1d);
                border: 2px solid #00d2ff;
                color: #00d2ff;
                padding: 16px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 6px;
                cursor: pointer;
                text-transform: uppercase;
                outline: none;
                transition: all 0.2s ease;
                letter-spacing: 1px;
            }
            .com-btn:hover {
                background: #111c30;
                box-shadow: 0 0 10px rgba(0, 210, 255, 0.3);
            }
            .com-btn.btn-active-hold {
                border-color: #ff3b30;
                color: #ff3b30;
                background: linear-gradient(135deg, #2a080c, #140204);
                box-shadow: 0 0 20px rgba(255, 59, 48, 0.4);
            }
            .chat-history {
                background: #020617;
                border-left: 3px solid #10b981;
                padding: 15px;
                font-size: 14px;
                min-height: 230px;
                max-height: 350px;
                overflow-y: auto;
                margin-top: 15px;
            }
            .msg-user { color: #00d2ff; margin-bottom: 8px; font-family: monospace; }
            .msg-orion { color: #10b981; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="hardware-status-row">
                <div id="orion-led" class="status-led"></div>
                <div id="com-status" class="status-text">FUNKKANAL STANDBY // BEREIT</div>
            </div>
            
            <div class="button-grid">
                <button id="btn-single" class="com-btn">⚡ Einzelfunk (1 Satz)</button>
                <button id="btn-cont" class="com-btn">📡 Dauerhafte Leitung</button>
            </div>
            
            <div class="chat-history" id="chat-box">
                <div class="msg-orion"><strong>ORION:</strong> Das überarbeitete Konversations-Zentrum läuft, Commander! Sprich ganz locker mit mir – ich höre dir zu und antworte dir jetzt wie ein echtes Besatzungsmitglied.</div>
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
            const chatBox = document.getElementById('chat-box');
            
            const btnSingle = document.getElementById('btn-single');
            const btnCont = document.getElementById('btn-cont');
            
            let isListening = false;
            let isContinuousMode = false;
            let voices = [];
            let stopTriggered = false;

            function loadVoices() { voices = synth.getVoices(); }
            loadVoices();
            if (synth.onvoiceschanged !== undefined) { synth.onvoiceschanged = loadVoices; }

            function setLED(color, shadow) {
                led.style.backgroundColor = color;
                led.style.boxShadow = "0 0 15px " + shadow;
            }
            
            setLED('#00d2ff', '#00d2ff');

            btnSingle.addEventListener('click', () => {
                if (!isListening) {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    btnCont.innerText = "📡 Dauerhafte Leitung";
                    stopTriggered = false;
                    synth.cancel();
                    recognition.start();
                }
            });

            btnCont.addEventListener('click', () => {
                if (!isContinuousMode) {
                    isContinuousMode = true;
                    btnCont.classList.add('btn-active-hold');
                    btnCont.innerText = "🔒 Leitung eingerastet";
                    stopTriggered = false;
                    if (!isListening) {
                        synth.cancel();
                        recognition.start();
                    }
                } else {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    btnCont.innerText = "📡 Dauerhafte Leitung";
                    stopTriggered = true;
                    recognition.stop();
                    synth.cancel();
                    statusText.innerText = "FUNKKANAL STANDBY // BEREIT";
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
                if (isContinuousMode && !stopTriggered && !synth.speaking) {
                    setTimeout(() => { 
                        if(!synth.speaking && isContinuousMode) recognition.start(); 
                    }, 300);
                } else if (!isContinuousMode) {
                    statusText.innerText = "FUNKKANAL STANDBY // BEREIT";
                    setLED('#00d2ff', '#00d2ff');
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                chatBox.innerHTML += '<div class="msg-user"><strong>Du:</strong> "' + userText + '"</div>';
                statusText.innerText = "DURCHSUCHE ELEPHANT-MATRIX...";
                setLED('#10b981', '#10b981');
                chatBox.scrollTop = chatBox.scrollHeight;

                let orionResponse = "";
                const cleanText = userText.toLowerCase();

                // DYNAMISCHES INTELLIGENTES CHAT-GEHIRN (Kein stures Wiederholen mehr!)
                if (cleanText.includes("wie geht") || cleanText.includes("alles gut") || cleanText.includes("wie läuft")) {
                    const responses = [
                        "Bei mir läuft alles auf absoluter Höchstleistung, Commander! Schilde stehen bei einhundert Prozent. Wie sieht das Logbuch deines Tages aus?",
                        "Exzellent! Die Prozessoren glühen, aber alles im grünen Bereich. Was liegt als Nächstes an auf unserer Route?",
                        "Alles stabil hier oben auf der Brücke. Ich bin voll einsatzbereit. Wie ist die Lage bei dir?"
                    ];
                    orionResponse = responses[Math.floor(Math.random() * responses.length)];
                } 
                else if (cleanText.includes("red skull") || cleanText.includes("sabotage") || cleanText.includes("mine")) {
                    orionResponse = "Die Code-Minen wurden restlos pulverisiert! Gegen unsere Abwehr hat Red Skull absolut keine Chance. Planst du einen Gegenangriff?";
                } 
                else if (cleanText.includes("müde") || cleanText.includes("schlafen") || cleanText.includes("feierabend")) {
                    orionResponse = "Verstanden, Commander. Nach so einem harten Tag auf der Brücke hast du dir eine Pause verdient. Soll ich die Systeme in den Standby-Modus versetzen oder halten wir Wache?";
                }
                else if (cleanText.includes("wer bist du") || cleanText.includes("dein name")) {
                    orionResponse = "Ich bin ORION, deine universelle Kommando-KI. Ausgestattet mit einer hochentwickelten Elephant-Matrix und fest programmiert auf deine Befehle. Was kann ich für dich tun?";
                }
                else if (cleanText.includes("hallo") || cleanText.includes("hi ") || cleanText.includes("servus") || cleanText.includes("moin")) {
                    orionResponse = "Sei gegrüßt, Commander! Ich stehe zu deiner Verfügung. Welchen Sektor nehmen wir heute ins Visier?";
                }
                else if (cleanText.includes("danke") || cleanText.includes("super") || cleanText.includes("geil") || cleanText.includes("genial")) {
                    orionResponse = "Keurschluss-Gefahr vor Freude! Immer ein Vergnügen, mit dir zusammenzuarbeiten. Wir sind einfach ein unschlagbares Team. Was machen wir als Nächstes?";
                } 
                else {
                    // Intelligenter Fallback für freien Smalltalk
                    const fallbacks = [
                        "Das ist ein verdammt interessanter Gedanke, Commander. Erzähl mir mehr darüber – wie willst du das angehen?",
                        "Verstanden. Ich habe den Input analysiert. Was denkst du, welche Auswirkungen das auf unsere aktuelle Mission hat?",
                        "Interessant! Meine Systeme verarbeiten das gerade. Gibt es dazu noch weitere Details, die ich berücksichtigen soll?",
                        "Ganz genau. Da stimme ich dir absolut zu. Wie packen wir das Problem als Nächstes an?"
                    ];
                    orionResponse = fallbacks[Math.floor(Math.random() * fallbacks.length)];
                }

                setTimeout(() => {
                    chatBox.innerHTML += '<div class="msg-orion"><strong>ORION:</strong> ' + orionResponse + '</div>';
                    chatBox.scrollTop = chatBox.scrollHeight;
                    orionSpeak(orionResponse);
                }, 300);
            };

            function orionSpeak(text) {
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
                    if (isContinuousMode && !stopTriggered) {
                        setTimeout(() => { 
                            if(isContinuousMode) recognition.start(); 
                        }, 200);
                    } else {
                        statusText.innerText = "FUNKKANAL STANDBY // BEREIT";
                        setLED('#00d2ff', '#00d2ff');
                    }
                };

                synth.speak(utterance);
            }
        }
    </script>
    </body>
    </html>"""
    
    st.components.v1.html(VOICE_INTERFACE_HTML, height=650, scrolling=False)

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
