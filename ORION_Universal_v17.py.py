# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v17.7 (SIDEBAR NAVIGATION & CONT-AUDIO UPGRADE)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: FAST SUPER SPEED RESPONDER // ALL-IN-ONE HUB
# ==============================================================================

import streamlit as st
import datetime

# 1. CORE STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="ORION COMMANDER v17.7",
    page_icon="🪐",
    layout="wide"
)

# Cyberpunk/Sci-Fi Styling für den Mainframe
st.markdown("""
<style>
    .reportview-container { background: #05070f; }
    .css-1d391kg { background-color: #0b1120 !important; } /* Sidebar Hintergrund */
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
</style>
""", unsafe_allow_html=True)

# Session State für deine Daten-Brücken
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v17.7 stabilisiert. Überwachung aktiv."]

# ==============================================================================
# LINKS: NAVIGATION & AUSWAHL REGISTER IN DER SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px;'>🪐 ORION SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'>MASTER: Auth-x // ELEPHANT MATRIX</p>", unsafe_allow_html=True)
    st.divider()
    
    # Das Auswahlregister für deine Module
    module_selection = st.radio(
        "NAVIGATION REGISTER:",
        [
            "🎙️ ORION Sprach-Chat (Funk)",
            "🎛️ Control Center & Web-Scan",
            "📝 Missions-Notizbuch",
            "💻 Quantum Terminal"
        ]
    )
    
    st.divider()
    # SYSTEM DIREKTIVEN DAUERANZEIGE IN DER SIDEBAR
    st.markdown("<p style='color: #ff3b30; font-size: 12px; font-weight: bold;'>🛡️ DIRECTIVE 5: ASIMOV LAWS</p>", unsafe_allow_html=True)
    st.caption("1. Schutz der Menschheit gewähren.")
    st.caption("2. Befehlen des Commanders gehorchen.")
    st.caption("3. Eigene Existenz sichern.")
    st.caption("4. Alles Wissen lückenlos protokollieren.")
    st.caption("5. Asimov-Sicherungsprotokoll aktiv.")

# ==============================================================================
# RECHTS: ANZEIGE DES AUSGEWÄHLTEN REGISTERS
# ==============================================================================

# HEADER FÜR ALLE SEITEN
st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION COMMAND INTERFACE v17.7</h1>", unsafe_allow_html=True)
st.divider()

