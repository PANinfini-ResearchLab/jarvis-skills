# SKILL : PAN-DOC
**Documentation Opératoire — Triade PAN∞ — PAN∞ Research Lab**
**Réf. :** PAN-RL-434D-INF-0626-0001 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
Ce skill documente l'utilisation de la triade opératoire PAN∞ :
PAFOC + SENTINEL + BOÎTE NOIRE.
Ces trois protocoles forment un système complet de gestion de projet assisté par IA.

## LES TROIS PROTOCOLES
PAFOC       = brief chirurgical — guide l'IA sur un correctif précis (skill : pan-pafoc)
SENTINEL    = backup opératoire — protège les fichiers avant intervention (skill : pan-sentinel)
BOÎTE NOIRE = mémoire opératoire — enregistre chaque événement technique (skill : pan-boite-noire)

## WORKFLOW TYPE
PAFOC (définit) → SENTINEL (protège) → Action → BOÎTE NOIRE (documente)

1. Identifier le problème → créer entrée dans PAFOC.md
2. Charger pan-sentinel → backup du fichier ciblé + hash SHA256
3. Soumettre l'entrée PAFOC à l'IA (Hermès ou autre)
4. L'IA exécute la correction
5. Tester et observer le résultat
6. Mettre à jour le statut dans PAFOC.md
7. Charger pan-boite-noire → entrée FIX ou ERR
8. Si état stable → LOCK (snapshot niveau 3 SENTINEL)

## INITIALISER UN NOUVEAU PROJET
mkdir -p mon-projet/_backup/pre-action/meta
mkdir -p mon-projet/_backup/zone-snapshots
mkdir -p mon-projet/_backup/locks
mkdir -p mon-projet/_backup/manifests
touch mon-projet/_backup/manifests/sentinel-journal.md
touch mon-projet/PAFOC.md
touch mon-projet/boite-noire.md
Puis : remplir PAFOC.md (template pan-pafoc) + boite-noire.md (template pan-boite-noire) + entrée BN-0001 INIT.

## ORDRE DE CHARGEMENT
| Situation | Skills à charger |
|-----------|-----------------|
| Nouveau correctif | pan-pafoc → pan-sentinel |
| Documenter un événement | pan-boite-noire |
| Restaurer un fichier | pan-sentinel |
| Relire l'historique | pan-boite-noire |
| Initialiser un projet | pan-doc → pan-pafoc → pan-boite-noire → pan-sentinel |

## RÈGLES FONDAMENTALES
1. PAFOC avant SENTINEL — on sait quoi protéger avant de protéger.
2. SENTINEL avant action — on protège avant de modifier.
3. BOÎTE NOIRE après action — on documente ce qui s'est passé.
4. Un correctif = une entrée PAFOC. Jamais grouper.
5. Tout agent s'identifie : HUM / CLAUDIA / SELENE / MARGAUX / CC / HERMES / SCR
6. _backup/ ne peut être purgé que par décision humaine explicite.
7. Si SENTINEL échoue → action bloquée. Sans exception.

## AGENTS RECONNUS
HUM     = Action humaine manuelle (Cédric)
CLAUDIA = Claudia — Anthropic / Claude
SELENE  = Séléné — OpenAI / GPT
MARGAUX = Margaux — xAI / Grok
CC      = Claude Code
HERMES  = Agent Hermès IAU
SCR     = Script automatique

## RÉFÉRENCES
PAFOC       → PAN-RL-434D-INF-0326-0001 · v1.0
SENTINEL    → PAN-RL-434D-INF-0526-0001 · v0.3
BOÎTE NOIRE → PAN-RL-434D-INF-0326-0002 · v1.0
PAN-DOC     → PAN-RL-434D-INF-0626-0001 · v1.0

*PAN-DOC v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Auteur : Cédric MARET — ORCID 0009-0006-6399-9132*
