#!/usr/bin/env python3
import subprocess
import json
import os
import platform
from datetime import datetime

DEFAULT_OUTPUT_DIR = os.path.expanduser("~/.hermes/inventory/")

def get_system_info():
    return {
        "hostname": subprocess.check_output(["hostname"]).decode().strip(),
        "os": platform.system(),
        "kernel": platform.uname().release,
        "architecture": platform.machine(),
        "uptime": subprocess.check_output(["uptime", "-p"]).decode().strip(),
    }

def get_cpu_info():
    result = subprocess.run(["lscpu"], capture_output=True, text=True)
    return {"details": result.stdout}

def get_gpu_info():
    try:
        result = subprocess.check_output([
            "nvidia-smi",
            "--query-gpu=index,name,memory.used,memory.total,temperature.gpu,utilization.gpu",
            "--format=csv,noheader"
        ]).decode().strip()
        gpus = []
        for line in result.split('\n'):
            if line:
                index, name, mem_used, mem_total, temp, util = line.split(', ')
                gpus.append({"index": index, "name": name, "mem_used": mem_used,
                            "mem_total": mem_total, "temp": temp, "util": util})
        return gpus
    except:
        return [{"error": "Aucun GPU NVIDIA détecté"}]

def get_ram_info():
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    return {"usage": result.stdout}

def get_storage_info():
    df = subprocess.run(["df", "-h"], capture_output=True, text=True).stdout
    lsblk = subprocess.run(["lsblk"], capture_output=True, text=True).stdout
    raid = subprocess.run(["cat", "/proc/mdstat"], capture_output=True, text=True).stdout
    return {"df": df, "lsblk": lsblk, "raid": raid}

def get_network_info():
    result = subprocess.run(["ip", "a"], capture_output=True, text=True)
    return {"interfaces": result.stdout}

def generate_inventory():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "gpu": get_gpu_info(),
        "ram": get_ram_info(),
        "storage": get_storage_info(),
        "network": get_network_info(),
    }

def save_inventory(inventory, output_path=None, format="md"):
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if output_path is None:
        output_path = os.path.join(DEFAULT_OUTPUT_DIR, f"inventory_{timestamp}.{format}")
    if format == "json":
        with open(output_path, "w") as f:
            json.dump(inventory, f, indent=2)
    else:
        md = f"# Inventaire Matériel — {inventory['system']['hostname']}\n"
        md += f"**Date:** {inventory['timestamp']}\n\n"
        md += f"## Système\n```\nHostname: {inventory['system']['hostname']}\nOS: {inventory['system']['os']}\nKernel: {inventory['system']['kernel']}\nUptime: {inventory['system']['uptime']}\n```\n\n"
        md += f"## CPU\n```\n{inventory['cpu']['details']}\n```\n\n"
        md += f"## GPU\n```\n{json.dumps(inventory['gpu'], indent=2)}\n```\n\n"
        md += f"## RAM\n```\n{inventory['ram']['usage']}\n```\n\n"
        md += f"## Stockage\n```\n{inventory['storage']['df']}\n{inventory['storage']['raid']}\n```\n\n"
        md += f"## Réseau\n```\n{inventory['network']['interfaces']}\n```\n\n"
        with open(output_path, "w") as f:
            f.write(md)
    return output_path

if __name__ == "__main__":
    inventory = generate_inventory()
    path = save_inventory(inventory)
    print(f"Inventaire sauvegardé : {path}")
    print(json.dumps(inventory, indent=2))
