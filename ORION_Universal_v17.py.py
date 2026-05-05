import streamlit as st
import requests
import base64

# --- SEITE KONFIGURIEREN ---
st.set_page_config(page_title="ORION COMMANDER v17", page_icon="🪐", layout="wide")

# --- SECRETS LADEN (Diagnose inklusive) ---
try:
    # Wir laden die Daten direkt aus den Streamlit Secrets
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_OWNER   = st.secrets["REPO_OWNER"]
    REPO_NAME    = st.secrets["REPO_NAME"]
    # Die Zieldatei für die Befehle
    FILE_PATH    = "zord_cmd.ps1"
except Exception as e:
    st.error(f"❌ Red Skull blockiert die Secrets! Fehlender Schlüssel: {e}")
    st.info("Bitte prüfe in den Streamlit Settings -> Secrets, ob GITHUB_TOKEN, REPO_OWNER und REPO_NAME eingetragen sind.")
    st.stop()

# --- FUNKTION: BEFEHL AN GITHUB SENDEN ---
def send_to_zord(command):
    """Übermittelt den PowerShell-Befehl an das GitHub Repository."""
    # Wir nutzen die offizielle GitHub API URL
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # 1. Schritt: Aktuelle Datei-Informationen (SHA-Hash) abrufen
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            file_data = response.json()
            sha = file_data['sha']
            
            # 2. Schritt: Befehl in Base64 umwandeln (Vorschrift von GitHub)
            content_b64 = base64.b64encode(command.encode("utf-8")).decode("utf-8")
            
            # 3. Schritt: Die Datei auf GitHub überschreiben
            payload = {
                "message": f"ORION Update: {command}",
                "content": content_b64,
                "sha": sha
            }
            
            put_res = requests.put(api_url, headers=headers, json=payload)
            
            if put_res.status_code == 200:
                st.success(f"✅ Befehl '{command}' erfolgreich an Zord gesendet!")
                return True
            else:
                st.error(f"❌ Schreibfehler (Status {put_res.status_code}): {put_res.text}")
        elif response.status_code == 404:
            st.error(f"❌ Fehler 404: Die Datei '{FILE_PATH}' wurde im Repo '{REPO_NAME}' nicht gefunden.")
            st.warning(f"Prüfe, ob die Datei im Repository '{REPO_OWNER}/{REPO_NAME}' wirklich existiert.")
        elif response.status_code == 401:
            st.error("❌ Fehler 401: GitHub Token ist ungültig oder hat keine 'repo'-Rechte.")
        else:
            st.error(f"❌ GitHub API Fehler {response.status_code}: {response.text}")
            
    except Exception as e:
        st.error(f"💥 Kritischer Verbindungsfehler: {e}")
    return False

# --- BENUTZEROBERFLÄCHE (UI) ---
st.header("🪐 ORION UNIVERSAL COMMANDER v17")
st.subheader("Zord Remote Control System")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Start Paint", use_container_width=True):
        send_to_zord("start mspaint")

with col2:
    if st.button("📝 Start Notepad", use_container_width=True):
        send_to_zord("start notepad")

with col3:
    if st.button("🔒 PC Sperren", use_container_width=True):
        send_to_zord("rundll32.exe user32.dll,LockWorkStation")

# --- STATUS-CHECK ---
st.divider()
with st.expander("📡 System-Status & Diagnose"):
    st.write(f"**Verbundenes Repo:** {REPO_OWNER}/{REPO_NAME}")
    st.write(f"**Dateipfad:** {FILE_PATH}")
    if st.button("🔍 Verbindung testen"):
        send_to_zord("WAITING")
