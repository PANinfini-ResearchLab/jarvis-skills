# SKILL : PAN-SKILL-FACTORY
Protocole de creation de skills Hermes — PAN∞ Research Lab
Ref. : PAN-RL-434D-PanHermesSkill-0626-0001 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
Ce skill definit le protocole de production de skills Hermes chez PAN∞.
Il previent la boucle infernale d amelioration croisee entre versions
interne et publique.

## NOMENCLATURE DES FAMILLES DE SKILLS

### Skills internes PAN∞
PAN-RL-434D-PanHermesSkill-[MMAA]-[####]
Exemples :
PAN-RL-434D-PanHermesSkill-0626-0001 → pan-skill-factory
PAN-RL-434D-PanHermesSkill-0626-0002 → pan-github (a creer)

### Skills grand public / communaute
PAN-RL-434D-InfinityHermesSkill-[MMAA]-[####]
Exemples :
PAN-RL-434D-InfinityHermesSkill-0626-0001 → skill-factory (version publique)
PAN-RL-434D-InfinityHermesSkill-0626-0002 → github-paninfini (version publique)

### Autres familles prevues
PAN-RL-434D-ClaudeCodeSkill-[MMAA]-[####]   → skills Claude Code
PAN-RL-434D-CodexSkill-[MMAA]-[####]        → skills OpenAI Codex
PAN-RL-434D-CursorSkill-[MMAA]-[####]       → skills Cursor
PAN-RL-434D-WindsurfSkill-[MMAA]-[####]     → skills Windsurf

## REGLE DE BIFURCATION — ANTI-BOUCLE

### Principe fondateur
Un skill nait en version PAN∞ (interne), est teste sur ODIN,
puis bifurque en version Infinity (publique) une seule fois.
Apres bifurcation, les deux versions evoluent independamment.

### Regles absolues
R1 - La version PanHermesSkill est developpee et testee sur ODIN en premier.
R2 - La version InfinityHermesSkill est generee depuis la Pan a la bifurcation.
R3 - Apres bifurcation, JAMAIS de re-synchronisation entre les deux versions.
R4 - La version Infinity evolue selon les retours communaute.
R5 - La version Pan evolue selon les besoins PAN∞.
R6 - Les deux versions ont des refs independantes (numeros ####  differents).
R7 - Toute amelioration de la version Pan NE REPART PAS vers la version Infinity.
R8 - Toute amelioration de la version Infinity NE REPART PAS vers la version Pan.

## WORKFLOW DE CREATION D UN SKILL

### Etape 1 — Conception interne (PanHermesSkill)
1. Identifier le besoin sur ODIN
2. Creer le skill dans ~/.hermes/skills/pan-[nom]/
3. Assigner la ref : PAN-RL-434D-PanHermesSkill-[MMAA]-[####]
4. Tester sur ODIN en conditions reelles
5. Valider le comportement avec Cedric
6. Pousser sur jarvis-skills-paninfini (repo PRIVE)

### Etape 2 — Bifurcation publique (InfinityHermesSkill)
1. Copier le skill Pan comme base
2. Supprimer toutes les refs PAN∞ :
   - Chemins /home/cedric/, /mnt/JARVIS-SSD/, /mnt/JARVIS-MODEL/
   - IPs 192.168.10.x, AUTOMATA-NET, bifrost
   - Refs ORCID, Zenodo, nomenclature 434D
   - Credentials paninfini2026
3. Remplacer par des variables configurables
4. Assigner une nouvelle ref : PAN-RL-434D-InfinityHermesSkill-[MMAA]-[####]
5. Ecrire une description generique sans refs PAN∞
6. Pousser sur jarvis-skills (repo PUBLIC)

### Etape 3 — Figer la bifurcation
1. Documenter dans ce skill la date de bifurcation
2. Les deux versions sont desormais independantes
3. NE JAMAIS synchroniser apres ce point

## CHECKLIST BIFURCATION

Avant de publier une version Infinity, verifier :
[ ] Aucun chemin /home/cedric/ ou /mnt/JARVIS-*
[ ] Aucune IP 192.168.10.x
[ ] Aucune ref AUTOMATA-NET ou bifrost
[ ] Aucun credential en dur (paninfini2026, tokens)
[ ] Aucune ref ORCID 0009-0006-6399-9132
[ ] Aucune nomenclature PAN-RL-434D dans le contenu
[ ] Variables configurables documentees
[ ] Description generique sans refs PAN∞
[ ] Teste sur une machine tierce si possible

## REGISTRE DES BIFURCATIONS

| Pan ref | Infinity ref | Skill | Date bifurcation | Statut |
|---------|-------------|-------|-----------------|--------|
| PanHermesSkill-0626-0001 | InfinityHermesSkill-0626-0001 | skill-factory | a faire | planifie |
| PanHermesSkill-0626-0002 | InfinityHermesSkill-0626-0002 | pan-github | a faire | planifie |

## EMPLACEMENT DES REPOS

Repo PRIVE (versions Pan) :
git@github.com:PANinfini-ResearchLab/jarvis-skills-paninfini.git
push : git push paninfini main

Repo PUBLIC (versions Infinity) :
git@github.com:PANinfini-ResearchLab/jarvis-skills.git
push : git push origin main

*PAN-SKILL-FACTORY v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Ref. PAN-RL-434D-PanHermesSkill-0626-0001*
*Auteur : Cedric MARET — ORCID 0009-0006-6399-9132*
