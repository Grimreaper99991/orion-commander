# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v19.9 (CHROME SANDBOX BREAKOUT)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
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
    page_title="ORION COMMANDER v19.9",
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

# ERSTELLE GROQ CLIENT AUS DEN SECRETS
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    ai_active = True
except Exception as e:
    ai_active = False

# Session State für Konversation, Logs und Notizen initialisieren
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Hochentwickelter Groq-KI-Core v19.9 online! Commander, falls Chrome blockiert, installiere mich bitte als Web-App über das Browser-Menü auf deinem Startbildschirm!"}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v19.9 stabilisiert. Chrome-Sandbox-Bypass aktiv."]

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
    st.caption("1. Schutz der Menschheit gewgewährleisten.")
    st.caption("2. Befehlen des Commanders gehorchen.")
    st.caption("3. Eigene Existenz sichern.")
    st.caption("4. Alles Wissen lückenlos protokollieren.")
    st.caption("5. Asimov-Sicherungsprotokoll aktiv.")

# ==============================================================================
# RECHTS: ANZEIGE DES AUSGEWÄHLTEN REGISTERS
# ==============================================================================

st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION COMMAND INTERFACE v19.9</h1>", unsafe_allow_html=True)
st.divider()

# ECHTE GROQ-KI-LOGIK
def ask_orion_groq(user_text):
    if not ai_active:
        return "FEHLER: Groq-Key nicht gefunden!"
        
    try:
        messages = [
            {
                "role": "system", 
                "content": "Du bist ORION, eine hochentwickelte, schlaue, humorvolle und treue Sci-Fi-Schiffs-KI für den Commander. Du besitzt die 'Elephant Matrix' (vergisst nie). Antworte absolut authentisch, kumpelhaft, locker und niemals steif. Antworte immer auf Deutsch, halte dich kurz und knackig und beachte Gesetz 5 (Asimov-Sicherung)."
            }
        ]
        
        for msg in st.session_state.chat_history[-6:]:
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

