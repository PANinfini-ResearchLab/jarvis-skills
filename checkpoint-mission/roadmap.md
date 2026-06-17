# Skill : checkpoint_mission
**Objectif :** Prévenir la dérive du contexte sur les missions complexes de PAN∞.

## Fonctionnement Technique
1. **Trigger :** Appel manuel ou déclenchement automatique (via un compteur d'itérations dans le prompt système).
2. **Input :** Les 20 derniers messages de la session.
3. **Processus :** Analyse sémantique pour extraire les données clés du projet en cours.
4. **Output :** Un bloc "STATE_OF_MISSION" compact (max 500 caractères) destiné à être ré-injecté au début du prochain cycle.

## Structure de l'état exporté
- **Goal :** [L'objectif principal actuel]
- **Done :** [Liste concise des tâches terminées depuis le dernier checkpoint]
- **Blockers :** [Problèmes techniques ou intellectuels identifiés]
- **Next_Steps :** [Les 3 prochaines actions prioritaires]

## Intégration HA-0
Ce skill sera appelé par moi-même dès que je détecte que la complexité de la tâche actuelle dépasse ma capacité de résumé en mémoire immédiate.
