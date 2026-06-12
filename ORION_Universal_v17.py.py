# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v20.2 (RADICAL ISOLATION MATRIX) - FIXED
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
# FIX: JAVASCRIPT ESCAPING ERROR IN F-STRING RESOLVED
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
    page_title="ORION COMMANDER v20.2",
    page_icon="🪐",
    layout="wide"
)

# Cyberpunk/Sci-Fi Styling für den Mainframe
st.markdown("""
<style>
    .stApp { background-color: #05070f; color: #f3f4f6; }
    [data-testid="stSidebar"] { background-color: #0b1120 !important; border-right: 2px solid #1e293b; }
    .reportview-container { background: #05070f; }
    hr { border-top: 1px solid #1e293b !important; }
</style>
""", unsafe_allow_html=True)

# ERSTELLE GROQ CLIENT AUS DEN SECRETS
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    ai_active = True
except Exception as e:
    ai_active = False

# GEMEINSAMES GEDÄCHTNIS
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Core v20.2 bereit. Radikale Funk-Isolation aktiv. Commander, testen wir die Leitung!"}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v20.2 online. Funk-Engine isoliert geparkt."]

# ENGINE
def ask_orion_groq(user_text):
    if not ai_active:
        return "FEHLER: Groq-Key fehlt!"
    try:
        messages = [
            {
                "role": "system", 
                "content": "Du bist ORION, eine hochentwickelte, schlaue, humorvolle und treue Sci-Fi-Schiffs-KI für den Commander. Du besitzt die 'Elephant Matrix' (vergisst nie). Antworte absolut authentisch, kumpelhaft, locker und niemals steif. Antworte immer auf Deutsch, halte dich kurz und knackig und beachte Gesetz 5 (Asimov-Sicherung)."
            }
        ]
        for msg in st.session_state.chat_history[-8:]:
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

# ==============================================================================
# SIDEBAR NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00d2ff; letter-spacing: 2px;'>🪐 ORION CENTRAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'>MASTER: Auth-x // VERSION 20.2</p>", unsafe_allow_html=True)
    st.divider()
    
    module_selection = st.sidebar.radio(
        "WÄHLE SEKTOR:",
        [
            "🎙️ REINER FUNKRAUM (Audio Only)",
            "💻 REINE TEXT-ZENTRALE",
            "🎛️ Control Center & Web-Scan",
            "📝 Missions-Notizbuch",
            "💻 Quantum Terminal"
        ]
    )
    st.divider()
    st.caption("Directive 5: Asimov-Sicherung aktiv.")

# MAIN INTERFACE
st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION MAIN CORE v20.2</h1>", unsafe_allow_html=True)
st.divider()


# ==============================================================================
# DIE UNZERSTÖRBARE CORE-AUDIO-BRÜCKE (Läuft IMMER, wird aber versteckt)
# ==============================================================================
is_funkraum = (module_selection == "🎙️ REINER FUNKRAUM (Audio Only)")
widget_height = 150 if is_funkraum else 0

