import subprocess
import json
import os
import time
from datetime import datetime

def benchmark_cpu():
    result = subprocess.run(["sysbench", "cpu", "--threads=80", "--time=10", "run"],
                           capture_output=True, text=True)
    return {"cpu_benchmark": result.stdout}

def benchmark_gpu():
    result = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,memory.used,utilization.gpu,temperature.gpu",
                             "--format=csv,noheader"], capture_output=True, text=True)
    return {"gpu_info": result.stdout}

def benchmark_ram():
    result = subprocess.run(["sysbench", "memory", "--threads=80", "--time=10", "run"],
                           capture_output=True, text=True)
    return {"ram_benchmark": result.stdout}

def benchmark_storage():
    result_read = subprocess.run(["dd", "if=/mnt/JARVIS-SSD/test_bench", "of=/dev/null",
                                  "bs=1M", "count=1000"], capture_output=True, text=True)
    result_write = subprocess.run(["dd", "if=/dev/zero", "of=/mnt/JARVIS-SSD/test_bench",
                                   "bs=1M", "count=1000"], capture_output=True, text=True)
    subprocess.run(["rm", "-f", "/mnt/JARVIS-SSD/test_bench"])
    return {"read": result_read.stderr, "write": result_write.stderr}

def compare_models(model1, model2):
    results = {}
    for model in [model1, model2]:
        start = time.time()
        subprocess.run(["ollama", "run", model, "Compte jusqu'à 10."],
                      capture_output=True, text=True)
        elapsed = time.time() - start
        results[model] = {"time_seconds": round(elapsed, 2)}
    return {"comparison": results}

def generate_report():
    report = f"# Benchmark ODIN — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    report += "## GPU\n```\n" + benchmark_gpu()["gpu_info"] + "\n```\n\n"
    report += "## RAM\n```\n" + subprocess.check_output(["free", "-h"]).decode() + "\n```\n\n"
    report += "## Stockage\n```\n" + subprocess.check_output(["df", "-h"]).decode() + "\n```\n\n"
    os.makedirs("/mnt/JARVIS-SSD/benchmarks", exist_ok=True)
    filename = f"/mnt/JARVIS-SSD/benchmarks/bench_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
    with open(filename, "w") as f:
        f.write(report)
    return {"saved_to": filename}

if __name__ == "__main__":
    print(json.dumps(generate_report(), indent=2))