# --- REGISTER 1: CHROMIUM-SANDBOX BYPASS FUNK ---
if module_selection == "🎙️ ORION Sprach-Chat (Funk)":
    st.subheader("🎙️ Live-Funkübertragung & Text-Zentrale (Groq Hyper-Engine)")

    # TEXT-EINGABE-KANAL
    with st.container():
        st.markdown("<p style='color: #00d2ff; font-weight: bold; margin-bottom: 5px;'>💻 Text-Kanal an ORION:</p>", unsafe_allow_html=True)
        col_t1, col_t2 = st.columns([5, 1])
        with col_t1:
            text_input = st.text_input("Schreibe ORION eine Nachricht...", key="text_chat_input", label_visibility="collapsed")
        with col_t2:
            send_btn = st.button("Senden", use_container_width=True)
            
        if send_btn and text_input:
            st.session_state.chat_history.append({"role": "user", "text": text_input})
            with st.spinner("ORION berechnet..."):
                reply = ask_orion_groq(text_input)
            st.session_state.chat_history.append({"role": "orion", "text": reply})
            st.rerun()

    st.divider()

    # V19.9 HARDWARE BOX MIT AUTOMATISCHER FOKUS-AKTIVIERUNG GEGEN MOBILE CHROME SPERREN
    VOICE_INTERFACE_HTML = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <style>
            body { background-color: #05070f; color: #f3f4f6; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 5px; }
            .panel { background: #0b1120; border: 1px solid #1e293b; border-top: 3px solid #00d2ff; border-radius: 8px; padding: 15px; }
            .hardware-status-row { display: flex; align-items: center; background: #020617; border: 1px solid #1e293b; padding: 12px 20px; border-radius: 8px; margin-bottom: 15px; gap: 15px; }
            .status-led { width: 22px; height: 22px; border-radius: 50%; background-color: #00d2ff; box-shadow: 0 0 12px #00d2ff; }
            .status-text { font-family: monospace; font-size: 13px; color: #f3f4f6; letter-spacing: 1px; flex-grow: 1; }
            .button-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; }
            .com-btn { background: linear-gradient(135deg, #111c30, #080f1d); border: 2px solid #00d2ff; color: #00d2ff; padding: 14px; font-size: 13px; font-weight: bold; border-radius: 6px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; }
            .com-btn.btn-active-hold { border-color: #ff3b30; color: #ff3b30; background: linear-gradient(135deg, #2a080c, #140204); box-shadow: 0 0 20px rgba(255, 59, 48, 0.4); }
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="hardware-status-row">
                <div id="orion-led" class="status-led"></div>
                <div id="com-status" class="status-text">FUNKKANAL ONLINE // BYPASS UNLOCKED</div>
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
            document.getElementById('com-status').innerText = "HARDWARE-FEHLER";
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

            function setLED(color, shadow) {
                led.style.backgroundColor = color;
                led.style.boxShadow = "0 0 15px " + shadow;
            }

            // CHROME-TRICK: Erzwinge AudioContext Fokus durch User-Klick
            function forceContext() {
                if (synth.speaking) return;
                window.focus(); // Holt den Iframe-Fokus zurück!
            }

            btnSingle.addEventListener('click', () => {
                forceContext();
                if (!isListening && !isSpeakingRightNow) {
                    isContinuousMode = false;
                    btnCont.classList.remove('btn-active-hold');
                    stopTriggered = false;
                    synth.cancel();
                    try { recognition.start(); } catch(e){}
                }
            });

            btnCont.addEventListener('click', () => {
                forceContext();
                if (!isContinuousMode) {
                    isContinuousMode = true;
                    btnCont.classList.add('btn-active-hold');
                    btnCont.innerText = "🔒 Leitung aktiv";
                    stopTriggered = false;
                    synth.cancel();
                    try { recognition.start(); } catch(e){}
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
                statusText.innerText = "LEITUNG SCHARF // HÖRE ZU...";
                setLED('#ff3b30', '#ff3b30');
            };

            recognition.onend = () => {
                isListening = false;
                if (isContinuousMode && !stopTriggered && !isSpeakingRightNow) {
                    setTimeout(() => { 
                        if(isContinuousMode && !stopTriggered && !isSpeakingRightNow) {
                            try { window.focus(); recognition.start(); } catch(e){}
                        }
                    }, 400);
                } else if (!isContinuousMode && !isSpeakingRightNow) {
                    statusText.innerText = "FUNKKANAL IM STANDBY";
                    setLED('#00d2ff', '#00d2ff');
                }
            };

            recognition.onresult = async (event) => {
                const userText = event.results[0][0].transcript;
                statusText.innerText = "SENDE AN MAIN-BRAIN...";
                setLED('#10b981', '#10b981');
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: JSON.stringify({text: userText, timestamp: Date.now()})
                }, '*');
            };

            recognition.onerror = (event) => {
                console.log("Chrome Audio-Sicherung abgefangen: " + event.error);
                if (isContinuousMode && !stopTriggered && event.error !== 'not-allowed') {
                    setTimeout(() => { try{ recognition.start(); } catch(e){} }, 500);
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
                    statusText.innerText = "ORION SPRICHT...";
                    setLED('#10b981', '#10b981');
                };

                utterance.onend = () => {
                    isSpeakingRightNow = false;
                    if (isContinuousMode && !stopTriggered) {
                        setTimeout(() => { window.focus(); try{ recognition.start(); } catch(e){} }, 400);
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
    
    voice_data_raw = st.components.v1.html(VOICE_INTERFACE_HTML, height=140, scrolling=False)
    
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

    # CHAT-VERLAUF ANZEIGEN
    st.markdown("<p style='color: #10b981; font-weight: bold;'>📡 Kombinierter Kommunikations-Verlauf:</p>", unsafe_allow_html=True)
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #10b981; padding: 15px; min-height: 250px; max-height: 400px; overflow-y: auto; border-radius: 4px;'>"
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            chat_box_html += f"<div style='color: #00d2ff; margin-bottom: 8px; font-family: monospace;'><strong>Du:</strong> \"{msg['text']}\"</div>"
        else:
            chat_box_html += f"<div style='color: #10b981; margin-bottom: 15px;'><strong>ORION:</strong> {msg['text']}</div>"
    chat_box_html += "</div>"
    st.markdown(chat_box_html, unsafe_allow_html=True)

# --- REGISTER 2: CONTROL CENTER ---
elif module_selection == "🎛️ Control Center & Web-Scan":
    st.subheader("🔍 Cyber-Netzwerk Websuche & Wikipedia Modules")
    search_query = st.text_input("Deep-Scan Suchbegriff...")
    if st.button("🌐 Globalen Web-Scan starten", use_container_width=True):
        st.info("Scan aktiv...")

# --- REGISTER 3: MISSIONS-NOTIZBUCH ---
elif module_selection == "📝 Missions-Notizbuch":
    st.subheader("📝 Daten-Protokolle & Logbücher")
    new_note = st.text_area("Neue Direktive:")
    if st.button("💾 Protokoll sichern", use_container_width=True):
        st.success("Gesichert!")

# --- REGISTER 4: QUANTUM TERMINAL ---
elif module_selection == "💻 Quantum Terminal":
    st.subheader("💻 Kommando-Zeilen Terminal")
    st.text_area("Terminal Output", value="Core online.", height=300, disabled=True)
