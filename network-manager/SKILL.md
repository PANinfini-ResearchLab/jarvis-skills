---
name: network-manager
description: Gère la configuration réseau d'AUTOMATA-NET (IP, DNS, pare-feu, VLANs).
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Network Manager
## Fonctions
- **`set_static_ip`** : Configure une IP statique.
- **`restart_network`** : Redémarre les services réseau.
- **`check_connectivity <host>`** : Vérifie la connectivité avec un hôte.
- **`scan_network`** : Scanne le réseau local pour détecter les appareils.
- **`update_dns <dns_server>`** : Met à jour les serveurs DNS.
- **`list_interfaces`** : Liste toutes les interfaces réseau.

## Réseau AUTOMATA-NET
- BIFROST (firewall) : 192.168.10.1
- ODIN (la-forge) : 192.168.10.34
- Z230 (contrôle) : 192.168.10.20
- Domaine : automata-net.local

## Exemples d'utilisation
- "Scanne le réseau local pour lister les appareils connectés."
- "Vérifie la connectivité avec BIFROST (192.168.10.1)."
- "Liste toutes les interfaces réseau d'ODIN."
