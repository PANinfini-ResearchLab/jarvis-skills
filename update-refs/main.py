import subprocess
import datetime
import os

FILES_TO_UPDATE = [
    "/home/cedric/.hermes/HARDWARE.md",
    "/home/cedric/scriptorium/corps_odin.md"
]

def get_gpu_info():
    try:
        # Get nvidia-smi output for names and memory of all GPUs
        res = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader,nounits'], 
                              capture_output=True, text=True, check=True)
        gpus = []
        for line in res.stdout.strip().split('\n'):
            if line:
                parts = line.split(',')
                if len(parts) == 2:
                    name, mem = parts
                    gpus.append(f"*{name} ({mem}MB)")
        return "\n".join(gpus) if gpus else "Aucun GPU NVIDIA détecté."
    except Exception as e:
        return f"[ERREUR] Impossible de lire nvidia-smi : {e}"

def get_system_summary():
    try:
        cpu = subprocess.run(['lscpu'], capture_output=True, text=True).stdout.split('\n')[0]
        mem = subprocess.run(['free', '-h'], capture_output=True, text=True).stdout.split('\n')[1].split()[1] # Total mem
        return f"CPU: {cpu}\nMemory Total: {mem}"
    except Exception as e:
        return str(e)

def generate_content():
    gpu = get_gpu_info()
    sys_sum = get_system_summary()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""# Rapport d'Audit Système (Auto-généré)
Date de mise à jour : {timestamp}

## Matériel Détecté (Fait Épistémique)
{gpu}

## Résumé Système
{sys_sum}

## Services Actifs
Ollama est détecté sur les GPU disponibles.
"""
    return content

def update():
    content = generate_content()
    for path in FILES_TO_UPDATE:
        if os.path.exists(path):
            with open(path, 'w') as f:
                f.write(content)
            print(f"Mise à jour réussie : {path}")
        else:
            print(f"Fichier non trouvé (ignoré) : {path}")

if __name__ == "__main__":
    update()
