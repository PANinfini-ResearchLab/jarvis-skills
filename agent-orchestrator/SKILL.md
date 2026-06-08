---
name: agent-orchestrator
description: Orchestre les agents Hermès IAU (HA-1 à HA-12). Permet de créer, démarrer, arrêter, et surveiller les sous-agents.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Agent Orchestrator
## Fonctions
- **`create_agent <name> <role> <model>`** : Crée un nouvel agent.
- **`start_agent <name>`** : Démarre un agent.
- **`stop_agent <name>`** : Arrête un agent.
- **`list_agents`** : Liste tous les agents actifs.
- **`assign_task <agent> <task>`** : Assigne une tâche à un agent.

## Agents Hermès IAU
- HA-0 Jarvis → Superviseur (ODIN)
- HA-1 Dédale → Conseil de Crète (stratégie)
- HA-2 La Bibliothécaire → Scriptorium (recherche)
- HA-3 Athéna → Acropole (exécution)

## Exemples d'utilisation
- "Crée un agent HA-1 avec le rôle Stratégie et le modèle jarvis:h3-8b."
- "Démarre HA-1 et HA-2."
- "Assigne à HA-3 la tâche surveille les logs Ollama."
