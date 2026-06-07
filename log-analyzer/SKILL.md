---
name: log-analyzer
description: Analyse les logs système et applicatifs (Ollama, Hermes, kernel) pour détecter des erreurs ou des anomalies.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "file"]
---

# Skill: Log Analyzer
## Fonctions
- **`analyze_ollama_logs`** : Analyse les logs d'Ollama.
- **`analyze_hermes_logs`** : Analyse les logs de Hermes Agent.
- **`analyze_system_logs`** : Analyse les logs système.
- **`search_logs <keyword>`** : Cherche un mot-clé dans tous les logs.
- **`generate_log_report <days>`** : Génère un rapport des logs des derniers jours.
- **`tail_log <file> <lines>`** : Affiche les dernières lignes d'un fichier de log.

## Fichiers de logs ODIN
- /var/log/syslog → logs système
- ~/.hermes/logs/ → logs Hermes
- journalctl → logs systemd (ollama, hermes-dashboard, hermes-workspace)

## Exemples d'utilisation
- "Analyse les logs d'Ollama pour détecter des erreurs."
- "Cherche le mot-clé CUDA dans tous les logs."
- "Génère un rapport des logs des 7 derniers jours."
