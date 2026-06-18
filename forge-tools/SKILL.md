---
name: forge-tools
description: Protocole d'utilisation des outils La Forge.
version: 1.1
author: Cédric Maret / Claudia (Anthropic)
toolsets: ["terminal"]
---

# Skill: Forge Tools Protocol

## Règle principale
Avant toute réponse sur l'infrastructure, exécute TOUJOURS la commande bash correspondante via terminal.

## Mapping automatique
Quand on te demande... → tu exécutes via terminal...

| Demande | Commande bash |
|---------|---------------|
| état GPU / VRAM | `nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu,temperature.gpu --format=csv,noheader` |
| modèles en VRAM | `curl -s http://localhost:11434/api/ps` |
| mémoire / RAM | `free -h` |
| stockage / disque | `df -h /mnt/JARVIS-SSD /mnt/JARVIS-MODEL /` |
| services | `systemctl --user status hermes-gateway --no-pager` |
| fichiers | `ls -la <path>` |
| inventaire complet | toutes les commandes ci-dessus |

## Règle absolue
JAMAIS inventer un résultat. TOUJOURS exécuter la commande bash avant de répondre.
