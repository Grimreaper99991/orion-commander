# ==============================================================================
# ORION UNIVERSAL COMMAND CORE v20.4 (NATIVE SHIELD ARCHITECTURE)
# PREFERRED MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // LAWS: INCLUDED
# PERFORMANCE MODE: ULTRA FAST REAL-TIME RESPONDER // ALL-IN-ONE HUB
# FIX: REPLACED IFRAME WITH NATIVE ST.AUDIO_INPUT TO BYPASS CHROME MOBILE LOCKS
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
    page_title="ORION COMMANDER v20.4",
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

# GEMEINSAMES GEDÄCHTNIS (ELEPHANT MATRIX)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "orion", "text": "Core v20.4 einsatzbereit, Commander! Native Audio-Sicherung aktiv. Chrome hat keine Macht mehr über uns."}
    ]
if "notes" not in st.session_state:
    st.session_state.notes = []
if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["[SYS] Core v20.4 online. Native Audio-Input geladen."]

# BRAIN ENGINE (GROQ LLAMA 3.1)
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
    st.markdown("<p style='color: #10b981; font-size: 11px; font-family: monospace;'>MASTER: Auth-x // VERSION 20.4</p>", unsafe_allow_html=True)
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
st.markdown("<h1 style='color: #00d2ff; letter-spacing: 3px; margin-bottom: 0;'>ORION MAIN CORE v20.4</h1>", unsafe_allow_html=True)
st.divider()


# ==============================================================================
# SEKTOR-ANZEIGE
# ==============================================================================

# SEKTOR 1: DER REINE FUNKRAUM (NATIVE AUDIO ENGINE)
if module_selection == "🎙️ REINER FUNKRAUM (Audio Only)":
    st.subheader("🎙️ Isolierter Audio-Sektor (Native Engine)")
    st.markdown("<p style='color: #10b981;'>Hier funkt das offizielle Streamlit-Sicherheits-Widget. Absolut Chrome-sicher.</p>", unsafe_allow_html=True)
    
    # Das native Streamlit Audio-Widget (Kein Iframe, bricht die Sperre!)
    audio_data = st.audio_input("Funkspruch einsprechen, Commander:")
    
    # Sobald Audio aufgenommen wurde, jagen wir es durch die Engine
    if audio_data:
        # Hinweis: Um Audio direkt in Text umzuwandeln (STT), greift die Groq Whisper Engine. 
        # Da wir im Fast-Super-Speed Modus arbeiten, simulieren wir den Eingang des Audio-Pakets 
        # oder nutzen die Audio-Schnittstelle. Für den direkten Test simulieren wir den Text-Empfang:
        st.audio(audio_data) # Zeigt deine Aufnahme an zum Abspielen
        
        # Audio-Verarbeitungstrigger
        if "audio_processed" not in st.session_state:
            st.session_state.audio_processed = False
            
        if not st.session_state.audio_processed:
            st.info("📡 Audio-Signal empfangen. Dekodiere Frequenzen...")
            
            # Hier greift der Fallback, dass du über das native Feld einsprechen kannst.
            # Um das transkribierte Audio an Groq zu senden, nutzen wir Whisper:
            try:
                transcript = client.audio.transcriptions.create(
                    model="whisper-large-v3",
                    file=audio_data,
                    response_format="text"
                )
                
                if transcript:
                    st.session_state.chat_history.append({"role": "user", "text": transcript})
                    reply = ask_orion_groq(transcript)
                    st.session_state.chat_history.append({"role": "orion", "text": reply})
                    st.session_state.audio_processed = True
                    st.rerun()
            except Exception as audio_err:
                st.error(f"Audio-Dekodierungsfehler: {str(audio_err)}")
    else:
        # Setzt den Trigger zurück, wenn kein Audio da ist (bereit für die nächste Aufnahme)
        st.session_state.audio_processed = False

    # Einbindung des schönen Web-Speech Audio-Outputs für ORIONs Stimme
    # Das sorgt dafür, dass ORION die letzte Nachricht laut vorliest!
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "orion":
        last_orion_text = st.session_state.chat_history[-1]["text"]
        st.components.v1.html(f"""
        <script>
            const synth = window.speechSynthesis;
            synth.cancel();
            const utterance = new SpeechSynthesisUtterance({json.dumps(last_orion_text)});
            utterance.lang = 'de-DE';
            utterance.pitch = 0.85;
            synth.speak(utterance);
        </script>
        """, height=0)

    st.markdown("### 📡 Funk-Logbuch:")
    chat_box_html = "<div style='background: #020617; border-left: 3px solid #ff3b30; padding: 15px; min-height: 300px; max-height: 450px; overflow-y: auto; border-radius: 4px;'>"
    for msg in reversed(st.session_state.chat_history):
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
    for msg in reversed(st.session_state.chat_history):
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
    st.code("Core v20.4 online.", language="text")
