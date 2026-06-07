---
name: ollama-manager
description: Gère les modèles Ollama (pull, rm, list, backup, restore). Optimise l'espace disque et la VRAM.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Ollama Manager
## Fonctions
- **`pull <model>`** : Télécharge un modèle.
- **`remove <model>`** : Supprime un modèle.
- **`list`** : Liste tous les modèles locaux.
- **`backup`** : Sauvegarde les modèles dans `/mnt/JARVIS-MODEL/backups/`.
- **`restore <model>`** : Restaure un modèle depuis une sauvegarde.
- **`clean`** : Supprime les modèles non utilisés depuis >7 jours.

## Modèles actifs sur ODIN
- jarvis:h4 → Modèle principal (9GB)
- jarvis:h4-q5 → Backup (10GB)
- jarvis:h3-8b → Sous-agents légers (4.9GB)
- qwen3.5:2b → Bot léger P1000 (2.7GB)

## Stockage modèles
- Principal : /mnt/JARVIS-SSD/ollama
- Archive : /mnt/JARVIS-MODEL

## Exemples d'utilisation
- "Liste tous les modèles Ollama disponibles."
- "Supprime les modèles non utilisés depuis 1 semaine."
- "Sauvegarde tous les modèles Ollama."
- "Télécharge Hermes-4-32B-Q4_K_M."
