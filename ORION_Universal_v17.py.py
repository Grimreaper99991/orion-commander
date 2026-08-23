import os
import logging
from typing import List, Dict, Any, Optional
from groq import Groq, GroqError

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("ORION-GROQ-ROUTER")

class GroqMatrixRouter:
    """
    ORION Multi-Model-Router für die Groq API.
    Führt Fallbacks über mehrere Modell-IDs durch, falls Modelle nicht erreichbar oder dekommissioniert sind.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            logger.warning("[GROQ-MATRIX]: Kein API-Key gefunden. Bitte GROQ_API_KEY setzen.")
            self.client = None
        else:
            self.client = Groq(api_key=self.api_key)

        # Aktuell verifizierte & aktive Groq Modell-IDs (Stand 2026)
        # Priorisiert nach Performanz & Verfügbarkeit
        self.default_matrix: List[str] = [
            "openai/gpt-oss-120b",       # Primäres High-Performance Modell
            "openai/gpt-oss-20b",        # Schnelles Ultra-Low-Latency Modell
            "qwen/qwen3.6-27b",          # Multimodales / Vielseitiges Backup
            "groq/compound",             # System-Compound Fallback
        ]

    def get_live_models(self) -> List[str]:
        """Holt dynamisch die aktuell aktiv unterstützten Modelle von der Groq API."""
        if not self.client:
            return []
        try:
            models_page = self.client.models.list()
            active_models = [m.id for m in models_page.data if hasattr(m, 'id')]
            logger.info(f"[GROQ-MATRIX]: Live-Modellliste erfolgreich abgerufen ({len(active_models)} Modelle).")
            return active_models
        except Exception as e:
            logger.error(f"[GROQ-MATRIX]: Fehler beim Abfragen der Live-Modellliste: {e}")
            return []

    def query(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2048,
        custom_matrix: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Sendet eine Anfrage an die Groq Model-Matrix mit automatischem Fallback.
        """
        if not self.client:
            return {
                "success": False,
                "error": "GROQ_API_KEY ist nicht konfiguriert.",
                "model_used": None,
                "response": None
            }

        # Modell-Reihenfolge festlegen
        candidate_models = custom_matrix or self.default_matrix
        error_logs = []

        # Versuch 1: Durchlaufen der vordefinierten Matrix
        for model_id in candidate_models:
            try:
                logger.info(f"[GROQ-MATRIX]: Sende Anfrage an Modell '{model_id}'...")
                response = self.client.chat.completions.create(
                    model=model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                
                content = response.choices[0].message.content
                logger.info(f"[GROQ-MATRIX]: Erfolgreich geantwortet mit Modell '{model_id}'.")
                
                return {
                    "success": True,
                    "model_used": model_id,
                    "response": content,
                    "raw_response": response
                }

            except GroqError as ge:
                err_msg = f"Modell '{model_id}' fehlgeschlagen: {ge}"
                logger.warning(f"[GROQ-MATRIX-FEHLER]: {err_msg}")
                error_logs.append(err_msg)
            except Exception as e:
                err_msg = f"Unerwarteter Fehler bei '{model_id}': {e}"
                logger.error(f"[GROQ-MATRIX-FEHLER]: {err_msg}")
                error_logs.append(err_msg)

        # Versuch 2: Dynamischer Fallback über API-Live-Abfrage (falls alle Kandidaten fehlschlagen)
        logger.warning("[GROQ-MATRIX]: Alle Standard-Modelle fehlgeschlagen. Starte Live-Auto-Fetch...")
        live_models = self.get_live_models()
        
        # Filter bereits ausprobierte Modelle heraus
        remaining_models = [m for m in live_models if m not in candidate_models]
        
        for model_id in remaining_models:
            try:
                logger.info(f"[GROQ-MATRIX-LIVE]: Versuche Ausweichmodell '{model_id}'...")
                response = self.client.chat.completions.create(
                    model=model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                content = response.choices[0].message.content
                return {
                    "success": True,
                    "model_used": model_id,
                    "response": content,
                    "raw_response": response
                }
            except Exception as e:
                error_logs.append(f"Live-Fallback '{model_id}' fehlgeschlagen: {e}")

        # Wenn gar kein Modell erreichbar war:
        return {
            "success": False,
            "error": "Keines der Matrix-Modelle konnte erreicht werden. Bitte API-Key oder Netzwerk prüfen.",
            "logs": error_logs,
            "model_used": None,
            "response": None
        }


# ==========================================
# Beispiel für die direkte Nutzung in ORION
# ==========================================
if __name__ == "__main__":
    # Test-Setup
    router = GroqMatrixRouter()

    sample_prompt = [
        {"role": "system", "content": "Du bist ORION, eine fortschrittliche KI-Steuerung."},
        {"role": "user", "content": "System-Statusüberprüfung: Ist die Multi-Model-Router-Matrix aktiv?"}
    ]

    result = router.query(sample_prompt)

    if result["success"]:
        print(f"\n[ERFOLG - Modell: {result['model_used']}]")
        print(f"Antwort:\n{result['response']}")
    else:
        print(f"\n[FEHLER]: {result['error']}")
