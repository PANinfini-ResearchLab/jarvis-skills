# SKILL : SENTINEL
**Protocole de Backup Opératoire — PAN∞ Research Lab**
**Réf. :** PAN-RL-434D-INF-0526-0001 · v0.3 · CC BY-SA 4.0

## DESCRIPTION
SENTINEL est le protocole de protection physique des fichiers avant toute intervention.
Aucune modification, suppression, refactorisation ou action d'IA codante sans backup préalable confirmé.

Formule : PAFOC demande. SENTINEL copie et hash. Action modifie. Test vérifie. Boîte Noire raconte. LOCK fige.

## QUAND CHARGER CETTE SKILL
- Avant toute modification d'un fichier de code ou de configuration
- Avant toute suppression, renommage, déplacement
- Avant toute refactorisation ou remplacement de bloc
- Avant toute intervention d'une IA codante (Hermès, Claude Code, script)
- Pour restaurer un fichier depuis un backup
- Pour poser ou vérifier un verrou multi-agents

## ARBORESCENCE
_backup/
├── pre-action/
│   └── meta/
├── zone-snapshots/
├── locks/
└── manifests/
    └── sentinel-journal.md

## NIVEAUX
| Niveau | Scope | Déclencheur |
|--------|-------|-------------|
| 1 — Ciblé | fichier unique | toute modification mineure |
| 2 — Zone | sous-dossier complet | refacto, remaniement large |
| 3 — LOCK | projet complet | version stable, fin de session |

## NOMMAGE
AAAA-MM-JJ_HHMMSS__AGENT__REF__NOM-ELEMENT
Agents : HUM / CLAUDIA / SELENE / MARGAUX / CC / HERMES / SCR
Exemples :
2026-05-18_0042__HUM__PAFOC-003__main.py
2026-05-18_0115__CC__BN-0012__config.json
2026-05-18_0200__HUM__LOCK-BN-0024__projet_v0.3

## HASH SHA256 — OBLIGATOIRE
sha256sum fichier.py
Get-FileHash .\fichier.py -Algorithm SHA256
Pour dossier : zipper d'abord, hasher le ZIP.

## MANIFEST NIVEAU 1
DATE            | AGENT | REF       | ÉLÉMENT      | HASH SHA256
----------------|-------|-----------|--------------|-------------
2026-05-18_0042 | HUM   | PAFOC-003 | src/main.py  | a3f5c8...

## MANIFEST NIVEAUX 2 ET 3
Date           :
Projet         :
Déclencheur    :
Type           : [Ciblé / Zone / LOCK]
Agent          :
Élément copié  :
Destination    :
Motif          :
Action prévue  :
Hash SHA256    :
Lien Boîte Noire :
Statut         : Backup créé — action non encore exécutée

## VERROU MULTI-AGENTS
ELEMENT.LOCK__AGENT__REF
ex : main.py.LOCK__CC__PAFOC-007
Le premier agent qui backupe pose le verrou. Les autres attendent (BN type WAIT).

## WORKFLOW
1.  PAFOC identifie une intervention
2.  Vérifier absence de verrou sur l'élément cible
3.  Backup pré-action (niveau 1 / 2 / 3 selon scope)
4.  Hash SHA256 → consigné dans journal ou manifest
5.  Pose du verrou si contexte multi-agents
6.  Exécution de l'action
7.  Test ou observation
8.  Suppression du verrou
9.  Mise à jour PAFOC
10. Entrée Boîte Noire
11. Si stable → LOCK + snapshot niveau 3

## RÈGLE D'ÉCHEC
Si le backup échoue → action BLOQUÉE.
1. Entrée Boîte Noire type ERR
2. NE PAS exécuter l'action
3. Corriger la cause, refaire le backup, reprendre.

## RESTAURATION
1. Lire la Boîte Noire — identifier l'entrée concernée
2. Trouver le manifest dans _backup/manifests/
3. Vérifier le hash SHA256
4. Si hash OK → copier l'ancien fichier à sa place
5. Si hash KO → chercher un backup antérieur ou un LOCK
6. Entrée ROLL dans la Boîte Noire

## RÉTENTION
pre-action   → 30 jours min, jusqu'au prochain LOCK
zone-snap    → jusqu'au LOCK suivant, min 2 LOCKs
locks/       → jamais purgé automatiquement
manifests/   → jamais purgés
Toute purge → entrée BN type PURGE.

## RÈGLES
R1  Aucune modification sans backup pré-action confirmé.
R2  On copie avant — jamais seulement après.
R3  Micro-action = fichier / Remaniement = dossier / LOCK = projet complet.
R4  Chaque backup est relié à une cause : PAFOC, BN, LOCK ou action manuelle.
R5  Un LOCK sans snapshot complet SENTINEL est incomplet.
R6  Un backup uniquement sur disque principal n'est pas une archive de survie.
R7  Le backup est lisible dans l'explorateur, sans outil spécialisé.
R8  Tout fichier sauvegardé a un hash SHA256 consigné dans son manifest.
R9  L'action est bloquée si le backup échoue.
R10 _backup/ ne peut être purgé que par décision humaine explicite.
R11 PAFOC.md et Boîte Noire sont les premiers fichiers à backuper.
R12 Tout agent s'identifie dans le manifest et dans le nommage.

*SENTINEL v0.3 — PAN∞ Research Lab — CC BY-SA 4.0 — Réf. PAN-RL-434D-INF-0526-0001*
