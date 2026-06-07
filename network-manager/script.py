import subprocess
import json

def check_connectivity(host):
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    return {"status": "OK" if result.returncode == 0 else "FAIL", "output": result.stdout}

def scan_network():
    result = subprocess.run(["nmap", "-sn", "192.168.10.0/24"], capture_output=True, text=True)
    return {"devices": result.stdout}

def list_interfaces():
    result = subprocess.run(["ip", "a"], capture_output=True, text=True)
    return {"interfaces": result.stdout}

def restart_network():
    subprocess.run(["sudo", "systemctl", "restart", "systemd-networkd"])
    return {"status": "Services réseau redémarrés"}

if __name__ == "__main__":
    print(json.dumps(list_interfaces(), indent=2))
