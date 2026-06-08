---
name: hardware-inventory
description: Effectue un inventaire complet et automatique du matériel physique (CPU, GPU, RAM, stockage, réseau, OS). Génère un rapport structuré en Markdown ou JSON.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Hardware Inventory
## Fonctions
- **`full_inventory`** : Génère un inventaire complet de la machine.
- **`quick_inventory`** : Génère un inventaire rapide (résumé).
- **`save_report <format>`** : Sauvegarde le rapport (md ou json).
- **`compare_inventory <file1> <file2>`** : Compare deux inventaires.
- **`update_inventory`** : Met à jour l'inventaire local.

## Stockage inventaires
- ~/.hermes/inventory/ → inventaires horodatés
- /mnt/JARVIS-SSD/inventory/ → archive longue durée

## Exemples d'utilisation
- "Effectue un inventaire complet de cette machine."
- "Génère un inventaire rapide en JSON."
- "Compare l'inventaire actuel avec celui d'hier."
- "Sauvegarde l'inventaire dans /mnt/JARVIS-SSD/inventory/."
