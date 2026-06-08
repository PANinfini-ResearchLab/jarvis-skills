#!/usr/bin/env python3
import json

REGISTRY = {
    "nvidia-smi":   {"class": "SYSTEM",   "autonomy": "auto_safe", "description": "Infos GPU NVIDIA"},
    "free":         {"class": "READ",     "autonomy": "auto",      "description": "Utilisation RAM"},
    "df":           {"class": "READ",     "autonomy": "auto",      "description": "Utilisation disques"},
    "lscpu":        {"class": "READ",     "autonomy": "auto",      "description": "Infos CPU"},
    "ip":           {"class": "READ",     "autonomy": "auto",      "description": "Infos réseau"},
    "cat":          {"class": "READ",     "autonomy": "auto",      "description": "Lecture fichier"},
    "ls":           {"class": "READ",     "autonomy": "auto",      "description": "Liste fichiers"},
    "write_file":   {"class": "WRITE",    "autonomy": "auto_safe", "description": "Écriture fichier"},
    "git":          {"class": "WRITE",    "autonomy": "auto_safe", "description": "Opérations Git"},
    "systemctl":    {"class": "SYSTEM",   "autonomy": "auto_safe", "description": "Gestion services"},
    "ollama":       {"class": "SYSTEM",   "autonomy": "auto_safe", "description": "Gestion modèles"},
    "rm -rf":       {"class": "CRITICAL", "autonomy": "locked",    "description": "Suppression récursive"},
    "ufw":          {"class": "CRITICAL", "autonomy": "locked",    "description": "Modification firewall"},
}

def get_tool(tool_name):
    return REGISTRY.get(tool_name, {"class": "UNKNOWN", "autonomy": "locked", "description": "Outil inconnu"})

def list_tools():
    return REGISTRY

if __name__ == "__main__":
    print(json.dumps(REGISTRY, indent=2))
