---
name: memory-optimizer
description: Optimise l'utilisation de la RAM (125GB) et de la VRAM (32GB) pour les modèles LLM et les processus système.
version: 1.0
author: Cédric Maret
toolsets: ["terminal"]
---

# Skill: Memory Optimizer
## Fonctions
- **`check_ram_usage`** : Affiche l'utilisation actuelle de la RAM.
- **`check_vram_usage`** : Affiche l'utilisation actuelle de la VRAM.
- **`kill_process <pid>`** : Tue un processus consommant trop de mémoire.
- **`optimize_ollama`** : Optimise l'utilisation mémoire d'Ollama.
- **`set_swap <size>`** : Configure ou désactive la swap.
- **`clear_cache`** : Libère le cache système.

## Ressources ODIN
- RAM : 125GB DDR4
- VRAM : 2× P100 16GB + P1000 4GB = 36GB total
- Swap : 8GB (désactivable)

## Exemples d'utilisation
- "Vérifie l'utilisation actuelle de la RAM et de la VRAM."
- "Optimise Ollama pour limiter à 2 modèles chargés."
- "Libère le cache système."
