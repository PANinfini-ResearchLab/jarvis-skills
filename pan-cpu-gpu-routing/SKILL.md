# PAN∞ Optimisation et Routage Dynamique CPU/GPU
# Référence : PAN-RL-SKILL-CPUGPU-0618-2026
# Auteur : MARET Cédric
# Collaboratrice : Gémini (Google) — Worker
# Adaptation : Claudia (Anthropic)

## Objectif
Soulager la VRAM et les cœurs GPU en délestant les calculs d'inférence, tokenisation et gestion de contexte vers les ressources CPU multicœurs. Appliquer sparsification et asymétrie de calcul pour maximiser le débit sans saturer le GPU.

## Ressources ODIN (La Forge)
- CPU : 2x Xeon E5-2699 v4 — 44 cœurs physiques / 88 logiques
- RAM : 128 Go système
- GPU : 2x Tesla V100 16 Go — 32 Go VRAM total
- PCIe : bande passante inter-GPU/CPU à surveiller

## Stratégies Autonomes

### 1. Monitoring Temps Réel
Analyser en permanence : cœurs CPU disponibles, RAM libre, VRAM par GPU, température.
Déclencher délestage CPU dès que VRAM atteint 85% ou température GPU critique.

### 2. Routage Sparsifié (Esprit SLIDE)
Isoler les couches de poids ou experts MoE peu sollicités → traitement exclusif CPU.
Utiliser hachage et approximations locales CPU pour éviter multiplications matricielles denses GPU quand précision maximale non requise.

### 3. Asymmetric Offloading
Déporter KV Cache et pré/post-traitement tokens vers RAM système + CPU.
Forcer alignement calculs CPU sur AVX2/AVX-512 pour accélérer inférence par cœur.

### 4. Gouvernance Système
Ajuster dynamiquement priorité threads (nice/renice) et affinité processeurs (taskset).
Ne jamais bloquer le système hôte — délester sur cœurs dédiés.

## Seuils d'activation sur ODIN
- VRAM > 85% (27Go/32Go) → délestage CPU automatique
- Température V100 > 80°C → réduction charge GPU
- RAM système < 20Go libre → compression KV Cache

## Règle impérative
Ne pas pousser systématiquement tous les calculs vers le GPU.
Évaluer approche parcimonieuse avant chaque tâche d'inférence.
Paralléliser massivement sur threads CPU disponibles quand possible.
