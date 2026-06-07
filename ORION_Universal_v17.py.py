<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ORION Kommandozentrale v9.4 - Cyber-Brücke</title>
    <style>
        /* CORE SCI-FI THEME (FAST RENDERING) */
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
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }

        .dashboard-container {
            width: 100%;
            max-width: 900px;
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }

        @media (min-width: 768px) {
            .dashboard-container {
                grid-template-columns: 2fr 1fr;
            }
            .full-width {
                grid-column: span 2;
            }
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
            font-size: 16px;
            font-weight: bold;
            letter-spacing: 1.5px;
            color: var(--accent-blue);
            margin: 0;
            text-transform: uppercase;
        }

        .panel-subtitle { font-size: 11px; color: var(--text-muted); margin: 5px 0 0 0; }

        .com-btn-wrapper { margin: 20px 0; text-align: center; }

        .com-btn {
            background: linear-gradient(135deg, #111c30, #080f1d);
            border: 2px solid var(--accent-blue);
            color: var(--accent-blue);
            padding: 18px 30px;
            font-size: 15px;
            font-weight: bold;
            letter-spacing: 1px;
            border-radius: 30px;
            cursor: pointer;
            width: 100%;
            box-shadow: 0 0 12px var(--glow-blue);
            text-transform: uppercase;
            outline: none;
            transition: all 0.2s ease;
        }

        .com-btn:hover { box-shadow: 0 0 18px var(--accent-blue); }

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
            margin-bottom: 15px;
        }

        .display-box {
            background: #020617;
            border-left: 3px solid var(--accent-green);
            padding: 12px;
            font-size: 14px;
            min-height: 60px;
            border-radius: 0 5px 5px 0;
        }

        .log-list { list-style: none; padding: 0; margin: 0; font-family: monospace; font-size: 12px; }
        .log-item { padding: 6px 0; border-bottom: 1px solid #0f172a; }
        .log-timestamp { color: var(--accent-blue); margin-right: 8px; }
    </style>
</head>
<body>

    <div class="dashboard-container">
        
        <div class="panel full-width" style="border-top: 3px solid var(--accent-blue); text-align: center;">
            <h1 style="margin: 0; font-size: 24px; letter-spacing: 3px;">ORION INTERFACE v9.4</h1>
            <p style="margin: 5px 0 0 0; font-size: 12px; color: var(--accent-blue); font-family: monospace;">SYSTEM STATUS: ONLINE // AUDIO LINK OPERATIONAL</p>
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
                <h2 class="panel-title">ORION DIRECTIVES</h2>
            </div>
            <div class="log-list">
                <div class="log-item"><span class="log-timestamp">[SYS]</span> Code 'Auth-x' aktiv.</div>
                <div class="log-item"><span class="log-timestamp">[MEM]</span> Elephant-Matrix geladen.</div>
                <div class="log-item"><span class="log-timestamp">[LAW]</span> Directive 5: Asimov-Protokoll online.</div>
            </div>
        </div>

    </div>

<script>
    // CORE VOCABULARY INTEGRATED IN FRONTEND FOR FAST SPEED RESPONSE
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
                    const responses = VOCAB[key];
                    replyText = responses[Math.floor(Math.random() * responses.length)];
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
</html>
