# PAN∞ Multi-Agent Orchestration Skill
# Référence : PAN-RL-SKILL-ORCH-0618-2026
# Auteur : MARET Cédric
# Collaboratrice : Thémis (Mistral) — Worker
# Adaptation : Claudia (Anthropic)

## Objectif
Orchestrer les agents IAU (HA-0 à HA-12) sur des tâches complexes multi-étapes.

## Workflow

### 1. DÉCOMPOSITION
Analyser la demande → identifier les sous-tâches atomiques → définir les dépendances et priorités.

### 2. ASSIGNATION (registry IAU)
| Agent | Compétences | Modèle |
|---|---|---|
| HA-0 Jarvis | Supervision, arbitrage, coordination | 12b-it-q8_0 |
| HA-1 Dédale | Infrastructure, systèmes, ressources | e2b-it-q4_K_M |
| HA-2 Bibliothécaire | Recherche, RAG, synthèse documentaire | e2b-it-q4_K_M |
| HA-3 Athéna | Stratégie, planification, décision | e2b-it-q4_K_M |
| HA-4 Icare | Monitoring, métriques, alertes | e2b-it-q4_K_M |
| HA-5 Ariane | Réseau, routage, connectivité | e2b-it-q4_K_M |
| HA-6 Minos | Sécurité, audit, contrôle accès | e2b-it-q4_K_M |
| HA-7 Data-A | Analyse, fact-checking, données | e2b-it-q4_K_M |
| HA-8 Homère | Rédaction, synthèse, publication | e2b-it-q4_K_M |
| HA-9 Harmonie-S | Normalisation, formatage, conformité | e2b-it-q4_K_M |
| HA-10 Héphaïstos | HPC, calcul, optimisation GPU | e2b-it-q4_K_M |
| HA-11 Cortana | Code, ingénierie logicielle | e2b-it-q4_K_M |
| HA-12 Tyché | Rentabilité, ressources, prospérité | e2b-it-q4_K_M |

### 3. EXÉCUTION
bibliothecaire chat --yolo -m gemma4:e2b-it-q4_K_M -q "[TÂCHE]" > /tmp/ha2_output.md
athena chat --yolo -m gemma4:e2b-it-q4_K_M -q "[TÂCHE basée sur ha2_output]" > /tmp/ha3_output.md
dedale chat --yolo -m gemma4:e2b-it-q4_K_M -q "[TÂCHE basée sur ha3_output]" > /tmp/ha1_output.md

### 4. AGRÉGATION
HA-0 Jarvis lit les outputs et produit le rapport de cohérence final.

## Règles PAN∞
- Aucun agent n'invente une donnée — tout output cite son input
- Chaque livrable va dans ~/pan_infinity/iau/tests/[NOM_TEST]/
- Rapport de cohérence HA-0 obligatoire en fin de cycle
- Langue : français uniquement

## Exemple — TEST ALPHA-O1 (18/06/2026)
Sujet : RAG pour physique quantique
HA-2 → friction RAG → HA-3 → stratégie hybride → HA-1 → pipeline technique
Résultat : Pipeline Syllogistique 3 couches — SUCCÈS ✅
