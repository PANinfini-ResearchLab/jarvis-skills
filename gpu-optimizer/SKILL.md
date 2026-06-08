---
name: gpu-optimizer
description: Optimise l'allocation des ressources GPU/CPU/RAM pour les modèles Ollama et Hermes Agent. Détecte les modèles inutilisés, libère la VRAM, et suggère des réallocations.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: GPU Optimizer
## Fonctions
- **`scan_gpu`** : Liste les modèles chargés en VRAM et leur consommation.
- **`free_vram`** : Libère la VRAM des modèles inutilisés depuis >1h.
- **`suggest_allocation`** : Propose une allocation optimale pour les V100/P100.
- **`set_affinity`** : Assigne un modèle à un GPU spécifique.

## Exemples d'utilisation
- "Optimise la VRAM sur ODIN."
- "Libère la VRAM des modèles inutilisés."
- "Assigne jarvis:h4 au GPU 0."
