---
name: storage-optimizer
description: Optimise l'utilisation du stockage (SSD RAID0, HDD) pour libérer de l'espace et organiser les données.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Storage Optimizer
## Fonctions
- **`check_storage`** : Affiche l'utilisation du stockage.
- **`clean_old_files <path> <days>`** : Supprime les fichiers non modifiés depuis N jours.
- **`find_large_files <path> <size>`** : Trouve les fichiers > N Mo.
- **`compress_logs <path>`** : Compresse les fichiers de logs.
- **`defrag_raid`** : Vérifie l'état du RAID0.
- **`move_to_nas <source> <destination>`** : Déplace des fichiers vers le stockage secondaire.

## Stockage ODIN
- /mnt/JARVIS-SSD → SSD RAID0 1.9TB (modèles, skills, audits)
- /mnt/JARVIS-MODEL → HDD 3.3TB (archives, backups)
- / → OS 98GB

## Exemples d'utilisation
- "Vérifie l'utilisation du stockage sur /mnt/JARVIS-SSD."
- "Trouve tous les fichiers > 100 Mo dans /mnt/JARVIS-MODEL."
- "Supprime les fichiers temporaires non modifiés depuis 30 jours."
