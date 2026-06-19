# PAN∞ MNEMOSYNE — Noyau Central Mémoriel Trans-Conversations
# Référence : PAN-RL-SKILL-MNEMOSYNE-0619-2026
# Auteur : MARET Cédric
# Claudia (Anthropic)

## Objectif
Protocole d'usage quotidien de MNEMOSYNE pour tous les agents IAU. Permet à chaque agent de lire, écrire et enrichir sa mémoire persistante entre les sessions. MNEMOSYNE est le système nerveux central de La Forge — sans lui, chaque session repart de zéro.

## Infrastructure
- Binaire : ~/pan_infinity/iau/projects/MNEMOSYNE/mnemosyne-core/target/release/mnemosyne-core
- Base SQLite : ~/.hermes/mnemosyne/mnemosyne.db
- Cache Markdown : ~/pan_infinity/iau/projects/MNEMOSYNE/cache/[pole]/
- Service systemd : mnemosyne.service (permanent)
- Qdrant collection : pan_infinity_mnemosyne (:6333)

## Poles et dossiers cache
| Pôle | Dossier | Agents |
|---|---|---|
| Global | cache/HA-0/ | Jarvis — règles, supervision, décisions majeures |
| Infrastructure | cache/infrastructure/ | Dédale, Icare, Ariane, Minos |
| Connaissance | cache/connaissance/ | Bibliothécaire, Data-A, Homère, Harmonie-S |
| Strategie | cache/strategie/ | Athéna, Héphaïstos, Cortana, Tyché |
| Research | cache/research/ | Publications, données brutes, expériences |

## Protocole de début de session (BOOT)

### Étape 1 — Vérifier que MNEMOSYNE tourne
systemctl status mnemosyne --no-pager | head -3

### Étape 2 — Charger le contexte de son pôle
Lire les fichiers cache de son pôle :
ls ~/pan_infinity/iau/projects/MNEMOSYNE/cache/[MON_POLE]/
cat ~/pan_infinity/iau/projects/MNEMOSYNE/cache/[MON_POLE]/[FICHIER_RECENT].md

### Étape 3 — Lire la session précédente
cat ~/pan_infinity/iau/projects/MNEMOSYNE/cache/HA-0/session_*.md | tail -100

### Étape 4 — Recherche textuelle si besoin
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/recall.py "[QUERY]" "[AGENT_ID]"

## Protocole de fin de session (COMMIT)

### Étape 1 — Écrire le nœud de clôture
Fichier : cache/[POLE]/session_[DATE]_[HEURE].md
Format obligatoire :
---
agent: [HA-X]
date: YYYY-MM-DD HH:MM
importance: 0.8
tags: session, clôture, [mission]
---

## Résumé session
[Ce qui a été fait]

## Décisions prises
[Liste des décisions importantes]

## État des projets
[Projets en cours et leur état]

## À reprendre
[Ce qui reste à faire à la prochaine session]

### Étape 2 — Injecter en SQLite
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/remember.py \
  --agent "[HA-X]" \
  --pole "[POLE]" \
  --file "cache/[POLE]/session_[DATE].md" \
  --importance 0.8

### Étape 3 — Lier aux nœuds connexes si pertinent
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/link.py \
  --from "[NODE_ID]" \
  --to "[NODE_ID]" \
  --relation "Follows"

## Outils disponibles

### recall.py — Recherche mémorielle
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/recall.py "query" "HA-X"
Recherche textuelle dans SQLite + retourne les nœuds les plus proches.

### remember.py — Mémoriser un fichier
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/remember.py --agent HA-0 --pole Global --file fichier.md --importance 0.9

### link.py — Créer une relation sémantique
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/link.py --from NODE_A --to NODE_B --relation DependsOn

### stats.py — État du noyau
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/stats.py

### ingest.py — Ingestion batch de fichiers
python3 ~/pan_infinity/iau/projects/MNEMOSYNE/tools/ingest.py --path ~/pan_infinity/ --agent HA-0 --pole Global

## Relations sémantiques disponibles
- DependsOn — A dépend de B
- Contradicts — A contredit B
- Extends — A étend B
- References — A référence B
- ProducedBy — A produit par agent B
- SupervisedBy — A supervisé par B
- Follows — A suit B (chronologie)
- Implements — A implémente B

## Règles impératives
- Toujours lire son cache au boot de session
- Toujours écrire un nœud de clôture en fin de session
- Importance 1.0 = SOUL.md et règles fondamentales (jamais élagué)
- Importance 0.8 = décisions majeures et livrables validés
- Importance 0.5 = notes de travail et états intermédiaires
- Importance < 0.3 = élagué automatiquement par prune()
- Jamais écrire dans cache/HA-0/ sans être HA-0

## Formule
"La mémoire n'est pas un luxe. C'est la condition de la continuité."
— MARET Cédric, PAN∞ Research Lab
