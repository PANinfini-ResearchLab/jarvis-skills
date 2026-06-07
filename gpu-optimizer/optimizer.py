import subprocess
import json
import os
from datetime import datetime, timedelta

def scan_gpu():
    result = subprocess.run(["nvidia-smi", "--query-gpu=index,name,utilization.gpu,memory.used,memory.total",
                             "--format=csv,noheader,nounits"], capture_output=True, text=True)
    gpu_data = result.stdout.strip().split('\n')
    models = subprocess.run(["ollama", "list"], capture_output=True, text=True).stdout
    loaded_models = [line.split()[0] for line in models.split('\n')[1:] if line.strip()]
    output = {"gpus": [], "models": loaded_models}
    for line in gpu_data:
        if line:
            index, name, gpu_util, mem_used, mem_total = line.split(', ')
            output["gpus"].append({"index": index, "name": name, "gpu_util": gpu_util, "mem_used": mem_used, "mem_total": mem_total})
    return output

if __name__ == "__main__":
    print(json.dumps(scan_gpu(), indent=2))
