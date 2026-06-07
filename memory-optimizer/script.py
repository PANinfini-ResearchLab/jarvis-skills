import subprocess
import json
import os

def check_ram_usage():
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    return {"ram_usage": result.stdout}

def check_vram_usage():
    result = subprocess.run(["nvidia-smi", "--query-gpu=index,name,memory.used,memory.total",
                             "--format=csv,noheader"], capture_output=True, text=True)
    return {"vram_usage": result.stdout}

def kill_process(pid):
    subprocess.run(["sudo", "kill", "-9", str(pid)])
    return {"status": f"Processus {pid} tué"}

def optimize_ollama(max_loaded_models=2):
    env_file = os.path.expanduser("~/.hermes/.env")
    with open(env_file, "a") as f:
        f.write(f"\nOLLAMA_MAX_LOADED_MODELS={max_loaded_models}\n")
    subprocess.run(["sudo", "systemctl", "restart", "ollama"])
    return {"status": f"Ollama optimisé pour {max_loaded_models} modèles max"}

def clear_cache():
    subprocess.run(["sync"])
    subprocess.run(["sudo", "bash", "-c", "echo 3 > /proc/sys/vm/drop_caches"])
    return {"status": "Cache système libéré"}

def check_all():
    return {
        "ram": check_ram_usage(),
        "vram": check_vram_usage()
    }

if __name__ == "__main__":
    print(json.dumps(check_all(), indent=2))
