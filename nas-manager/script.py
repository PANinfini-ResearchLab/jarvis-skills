import subprocess
import json
import os

def create_backup(source, destination):
    os.makedirs(destination, exist_ok=True)
    subprocess.run(["rsync", "-avz", "--delete", f"{source}/", destination])
    return {"status": f"Sauvegarde de {source} vers {destination} terminée"}

def list_shares():
    result = subprocess.run(["mount"], capture_output=True, text=True)
    return {"shares": result.stdout}

def check_disk_usage():
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    return {"disk_usage": result.stdout}

def set_permissions(path, user, permissions):
    subprocess.run(["sudo", "chown", f"{user}:{user}", path])
    subprocess.run(["sudo", "chmod", permissions, path])
    return {"status": f"Permissions {permissions} définies pour {path}"}

def start_smb_server():
    subprocess.run(["sudo", "systemctl", "start", "smbd"])
    subprocess.run(["sudo", "systemctl", "enable", "smbd"])
    return {"status": "Serveur SMB démarré"}

if __name__ == "__main__":
    print(json.dumps(check_disk_usage(), indent=2))
