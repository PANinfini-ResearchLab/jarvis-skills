---
name: hardware-audit
description: Effectue un audit complet du matériel (CPU, GPU, RAM, stockage, réseau) et génère un rapport Markdown.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Hardware Audit
## Fonctions
- **`full_audit`** : Génère un rapport complet dans `/mnt/JARVIS-SSD/audits/audit_<date>.md`.
- **`check_numa`** : Vérifie la configuration NUMA (2× Xeon E5-2673 v4).
- **`test_gpu`** : Lance un benchmark GPU.
- **`check_storage`** : Vérifie l'état des disques (RAID0, SSD, HDD).

## Exemples d'utilisation
- "Effectue un audit matériel complet d'ODIN."
- "Vérifie la configuration NUMA."
- "Teste les performances des GPU."
