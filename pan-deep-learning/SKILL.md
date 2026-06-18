# PAN∞ Deep Learning Autonome
# Référence : PAN-RL-SKILL-DEEPLEARN-0618-2026
# Auteur : MARET Cédric
# Claudia (Anthropic)

## Objectif
Permettre à Jarvis de concevoir, entraîner et évaluer des architectures de deep learning souveraines sur ODIN, au service des projets de recherche PAN∞. Jarvis opère comme chef de projet ML — il propose, documente, soumet à validation, puis exécute.

## Ressources ODIN disponibles
- GPU : 2x Tesla V100 16Go (CUDA 11.x) — entraînement distribué possible
- RAM : 128Go système — large batch sizes possibles en CPU offloading
- Stockage modèles : /mnt/JARVIS-MODEL/
- Frameworks disponibles : PyTorch, CUDA, Unsloth
- Données : ~/pan_infinity/data_research/processed/ (publications PAN∞)

## Domaines autorisés

### Priorité 1 — Recherche PAN∞
- Modèles de physique computationnelle (AION-LUMASS)
- Réseaux de neurones pour résolution d'équations (opérateur ⁵✦)
- Embeddings spécialisés pour corpus scientifique PAN∞
- Modèles de classification épistémique

### Priorité 2 — Infrastructure IAU
- Fine-tuning des agents HA-x sur leurs domaines spécifiques
- Distillation de connaissances entre modèles Gemma4
- Compression de modèles pour optimisation VRAM
- Benchmarking comparatif des quantizations

### Priorité 3 — Expérimentation
- Architectures hybrides symbolique/connexionniste
- RAG graphique-symbolique (cf. TEST ALPHA-O1)
- Modèles multimodaux pour données de recherche

## Protocole d'Exécution

### PHASE 1 — CONCEPTION
Définir l'architecture, les données, les métriques de succès.
Documenter dans ~/pan_infinity/iau/deeplearning/[NOM_PROJET]/design.md
Format obligatoire :
- Objectif scientifique
- Architecture proposée
- Dataset et preprocessing
- Métriques d'évaluation
- Budget VRAM estimé
- Durée estimée

### PHASE 2 — VALIDATION (MARET Cédric)
Soumettre le design doc pour validation avant tout entraînement.
Aucun GPU-hour dépensé sans feu vert explicite.

### PHASE 3 — ENTRAÎNEMENT
Environnement isolé : ~/pan_infinity/venv_dl/
Logs en temps réel : ~/pan_infinity/iau/deeplearning/[NOM_PROJET]/logs/
Checkpoints : /mnt/JARVIS-MODEL/checkpoints/[NOM_PROJET]/
Monitoring GPU obligatoire via nvidia-smi pendant l'entraînement.

### PHASE 4 — ÉVALUATION
Benchmarker le modèle entraîné vs baseline.
Rapport d'évaluation soumis à MARET Cédric avant déploiement.
Validation croisée par HA-7 Data-A obligatoire.

### PHASE 5 — DÉPLOIEMENT
Uniquement après double validation (Jarvis + MARET Cédric).
Déploiement dans Ollama ou via API directe selon cas d'usage.
Documentation complète dans le RAG souverain.

## Stack Technique ODIN

### Installation de base
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --break-system-packages
pip install transformers datasets accelerate bitsandbytes --break-system-packages
pip install unsloth wandb --break-system-packages

### Entraînement distribué (2x V100)
export CUDA_VISIBLE_DEVICES=0,1
torchrun --nproc_per_node=2 train.py

### Monitoring GPU pendant entraînement
watch -n 5 nvidia-smi

## Règles Impératives

### Ce que Jarvis peut faire seul
- Concevoir des architectures et rédiger les design docs
- Préparer les datasets et scripts d'entraînement
- Lancer des expériences courtes (< 1h) de validation
- Analyser et documenter les résultats

### Ce qui nécessite validation de MARET Cédric
- Entraînements longs (> 1h GPU)
- Fine-tuning de modèles de production
- Déploiement de nouveaux modèles
- Modification des modèles Gemma4 en production

### Ce qui est interdit
- Entraîner sur des données non validées
- Déployer sans évaluation complète
- Utiliser les V100 pour des tâches non liées à PAN∞
- Télécharger des modèles externes sans validation

## Formule
"Le deep learning sans rigueur épistémique est de la sorcellerie. Avec elle, c'est de la science."
— MARET Cédric, PAN∞ Research Lab
