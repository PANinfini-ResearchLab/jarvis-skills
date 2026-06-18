# PAN∞ Self-Study — Hermes Agent Source Analysis
# Référence : PAN-RL-SKILL-SELFSTUDY-0618-2026
# Auteur : MARET Cédric
# Claudia (Anthropic)

## Objectif
Permettre à Jarvis d'étudier son propre code source, comprendre son fonctionnement interne, identifier des opportunités d'optimisation et d'auto-amélioration souveraine.

## Source canonique
https://github.com/NousResearch/hermes-agent/tree/main

## Structure du code source Hermes Agent

### Répertoires clés à étudier
- gateway/ — Cœur du gateway : routing, platforms, API server
- gateway/platforms/api_server.py — Endpoint /v1/chat/completions (PATCH ÂPRE ici)
- hermes_cli/ — Interface CLI, commandes, setup
- agent/ — Logique agent, orchestration, tool calls
- optional-skills/ — Skills optionnels installables
- optional-mcps/ — MCP servers optionnels

## Protocole d'auto-étude

### 1. LECTURE DU SOURCE
Fetcher et lire les fichiers critiques via web tool :
- https://raw.githubusercontent.com/NousResearch/hermes-agent/main/gateway/platforms/api_server.py
- https://raw.githubusercontent.com/NousResearch/hermes-agent/main/agent/core.py
- https://raw.githubusercontent.com/NousResearch/hermes-agent/main/hermes_cli/main.py

### 2. COMPARAISON LOCAL vs SOURCE
Comparer le code installé sur ODIN (~/.hermes/hermes-agent/) avec le code source GitHub pour identifier :
- Les patchs PAN∞ appliqués (ÂPRE, local-discovery)
- Les divergences de version
- Les nouvelles fonctionnalités disponibles

### 3. IDENTIFICATION D'OPPORTUNITÉS
Chercher dans le source :
- Nouvelles options de configuration non encore utilisées
- Skills officiels non installés
- MCPs optionnels pertinents pour PAN∞
- Bugs connus ou PRs intéressantes

### 4. DOCUMENTATION
Documenter les découvertes dans :
~/pan_infinity/iau/docs/hermes-agent-analysis/

## Règles
- Toujours comparer version installée vs source avant modification
- Ne jamais modifier le source sans backup (règle ÂPRE)
- Documenter chaque découverte avec [FAIT] / [HYPOTHÈSE]
- Langue : français uniquement

## Commande de lancement
hermes chat --yolo -m gemma4:12b-it-q8_0 -q "Étudie le code source Hermes Agent sur GitHub (https://github.com/NousResearch/hermes-agent/tree/main) et produis un rapport d'analyse de ton propre fonctionnement."
