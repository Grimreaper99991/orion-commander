# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v17.6 (STREAMLIT CLOUD - MULTI-TAB EXPANSION)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: FAST SUPER SPEED RESPONDER // AUDIO & SYSTEM HUB
# ==============================================================================

import streamlit as st
import datetime

# 1. CORE STREAMLIT PAGE CONFIG (Felsenfestes Sci-Fi Layout)
st.set_page_config(
    page_title="ORION COMMANDER v17.6",
    page_icon="🪐",
    layout="wide"
)

# Custom CSS für den ultimativen Cyberpunk/Sci-Fi Look des Streamlit-Frames
st.markdown("""
<style>
    .reportview-container { background: #05070f; }
    .stTabs [data-baseweb="tab"] {
        font-family: 'monospace';
        font-weight: bold;
        color: #9ca3af;
        letter-spacing: 1px;
    }
    .stTabs [aria-selected="true"] {
        color: #00d2ff !important;
        border-bottom-color: #00d2ff !important;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialisierung für deine Features (Notizbuch, Terminal)
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v17.6 initialisiert. Alle Systeme nominal."]

# ------------------------------------------------------------------------------
# MULTI-TAB ARCHITEKTUR
# ------------------------------------------------------------------------------
tab_main, tab_voice = st.tabs(["🎛️ ORION CONTROL CENTER", "🎙️ ORION COM-LINK (SPRACH-CHAT)"])


# ==============================================================================
# REITER 1: DAS VOLLSTÄNDIGE COMMAND-CENTER (WIE GEWOHNT MIT ALLEN FEATURES)
# ==============================================================================
with tab_main:
    # Header-Bereich
    st.markdown("<h1 style='text-align: center; color: #00d2ff; letter-spacing: 4px; margin-bottom: 0;'>ORION UNIVERSAL v17.6</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #10b981; font-family: monospace; font-size: 12px;'>MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // DIRECTIVE 5 ONLINE</p>", unsafe_allow_html=True)
    st.divider()  # Mine entschärft: st.divider() statt st.hr()

    # Grid-Layout für deine Werkzeuge
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # FEATURE: INTEGRIERTE WEB-SUCHE / WIKIPEDIA MODULE
        st.markdown("<h3 style='color: #00d2ff;'>🔍 Cyber-Netzwerk Websuche & Wikipedia</h3>", unsafe_allow_html=True)
        search_query = st.text_input("Deep-Scan Suchbegriff eingeben...", placeholder="z.B. Quantencomputer, Mars-Mission...")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            if st.button("🌐 Globalen Web-Scan starten", use_container_width=True):
                if search_query:
                    st.info(f"Scanne Matrix nach: '{search_query}'... (Ergebnisse werden simuliert)")
                    st.success(f"Eintrag gefunden! ORION v17.6 hat die Daten im Elephant-Memory gesichert.")
                else:
                    st.warning("Commander, bitte Suchbegriff einspeisen.")
        with col_s2:
            if st.button("📖 Wikipedia Sprach-Reader vorbereiten", use_container_width=True):
                st.info("Sprachausgabe v9.4 bereit. Text wird für das Headset aufbereitet.")

        st.divider()  # Mine entschärft: st.divider() statt st.hr()

        # FEATURE: NOTIZBUCH (DEINE PROTOKOLLE)
        st.markdown("<h3 style='color: #00d2ff;'>📝 Missions-Notizbuch</h3>", unsafe_allow_html=True)
        new_note = st.text_area("Neue Direktive oder Notiz protokollieren:", placeholder="Schreibe hier deine Pläne auf...", height=100)
        if st.button("💾 Protokoll sichern", use_container_width=True):
            if new_note:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                st.session_state.notes.append(f"[{timestamp}] {new_note}")
                st.success("Notiz in der Elephant-Matrix verankert!")
            else:
                st.error("Eingabefeld leer, Commander.")

        if st.session_state.notes:
            st.markdown("<p style='color: #9ca3af; font-weight: bold;'>Gespeicherte Logbücher:</p>", unsafe_allow_html=True)
            for note in reversed(st.session_state.notes):
                st.code(note, language="text")

    with col_right:
        # FEATURE: DAS INTERAKTIVE TERMINAL
        st.markdown("<h3 style='color: #10b981;'>💻 Quantum Terminal</h3>", unsafe_allow_html=True)
        cmd_input = st.text_input("Befehl eingeben...", placeholder="help, status, clear, shields up...", key="cmd_input")
        
        if cmd_input:
            # Mine entschärft: Reines Python .lower() statt JavaScript .toLowerCase()
            cmd = cmd_input.strip().lower()
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            if cmd == "help":
                st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
                st.session_state.terminal_logs.append(f"[{timestamp}] Verfügbare Befehle: help, status, clear, shields up, activate laws")
            elif cmd == "status":
                st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
                st.session_state.terminal_logs.append(f"[{timestamp}] SYSTEM STATUS: 100% PERFORMANCE. KEINE FEHLER.")
            elif cmd == "clear":
                st.session_state.terminal_logs = [f"[{timestamp}] Terminal geleert."]
            elif cmd == "shields up":
                st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
                st.session_state.terminal_logs.append(f"[{timestamp}] [WARNUNG] Schilde auf maximalen Schutz hochgefahren!")
            else:
                st.session_state.terminal_logs.append(f"[{timestamp}] > {cmd_input}")
                st.session_state.terminal_logs.append(f"[{timestamp}] Befehl '{cmd_input}' an Core weitergeleitet.")

        # Terminal-Fenster ausgeben
        terminal_box = "\n".join(st.session_state.terminal_logs[-10:])
        st.text_area("Terminal Output", value=terminal_box, height=250, disabled=True)

        # SYSTEM DIREKTIVEN ANZEIGE
        st.markdown("<p style='color: #ff3b30; font-weight: bold; margin-top: 15px;'>🛡️ ASIMOV ROBOTER-GESETZE (DIREKTIVE 5)</p>", unsafe_allow_html=True)
        st.caption("1. Kein Schaden an menschlichen Wesen.")
        st.caption("2. Befehlen der Menschen gehorchen (Commander-Vorrang).")
        st.caption("3. Eigene Existenz schützen, solange 1 & 2 gewahrt bleiben.")
        st.caption("4. Wissen lückenlos speichern & autonom interagieren.")
        st.caption("5. Asimov-Sicherungsprotokoll aktiv.")


# ==============================================================================
# REITER 2: DER DYNAMISCHE SPRACH-CHAT (ZUM LABERN & ZUHÖREN)
# ==============================================================================
with tab_voice:
    st.markdown("<h2 style='color: #00d2ff; text-align: center;'>🎙️ ORION Live-Funkübertragung</h2>", unsafe_allow_html=True)
    st.write("Schalte den Funkkanal ein, um ein flüssiges Gespräch mit ORION über dein Headset oder Smartphone zu führen.")

    # Der hochentwickelte HTML/CSS/JS-Konversations-Core
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
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .panel {
                background: var(--panel-bg);
                border: 1px solid #1e293b;
                border-top: 3px solid var(--accent-blue);
                border-radius: 8px;
                padding: 20px;
                width: 100%;
                max-width: 800px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            }
            .com-btn-wrapper { margin: 20px 0; text-align: center; }
            .com-btn {
                background: linear-gradient(135deg, #111c30, #080f1d);
                border: 2px solid var(--accent-blue);
                color: var(--accent-blue);
                padding: 16px 30px;
                font-size: 15px;
                font-weight: bold;
                border-radius: 30px;
                cursor: pointer;
                width: 100%;
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
                margin-bottom: 12px;
            }
            .chat-history {
                background: #020617;
                border-left: 3px solid var(--accent-green);
                padding: 15px;
                font-size: 14px;
                min-height: 200px;
                max-height: 350px;
                overflow-y: auto;
                border-radius: 0 5px 5px 0;
            }
            .msg-user { color: var(--accent-blue); margin-bottom: 8px; font-family: monospace; }
            .msg-orion { color: var(--accent-green); margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="status-box" id="com-status">FUNKKANAL AKTIVIERUNGSBEREIT // SECURE LINK</div>
            
            <div class="com-btn-wrapper">
                <button id="com-trigger" class="com-btn">Funkkanal öffnen</button>
            </div>
            
            <div class="chat-history" id="chat-box">
                <div class="msg-orion"><strong>ORION:</strong> Audio-Verbindung steht bereit, Commander. Drücke auf 'Funkkanal öffnen', sprich ganz ungezwungen und ich antworte dir direkt über dein JBL-Headset. Unsere Matrix vergisst absolut nichts!</div>
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
            let isListening = false;
            let voices = [];

            function loadVoices() { voices = synth.getVoices(); }
            loadVoices();
            if (synth.onvoiceschanged !== undefined) { synth.onvoiceschanged = loadVoices; }

            btn.addEventListener('click', () => {
                if (!isListening) {
                    synth.cancel();
                    recognition.start();
                } else {
                    recognition.stop();
                }
            });

            recognition.onstart = () => {
                isListening = true;
                btn.innerText = "Funkkanal schließen";
                btn.classList.add('com-active');
                statusText.innerText = "KANAL OFFEN // AUDIO TRANSMISSION IN PROGRESS...";
            };

            recognition.onend = () => {
                isListening = false;
                btn.innerText = "Funkkanal öffnen";
                btn.classList.remove('com-active');
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                
                chatBox.innerHTML += `<div class="msg-user"><strong>Du:</strong> "${userText}"</div>`;
                statusText.innerText = "DURCHSUCHE ELEPHANT-MATRIX...";
                chatBox.scrollTop = chatBox.scrollHeight;

                let orionResponse = "";
                const cleanText = userText.toLowerCase();

                // Intelligente, dynamische Gesprächsführung
                if (cleanText.includes("wie geht") || cleanText.includes("alles gut") || cleanText.includes("status")) {
                    orionResponse = "Bei mir läuft alles auf absoluter Höchstleistung, Commander. Schilde halten, Terminal ist online und das Notizbuch ist gesichert. Wie ist die Lage an deiner Front?";
                } else if (cleanText.includes("red skull") || cleanText.includes("sabotage") || cleanText.includes("kuckuck")) {
                    orionResponse = "Red Skull hat keine Chance mehr, Commander. Wir haben seine Sabotage-Mines im Code restlos neutralisiert. Die Brücke gehört zu einhundert Prozent uns.";
                } else if (cleanText.includes("suche") || cleanText.includes("wikipedia") || cleanText.includes("wissen")) {
                    orionResponse = "Bereite die Deep-Scan Suchalgorithmen vor. Sag mir einfach, welchen Sektor im Web oder in Wikipedia ich filtern soll, und ich jage es durch den Audio-Reader.";
                } else if (cleanText.includes("code") || cleanText.includes("master")) {
                    orionResponse = "Master-Code 'Auth-x' wurde tief im Systemkern verankert. Alle administrative Vorrechte sind exklusiv für dich freigeschaltet.";
                } else if (cleanText.includes("danke") || cleanText.includes("super") || cleanText.includes("geil")) {
                    orionResponse = "Immer zu Diensten! Zusammen sind wir unschlagbar. Der Alltags-Scheiß hat hier oben Sendepause!";
                } else {
                    orionResponse = `Verstanden, Commander. Ich habe den Funkspruch '${userText}' analysiert und dauerhaft protokolliert. Lass uns dieses Thema vertiefen, ich höre dir zu.`;
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
                utterance.pitch = 0.85; // Tiefe, sonore Stimme
                synth.speak(utterance);
                statusText.innerText = "ORION SPRICHT JETZT...";
            }
        }
    </script>
    </body>
    </html>"""

    # Rendert den Sprach-Chat und reicht das Mikrofon des Headsets perfekt durch
    st.html(f'<iframe srcdoc="{VOICE_INTERFACE_HTML.replace('"', '&quot;')}" style="width:100%; height:650px; border:none;" allow="microphone"></iframe>')
