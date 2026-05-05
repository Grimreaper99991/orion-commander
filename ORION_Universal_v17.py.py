import streamlit as st
import requests
import base64

# --- GITHUB CONNECTION ---
# Wir holen die Daten genau so aus den Secrets, wie du sie im TOML-Format angelegt hast
try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_OWNER = st.secrets["REPO_OWNER"]
    REPO_NAME = st.secrets["REPO_NAME"]
    FILE_PATH = "zord_cmd.ps1" # Der Name der Datei auf GitHub
except Exception as e:
    st.error(f"Fehler beim Laden der Secrets: {e}")

def send_to_zord(command):
    """Schreibt einen PowerShell-Befehl direkt in dein GitHub-Repo"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 1. Wir holen die aktuelle Version der Datei (SHA), um sie überschreiben zu dürfen
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_data = response.json()
        sha = file_data['sha']
        
        # 2. Den Befehl für GitHub vorbereiten (muss Base64 sein)
        content_b64 = base64.b64encode(command.encode("utf-8")).decode("utf-8")
        
        # 3. Das Update-Paket schnüren
        payload = {
            "message": "ORION Zord Command Update",
            "content": content_b64,
            "sha": sha
        }
        
        # 4. Ab die Post!
        update_res = requests.put(url, headers=headers, json=payload)
        
        if update_res.status_code == 200:
            return True
    return False

# --- BEISPIEL FÜR EINEN BUTTON ---
if st.button("🚀 Zord: Paint starten"):
    if send_to_zord("start mspaint"):
        st.success("Befehl an Zord übertragen!")
    else:
        st.error("Übertragung fehlgeschlagen.")
