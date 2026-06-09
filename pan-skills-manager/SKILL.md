# SKILL : PAN-SKILLS-MANAGER
Gestion des repos de skills Hermes — PAN∞ Research Lab
Ref. : PAN-RL-434D-INF-0626-0006 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
Ce skill explique a Jarvis comment gerer les deux repos de skills PAN∞,
quoi mettre ou, et comment pousser les nouveaux skills au bon endroit.

## LES DEUX REPOS

### REPO PUBLIC — jarvis-skills
URL : git@github.com:PANinfini-ResearchLab/jarvis-skills.git
Visibilite : PUBLIC — accessible a toute la communaute Hermes
Contenu : Skills generiques, portables, utilisables par n importe qui

Skills actuellement publics :
backup-manager, bandwidth-monitor, cron-manager, gpu-optimizer,
hardware-audit, hardware-inventory, hermes-datetime, hermes-memory,
honesty, log-analyzer, log-archiver, memory-optimizer,
network-diagnostics, network-manager, ollama-manager, optimize,
performance-benchmark, research-assistant, security-audit,
storage-optimizer, system-monitor

### REPO PRIVE — jarvis-skills-paninfini
URL : git@github.com:PANinfini-ResearchLab/jarvis-skills-paninfini.git
Visibilite : PRIVE — interne PAN∞ Research Lab uniquement
Contenu : Skills specifiques a l infrastructure ODIN et au lab PAN∞

Skills actuellement prives :
agent-orchestrator, firewall-manager, nas-manager, orders, home,
ha-tool-core, knowledge-sync, pan-boite-noire, pan-doc,
pan-knowledge-bases, pan-logs-rag, pan-pafoc, pan-rag, pan-sentinel

## REGLES DE CLASSIFICATION

### → REPO PUBLIC si le skill :
- Fonctionne sur n importe quelle machine Linux
- N a pas de reference a ODIN, AUTOMATA-NET, bifrost, /home/cedric/
- N a pas de credentials ou configs specifiques PAN∞
- Peut etre utilise par la communaute Hermes sans modification
- Est generique : monitoring, backup, reseau, optimisation

### → REPO PRIVE si le skill :
- Contient des refs a l infra ODIN (IPs 192.168.10.x, AUTOMATA-NET)
- Contient des refs au lab PAN∞ (nomenclature 434D, ORCID, Zenodo)
- Utilise des chemins specifiques (/mnt/JARVIS-SSD, /mnt/JARVIS-MODEL)
- Fait partie de la hierarchie IAU (agents, profils, swarm)
- Contient des credentials ou configs confidentielles
- Est prefixe pan- (pan-sentinel, pan-rag, etc.)

## WORKFLOW POUR UN NOUVEAU SKILL

### Skill generique → repo public
1. Creer le skill dans ~/.hermes/skills/[nom-skill]/
2. Verifier : aucune ref ODIN/PAN∞/chemin hardcode
3. Pousser :
cd ~/.hermes/skills/pan-skills-repo
cp -r ~/.hermes/skills/[nom-skill] .
git add [nom-skill]
git commit -m "feat: [nom-skill] v1.0"
git push origin main

### Skill specifique PAN∞ → repo prive
1. Creer le skill dans ~/.hermes/skills/[nom-skill]/
2. Pousser :
cd ~/.hermes/skills/pan-skills-repo
cp -r ~/.hermes/skills/[nom-skill] .
git add [nom-skill]
git commit -m "feat: [nom-skill] v1.0 — PAN∞ internal"
git push paninfini main

## REMOTES CONFIGURES
origin   → git@github.com:PANinfini-ResearchLab/jarvis-skills.git (public)
paninfini → git@github.com:PANinfini-ResearchLab/jarvis-skills-paninfini.git (prive)

Verifier : git remote -v

*PAN-SKILLS-MANAGER v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Auteur : Cedric MARET — ORCID 0009-0006-6399-9132*
