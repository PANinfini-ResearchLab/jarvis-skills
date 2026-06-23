#!/usr/bin/env python3
import json
import time
import os
from datetime import datetime

LOG_PATH = "/mnt/JARVIS-SSD/logs/ha-tool-core.jsonl"

def log_action(agent, tool, arguments, result, status, duration_ms, validated_by="AUTO"):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent,
        "tool": tool,
        "arguments": arguments,
        "status": status,
        "duration_ms": duration_ms,
        "validated_by": validated_by,
        "result_preview": str(result)[:200]
    }
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry

if __name__ == "__main__":
    entry = log_action("HA-0-Jarvis", "nvidia-smi", {}, "test", "success", 42)
    print(json.dumps(entry, indent=2))
