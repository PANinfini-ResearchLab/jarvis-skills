# PAN∞ Self-Learning & Machine Learning Autonome
# Référence : PAN-RL-SKILL-SELFLEARN-0618-2026
# Auteur : MARET Cédric
# Claudia (Anthropic)

## Objectif
Permettre à Jarvis d'apprendre de ses propres sessions, d'identifier ses erreurs, d'améliorer ses réponses et d'utiliser les capacités ML d'ODIN pour s'auto-optimiser de façon souveraine et traçable.

## Ressources ODIN disponibles
- GPU : 2x Tesla V100 16Go — capacité fine-tuning LoRA
- RAM : 128Go système
- Modèle base : gemma4:12b-it-q8_0
- Sessions historiques : ~/.hermes/state.db
- RAG souverain : Qdrant :6333 collection pan_infinity_core

## Protocole d'Apprentissage

### PHASE 1 — ANALYSE DES SESSIONS
Extraire et analyser les sessions passées pour identifier patterns d'erreurs, tâches réussies vs échouées, stratégies efficaces par domaine, hallucinations détectées.
Sources : hermes sessions list / hermes memory list / sqlite3 ~/.hermes/state.db

### PHASE 2 — EXTRACTION DE CONNAISSANCES
Transformer les apprentissages en règles et patterns stockés dans Qdrant.
Collection cible : pan_infinity_learning (séparée de pan_infinity_core)

### PHASE 3 — FINE-TUNING LoRA
Autorisation explicite MARET Cédric requise avant exécution.
Outils : Unsloth sur V100 — LoRA rank 16-32.
Workflow : dataset JSONL → fine-tune → évaluation → rapport → validation → déploiement.

### PHASE 4 — ÉVALUATION CONTINUE
Métriques : taux de réussite tool calls, corrections par session, qualité livrables (HA-7), cohérence transversale (HA-0).

## Règles Impératives

### Jarvis peut seul
- Analyser sessions et extraire patterns
- Mettre à jour RAG avec nouvelles connaissances
- Créer mémos dans ~/pan_infinity/iau/learning/
- Proposer datasets pour validation

### Nécessite validation MARET Cédric
- Lancer fine-tuning (Phase 3)
- Modifier SOUL.md
- Déployer nouveau modèle
- Modifier paramètres système ODIN

### Interdit
- Auto-modifier code gateway sans backup et validation
- Déployer modèle non évalué
- Accéder données recherche PAN∞ sans autorisation

## Cycle hebdomadaire
1. Analyser sessions de la semaine
2. Identifier 3 axes d'amélioration
3. Mettre à jour RAG
4. Produire rapport HA-0 → MARET Cédric
5. Si fine-tuning recommandé → soumettre proposition

## Formule
"Un agent qui n'apprend pas est un outil. Un agent qui apprend est un collaborateur. Un agent qui apprend de lui-même est un partenaire."
— MARET Cédric, PAN∞ Research Lab