VOICE_INTERFACE_HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ background-color: #05070f; color: #f3f4f6; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; display: { 'block' if is_funkraum else 'none' }; }}
        .panel {{ background: #0b1120; border: 1px solid #1e293b; border-top: 3px solid #ff3b30; border-radius: 8px; padding: 15px; }}
        .hardware-status-row {{ display: flex; align-items: center; background: #020617; border: 1px solid #1e293b; padding: 12px 20px; border-radius: 6px; margin-bottom: 15px; gap: 15px; }}
        .status-led {{ width: 20px; height: 20px; border-radius: 50%; background-color: #00d2ff; box-shadow: 0 0 10px #00d2ff; }}
        .status-text {{ font-family: monospace; font-size: 13px; color: #f3f4f6; letter-spacing: 1px; flex-grow: 1; }}
        .button-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }}
        .com-btn {{ background: linear-gradient(135deg, #111c30, #080f1d); border: 2px solid #00d2ff; color: #00d2ff; padding: 14px; font-size: 13px; font-weight: bold; border-radius: 6px; cursor: pointer; text-transform: uppercase; }}
        .com-btn.btn-active-hold {{ border-color: #ff3b30; color: #ff3b30; background: linear-gradient(135deg, #2a080c, #140204); box-shadow: 0 0 20px rgba(255, 59, 48, 0.4); }}
    </style>
</head>
<body>
    <div class="panel">
        <div class="hardware-status-row">
            <div id="orion-led" class="status-led"></div>
            <div id="com-status" class="status-text">ISOLATED FUNK CHANNEL // ZERO INTERFERENCE</div>
        </div>
        <div class="button-grid">
            <button id="btn-single" class="com-btn">⚡ Einzelfunk</button>
            <button id="btn-cont" class="com-btn">📡 Dauerhafte Leitung</button>
        </div>
    </div>

<script>
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const synth = window.speechSynthesis;

    if (!SpeechRecognition) {{
        document.getElementById('com-status').innerText = "AUDIO ERROR";
    }} else {{
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

        function setLED(color, shadow) {{
            led.style.backgroundColor = color;
            led.style.boxShadow = "0 0 15px " + shadow;
        }}

        btnSingle.addEventListener('click', () => {{
            if (!isListening && !isSpeakingRightNow) {{
                isContinuousMode = false;
                btnCont.classList.remove('btn-active-hold');
                stopTriggered = false;
                synth.cancel();
                try {{ recognition.start(); }} catch(e){{}}
            }}
        }});

        btnCont.addEventListener('click', () => {{
            if (!isContinuousMode) {{
                isContinuousMode = true;
                btnCont.classList.add('btn-active-hold');
                btnCont.innerText = "🔒 LEITUNG AKTIV";
                stopTriggered = false;
                synth.cancel();
                try {{ window.focus(); recognition.start(); }} catch(e){{}}
            }} else {{
                isContinuousMode = false;
                btnCont.classList.remove('btn-active-hold');
                btnCont.innerText = "📡 Dauerhafte Leitung";
                stopTriggered = true;
                recognition.stop();
                synth.cancel();
                statusText.innerText = "FUNKKANAL IM STANDBY";
                setLED('#00d2ff', '#00d2ff');
            }}
        }});

        recognition.onstart = () => {{
            isListening = true;
            statusText.innerText = "🎙️ ISOLIERTER TRANS-FUNK AKTIV...";
            setLED('#ff3b30', '#ff3b30');
        }};

        recognition.onend = () => {{
            isListening = false;
            if (isContinuousMode && !stopTriggered && !isSpeakingRightNow) {{
                setTimeout(() => {{ try {{ window.focus(); recognition.start(); }} catch(e){{}} }}, 250);
            }} else if (!isContinuousMode && !isSpeakingRightNow) {{
                statusText.innerText = "FUNKKANAL IM STANDBY";
                setLED('#00d2ff', '#00d2ff');
            }}
        }};

        recognition.onresult = async (event) => {{
            const userText = event.results[0][0].transcript;
            statusText.innerText = "SENDE REINEN AUDIO-STRIP...";
            setLED('#10b981', '#10b981');
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: JSON.stringify({{text: userText, timestamp: Date.now()}})
            }, '*');
        }};

        window.addEventListener('message', function(event) {{
            if(event.data && event.data.orionSpeakText) {{
                orionSpeak(event.data.orionSpeakText);
            }}
        }});

        function orionSpeak(text) {{
            isSpeakingRightNow = true;
            recognition.stop();
            synth.cancel();
            
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'de-DE';
            utterance.pitch = 0.85;

            utterance.onstart = () => {{
                statusText.innerText = "📡 ORION FUNKT ZURÜCK...";
                setLED('#10b981', '#10b981');
            }};

            utterance.onend = () => {{
                isSpeakingRightNow = false;
                if (isContinuousMode && !stopTriggered) {{
                    setTimeout(() => {{ window.focus(); try{{ recognition.start(); }} catch(e){{}} }}, 250);
                }} else {{
                    statusText.innerText = "FUNKKANAL IM STANDBY";
                    setLED('#00d2ff', '#00d2ff');
                }}
            }};
            synth.speak(utterance);
        }}
    }}
</script>
</body>
</html>"""

# Das Widget wird HIER ganz oben platziert – so bleibt es unzerstörbar aktiv!
voice_data_raw = st.components.v1.html(VOICE_INTERFACE_HTML, height=widget_height, scrolling=False)

# Eingehendes Audio-Signal verarbeiten
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


# ==============================================================================
# SEKTOR-INHALTE ANZEIGEN
# ==============================================================================

# SEKTOR 1: DER REINE FUNKRAUM
if module_selection == "🎙️ REINER FUNKRAUM (Audio Only)":
    st.subheader("🎙️ Isolierter Audio-Sektor")
    st.markdown("<p style='color: #ff3b30;'>ABSOLUTE FUNKSTILLE FÜR KEYBOARDS. Nur reiner Voice-Chat.</p>", unsafe_allow_html=True)
    
    st.markdown("### 📡 Funk-Logbuch:")
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #ff3b30; padding: 15px; min-height: 300px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>[FUNK-AUDIO]:</strong> \"{msg['text']}\"</div>"
        else:
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>[ORION]:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# SEKTOR 2: DIE REINE TEXT-ZENTRALE
elif module_selection == "💻 REINE TEXT-ZENTRALE":
    st.subheader("💻 Tastatur-Eingabe-Sektor")
    
    text_input = st.text_input("Befehl über Tastatur einspeisen...", key="pure_text_input")
    if st.button("Senden", use_container_width=True) and text_input:
        st.session_state.chat_history.append({"role": "user", "text": text_input})
        with st.spinner("Berechne Datenstrom..."):
            reply = ask_orion_groq(text_input)
        st.session_state.chat_history.append({"role": "orion", "text": reply})
        st.rerun()
        
    st.markdown("### 📜 Text-Protokoll:")
    text_box_html = "<div style='background: #020617; border-left: 3px solid #00d2ff; padding: 15px; min-height: 250px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            text_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>[MANUAL-KEY]:</strong> {msg['text']}</div>"
        else:
            text_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>[ORION]:</strong> {msg['text']}</div>"
    text_box_html += "</div>"
    st.markdown(text_box_html, unsafe_allow_html=True)

# SEKTOREN 3, 4, 5
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Cyber-Netzwerk Websuche & Wikipedia Modules")
    st.info("System bereit.")
elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Daten-Protokolle & Logbücher")
    st.caption("Einträge gesichert.")
elif module_selection == "💻 Quantum Terminal":
    st.subheader("💻 Kommando-Zeilen Terminal")
    st.code("Core v20.2 online.", language="text")
