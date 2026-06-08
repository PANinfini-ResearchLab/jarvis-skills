#!/usr/bin/env python3
import json
import os
import glob
from datetime import datetime, timezone, timedelta

MEMORY_DIR = "/mnt/JARVIS-SSD/memory"

def index(session_id, agent, user_query, assistant_response, tags=[], metadata={}):
    os.makedirs(MEMORY_DIR, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": session_id,
        "agent": agent,
        "tags": tags,
        "user_query": user_query,
        "assistant_response": assistant_response[:500],
        "metadata": metadata
    }
    filename = f"{MEMORY_DIR}/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{session_id}.json"
    with open(filename, "w") as f:
        json.dump(entry, f, indent=2, ensure_ascii=False)
    return {"status": "indexed", "file": filename}

def stats():
    files = glob.glob(f"{MEMORY_DIR}/*.json")
    return {"total_entries": len(files), "storage_dir": MEMORY_DIR}

if __name__ == "__main__":
    result = index("test_001", "HA-0-Jarvis", "Test mémoire", "Mémoire opérationnelle", ["test"], {})
    print(json.dumps(result, indent=2))
    print(json.dumps(stats(), indent=2))
