import subprocess
import json

def allow_port(port, protocol="tcp"):
    subprocess.run(["sudo", "ufw", "allow", f"{port}/{protocol}"])
    return {"status": f"Port {port}/{protocol} autorisé"}

def block_port(port, protocol="tcp"):
    subprocess.run(["sudo", "ufw", "deny", f"{port}/{protocol}"])
    return {"status": f"Port {port}/{protocol} bloqué"}

def allow_ip(ip):
    subprocess.run(["sudo", "ufw", "allow", "from", ip])
    return {"status": f"IP {ip} autorisée"}

def block_ip(ip):
    subprocess.run(["sudo", "ufw", "deny", "from", ip])
    return {"status": f"IP {ip} bloquée"}

def list_rules():
    result = subprocess.run(["sudo", "ufw", "status", "verbose"], capture_output=True, text=True)
    return {"rules": result.stdout}

def restart_firewall():
    subprocess.run(["sudo", "ufw", "disable"])
    subprocess.run(["sudo", "ufw", "enable"])
    return {"status": "Pare-feu redémarré"}

if __name__ == "__main__":
    print(json.dumps(list_rules(), indent=2))
