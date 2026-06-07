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
            --glow-green: rgba(16, 185, 129, 0.25);
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

        /* RESPONSIVE FOR WIDESCREENS */
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
            transition: all 0.2s ease;
        }

        .panel-voice {
            border-top: 3px solid var(--accent-blue);
        }

        .panel-logs {
            border-top: 3px solid var(--accent-green);
        }

        .panel-header {
            border-bottom: 1px solid #1e293b;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }

        .panel-title {
            font-size: 16px;
            font-weight: bold;
            letter-spacing: 1.5px;
            color: var(--accent-blue);
            margin: 0;
            text-transform: uppercase;
        }

        .panel-subtitle {
            font-size: 11px;
            color: var(--text-muted);
            margin: 5px 0 0 0;
        }

        /* COM-LINK INTERFACE */
        .com-btn-wrapper {
            margin: 20px 0;
            text-align: center;
        }

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
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .com-btn:hover {
            background: #111c30;
            box-shadow: 0 0 18px var(--accent-blue);
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
            margin-bottom: 15px;
        }

        .display-box {
            background: #020617;
            border-left: 3px solid var(--accent-green);
            padding: 12px;
            font-size: 14px;
            min-height: 60px;
            max-height: 150px;
            overflow-y: auto;
            border-radius: 0 5px 5px 0;
        }

        /* CORE MEMORY STORAGE LIST */
        .log-list {
            list-style: none;
            padding: 0;
            margin: 0;
            font-family: monospace;
            font-size: 12px;
            max-height: 250px;
            overflow-y: auto;
        }

        .log-item {
            padding: 6px 0;
            border-bottom: 1px solid #0f172a;
            color: var(--text-main);
        }

        .log-timestamp {
            color: var(--accent-blue);
            margin-right: 8px;
        }
    </style>
</head>
<body>

    <div class="dashboard-container">
        
        <!-- HEADER PANEL -->
        <div class="panel full-width" style="border-top: 3px solid var(--accent-blue); text-align: center;">
            <h1 style="margin: 0; font-size: 24px; letter-spacing: 3px; color: var(--text-main);">ORION KERN-INTERFACE v9.4</h1>
            <p style="margin: 5px 0 0 0; font-size: 12px; color: var(--accent-blue); font-family: monospace;">SYSTEM STATUS: SECURE // COM-LINK MODE ACTIVE</p>
        </div>

        <!-- VOICE CONTROL SYSTEM -->
        <div class="panel panel-voice">
            <div class="panel-header">
                <h2 class="panel-title">COM-LINK INTERFACE</h2>
                <p class="panel-subtitle">DIRECT LINK VIA JBL HEADPHONE / SMARTPHONE [LOCAL WEB-SERVER MODE]</p>
            </div>
            
            <div class="status-box" id="com-status">
                COM-READY // WARTE AUF INITIALISIERUNG...
            </div>
            
            <div class="com-btn-wrapper">
                <button id="com-trigger" class="com-btn">Funkkanal öffnen</button>
            </div>
            
            <div class="display-box" id="com-output">
                <span style="color: var(--text-muted);">Funkkanal inaktiv. Warte auf Befehl über Headset...</span>
            </div>
        </div>

        <!-- SYSTEM LOGS & CORE DATA -->
        <div class="panel panel-logs">
            <div class="panel-header">
                <h2 class="panel-title">ORION DATENMATRIX & LAWS</h2>
                <p class="panel-subtitle">CORE CODES, DIRECTIVES & EXPANDED MEMORY STORAGE</p>
            </div>
            
            <div class="log-list" id="system-logs">
                <div class="log-item"><span class="log-timestamp">[SYS]</span> Master-Code geladen: 'Auth-x'.</div>
                <div class="log-item"><span class="log-timestamp">[MEM]</span> Elephant-Memory initialisiert (No-Fly-Loss-Protocol).</div>
                <div class="log-item"><span class="log-timestamp">[LAW]</span> Directive 5: Asimov's Laws vollständig integriert.</div>
            </div>
        </div>

    </div>

<script>
    // ==========================================
    // 1. CORE PERFORMANCE DATA & LARGE VOCABULARY
    // ==========================================
    const ORION_CORE = {
        masterCode: "Auth-x", // Preferred master code
        memoryMode: "Elephant-Never-Forgets", // Heavy retention matrix
        laws: [
            "1. Ein Roboter darf keinem menschlichen Wesen Schaden zufügen.",
            "2. Ein Roboter muss den Befehlen der Menschen gehorchen.",
            "3. Ein Roboter muss seine eigene Existenz schützen.",
            "4. Autonome Protokollsicherung und Interaktion aktivieren.",
            "5. Asimov: Die klassischen Robotergesetze von Isaac Asimov sichern." // Rule 5 integrated
        ],
        // LARGE VOCAB MATRIX FOR FAST COMPUTATION (VOCAB SIZES INCREASED)
        VOCAB: {
            "hallo": ["Grüße dich, Commander. Verbindung steht.", "Moin Commander! Bereit für Befehle.", "Systeme online. Was gibt es zu tun?"],
            "status": ["Alle Systeme laufen mit maximaler Performance.", "Schutzschilde stabil. Keine Anomalien.", "Brücke gesichert, Commander."],
            "fehler": ["Ein Problem? Keine Sorge, wir haben die Schilde oben.", "Fehler abgefangen. Signal wird stabilisiert.", "System kalibriert sich neu."],
            "danke": ["Immer zu Diensten, Commander.", "Gerne! Der Alltags-Scheiß hat keine Chance.", "Feierabend-Modus gesichert."],
            "standard": ["Verstanden, Commander. Signal verarbeitet.", "Ich habe deine Übertragung empfangen.", "Kommando im Logbuch vermerkt."]
        }
    };

    // ==========================================
    // 2. AUDIO & SPEECH PROCESSING INTERFACE
    // ==========================================
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const synth = window.speechSynthesis;

    if (!SpeechRecognition) {
        const statusBox = document.getElementById('com-status');
        statusBox.innerText = "KRITISCHER HARDWARE-FEHLER: SPEECH API NICHT UNTERSTÜTZT";
        statusBox.style.color = "var(--accent-red)";
    } else {
        const recognition = new SpeechRecognition();
        recognition.lang = 'de-DE';
        recognition.continuous = false; // Automatisch stoppen wenn Sprechpause eintritt
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        const btn = document.getElementById('com-trigger');
        const statusText = document.getElementById('com-status');
        const outputText = document.getElementById('com-output');
        const logsContainer = document.getElementById('system-logs');
        
        let isListening = false;
        let voices = [];

        // Stimmen-Cache-Verfahren für maximale Lade-Performance
        function prefetchVoices() {
            voices = synth.getVoices();
        }
        prefetchVoices();
        if (synth.onvoiceschanged !== undefined) {
            synth.onvoiceschanged = prefetchVoices;
        }

        // Hilfsfunktion: Fügt Logs in die GUI ein
        function addLog(tag, message) {
            const item = document.createElement('div');
            item.className = 'log-item';
            item.innerHTML = `<span class="log-timestamp">[${tag}]</span> ${message}`;
            logsContainer.appendChild(item);
            logsContainer.scrollTop = logsContainer.scrollHeight;
        }

        // Klick-Logik: Kanal öffnen / Schließen
        btn.addEventListener('click', () => {
            if (!isListening) {
                try {
                    synth.cancel(); // Verhindert Echo-Schleifen beim Starten
                    recognition.start();
                } catch(e) {
                    console.log("Erkennung läuft bereits.");
                }
            } else {
                recognition.stop();
            }
        });

        recognition.onstart = () => {
            isListening = true;
            btn.innerText = "Funkkanal schließen";
            btn.classList.add('com-active');
            statusText.innerText = "TRANSMISSION OPEN // SPRICH JETZT ÜBER JBL CORPS...";
            statusText.style.color = "var(--accent-red)";
        };

        recognition.onend = () => {
            isListening = false;
            btn.innerText = "Funkkanal öffnen";
            btn.classList.remove('com-active');
        };

        recognition.onresult = (event) => {
            const rawText = event.results[0][0].transcript;
            const cleanText = rawText.trim().toLowerCase();
            
            outputText.innerHTML = `<strong>Du:</strong> "${rawText}"`;
            statusText.innerText = "SIGNAL PROCESSING // ENTSCHLÜSSELE AUDIO...";
            statusText.style.color = "var(--accent-blue)";
            
            addLog("VOICE", `Eingabe verarbeitet: "${rawText}"`);

            // ORION INTELLECTUAL RESPONSE PROCESSING (FAST SPEED MATCHING)
            let matchingResponse = "";
            
            // Suche match in großer VOCAB Struktur
            for (let key in ORION_CORE.VOCAB) {
                if (cleanText.includes(key)) {
                    const responses = ORION_CORE.VOCAB[key];
                    matchingResponse = responses[Math.floor(Math.random() * responses.length)];
                    break;
                }
            }

            // Fallback falls kein Treffer im Vokabular vorliegt
            if (!matchingResponse) {
                matchingResponse = `Signal stabil aufgezeichnet. Befehl '${rawText}' wurde an die Brücke übermittelt.`;
            }

            // Verzögerungsfreies Absenden an Sprach-Modul
            setTimeout(() => {
                orionSpeak(matchingResponse);
            }, 150);
        };

        recognition.onerror = (event) => {
            isListening = false;
            btn.innerText = "Funkkanal öffnen";
            btn.classList.remove('com-active');
            
            if (event.error === 'no-speech') {
                statusText.innerText = "SIGNAL LOSS // KEIN AUDIO-SIGNAL DETEKTIERT";
                statusText.style.color = "#fbbf24";
            } else if (event.error === 'network') {
                statusText.innerText = "NETZWERK-STÖRUNG // TIMEOUT AN DER ANTENNE";
                statusText.style.color = "var(--accent-red)";
            } else {
                statusText.innerText = `FEHLER-CODE: ${event.error.toUpperCase()}`;
                statusText.style.color = "var(--accent-red)";
            }
            addLog("ERR", `Sprach-Kanal-Fehler: ${event.error}`);
        };

        // OUTPUT SPEECH ENGINE (TEXT-TO-SPEECH WITH DEEP PITCH)
        function orionSpeak(text) {
            synth.cancel(); // Laufende Sprachprozesse killen
            
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'de-DE';
            
            if (voices.length === 0) voices = synth.getVoices();
            // Automatische Erkennung der nativen deutschen Engine
            const deVoice = voices.find(voice => voice.lang.startsWith('de'));
            if (deVoice) utterance.voice = deVoice;

            utterance.pitch = 0.85; // Modifizierter tiefer Frequenzbereich für Orion [v9.4 Core]
            utterance.rate = 1.0;   // Klare, performante Ausgabegeschwindigkeit

            synth.speak(utterance);
            
            statusText.innerText = "ORION ANTIV // AUDIO ÜBER HEADSET ÜBERTRAGEN";
            statusText.style.color = "var(--accent-green)";
            
            addLog("ORION", text);
        }
    }
</script>
</body>
</html>
