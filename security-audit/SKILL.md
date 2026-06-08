---
name: security-audit
description: Audite la sécurité d'ODIN et du réseau AUTOMATA-NET (permissions, ports, logs, vulnérabilités).
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Security Audit
## Fonctions
- **`check_permissions`** : Vérifie les permissions des fichiers sensibles.
- **`scan_open_ports`** : Scanne les ports ouverts sur ODIN.
- **`check_ssh`** : Vérifie les clés SSH et les connexions récentes.
- **`audit_logs`** : Analyse les logs système pour détecter des activités suspectes.
- **`generate_security_report`** : Génère un rapport de sécurité complet.

## Fichiers sensibles à surveiller
- ~/.hermes/.env → tokens et clés API
- ~/.hermes/SOUL.md → identité Jarvis
- ~/.ssh/ → clés SSH
- /etc/systemd/system/hermes-*.service → services

## Ports exposés ODIN
- 22 → SSH (accès restreint)
- 8642 → Hermes Gateway
- 9119 → Hermes Dashboard
- 3000 → Hermes Workspace
- 11434 → Ollama (local uniquement)

## Règles de sécurité
- Ollama sur localhost uniquement (jamais exposé sur 0.0.0.0)
- Gateway accessible réseau local AUTOMATA-NET uniquement
- Token Telegram allowlist : 8664542027 uniquement
- Clés SSH dédiées par service (id_jarvis_github)

## Exemples d'utilisation
- "Vérifie les permissions des fichiers dans ~/.hermes/."
- "Scanne les ports ouverts sur ODIN."
- "Vérifie les connexions SSH récentes."
- "Génère un rapport de sécurité complet."
