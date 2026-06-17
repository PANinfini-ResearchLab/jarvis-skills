import subprocess
import sys
import os

def get_gpu_stats():
    try:
        res = subprocess.run(['nvidia-smi', '--query-gpu=name,temperature.C,memory.used,memory.total,utilization.gpu', 
                              '--format=csv,noheader,nounits'], 
                              capture_output=True, text=True, check=True)
        stats = []
        for line in res.stdout.strip().split('\n'):
            if line:
                name, temp, mem_used, mem_total, util = line.split(',')
                stats.append({
                    "name": name,
                    "temp": int(temp),
                    "mem_used": int(mem_used),
                    "mem_total": int(mem_total),
                    "util": int(util)
                })
        return stats
    except Exception as e:
        return f"Erreur nvidia-smi : {e}"

def get_disk_stats():
    paths = ["/mnt/JARVIS-SSD", "/"]
    stats = []
    for path in paths:
        try:
            res = subprocess.run(['df', '-h', path], capture_output=True, text=True).stdout.splitlines()
            # Ligne 1 est l'en-tête, ligne 2 contient les données
            parts = res[1].split()
            stats.append(f"{path}: {parts[2]} utilisé sur {parts[1]}")
        except:
            pass
    return stats

def check_health():
    gpu_stats = get_gpu_stats()
    disk_stats = get_disk_stats()
    
    report = []
    report.append("=== RAPPORT DE SANTÉ ODIN ===")
    
    for gpu in gpu_stats:
        if isinstance(gpu, dict):
            status = "OK"
            if gpu['temp'] > 85: status = "!!! ALERTE THERMIQUE !!!"
            if (gpu['mem_used'] / gpu['mem_total']) > 0.9: status = "!!! ALERTE MÉMOIRE !!!"
            
            report.append(f"GPU {gpu['name']} : Temp {gpu['temp']}C | Util: {gpu['util']}% | VRAM: {gpu['mem_used']}MB/{gpu['mem_total']}MB [{status}]")
        else:
            report.append(gpu)
    
    report.append("\n--- Stockage ---")
    for ds in disk_stats:
        report.append(ds)
        
    return "\n".join(report)

if __name__ == "__main__":
    print(check_health())
