---
name: knowledge-sync
description: Synchronise les connaissances entre les agents Hermès IAU via des fichiers Markdown. Permet de partager des notes, des recherches, et des décisions.
version: 1.0
author: Cédric Maret
toolsets: ["file", "terminal"]
---

# Skill: Knowledge Sync
## Fonctions
- **`sync_all`** : Synchronise tous les fichiers de connaissances entre les agents.
- **`push <file>`** : Envoie un fichier vers tous les agents.
- **`pull <file>`** : Récupère un fichier depuis un agent.
- **`list_knowledge`** : Liste tous les fichiers de connaissances disponibles.

## Répertoires de connaissances
- `/mnt/JARVIS-SSD/knowledge/` → Base commune à tous les agents
- `~/.hermes/SOUL.md` → Identité Jarvis
- `~/.hermes/AGENTS.md` → Infrastructure ODIN

## Agents concernés
- HA-0 Jarvis (ODIN 192.168.10.34)
- HA-1 Dédale
- HA-2 La Bibliothécaire
- HA-3 Athéna

## Exemples d'utilisation
- "Synchronise toutes les connaissances entre les agents."
- "Envoie le fichier theorie_astrophysique.md à HA-1 et HA-2."
- "Liste tous les fichiers de connaissances disponibles."
