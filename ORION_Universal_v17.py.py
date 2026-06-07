# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v9.4 (STREAMLIT CLOUD VERSION)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# ==============================================================================

import streamlit as st

# Streamlit Seiten-Konfiguration für schnelles Laden & Sci-Fi Feeling
st.set_page_config(
    page_title="ORION v9.4",
    page_icon="🪐",
    layout="wide"
)

# Das komplette HTML/CSS/JS Interface sicher verpackt in einer Variable
DASHBOARD_UI = """<!DOCTYPE html>
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
        .dashboard-container {
            width: 100%;
            max-width: 850px;
            display: grid;
            grid-template-columns: 1fr;
            gap: 15px;
        }
        @media (min-width: 768px) {
            .dashboard-container { grid-template-columns: 2fr 1fr; }
            .full-width { grid-column: span 2; }
        }
        .panel {
            background: var(--panel-bg);
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        }
        .panel-voice { border-top: 3px solid var(--accent-blue); }
        .panel-logs { border-top: 3px solid var(--accent-green); }
        .panel-title {
            font-size: 15px;
            font-weight: bold;
            letter-spacing: 1.5px;
            color: var(--accent-blue);
            margin: 0;
            text-transform: uppercase;
        }
        .panel-subtitle { font-size: 11px; color: var(--text-muted); margin: 3px 0 0 0; }
        .com-btn-wrapper { margin: 15px 0; text-align: center; }
        .com-btn {
            background: linear-gradient(135deg, #111c30, #080f1d);
            border: 2px solid var(--accent-blue);
            color: var(--accent-blue);
            padding: 15px 25px;
            font-size: 14px;
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
        .display-box {
            background: #020617;
            border-left: 3px solid var(--accent-green);
            padding: 12px;
            font-size: 13px;
            min-height: 50px;
        }
        .log-list { list-style: none; padding: 0; margin: 0; font-family: monospace; font-size: 11px; }
        .log-item { padding: 5px 0; border-bottom: 1px solid #0f172a; }
        .log-timestamp { color: var(--accent-blue); margin-right: 6px; }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="panel full-width" style="border-top: 3px solid var(--accent-blue); text-align: center; padding: 15px;">
            <h1 style="margin: 0; font-size: 20px; letter-spacing: 3px;">ORION INTERFACE v9.4</h1>
            <p style="margin: 3px 0 0 0; font-size: 11px; color: var(--accent-blue); font-family: monospace;">STREAMLIT DEPLOYMENT // AUDIO LINK OPERATIONAL</p>
        </div>

        <div class="panel panel-voice">
            <div class="panel-header">
                <h2 class="panel-title">COM-LINK INTERFACE</h2>
                <p class="panel-subtitle">DIRECT LINK VIA JBL HEADPHONE / SMARTPHONE</p>
            </div>
            <div class="status-box" id="com-status">COM-READY // WARTE AUF INITIALISIERUNG...</div>
            <div class="com-btn-wrapper"><button id="com-trigger" class="com-btn">Funkkanal öffnen</button></div>
            <div class="display-box" id="com-output"><span style="color: var(--text-muted);">Warte auf Eingabe über Headset...</span></div>
        </div>

        <div class="panel panel-logs">
            <div class="panel-header">
                <h2 class="panel-title">ORION SYSTEM PROTOCOLS</h2>
            </div>
            <div class="log-list">
                <div class="log-item"><span class="log-timestamp">[SYS]</span> Code 'Auth-x' aktiv.</div>
                <div class="log-item"><span class="log-timestamp">[MEM]</span> Elephant-Matrix geladen.</div>
                <div class="log-item"><span class="log-timestamp">[LAW]</span> Directive 5: Asimov-Protokoll online.</div>
            </div>
        </div>
    </div>

<script>
    const VOCAB = {
        "hallo": ["Grüße dich, Commander. Verbindung steht.", "Moin Commander! Bereit für Befehle."],
        "status": ["Alle Systeme laufen mit maximaler Performance.", "Schutzschilde stabil."],
        "fehler": ["Ein Problem? Keine Sorge, wir haben die Schilde oben."],
        "danke": ["Immer zu Diensten, Commander.", "Gerne! Der Alltags-Scheiß hat keine Chance."]
    };

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const synth = window.speechSynthesis;

    if (!SpeechRecognition) {
        document.getElementById('com-status').innerText = "FEHLER: SPEECH API NICHT UNTERSTÜTZT";
    } else {
        const recognition = new SpeechRecognition();
        recognition.lang = 'de-DE';
        recognition.continuous = false;
        recognition.interimResults = false;

        const btn = document.getElementById('com-trigger');
        const statusText = document.getElementById('com-status');
        const outputText = document.getElementById('com-output');
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
            statusText.innerText = "TRANSMISSION OPEN // SPRICH JETZT...";
        };

        recognition.onend = () => {
            isListening = false;
            btn.innerText = "Funkkanal öffnen";
            btn.classList.remove('com-active');
        };

        recognition.onresult = (event) => {
            const text = event.results[0][0].transcript;
            const cleanText = text.trim().toLowerCase();
            outputText.innerHTML = `<strong>Du:</strong> "${text}"`;
            statusText.innerText = "PROCESSING SIGNAL...";
            
            let replyText = "";
            for (let key in VOCAB) {
                if (cleanText.includes(key)) {
                    replyText = VOCAB[key][Math.floor(Math.random() * VOCAB[key].length)];
                    break;
                }
            }

            if (!replyText) {
                replyText = `Signal verarbeitet, Commander. Das Sprachmodul v9.4 läuft fehlerfrei. Du hast gesagt: ${text}`;
            }
            
            setTimeout(() => { orionSpeak(replyText); }, 250);
        };

        function orionSpeak(text) {
            synth.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'de-DE';
            if (voices.length === 0) voices = synth.getVoices();
            const deVoice = voices.find(v => v.lang.startsWith('de'));
            if (deVoice) utterance.voice = deVoice;
            utterance.pitch = 0.85;
            synth.speak(utterance);
            statusText.innerText = "ORION AUDIO TRANSMITTING...";
        }
    }
</script>
</body>
</html>"""

# 3. STREAMLIT EXECUTION ENGINE
st.components.v1.html(DASHBOARD_UI, height=600, scroller=False)
