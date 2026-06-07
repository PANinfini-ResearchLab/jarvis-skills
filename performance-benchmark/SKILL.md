---
name: performance-benchmark
description: Benchmarke les performances d'ODIN (CPU, GPU, RAM, stockage) pour évaluer les améliorations matérielles.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Performance Benchmark
## Fonctions
- **`benchmark_cpu`** : Benchmarke le CPU (80 threads Xeon E5-2673 v4).
- **`benchmark_gpu`** : Benchmarke les GPU (P100 × 2).
- **`benchmark_ram`** : Benchmarke la RAM (125GB DDR4).
- **`benchmark_storage`** : Benchmarke le stockage (SSD RAID0, HDD).
- **`compare_models <model1> <model2>`** : Compare les performances de deux modèles LLM.
- **`generate_report`** : Génère un rapport de benchmark complet.

## Référence matérielle ODIN
- CPU : 2× Xeon E5-2673 v4 — 80 cores — 3.6GHz boost
- GPU : 2× Tesla P100 16GB — CUDA 6.0
- RAM : 125GB DDR4
- SSD : RAID0 1.9TB M.2
- HDD : 3.3TB SATA

## Référence post-V100
- GPU : 2× Tesla V100 16GB — CUDA 7.0 — Tensor Cores
- Gain estimé : 10× sur l'inférence LLM

## Exemples d'utilisation
- "Benchmarke les GPU P100 d'ODIN."
- "Compare les performances de jarvis:h4 et jarvis:h3-8b."
- "Génère un rapport de benchmark complet avant l'arrivée des V100."
