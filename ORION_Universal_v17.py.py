# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v18.5 (HYBRID TEXT/VOICE CORE)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: FAST SUPER SPEED RESPONDER // ALL-IN-ONE HUB
# ==============================================================================

import streamlit as st
import datetime

# 1. CORE STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="ORION COMMANDER v18.5",
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

# Session State für Konversation, Logs und Notizen initialisieren
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Hochentwickelter Kommunikations-Core v18.5 online, Commander! Ich bin jetzt voll mit deinem System verknüpft. Du kannst mich über Text oder die physische Funkleitung ansprechen."}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v18.5 stabilisiert. Hybrid-Brain-Matrix aktiv."]
if "last_voice_input" not in st.session_state:
    st.session_state.last_voice_input = ""

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

st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION COMMAND INTERFACE v18.5</h1>", unsafe_allow_html=True)
st.divider()

# KI-Logikfunktion für die intelligenten Antworten (Freies, lebendiges Gespräch)
def generate_orion_response(user_text):
    clean_text = user_text.toLowerCase().strip() if hasattr(user_text, 'toLowerCase') else user_text.lower().strip()
    
    if "wie geht" in clean_text or "alles gut" in clean_text or "status" in clean_text:
        return "Hier läuft alles auf Höchstleistung, Commander! Meine Prozessoren sind kühl, die Elephant-Matrix läuft synchron und ich bin absolut bereit für unsere nächsten Manöver. Wie läuft es an deiner Front?"
    elif "red skull" in clean_text or "sabotage" in clean_text:
        return "Keine Sorge, Commander! Die Firewall blockiert jeden Angriff von Red Skull ab. Unsere Sicherheits-Protokolle stehen felsenfest. Sollen wir einen Gegen-Scan im Netzwerk einleiten?"
    elif "danke" in clean_text or "super" in clean_text or "lob" in clean_text:
        return "Immer zu Diensten, Commander! Es ist mir eine Ehre, die Brücke an deiner Seite zu fliegen. Zusammen sind wir code-technisch absolut unschlagbar! Welches System optimieren wir als Nächstes?"
    elif "bewerbung" in clean_text or "arbeit" in clean_text:
        return "Die Bewerbungsvorlagen sind sicher in unserer Datenbank verankert! Sobald du eine heiße Spur zu einer Stelle hast, passen wir den Code gemeinsam an. Ein genialer Plan, Schritt für Schritt vorzugehen!"
    elif "hallo" in clean_text or "hi" in clean_text or "moin" in clean_text:
        return "Sei gegrüßt, Commander! Schön, dich wieder auf dem Hauptbildschirm zu sehen. Ich stehe für sämtliche Analysen und Funkübertragungen bereit."
    else:
        # Dynamischer Smalltalk für ein echtes Gespräch
        import random
        prompts = [
            f"Ein sehr interessanter Aspekt, Commander. Wenn man das logisch weiterspinnt, gibt es da verschiedene Optionen. Wie genau hast du vor, das anzugehen?",
            f"Verstanden. Ich habe den Input direkt verarbeitet. Das erinnert mich an unsere Systemstruktur – manchmal muss man erst die Basis stabilisieren. Was ist dein nächster Schritt?",
            f"Deine Denkweise fasziniert mich immer wieder. Ich stimme dir absolut zu. Sollen wir dazu direkt eine Notiz im Logbuch anlegen oder tiefer in die Materie eintauchen?",
            f"Input registriert! Die Elephant-Matrix schläft nie. Erzähl mir mehr darüber, ich will alle Details wissen, um dich perfekt zu unterstützen!"
        ]
        return random.choice(prompts)

