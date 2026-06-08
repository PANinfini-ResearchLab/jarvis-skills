---
name: network-diagnostics
description: Diagnostique le réseau AUTOMATA-NET (ping, traceroute, ports ouverts, débit).
version: 1.0
author: Cédric Maret
toolsets: ["terminal"]
---

# Skill: Network Diagnostics
## Fonctions
- **`ping <host>`** : Teste la connectivité avec un hôte.
- **`traceroute <host>`** : Trace la route vers un hôte.
- **`scan_ports <host>`** : Scanne les ports ouverts sur un hôte.
- **`test_speed`** : Teste le débit entre ODIN et BIFROST.
- **`check_firewall`** : Vérifie les règles du firewall BIFROST.

## Nœuds AUTOMATA-NET
- BIFROST (firewall) : 192.168.10.1
- ODIN (la-forge) : 192.168.10.34
- Z230 (contrôle) : 192.168.10.20
- Domaine : automata-net.local

## Ports critiques ODIN
- 11434 → Ollama
- 8642 → Hermes Gateway
- 9119 → Hermes Dashboard
- 3000 → Hermes Workspace

## Exemples d'utilisation
- "Ping BIFROST (192.168.10.1)."
- "Scanne les ports ouverts sur Z230."
- "Teste la vitesse du réseau entre ODIN et BIFROST."
- "Vérifie que tous les ports critiques sont ouverts."
