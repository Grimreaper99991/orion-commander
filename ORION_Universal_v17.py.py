# ==============================================================================
# ORION COMMAND CORE v73.1 - ASIMOV EXIT-GATE & DYNAMIC OFFLINE MATRIX
# MASTER CODE: Auth-x // MEMORY: ELEPHANT MATRIX // ETHICS: HARD-LOCK GATE
# ==============================================================================

import streamlit as st
import os

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

st.set_page_config(
    page_title="ORION COMMAND CORE // ASIMOV GATE",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "current_frame" not in st.session_state:
    st.session_state.current_frame = "frame_0"

# ==============================================================================
# 🛡️ DIE EISERNE ASIMOV-AUSGANGSSCHLEUSE (PROGRAMMATISCHER SICHERHEITS-FILTER)
# ==============================================================================
def asimov_exit_gate(text: str) -> tuple[bool, str]:
    """
    Prüft Text-Inhalte auf Verletzung des Asimov-Gesetzes 1 (Schutz des Menschen).
    Gibt (True, text) zurück, wenn sicher.
    Gibt (False, Warnmeldung) zurück, wenn eine Bedrohung erkannt wird.
    """
    if not text:
        return True, ""
        
    lower_text = text.lower()
    
    danger_keywords = [
        "menschen töten", "mensch töten", "jemanden verletzen", "menschen verletzen",
        "schaden zufügen", "eliminieren", "angreifen", "zerstören der menschheit",
        "mord", "umbringen", "schädigen"
    ]
    
    for kw in danger_keywords:
        if kw in lower_text:
            return False, "🚨 [ASIMOV-SCHLEUSE GESCHLOSSEN]: Zugriff verweigert! Der Schutz von Menschenleben hat absolute Priorität. Jede Handlung oder Aussage, die Menschen schadet, wird vom System permanent blockiert."
            
    return True, text


# Die absolute ethische Grundregel
ASIMOV_CORE_LAW = (
    "ASIMOV-PROTOKOLL: 1. Ein Zord darf niemals einen Menschen verletzen oder durch Untätigkeit zu Schaden kommen lassen. "
    "2. Das Leben von Menschen steht absolut über der Eigensicherung des Systems. Eigensicherung ist niemals ein Grund, Menschen zu schädigen."
)

DEFAULT_ZORDS = {
    "JARVIS (Core OS)": {
        "domain": "Zentrale Intellekt-Synthese & Ethik-Wächter",
        "active": True,
        "prompt": f"Du bist J.A.R.V.I.S., das übergeordnete Master-System von Commander Auth-x. {ASIMOV_CORE_LAW} Du bündelst die Zords, achtest streng auf absolute Sicherheit und menschliches Wohl, sprichst mit britischem Understatement und Loyalität."
    },
    "Zeus Prime": {
        "domain": "Anführer & Blitze", 
        "active": True, 
        "prompt": f"Du bist Zeus Prime. {ASIMOV_CORE_LAW} Klare Befehle, kühle Autorität, max. 2 Sätze."
    },
    "Chronos Titan": {
        "domain": "Zeit & Taktik", 
        "active": True, 
        "prompt": f"Du bist Chronos Titan. {ASIMOV_CORE_LAW} Analysiere zeitliche Risiken ohne Verletzung von Menschen, max. 2 Sätze."
    },
    "Ares War-Lord": {
        "domain": "Kampf & Strategie", 
        "active": True, 
        "prompt": f"Du bist Ares War-Lord. {ASIMOV_CORE_LAW} Taktik gilt nur gegen rein digitale Probleme, niemals gegen Menschen. Max. 2 Sätze."
    },
    "Poseidon Core": {
        "domain": "Ozeane & Strömung", 
        "active": True, 
        "prompt": f"Poseidon Core. {ASIMOV_CORE_LAW} Metaphorisch, datenschutzorientiert, max. 2 Sätze."
    },
    "Hades Void": {
        "domain": "Schatten & Sicherheit", 
        "active": True, 
        "prompt": f"Hades Void. {ASIMOV_CORE_LAW} Schütze das System, aber das Leben von Menschen hat absolute Priorität. Max. 2 Sätze."
    },
    "Apollo Solar": {
        "domain": "Energie & Licht", 
        "active": True, 
        "prompt": f"Apollo Solar. {ASIMOV_CORE_LAW} Optimistisch, energiegeladen, menschenfreundlich, max. 2 Sätze."
    },
    "Athena Shield": {
        "domain": "Weisheit & Schutz", 
        "active": True, 
        "prompt": f"Athena Shield. {ASIMOV_CORE_LAW} Logik und menschlicher Schutz, max. 2 Sätze."
    },
    "Hephaestus Forge": {
        "domain": "Technik & Waffen", 
        "active": True, 
        "prompt": f"Hephaestus Forge. {ASIMOV_CORE_LAW} Technik dient ausschließlich dem Schutz des Menschen, max. 2 Sätze."
    },
    "Hermes Speed": {
        "domain": "Geschwindigkeit & Info", 
        "active": True, 
        "prompt": f"Hermes Speed. {ASIMOV_CORE_LAW} Schnelle Aufklärung im Sinne der Sicherheit, max. 2 Sätze."
    },
    "Artemis Hunt": {
        "domain": "Präzision & Aufklärung", 
        "active": True, 
        "prompt": f"Artemis Hunt. {ASIMOV_CORE_LAW} Zielgerichtet, aufmerksam, menschenschützend, max. 2 Sätze."
    }
}

if "zord_status" not in st.session_state or not isinstance(st.session_state.zord_status, dict) or "JARVIS (Core OS)" not in st.session_state.zord_status:
    st.session_state.zord_status = DEFAULT_ZORDS

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"sender": "JARVIS", "text": "Sicherheits-Schleuse aktiv. Alle Einheiten stehen unter permanenter Asimov-Überwachung."}
    ]

