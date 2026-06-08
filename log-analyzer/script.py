import subprocess
import json
import os
from datetime import datetime, timedelta

def analyze_ollama_logs():
    result = subprocess.run(["journalctl", "-u", "ollama", "--no-pager", "-n", "100"],
                           capture_output=True, text=True)
    lines = result.stdout.split('\n')
    errors = [l for l in lines if "error" in l.lower() or "fail" in l.lower()]
    warnings = [l for l in lines if "warn" in l.lower()]
    return {"total_lines": len(lines), "errors": errors, "warnings": warnings}

def search_logs(keyword):
    result = subprocess.run(["journalctl", "--no-pager", "-n", "500"],
                           capture_output=True, text=True)
    matches = [l for l in result.stdout.split('\n') if keyword.lower() in l.lower()]
    return {"keyword": keyword, "matches": matches}

def generate_log_report(days=7):
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    result = subprocess.run(["journalctl", "--since", since_date, "--no-pager"],
                           capture_output=True, text=True)
    os.makedirs("/mnt/JARVIS-SSD/logs/reports", exist_ok=True)
    filename = f"/mnt/JARVIS-SSD/logs/reports/log_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(filename, "w") as f:
        f.write(f"# Rapport Logs — {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(f"```\n{result.stdout}\n```")
    return {"saved_to": filename}

def tail_log(file, lines=50):
    result = subprocess.run(["tail", "-n", str(lines), file], capture_output=True, text=True)
    return {"file": file, "last_lines": result.stdout}

if __name__ == "__main__":
    print(json.dumps(analyze_ollama_logs(), indent=2))
