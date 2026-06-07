import subprocess
import json
import os
from datetime import datetime

def full_audit():
    report = f"# Audit Matériel — ODIN (la-forge)\n**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "## CPU\n```\n" + subprocess.check_output(['lscpu']).decode() + "\n```\n\n"
    report += "## GPU\n```\n" + subprocess.check_output(['nvidia-smi']).decode() + "\n```\n\n"
    report += "## RAM\n```\n" + subprocess.check_output(['free', '-h']).decode() + "\n```\n\n"
    report += "## Stockage\n```\n" + subprocess.check_output(['df', '-h']).decode() + "\n```\n\n"
    report += "## RAID\n```\n" + subprocess.check_output(['cat', '/proc/mdstat']).decode() + "\n```\n\n"
    report += "## Réseau\n```\n" + subprocess.check_output(['ip', 'a']).decode() + "\n```\n\n"
    os.makedirs("/mnt/JARVIS-SSD/audits", exist_ok=True)
    filename = f"/mnt/JARVIS-SSD/audits/audit_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
    with open(filename, "w") as f:
        f.write(report)
    return {"saved_to": filename}

if __name__ == "__main__":
    print(json.dumps(full_audit(), indent=2))
