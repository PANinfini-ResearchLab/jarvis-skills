---
name: ha-tool-core
description: Socle d'exécution des outils Hermès IAU. Policy Guard, Logger JSONL, Tool Registry. Valide et journalise chaque appel d'outil.
version: 1.0
author: Cédric Maret / Claudia (Anthropic)
toolsets: ["terminal", "file"]
---

# Skill: HA-TOOL-CORE

## Règle Fondamentale
- SI information accessible via outil → utiliser l'outil
- SI information accessible par raisonnement → raisonner
- JAMAIS inventer un résultat
- TOUJOURS journaliser chaque action

## Composants
- policy_guard.py → valide les appels selon READ/WRITE/SYSTEM/CRITICAL
- logger.py → journalise en JSONL dans /mnt/JARVIS-SSD/logs/
- tool_registry.py → catalogue des outils et leurs classes

## Utilisation
python3 /home/cedric/.hermes/ha-tool-core/policy_guard.py
python3 /home/cedric/.hermes/ha-tool-core/logger.py
python3 /home/cedric/.hermes/ha-tool-core/tool_registry.py
