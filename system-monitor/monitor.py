import subprocess
import time
import requests
from threading import Thread

TELEGRAM_BOT_TOKEN = "8979976268:AAEEmM3OaJ_36GoqAsTU4cA57ndbAsXLdQc"
CHAT_ID = "8664542027"

thresholds = {"gpu_util": 80, "ram_util": 85, "storage_util": 90}

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": f"🚨 ALERTE ODIN:\n{message}"})

def get_gpu_util():
    result = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                           capture_output=True, text=True)
    return [float(x) for x in result.stdout.strip().split('\n') if x]

def get_ram_util():
    result = subprocess.run(["free", "--bytes"], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if line.startswith('Mem:'):
            parts = line.split()
            return float(parts[2]) / float(parts[1]) * 100
    return 0

def get_storage_util():
    result = subprocess.run(["df", "/mnt/JARVIS-SSD"], capture_output=True, text=True)
    for line in result.stdout.split('\n')[1:]:
        if line:
            return float(line.split()[4].replace('%', ''))
    return 0

def check_thresholds():
    alerts = []
    for i, util in enumerate(get_gpu_util()):
        if util > thresholds["gpu_util"]:
            alerts.append(f"GPU {i} à {util:.1f}% (> {thresholds['gpu_util']}%)")
    ram = get_ram_util()
    if ram > thresholds["ram_util"]:
        alerts.append(f"RAM à {ram:.1f}% (> {thresholds['ram_util']}%)")
    storage = get_storage_util()
    if storage > thresholds["storage_util"]:
        alerts.append(f"Stockage à {storage:.1f}% (> {thresholds['storage_util']}%)")
    return alerts

def monitor_loop():
    while True:
        for alert in check_thresholds():
            send_telegram_alert(alert)
        time.sleep(300)

if __name__ == "__main__":
    Thread(target=monitor_loop, daemon=True).start()
    print("Monitoring démarré — alertes Telegram actives")
    while True:
        time.sleep(60)
