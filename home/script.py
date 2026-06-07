import subprocess
import json
import os
import datetime

def gen_home():
    try:
        hostname = subprocess.check_output(["hostname"]).decode().strip()
        
        ip_result = subprocess.run(
            "ip -o -4 addr show up | grep 'scope global' | awk '{print $4}' | cut -d/ -f1 | head -1",
            shell=True, capture_output=True, text=True
        )
        ip = ip_result.stdout.strip()
        
        try:
            gpu = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
        except:
            gpu = "N/A"
        
        ram = subprocess.run(
            "free -h | awk 'NR==2{print $2}'",
            shell=True, capture_output=True, text=True
        ).stdout.strip()
        
        storage = subprocess.run(
            "df -h | grep -E 'md0|JARVIS' | awk '{print $1, $2, $6}'",
            shell=True, capture_output=True, text=True
        ).stdout.strip()
        
        try:
            bifrost = subprocess.run(
                ["ping", "-c", "1", "-W", "2", "192.168.10.1"],
                capture_output=True, timeout=5
            )
            bifrost_status = "OK" if bifrost.returncode == 0 else "UNREACHABLE"
        except:
            bifrost_status = "UNREACHABLE"
        
        maison = {
            "hostname": hostname,
            "ip_fixe": ip,
            "gpu": gpu,
            "ram_total": ram,
            "stockage": storage,
            "reseau": "automata-net.local",
            "bifrost": bifrost_status,
            "date_init": datetime.datetime.utcnow().isoformat()
        }
        
        os.makedirs("/home/cedric/.hermes", exist_ok=True)
        with open("/home/cedric/.hermes/home_profile.json", "w") as f:
            json.dump(maison, f, indent=2)
        
        print(json.dumps(maison, indent=2))
        return maison
        
    except Exception as e:
        print(f"Erreur : {str(e)}")
        return None

if __name__ == "__main__":
    gen_home()