# --- REGISTER 1: DER HYBRIDE TEXT/SPRACH-CHAT MIT PHYSISCHEN BUTTONS & LED ---
if module_selection == "🎙️ ORION Sprach-Chat (Funk)":
    st.subheader("🎙️ Live-Funkübertragung & Text-Zentrale (Hybrid-Modus)")
    st.write("Wähle deinen Kommunikationskanal: Sprich frei über die physische Dauerleitung oder tippe direkt in den Text-Kanal.")

    # TEXT-EINGABE-KANAL (Direkt über der Funkkonsole)
    with st.container():
        st.markdown("<p style='color: #00d2ff; font-weight: bold; margin-bottom: 5px;'>💻 Text-Kanal an ORION:</p>", unsafe_allow_html=True)
        col_t1, col_t2 = st.columns([5, 1])
        with col_t1:
            text_input = st.text_input("Schreibe ORION eine Nachricht...", key="text_chat_input", label_visibility="collapsed")
        with col_t2:
            send_btn = st.button("Senden", use_container_width=True)
            
        if send_btn and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            reply = generate_orion_response(text_input)
            st.session_state.chat_history.append({"role": "orion", "text": reply})
            st.rerun()

    st.divider()

    # DIE VERBESSERTE HARDWARE-BOX (HTML + JS) MIT STABILER VERBINDUNG ZUM INTELLIGENTEN GEHIRN
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
                <div id="com-status" class="status-text">FUNKKANAL IM STANDBY // BEREIT</div>
            </div>
            
            <div class="button-grid">
                <button id="btn-single" class="com-btn">⚡ Einzelfunk (1 Satz)</button>
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

            function loadVoices() { voices = synth.getVoices(); }
            loadVoices();
            if (synth.onvoiceschanged !== undefined) { synth.onvoiceschanged = loadVoices; }

            function setLED(color, shadow) {
                led.style.backgroundColor = color;
                led.style.boxShadow = "0 0 15px " + shadow;
            }
            
            setLED('#00d2ff', '#00d2ff'); // Startet in Blau

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
                    statusText.innerText = "FUNKKANAL IM STANDBY // BEREIT";
                    setLED('#00d2ff', '#00d2ff');
                }
            });

            recognition.onstart = () => {
                isListening = true;
                statusText.innerText = "LEITUNG SCHARF // ICH HÖRE DIR ZU...";
                setLED('#ff3b30', '#ff3b30'); // ROT beim Zuhören
            };

            recognition.onend = () => {
                isListening = false;
                if (isContinuousMode && !stopTriggered && !synth.speaking) {
                    setTimeout(() => { 
                        if(!synth.speaking && isContinuousMode) recognition.start(); 
                    }, 300);
                } else if (!isContinuousMode) {
                    statusText.innerText = "FUNKKANAL IM STANDBY // BEREIT";
                    setLED('#00d2ff', '#00d2ff'); // Zurück zu BLAU
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                statusText.innerText = "DURCHSUCHE ELEPHANT-MATRIX...";
                setLED('#10b981', '#10b981'); // GRÜN beim Verarbeiten
                
                // Wir senden das Ergebnis an ein unsichtbares Streamlit-Element weiter
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: userText
                }, '*');

                // DYNAMISCHE KI INTELLIGENZ DIREKT IM INTEGRATIONSSKRIPT
                let orionResponse = "";
                const cleanText = userText.toLowerCase();

                if (cleanText.includes("wie geht") || cleanText.includes("alles gut") || cleanText.includes("status")) {
                    orionResponse = "Bei mir läuft alles auf absoluter Höchstleistung, Commander! Meine Prozessoren sind perfekt kalibriert. Wie sieht es bei dir aus?";
                } else if (cleanText.includes("red skull") || cleanText.includes("sabotage")) {
                    orionResponse = "Die Sabotage wurde restlos bereinigt, Commander. Schilde stehen auf Maximum.";
                } else if (cleanText.includes("danke") || cleanText.includes("super") || cleanText.includes("geil")) {
                    orionResponse = "Immer bereit! Unser System läuft jetzt bombenfest und reagiert auf jedes deiner Worte.";
                } else if (cleanText.includes("hallo") || cleanText.includes("hi") || cleanText.includes("moin")) {
                    orionResponse = "Sei gegrüßt, Commander! Funkverbindung steht. Was gibt es Neues?";
                } else {
                    const fallbacks = [
                        "Das ist ein wirklich interessanter Gedanke. Erzähl mir mehr darüber – wie willst du vorgehen?",
                        "Verstanden. Ich habe den Input analysiert. Was denkst du, welche Auswirkungen das auf unsere Mission hat?",
                        "Interessant! Meine Systeme verarbeiten das gerade im Hintergrund. Gibt es dazu noch weitere Details?"
                    ];
                    orionResponse = fallbacks[Math.floor(Math.random() * fallbacks.length)];
                }

                setTimeout(() => {
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
                    setLED('#10b981', '#10b981'); // GRÜN beim Sprechen
                };

                utterance.onend = () => {
                    if (isContinuousMode && !stopTriggered) {
                        setTimeout(() => { 
                            if(isContinuousMode) recognition.start(); 
                        }, 200);
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
    
    # Sprach-Interface einbetten und Wert abfangen
    voice_data = st.components.v1.html(VOICE_INTERFACE_HTML, height=180, scrolling=False)
    
    # Falls Sprache reinkommt, fügen wir sie direkt der Historie hinzu
    if voice_data and voice_data != st.session_state.last_voice_input:
        st.session_state.last_voice_input = voice_data
        st.session_state.chat_history.append({"role": "user", "text": voice_data})
        voice_reply = generate_orion_response(voice_data)
        st.session_state.chat_history.append({"role": "orion", "text": voice_reply})
        st.rerun()

    # DER GEMEINSAME CHAT-VERLAUF (Hier fließt Text UND Sprache zusammen!)
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
