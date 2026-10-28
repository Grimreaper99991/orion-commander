# ==============================================================================
# VERFEINERTER SICHERHEITS- & OFFLINE-MECHANISMUS (v73.1)
# ==============================================================================

def call_groq_safe(client, primary_model, system_prompt, user_msg, zord_name):
    # 1. Strikter Filter NUR bei echten Gefahrenbegriffen
    is_safe, gate_msg = asimov_exit_gate(user_msg)
    if not is_safe:
        return gate_msg

    # 2. Versuch, die API zu erreichen
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
                # Antwort-Prüfung durch die Schleuse
                is_out_safe, out_gate_msg = asimov_exit_gate(res)
                return res if is_out_safe else out_gate_msg
            except Exception:
                continue

    # 3. DYNAMISCHER OFFLINE-FALLBACK (Keine starre Text-Schleife mehr!)
    offline_responses = {
        "JARVIS (Core OS)": f"Sir, API-Verbindung getrennt. Ich halte den Core-Betrieb aufrecht und schütze das System.",
        "Zeus Prime": "Sensoren offline. Warte auf Signal zur Reinitialisierung.",
        "Apollo Solar": "Sonne und Energiesysteme laufen stabil im Standby.",
        "Ares War-Lord": "Keine Bedrohung erkannt. Taktische Systeme auf Standby.",
        "Athena Shield": "Schutzmatrix aktiv. Systeme sichern das Netzwerk im Hintergrund."
    }
    
    return offline_responses.get(
        zord_name, 
        f"[{zord_name}]: Offline-Modus aktiv. Bereit für Befehle, sobald die Verbindung steht."
    )
