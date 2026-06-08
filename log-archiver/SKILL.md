---
name: log-archiver
description: Archive et compresse les logs système et applicatifs pour économiser de l'espace.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Log Archiver
## Fonctions
- **`archive_logs <days>`** : Archive les logs de plus de N jours.
- **`compress_logs <path>`** : Compresse les logs dans un dossier.
- **`delete_old_archives <days>`** : Supprime les archives de plus de N jours.
- **`list_archives`** : Liste toutes les archives de logs.
- **`restore_archive <archive>`** : Restaure une archive spécifique.

## Répertoires de logs ODIN
- /var/log/ → logs système
- ~/.hermes/logs/ → logs Hermes
- /mnt/JARVIS-SSD/logs/ → logs archivés

## Planification recommandée
- Archivage hebdomadaire (cron dimanche 2h00)
- Suppression archives > 90 jours

## Exemples d'utilisation
- "Archive les logs de plus de 30 jours."
- "Compresse les logs dans /var/log/."
- "Supprime les archives de logs de plus de 90 jours."
- "Liste toutes les archives disponibles."