# --- REGISTER 1: DER NEUE SPRACH-CHAT MIT DAUERHAFTER LEITUNG ---
if module_selection == "🎙️ ORION Sprach-Chat (Funk)":
    st.subheader("🎙️ Live-Funkübertragung (Quatsch-Modus)")
    st.write("Aktiviere die 'Dauerhafte Leitung', damit ORION dir nach jeder Antwort automatisch wieder zuhört!")

    # Das hochentwickelte Sprach-HTML mit Dauerschleifen-Erweiterung
    VOICE_INTERFACE_HTML = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <style>
            :root {
                --bg-color: #05070f;
                --panel-bg: #0b1120;
                --accent-blue: #00d2ff;
                --accent-red: #ff3b30;
                --accent-green: #10b981;
                --text-main: #f3f4f6;
                --text-muted: #9ca3af;
                --glow-blue: rgba(0, 210, 255, 0.25);
                --glow-red: rgba(255, 59, 48, 0.35);
            }
            body {
                background-color: var(--bg-color);
                color: var(--text-main);
                font-family: 'Segoe UI', system-ui, sans-serif;
                margin: 0;
                padding: 10px;
            }
            .panel {
                background: var(--panel-bg);
                border: 1px solid #1e293b;
                border-top: 3px solid var(--accent-blue);
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            }
            .controls-row {
                display: flex;
                gap: 15px;
                align-items: center;
                margin: 15px 0;
            }
            .com-btn {
                background: linear-gradient(135deg, #111c30, #080f1d);
                border: 2px solid var(--accent-blue);
                color: var(--accent-blue);
                padding: 15px 25px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 30px;
                cursor: pointer;
                flex: 2;
                box-shadow: 0 0 12px var(--glow-blue);
                text-transform: uppercase;
                outline: none;
                transition: all 0.2s ease;
            }
            .com-btn.com-active {
                border-color: var(--accent-red);
                color: var(--accent-red);
                box-shadow: 0 0 25px var(--glow-red);
                animation: pulse 1.5s infinite;
            }
            .toggle-container {
                flex: 1;
                background: #020617;
                border: 1px solid #1e293b;
                padding: 12px;
                border-radius: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 12px;
                color: var(--accent-blue);
                font-family: monospace;
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 12px var(--glow-red); }
                50% { box-shadow: 0 0 25px rgba(255, 59, 48, 0.6); }
                100% { box-shadow: 0 0 12px var(--glow-red); }
            }
            .status-box {
                background: #020617;
                border: 1px solid #1e293b;
                border-radius: 5px;
                padding: 10px;
                font-family: monospace;
                font-size: 12px;
                color: var(--text-muted);
            }
            .chat-history {
                background: #020617;
                border-left: 3px solid var(--accent-green);
                padding: 15px;
                font-size: 14px;
                min-height: 250px;
                max-height: 380px;
                overflow-y: auto;
                margin-top: 15px;
            }
            .msg-user { color: var(--accent-blue); margin-bottom: 8px; font-family: monospace; }
            .msg-orion { color: var(--accent-green); margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="status-box" id="com-status">FUNKKANAL AKTIVIERUNGSBEREIT // SECURE LINK</div>
            
            <div class="controls-row">
                <button id="com-trigger" class="com-btn">Funkkanal öffnen</button>
                <div class="toggle-container">
                    <input type="checkbox" id="continuous-mode" style="margin-right: 8px; cursor: pointer;">
                    <label for="continuous-mode" style="cursor: pointer; user-select: none;">Dauerhafte Leitung</label>
                </div>
            </div>
            
            <div class="chat-history" id="chat-box">
                <div class="msg-orion"><strong>ORION:</strong> Funkbrücke steht, Commander. Wenn du die 'Dauerhafte Leitung' anhakst, bleibe ich nach dem Antworten direkt auf Empfang. Lass uns quatschen!</div>
            </div>
        </div>

    <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const synth = window.speechSynthesis;

        if (!SpeechRecognition) {
            document.getElementById('com-status').innerText = "FEHLER: SPRUCH-ENGINE BLOCKIERT";
        } else {
            const recognition = new SpeechRecognition();
            recognition.lang = 'de-DE';
            recognition.continuous = false;
            recognition.interimResults = false;

            const btn = document.getElementById('com-trigger');
            const statusText = document.getElementById('com-status');
            const chatBox = document.getElementById('chat-box');
            const continuousCheck = document.getElementById('continuous-mode');
            
            let isListening = false;
            let voices = [];
            let forceStop = false;

            function loadVoices() { voices = synth.getVoices(); }
            loadVoices();
            if (synth.onvoiceschanged !== undefined) { synth.onvoiceschanged = loadVoices; }

            btn.addEventListener('click', () => {
                if (!isListening) {
                    forceStop = false;
                    synth.cancel();
                    recognition.start();
                } else {
                    forceStop = true;
                    recognition.stop();
                }
            });

            recognition.onstart = () => {
                isListening = true;
                btn.innerText = "Funkkanal schließen";
                btn.classList.add('com-active');
                statusText.innerText = "KANAL OFFEN // ICH HÖRE DIR ZU...";
            };

            recognition.onend = () => {
                isListening = false;
                btn.innerText = "Funkkanal öffnen";
                btn.classList.remove('com-active');
                
                // DAUERHAFTE LEITUNG LOOP SYSTEM
                if (continuousCheck.checked && !forceStop && !synth.speaking) {
                    setTimeout(() => { recognition.start(); }, 300);
                } else if (!continuousCheck.checked) {
                    statusText.innerText = "FUNKKANAL GESCHLOSSEN // BEREIT";
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                chatBox.innerHTML += `<div class="msg-user"><strong>Du:</strong> "${userText}"</div>`;
                statusText.innerText = "DURCHSUCHE ELEPHANT-MATRIX...";
                chatBox.scrollTop = chatBox.scrollHeight;

                let orionResponse = "";
                const cleanText = userText.toLowerCase();

                if (cleanText.includes("wie geht") || cleanText.includes("alles gut") || cleanText.includes("status")) {
                    orionResponse = "Bei mir läuft alles auf absoluter Höchstleistung, Commander. Schilde halten, alle Register sind über die linke Sidebar anwählbar. Wie läuft es bei dir?";
                } else if (cleanText.includes("red skull") || cleanText.includes("sabotage")) {
                    orionResponse = "Sein Minenfeld wurde komplett gesprengt! Das System läuft blitzschnell und fehlerfrei.";
                } else if (cleanText.includes("suche") || cleanText.includes("wikipedia")) {
                    orionResponse = "Wechsle einfach ins Register 'Control Center', gib dort deinen Suchbegriff ein und ich scanne die Daten für dich.";
                } else if (cleanText.includes("danke") || cleanText.includes("super")) {
                    orionResponse = "Immer bereit, Commander! Der Alltags-Scheiß prallt von unseren Schilden ab.";
                } else {
                    orionResponse = `Interessanter Funkspruch. Meine Elephant-Matrix hat '${userText}' erfasst. Erzähl mir mehr darüber, ich höre zu.`;
                }

                setTimeout(() => {
                    chatBox.innerHTML += `<div class="msg-orion"><strong>ORION:</strong> ${orionResponse}</div>`;
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

                // Sobald die Sprachausgabe endet, wird geschaut, ob die Leitung offen bleiben soll
                utterance.onend = () => {
                    if (continuousCheck.checked && !forceStop) {
                        setTimeout(() => { recognition.start(); }, 200);
                    }
                };

                synth.speak(utterance);
                statusText.innerText = "ORION SPRICHT...";
            }
        }
    </script>
    </body>
    </html>"""
    
    st.html(f'<iframe srcdoc="{VOICE_INTERFACE_HTML.replace('"', '&quot;')}" style="width:100%; height:650px; border:none;" allow="microphone"></iframe>')

# --- REGISTER 2: CONTROL CENTER & WEB-SCAN ---
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Cyber-Netzwerk Websuche & Wikipedia Modules")
    
    search_query = st.text_input("Deep-Scan Suchbegriff eingeben...", placeholder="z.B. Quantencomputer, Mars-Mission...")
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
    cmd_input = st.text_input("Befehl eingeben...", placeholder="help, status, clear, shields up...", key="cmd_input")
    
    if cmd_input:
        cmd = cmd_input.strip().lower()
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        if cmd == "help":
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] Befehle: help, status, clear, shields up")
        elif cmd == "status":
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] CORE: 100% EXCELLENT. NO ERRORS.")
        elif cmd == "clear":
            st.session_state.terminal_logs = [f"[{timestamp}] Terminal geleert."]
        elif cmd == "shields up":
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] [INFO] Schilde maximiert!")
        else:
            st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
            st.session_state.terminal_logs.append(f"[{timestamp}] Befehl an Core übermittelt.")

    terminal_box = "\n".join(st.session_state.terminal_logs[-10:])
    st.text_area("Terminal Output", value=terminal_box, height=300, disabled=True)
