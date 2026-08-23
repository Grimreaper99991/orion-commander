import os
import logging
import streamlit as st
from typing import List, Dict, Any, Optional

try:
    from groq import Groq, GroqError
except ImportError:
    st.error("Das 'groq' Paket ist nicht installiert. Bitte im Terminal ausführen: pip install groq")
    st.stop()

# -----------------------------------------------------------------------------
# 1. LOGGING & SEITEN-SETUP
# -----------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("ORION-STREAMLIT")

st.set_page_config(
    page_title="ORION Command Core",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. GROQ ROUTER MATRIX
# -----------------------------------------------------------------------------
class GroqMatrixRouter:
    """
    ORION Multi-Model-Router für die Groq API.
    Führt automatische Fallbacks durch, falls Modelle nicht erreichbar oder dekommissioniert sind.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            self.client = None
        else:
            self.client = Groq(api_key=self.api_key)

        # Aktuelle & aktive Groq Modell-IDs (Stand 2026)
        self.default_matrix: List[str] = [
            "openai/gpt-oss-120b",                       # Primär: High-Performance Reasoning
            "openai/gpt-oss-20b",                        # Fast: Low-Latency Router
            "qwen/qwen3.6-27b",                          # Vision & Vielseitiges Backup
            "meta-llama/llama-4-scout-17b-16e-instruct", # Scout Llama Backup
            "llama-3.1-8b-instant",                      # Standard Fast Fallback
        ]

    def get_live_models(self) -> List[str]:
        """Holt dynamisch die aktuell aktiv unterstützten Modelle von der Groq API."""
        if not self.client:
            return []
        try:
            models_page = self.client.models.list()
            active_models = [m.id for m in models_page.data if hasattr(m, 'id')]
            return active_models
        except Exception as e:
            logger.error(f"[GROQ-MATRIX]: Fehler beim Live-Model-Fetch: {e}")
            return []

    def query(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2048
    ) -> Dict[str, Any]:
        """Sendet eine Anfrage an die Groq Model-Matrix mit automatischem Fallback."""
        if not self.client:
            return {
                "success": False,
                "error": "Kein gültiger GROQ_API_KEY vorhanden. Bitte API-Key in der Sidebar eingeben.",
                "model_used": None,
                "response": None
            }

        error_logs = []

        # Versuch 1: Vordefinierte Matrix durchlaufen
        for model_id in self.default_matrix:
            try:
                logger.info(f"[GROQ-MATRIX]: Anfrage an '{model_id}'...")
                response = self.client.chat.completions.create(
                    model=model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                content = response.choices[0].message.content
                logger.info(f"[GROQ-MATRIX]: Erfolg mit Modell '{model_id}'.")
                return {
                    "success": True,
                    "model_used": model_id,
                    "response": content,
                    "error_logs": error_logs
                }
            except Exception as e:
                err_text = f"Modell '{model_id}' fehlgeschlagen: {str(e)}"
                logger.warning(f"[GROQ-MATRIX-FEHLER]: {err_text}")
                error_logs.append(err_text)

        # Versuch 2: Live-Auto-Fetch (Fallback)
        logger.warning("[GROQ-MATRIX]: Standard-Matrix erschöpft. Starte Live-Auto-Fetch...")
        live_models = self.get_live_models()
        remaining_models = [m for m in live_models if m not in self.default_matrix]

        for model_id in remaining_models:
            try:
                response = self.client.chat.completions.create(
                    model=model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                content = response.choices[0].message.content
                return {
                    "success": True,
                    "model_used": f"{model_id} (Live-Fallback)",
                    "response": content,
                    "error_logs": error_logs
                }
            except Exception as e:
                error_logs.append(f"Live-Fallback '{model_id}' fehlgeschlagen: {str(e)}")

        return {
            "success": False,
            "error": "Keines der Matrix-Modelle konnte erreicht werden.",
            "error_logs": error_logs,
            "model_used": None,
            "response": None
        }

# -----------------------------------------------------------------------------
# 3. STREAMLIT SESSION STATE INITIALISIERUNG
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist ORION, ein hochentwickeltes KI-Betriebssystem. Antworte präzise, intelligent und direkt."}
    ]

if "last_model_used" not in st.session_state:
    st.session_state.last_model_used = "Inaktiv"

# -----------------------------------------------------------------------------
# 4. SIDEBAR - STEUERUNG & KEY-MANAGEMENT
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚡ ORION Core Control")
    st.markdown("---")
    
    # API-Key Eingabe (aus st.secrets, Umgebungsvariablen oder manuelle Eingabe)
    default_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
    user_api_key = st.text_input("Groq API Key:", value=default_key, type="password")
    
    st.markdown("---")
    st.subheader("Matrix Status")
    
    # Router Initialisieren
    router = GroqMatrixRouter(api_key=user_api_key)
    
    if user_api_key:
        st.success("API Key Geladen")
    else:
        st.error("API Key fehlt!")
        
    st.info(f"Aktives Modell: **{st.session_state.last_model_used}**")
    
    # System-Reset
    if st.button("💬 Chat-Verlauf zurücksetzen"):
        st.session_state.messages = [
            {"role": "system", "content": "Du bist ORION, ein hochentwickeltes KI-Betriebssystem. Antworte präzise, intelligent und direkt."}
        ]
        st.session_state.last_model_used = "Inaktiv"
        st.rerun()

    st.markdown("---")
    st.caption("ORION Universal Core Matrix v21.4")

# -----------------------------------------------------------------------------
# 5. HAUPTFENSTER - CHAT INTERFACE
# -----------------------------------------------------------------------------
st.title("🛡️ ORION AI Gateway")
st.caption("Multi-Model-Router mit automatischem Groq-Fallback System")

# Verlauf anzeigen (ohne den System-Prompt)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Benutzereingabe
if prompt := st.chat_input("Befehl oder Frage eingeben..."):
    # 1. User Message hinzufügen
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 2. KI Antwort generieren
    with st.chat_message("assistant"):
        with st.spinner("ORION Router analysiert und sendet Anfrage..."):
            res = router.query(messages=st.session_state.messages)

            if res["success"]:
                response_text = res["response"]
                st.write(response_text)
                
                # Model-Information aktualisieren
                st.session_state.last_model_used = res["model_used"]
                st.caption(f"🤖 Antworterstellend: `{res['model_used']}`")
                
                # In Session Speichern
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            else:
                st.error(f"❌ **GROQ-MATRIX-FEHLER**: {res['error']}")
                if res.get("error_logs"):
                    with st.expander("Fehler-Logbuch anzeigen"):
                        for err in res["error_logs"]:
                            st.write(f"- `{err}`")