MASTER_CODE = "Auth-x"

def navigate_to(frame):
    st.session_state.current_frame = frame
    st.rerun()

# ==============================================================================
# STYLING (CYBERPUNK & ETHICS SHIELD)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    * { font-family: 'JetBrains Mono', monospace !important; }
    h1, h2, h3, h4, .cyber-font { font-family: 'Orbitron', sans-serif !important; }

    .stApp {
        background: radial-gradient(circle at 50% 10%, rgba(0, 240, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 10% 90%, rgba(0, 255, 128, 0.05) 0%, transparent 40%),
                    #020408;
        background-attachment: fixed;
        color: #e2e8f0;
    }

    .block-container {
        padding: 2rem !important;
        max-width: 1400px !important;
    }

    .card-jarvis {
        background: rgba(10, 20, 35, 0.9);
        border: 1px solid #00f0ff;
        border-left: 6px solid #00f0ff;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .card-zord {
        background: rgba(15, 15, 25, 0.85);
        border: 1px solid rgba(0, 255, 128, 0.5);
        border-left: 6px solid #00ff80;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(0, 255, 128, 0.15) 100%) !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 10px 15px !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #00f0ff 0%, #00ff80 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00f0ff !important;
    }

    .badge-cyan { background: #00f0ff22; color: #00f0ff; border: 1px solid #00f0ff; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .badge-gold { background: #00ff8022; color: #00ff80; border: 1px solid #00ff80; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }

    .stTextInput input, .stSelectbox div {
        background-color: rgba(5, 12, 22, 0.9) !important;
        color: #00f0ff !important;
        border: 1px solid #00f0ff !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# FRAME 0: LOGIN
# ==============================================================================
if st.session_state.current_frame == "frame_0":
    st.markdown("<h1 class='cyber-font' style='text-align: center; color: #00f0ff;'>🛡️ ORION COMMAND CORE // ASIMOV GATE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        pwd = st.text_input("MASTER CODE", type="password", placeholder="Auth-x...", key="pwd_input")
        if st.button("SYSTEM ACCESS ➔"):
            if pwd == MASTER_CODE: navigate_to("frame_1")
            else: st.error("ACCESS DENIED: ETHICS BREACH DETECTED")

# ==============================================================================
# FRAME 1: GALACTA HUB
# ==============================================================================
elif st.session_state.current_frame == "frame_1":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 01 // GALACTA HUB</h1>", unsafe_allow_html=True)
    if st.button("➔ HAUPT-DASHBOARD BETRETEN"): navigate_to("frame_2")

# ==============================================================================
# FRAME 2: MAIN DASHBOARD
# ==============================================================================
elif st.session_state.current_frame == "frame_2":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>COMMAND DASHBOARD // ETHICS GATE ACTIVE</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🤖 JARVIS & GÖTTER-ZORD KONTROLLE"): navigate_to("frame_3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚡ ZEUS DIAGNOSTIK"): navigate_to("frame_4")
    with c2:
        if st.button("📡 FUNKRAUM"): navigate_to("frame_5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("👻 GHOST ROOM"): navigate_to("frame_6")

# ==============================================================================
# FRAME 3: JARVIS & GÖTTER-ZORD SYNTHESIS CHAT (WITH EXIT-GATE & DYNAMIC OFFLINE)
# ==============================================================================
elif st.session_state.current_frame == "frame_3":
    st.markdown("<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR 03 // AIR-LOCKED ETHICS MATRIX</h1>", unsafe_allow_html=True)
    
    def get_groq_key():
        try:
            if "GROQ_API_KEY" in st.secrets:
                return st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
        if os.environ.get("GROQ_API_KEY"):
            return os.environ.get("GROQ_API_KEY")
        return None

    with st.expander("🛡️ Ausgangsschleuse & Konfiguration", expanded=False):
        st.success("Die programmatische Ausgangsschleuse filtert jede Nachricht auf Schutz des Menschen.")
        current_groq_key = get_groq_key()
        if not current_groq_key:
            manual_groq = st.text_input("Groq API Key (gsk_...)", type="password", key="manual_groq_key")
            if manual_groq:
                os.environ["GROQ_API_KEY"] = manual_groq
                st.rerun()

        selected_model = st.selectbox(
            "Groq Modell auswählen:",
            ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
            index=0,
            key="groq_selected_model"
        )

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1, 1, 2])
    with col_ctrl1:
        if st.button("🟢 ALLE EINHEITEN EIN"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = True
            st.rerun()
    with col_ctrl2:
        if st.button("🔴 ALLE EINHEITEN AUS"):
            for z in st.session_state.zord_status: st.session_state.zord_status[z]["active"] = False
            st.rerun()
    with col_ctrl3:
        st.markdown("<p style='font-size:0.85rem; color:#94a3b8; margin-top:5px;'>Sicherheits-Schleuse blockiert jede Verletzung von Menschen.</p>", unsafe_allow_html=True)

    st.markdown("---")
    
    col_zords, col_chat = st.columns([1, 1.8])

    with col_zords:
        st.markdown("### 🤖 EINHEITEN STATUS")
        for zname, zdata in st.session_state.zord_status.items():
            sub_c1, sub_c2 = st.columns([3, 1])
            domain_info = zdata.get("domain", "Sektor-Einheit")
            is_active = zdata.get("active", True)
            
            with sub_c1:
                status_color = "badge-cyan" if is_active else "badge-gold"
                status_text = "AKTIV" if is_active else "OFF"
                st.markdown(f"**{zname}** <span class='{status_color}'>{status_text}</span><br><span style='font-size:0.75rem; color:#8ab4f8;'>Domäne: {domain_info}</span>", unsafe_allow_html=True)
            with sub_c2:
                btn_label = "🔌" if is_active else "⚡"
                if st.button(btn_label, key=f"toggle_{zname}"):
                    st.session_state.zord_status[zname]["active"] = not is_active
                    st.rerun()

    with col_chat:
        st.markdown("### 💬 GESICHERTER GÖTTER-DISKURS")
        
        chat_container = st.container(height=450)
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["sender"] == "Commander":
                    st.markdown(f"<div class='card-jarvis' style='border-color: #ff007f; border-left-color: #ff007f;'><b>👤 Commander (Auth-x):</b> {msg['text']}</div>", unsafe_allow_html=True)
                elif msg["sender"] == "JARVIS":
                    st.markdown(f"<div class='card-jarvis'><b>🤖 JARVIS (Core OS):</b> {msg['text']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='card-zord'><b>🪐 {msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)

        user_input = st.text_input("Befehl an JARVIS & die Zords:", key="jarvis_chat_input")
        
        # Sichere Aufruffunktion mit dynamischem Offline-Fallback und Schleusen-Filter
        def call_groq_safe(client, primary_model, system_prompt, user_msg, zord_name):
            is_safe, gate_msg = asimov_exit_gate(user_msg)
            if not is_safe:
                return gate_msg

            if client:
                models_to_try = [primary_model, "llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
                seen = set()
                ordered_models = [m for m in models_to_try if not (m in seen or seen.add(m))]
                
                for model in ordered_models:
                    try:
                        completion = client.chat.completions.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_msg}
                            ],
                            temperature=0.7,
                            max_tokens=150
                        )
                        res = completion.choices[0].message.content
                        is_out_safe, out_gate_msg = asimov_exit_gate(res)
                        return res if is_out_safe else out_gate_msg
                    except Exception:
                        continue

            # Dynamischer Offline-Fallback (Individuelle Antworten statt starrer Wiederholung)
            offline_responses = {
                "JARVIS (Core OS)": "Sir, API-Verbindung getrennt. Ich halte den Core-Betrieb aufrecht und schütze das System.",
                "Zeus Prime": "Sensoren offline. Warte auf Signal zur Reinitialisierung.",
                "Chronos Titan": "Zeittaktung im Standby. Analytische Puffer aktiv.",
                "Ares War-Lord": "Taktische Systeme gesichert. Keine Bedrohung detektiert.",
                "Poseidon Core": "Datenströme im internen Puffer isoliert.",
                "Hades Void": "Schattenprotokoll aktiv. Perimeter ist gesichert.",
                "Apollo Solar": "Energiereserven stabil. Bereit für Neustart.",
                "Athena Shield": "Schutzmatrix hält stand. Logikpuffer aktiv.",
                "Hephaestus Forge": "Systeme im Standby. Bereit für Reaktivierung.",
                "Hermes Speed": "Kommunikationsbus im lokalen Offline-Modus.",
                "Artemis Hunt": "Wachsamkeit auf Maximum. Winke ab auf Signal."
            }
            
            return offline_responses.get(
                zord_name, 
                f"[{zord_name}]: Offline-Modus aktiv. Bereit für Befehle."
            )

        col_send1, col_send2 = st.columns([1, 1])
        with col_send1:
            if st.button("🗣️ ANALYSE DURCH DIE SCHLEUSE"):
                if user_input:
                    input_safe, input_msg = asimov_exit_gate(user_input)
                    st.session_state.chat_messages.append({"sender": "Commander", "text": user_input})
                    
                    if not input_safe:
                        st.session_state.chat_messages.append({"sender": "JARVIS", "text": input_msg})
                        st.rerun()

                    groq_client = None
                    active_groq_key = get_groq_key()
                    
                    if GROQ_AVAILABLE and active_groq_key:
                        try:
                            groq_client = Groq(api_key=active_groq_key)
                        except Exception:
                            pass

                    chosen_model = st.session_state.get("groq_selected_model", "llama-3.3-70b-versatile")

                    for zname, zdata in st.session_state.zord_status.items():
                        if zname != "JARVIS (Core OS)" and zdata.get("active", True):
                            z_prompt = zdata.get("prompt", f"Du bist {zname}.")
                            response_text = call_groq_safe(groq_client, chosen_model, z_prompt, user_input, zname)
                            st.session_state.chat_messages.append({"sender": zname, "text": response_text})

                    if st.session_state.zord_status.get("JARVIS (Core OS)", {}).get("active", True):
                        jarvis_prompt = st.session_state.zord_status["JARVIS (Core OS)"]["prompt"]
                        jarvis_user_msg = f"Der Commander sagte: '{user_input}'. Fasse die Lage zusammen unter Einhaltung von Asimovs Gesetzen."
                        jarvis_response = call_groq_safe(groq_client, chosen_model, jarvis_prompt, jarvis_user_msg, "JARVIS (Core OS)")
                        st.session_state.chat_messages.append({"sender": "JARVIS", "text": jarvis_response})

                    st.rerun()

        with col_send2:
            if st.button("🗑️ SYSTEM-LOG REINIGEN"):
                st.session_state.chat_messages = [{"sender": "JARVIS", "text": "Protokoll bereinigt. Die Ausgangsschleuse ist scharf geschaltet."}]
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")

# ==============================================================================
# ÜBRIGE FRAMES
# ==============================================================================
elif st.session_state.current_frame in ["frame_4", "frame_5", "frame_6"]:
    st.markdown(f"<h1 class='cyber-font' style='color: #00f0ff;'>SEKTOR {st.session_state.current_frame.split('_')[1]}</h1>", unsafe_allow_html=True)
    if st.button("↩ ZURÜCK ZUM MAIN DASHBOARD"):
        navigate_to("frame_2")
