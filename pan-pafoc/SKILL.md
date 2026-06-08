# SKILL : PAFOC
**Brief Chirurgical pour IA Codante — PAN∞ Research Lab**
**Réf. :** PAN-RL-434D-INF-0326-0001 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
PAFOC est un protocole de brief chirurgical destiné à guider une IA codante sur des
correctifs précis, sans lui soumettre l'intégralité du code source.
Principe fondateur : On explique. On propose. On attend le retour.

## QUAND CHARGER CETTE SKILL
- Pour créer un brief de correction avant de soumettre à une IA codante
- Pour guider Hermès sur un correctif précis sans exposer tout le code
- Pour consulter le tableau de suivi avant une intervention
- Pour documenter et tracer une décision de correction
- Toujours AVANT de charger SENTINEL (PAFOC définit ce qui doit être protégé)

## LA MÉTHODE PAFOC
P = PROBE    — Sonder le code. Localiser le point exact. Pas de conjecture.
A = ANALYST  — Décrire le comportement actuel. Une phrase. Nommer le problème.
F = FOCAL    — Un correctif = une entrée. Pas de refactoring global.
O = OUVERTURE — Proposer une direction, laisser l'IA interpréter.
C = CARET    — Insérer, tracer, valider. Chaque entrée = documentation permanente.

## RÈGLES D'UTILISATION
Fichier             = nom exact (ex : message.rs, config.py)
Ligne               = numéro exact ou plage (ex : 142 ou 142-156). Pas de zone vague.
Comportement actuel = une phrase. Ce qui se passe et pourquoi c'est un problème.
Correction proposée = direction claire : pseudo-code, intention nommée, contrainte.
Résultat attendu    = comportement après correction, formulé de manière testable.
Retour              = rempli par l'IA ou l'auteur après test.

## STATUTS
⬜ À traiter  = aucune action tentée
🔄 En cours   = l'IA travaille, ou correction partielle appliquée
✅ Validé     = correction appliquée, testée, acceptée. Entrée close.
❌ Rejeté     = correction tentée mais non retenue. Motif à renseigner.
⚠  Effet de bord = correction appliquée, comportement inattendu. À investiguer.

## TABLEAU DE SUIVI
**Projet :** _______ · **Version :** _______ · **Ouverture :** _______

| # | Fichier | Ligne | Comportement actuel | Correction proposée | Résultat attendu | Retour |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 001 | | | | | | ⬜ |
| 002 | | | | | | ⬜ |
| 003 | | | | | | ⬜ |
| 004 | | | | | | ⬜ |
| 005 | | | | | | ⬜ |

## WORKFLOW PAFOC → SENTINEL → BOÎTE NOIRE
1. PAFOC : créer une entrée (fichier + ligne + problème)
2. SENTINEL : backup du fichier ciblé (niveau 1 minimum)
3. Soumettre l'entrée PAFOC à l'IA codante
4. L'IA exécute la correction
5. Tester et observer
6. Mettre à jour le statut PAFOC
7. Boîte Noire : entrée FIX ou ERR selon résultat

## POURQUOI PAFOC
Sans PAFOC : l'IA reçoit le fichier entier, cherche elle-même, coûteux en tokens, risque de régression.
Avec PAFOC : intervention chirurgicale, économe, précis, traçable, documenté automatiquement.

*PAFOC v1.0 — PAN∞ Research Lab — CC BY-SA 4.0 — Réf. PAN-RL-434D-INF-0326-0001*
