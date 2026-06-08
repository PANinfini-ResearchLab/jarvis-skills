---
name: hermes-memory
description: Mémoire transversale pour Jarvis HA-0. Indexation automatique des conversations, recherche sémantique, historique structuré par session/user/tags.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Hermes Memory

## Concept
Mémoire persistante et recherchable pour tous les agents Hermès IAU.
Chaque échange significatif est indexé avec métadonnées structurées.

## Structure d'une entrée mémoire
```json

cat > ~/.hermes/skills/hermes-memory/memory.py << 'EOF'
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

def search(query, limit=10):
    results = []
    for filepath in glob.glob(f"{MEMORY_DIR}/*.json"):
        with open(filepath) as f:
            entry = json.load(f)
        text = f"{entry.get('user_query','')} {entry.get('assistant_response','')} {' '.join(entry.get('tags',[]))}"
        if query.lower() in text.lower():
            results.append(entry)
    return results[:limit]

def history(days=7):
    results = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    for filepath in glob.glob(f"{MEMORY_DIR}/*.json"):
        with open(filepath) as f:
            entry = json.load(f)
        ts = datetime.fromisoformat(entry["timestamp"])
        if ts > cutoff:
            results.append(entry)
    return sorted(results, key=lambda x: x["timestamp"], reverse=True)

def cleanup(max_days=180):
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_days)
    deleted = []
    for filepath in glob.glob(f"{MEMORY_DIR}/*.json"):
        with open(filepath) as f:
            entry = json.load(f)
        ts = datetime.fromisoformat(entry["timestamp"])
        if ts < cutoff:
            os.remove(filepath)
            deleted.append(filepath)
    return {"deleted": len(deleted), "files": deleted}

def stats():
    files = glob.glob(f"{MEMORY_DIR}/*.json")
    return {"total_entries": len(files), "storage_dir": MEMORY_DIR}

if __name__ == "__main__":
    result = index("test_001", "HA-0-Jarvis", "Test mémoire", "Mémoire opérationnelle", ["test"], {})
    print(json.dumps(result, indent=2))
    print(json.dumps(stats(), indent=2))
