# SKILL : BOÎTE NOIRE
**Journal Technique de Mémoire Opératoire — PAN∞ Research Lab**
**Réf. :** PAN-RL-434D-INF-0326-0002 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
La Boîte Noire est la mémoire opératoire d'un projet. Elle enregistre chaque événement
technique identifiable, de l'initialisation à la fermeture.
Objectif : permettre à un humain ou à une IA de comprendre ce qui s'est passé sans relire l'intégralité du code.

## QUAND CHARGER CETTE SKILL
- Pour enregistrer un événement technique
- Avant toute intervention : lire les 5 dernières entrées et l'état actuel
- Pour consulter l'historique d'une zone ou d'un fichier
- Pour documenter une décision d'architecture ou un effet de bord
- Pour signaler une alerte WARN ou une situation critique CRIT

## RÈGLES DE TENUE
- Une entrée = un événement technique identifiable. Pas de fusion.
- Court, factuel, exploitable. Pas de journal littéraire.
- Ne pas recopier le code — mentionner fichiers, lignes, logique.
- Consigner les effets de bord, même mineurs.
- Consigner les échecs et les annulations. Aucun évitement.
- Chaque entrée lisible hors contexte immédiat.
- Ne pas attendre la fin de session. Écrire au moment où ça se passe.

## LÉGENDE DES TYPES
INIT  = Initialisation — mise en place d'un module, d'une structure
FIX   = Correctif — correction d'un bug ou comportement non souhaité
MOD   = Modification — ajustement fonctionnel ou structurel
TEST  = Test — vérification, essai, validation ou échec
DEC   = Décision — arbitrage technique ou choix d'architecture
WARN  = Alerte — risque, dette technique, point sensible
ROLL  = Retour arrière — annulation d'une modification précédente
LOCK  = Stabilisation — snapshot de version, état figé
ERR   = Erreur SENTINEL — échec opérationnel, BLOQUE l'action en cours
CRIT  = Critique SENTINEL — état grave, REMONTE IMMÉDIATEMENT À CÉDRIC
WAIT  = Attente SENTINEL — en attente de verrou
PURGE = Purge SENTINEL — JAMAIS sans validation Cédric

## STATUTS
⬜ OUVERT    = action non encore exécutée
🔄 EN COURS  = action en cours de réalisation
✅ CLÔTURÉ   = exécuté et validé
⚠  VIGILANCE = exécuté mais à surveiller
❌ ANNULÉ    = abandonné ou retour arrière effectué

## FORMAT D'ENTRÉE STANDARD
### [BN-XXXX] — TYPE : CODE
**Date :** JJ/MM/AAAA HH:MM
**Statut :** ⬜
**Auteur :** Cédric / IA / Mixte
**Zone concernée :**
**Fichier(s) :**
**Ligne(s) :**
**Contexte :**
**Action :**
**Intention :**
**Résultat observé :**
**Effets de bord :**
**Décision finale :**
**Lien PAFOC :** aucun
**Note courte :**

## RÈGLE DE RELECTURE POUR IA
Avant toute intervention, lire dans cet ordre :
1. État actuel du projet
2. Les 5 dernières entrées du journal
3. Toutes les entrées sur la zone ou le fichier concerné
4. Le PAFOC correspondant s'il existe
5. Les entrées WARN et CRIT actives
Si verrou actif ou décision contradictoire détecté : signaler à Cédric avant toute action.

## TEMPLATE NOUVEAU PROJET
# BOÎTE NOIRE DU PROJET
**Projet :** [NOM]
**Référence :** [PAN-RL-434D-DOM-MMAA-####]
**Version :** v1.0
**Date d'ouverture :** [JJ/MM/AAAA]
**Responsable :** Cédric Maret

### [BN-0001] — TYPE : INIT
**Date :** [JJ/MM/AAAA HH:MM]
**Statut :** ✅
**Auteur :** Mixte
**Contexte :** Ouverture du projet et mise en place de la Boîte Noire.
**Action :** Création du fichier boite-noire.md.
**Résultat observé :** Structure initiale en place.
**Effets de bord :** Aucun.
**Lien PAFOC :** aucun

*Boîte Noire v1.0 — PAN∞ Research Lab — CC BY-SA 4.0 — Réf. PAN-RL-434D-INF-0326-0002*
