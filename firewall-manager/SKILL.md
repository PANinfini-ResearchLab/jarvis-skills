---
name: firewall-manager
description: Gère les règles du pare-feu BIFROST (IPFire) pour le réseau AUTOMATA-NET.
version: 1.0
author: Cédric Maret
toolsets: ["terminal"]
---

# Skill: Firewall Manager
## Fonctions
- **`allow_port <port> <protocol>`** : Autorise un port.
- **`block_port <port> <protocol>`** : Bloque un port.
- **`allow_ip <ip>`** : Autorise une IP.
- **`block_ip <ip>`** : Bloque une IP.
- **`list_rules`** : Liste toutes les règles du pare-feu.
- **`restart_firewall`** : Redémarre le pare-feu.

## Ports critiques ODIN
- 22 → SSH
- 8642 → Hermes Gateway
- 9119 → Hermes Dashboard
- 3000 → Hermes Workspace
- 11434 → Ollama (localhost uniquement)

## Réseau AUTOMATA-NET
- BIFROST : 192.168.10.1
- Plage autorisée : 192.168.10.0/24

## Exemples d'utilisation
- "Autorise le port 8642 en TCP pour Hermes Gateway."
- "Bloque toute IP hors 192.168.10.0/24."
- "Liste toutes les règles du pare-feu."
