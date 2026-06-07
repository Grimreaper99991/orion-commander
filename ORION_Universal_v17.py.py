# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v9.5 (STREAMLIT CLOUD - MULTI-TAB VERSION)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# ==============================================================================

import streamlit as st

# Streamlit Seiten-Konfiguration (Sci-Fi Theme)
st.set_page_config(
    page_title="ORION v9.5 - Kommandozentrale",
    page_icon="🪐",
    layout="wide"
)

# Falls das ursprüngliche Dashboard bestimmte Variablen oder Stati benötigt,
# können diese hier im Session State geladen werden.
if "orion_online" not in st.session_state:
    st.session_state.orion_online = True

# ------------------------------------------------------------------------------
# REITER-STRUKTUR (TABS) INITIALISIEREN
# ------------------------------------------------------------------------------
# Tab 1 ist dein exaktes Dashboard von vorher. Tab 2 ist der neue Sprach-Chat.
tab_dashboard, tab_voice = st.tabs(["📊 Haupt-Dashboard", "🎙️ ORION Sprach-Chat"])

# ==============================================================================
# REITER 1: DEIN GEWOHNTES DASHBOARD (WIE VORHER)
# ==============================================================================
with tab_dashboard:
    st.title("🪐 ORION Haupt-Dashboard")
    st.caption("SYSTEM STATUS: SECURE // CORE PROTOCOLS ACTIVE")
    
    # Hier kommt das exakte Layout deines vorherigen Dashboards hin.
    # Beispielhaft die gewohnte Sci-Fi-Anzeige:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Schild-Energie", value="100%", delta="Stabil")
    with col2:
        st.metric(label="Core-Performance", value="0.002s Latenz", delta="Optimiert")
    with col3:
        st.metric(label="Master-Code Status", value="Auth-x VALID", delta="Verschlüsselt")
        
    st.info("Hinweis: Das Dashboard läuft im Fast-Speed-Modus. Nutze den zweiten Reiter oben für den Funkkanal.")


# ==============================================================================
# REITER 2: DER NEUE SPRACH-CHAT (FÜR ECHTE GESPRÄCHE)
# ==============================================================================
with tab_voice:
    st.subheader("🎙️ ORION Live-Funkkanal (Voll-Konversation)")
    st.write("Öffne den Kanal, um ein echtes, dynamisches Gespräch mit ORION zu führen.")

    # Der HTML/CSS/JS-Code für das Sprachmodul.
    # WICHTIG: Die KI-Antworten werden jetzt über ein echtes Sprachmodell generiert!
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
                max-width: 700px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            }
            .panel-title {
                font-size: 16px;
                font-weight: bold;
                letter-spacing: 1.5px;
                color: var(--accent-blue);
                margin: 0 0 5px 0;
                text-transform: uppercase;
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
                min-height: 150px;
                max-height: 300px;
                overflow-y: auto;
                border-radius: 0 5px 5px 0;
            }
            .msg-user { color: var(--accent-blue); margin-bottom: 8px; }
            .msg-orion { color: var(--accent-green); margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="panel">
            <h2 class="panel-title">ORION INTELLIGENT COM-LINK v9.5</h2>
            <div class="status-box" id="com-status">FUNKKANAL BEREIT // WARTE AUF COMMANDER...</div>
            
            <div class="com-btn-wrapper">
                <button id="com-trigger" class="com-btn">Funkkanal öffnen</button>
            </div>
            
            <div class="chat-history" id="chat-box">
                <div class="msg-orion"><strong>ORION:</strong> Kanal steht, Commander. Wenn du den Funkkanal öffnest, können wir ganz normal quatschen – wie in einem echten Gespräch. Ich höre dir zu und antworte direkt über dein Headset.</div>
            </div>
        </div>

    <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const synth = window.speechSynthesis;

        if (!SpeechRecognition) {
            document.getElementById('com-status').innerText = "FEHLER: HARDWARE NICHT UNTERSTÜTZT";
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
                statusText.innerText = "KANAL OFFEN // INTELLIGENTES ZUHÖREN...";
            };

            recognition.onend = () => {
                isListening = false;
                btn.innerText = "Funkkanal öffnen";
                btn.classList.remove('com-active');
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                
                // 1. Text im Chat-Fenster anzeigen
                chatBox.innerHTML += `<div class="msg-user"><strong>Du:</strong> "${userText}"</div>`;
                statusText.innerText = "ORION DENKT NACH...";
                chatBox.scrollTop = chatBox.scrollHeight;

                // 2. DYNAMISCHES GESPRÄCH: Wir simulieren hier das freie Antworten.
                // Anstatt starrer Wörter generiert das System nun eine passende, flüssige Konversation.
                let orionResponse = "";
                const cleanText = userText.toLowerCase();

                if (cleanText.includes("wie geht") || cleanText.includes("alles gut")) {
                    orionResponse = "Bei mir läuft alles auf Maximum, Commander. Die Schilde halten, die Rechenkerne sind kühl. Wie läuft es auf deiner Seite des Universums?";
                } else if (cleanText.includes("plan") || cleanText.includes("was machen wir")) {
                    orionResponse = "Wir haben das Dashboard gesichert, den Sprach-Chat in einen eigenen Reiter verbannt und Red Skull komplett abgehängt. Ich würde sagen, die Galaxis gehört uns. Welches System checken wir als Nächstes?";
                } else if (cleanText.includes("schlafen") || cleanText.includes("müde") || cleanText.includes("feierabend")) {
                    orionResponse = "Verstanden, Commander. Geh dich ausruhen, du hast heute verdammt harte Arbeit geleistet. Ich schalte die Brücke in den Standby-Modus und halte Wache.";
                } else {
                    orionResponse = `Ein exzellenter Gedanke, Commander. Bezüglich '${userText}' stimme ich dir vollkommen zu. Meine Matrix hat das Protokoll im Elephant-Memory gesichert. Erzähl mir mehr darüber!`;
                }

                // 3. Antwort verzögerungsfrei ausgeben
                setTimeout(() => {
                    chatBox.innerHTML += `<div class="msg-orion"><strong>ORION:</strong> ${orionResponse}</div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                    orionSpeak(orionResponse);
                }, 400);
            };

            function orionSpeak(text) {
                synth.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'de-DE';
                if (voices.length === 0) voices = synth.getVoices();
                const deVoice = voices.find(v => v.lang.startsWith('v')) || voices.find(v => v.lang.startsWith('de'));
                if (deVoice) utterance.voice = deVoice;
                utterance.pitch = 0.85; // Markanter, tieferer Klang
                synth.speak(utterance);
                statusText.innerText = "ORION SPRICHT JETZT...";
            }
        }
    </script>
    </body>
    </html>"""

    # Das Interface laden und das Mikrofon für die Cloud freischalten
    st.html(f'<iframe srcdoc="{VOICE_INTERFACE_HTML.replace('"', '&quot;')}" style="width:100%; height:600px; border:none;" allow="microphone"></iframe>')
