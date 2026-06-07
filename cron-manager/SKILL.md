---
name: cron-manager
description: Gère les tâches cron pour automatiser les sauvegardes, audits, et optimisations.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Cron Manager
## Fonctions
- **`add_job <name> <command> <schedule>`** : Ajoute une tâche cron.
- **`remove_job <name>`** : Supprime une tâche cron.
- **`list_jobs`** : Liste toutes les tâches cron.
- **`enable_job <name>`** : Active une tâche cron.
- **`disable_job <name>`** : Désactive une tâche cron.

## Tâches cron actives sur ODIN
- @reboot → Chargement Jarvis en VRAM
- 0 3 * * * → Backup mémoire GitHub (jarvis-memory)
- 0 * * * * → Sync skills GitHub (jarvis-skills)

## Exemples d'utilisation
- "Liste toutes les tâches cron actuelles."
- "Ajoute une tâche cron pour auditer le matériel tous les lundis à 4h00."
- "Supprime la tâche backup_hermes."
