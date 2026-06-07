import subprocess
import json
import time
import requests
from threading import Thread

TELEGRAM_BOT_TOKEN = "8979976268:AAEEmM3OaJ_36GoqAsTU4cA57ndbAsXLdQc"
CHAT_ID = "8664542027"
threshold = 100  # Mbps

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": f"🚨 ALERTE BANDE PASSANTE:\n{message}"})

def get_usage():
    result = subprocess.run(["ifstat", "-i", "eno1", "1", "1"], capture_output=True, text=True)
    return {"usage": result.stdout}

def get_usage_by_ip():
    result = subprocess.run(["sudo", "nethogs", "-t", "-d", "1", "eno1"],
                           capture_output=True, text=True, timeout=5)
    return {"usage_by_ip": result.stdout}

def set_alert(new_threshold):
    global threshold
    threshold = new_threshold
    return {"status": f"Seuil d'alerte défini à {threshold} Mbps"}

def monitor_loop():
    while True:
        usage = get_usage()
        time.sleep(60)

def start_monitoring():
    Thread(target=monitor_loop, daemon=True).start()
    return {"status": "Surveillance bande passante démarrée"}

if __name__ == "__main__":
    print(json.dumps(get_usage(), indent=2))
