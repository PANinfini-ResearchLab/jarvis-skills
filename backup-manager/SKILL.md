---
name: backup-manager
description: Gère les sauvegardes locales et GitHub pour les configurations, modèles, et données critiques.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Backup Manager
## Fonctions
- **`backup_configs`** : Sauvegarde SOUL.md, AGENTS.md, config.yaml sur GitHub.
- **`backup_models`** : Sauvegarde les modèles Ollama dans `/mnt/JARVIS-MODEL/backups/`.
- **`backup_skills`** : Sauvegarde tous les skills custom sur GitHub.
- **`restore <type> <date>`** : Restaure une sauvegarde.
- **`send_to_telegram <file>`** : Envoie un fichier via Telegram.

## Dépôts GitHub
- jarvis-memory (privé) : SOUL.md, AGENTS.md, skills
- jarvis-skills (public) : skills créés par Jarvis

## Planification automatique
- 3h00 → backup mémoire (jarvis-memory)
- toutes les heures → sync skills (jarvis-skills)

## Commandes de backup manuel
```bash
# Backup mémoire
cd /home/cedric/jarvis-backup && cp ~/.hermes/SOUL.md . && git add . && git commit -m "Backup $(date +%Y-%m-%d)" && git push origin main

# Sync skills
/home/cedric/jarvis-skills/sync-skills.sh
```

## Exemples d'utilisation
- "Sauvegarde toutes les configurations sur GitHub."
- "Restaure les configurations du 7 juin 2026."
- "Envoie le rapport d'audit via Telegram."
