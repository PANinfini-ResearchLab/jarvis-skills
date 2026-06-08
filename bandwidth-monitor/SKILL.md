---
name: bandwidth-monitor
description: Surveille la bande passante du réseau AUTOMATA-NET en temps réel.
version: 1.0
author: Cédric Maret
toolsets: ["terminal"]
---

# Skill: Bandwidth Monitor
## Fonctions
- **`start_monitoring`** : Lance la surveillance de la bande passante.
- **`stop_monitoring`** : Arrête la surveillance.
- **`get_usage`** : Affiche l'utilisation actuelle de la bande passante.
- **`get_usage_by_ip`** : Affiche l'utilisation par IP.
- **`set_alert <threshold>`** : Définit un seuil d'alerte en Mbps.

## Interfaces ODIN
- eno1 : 192.168.10.34 (interface principale AUTOMATA-NET)
- eno2/3/4 : DOWN (non utilisées)

## Alertes Telegram
- Bot : @jarvis_paninfini_bot
- Chat ID : 8664542027

## Exemples d'utilisation
- "Affiche l'utilisation actuelle de la bande passante."
- "Définit une alerte si la bande passante dépasse 100 Mbps."
- "Surveille le trafic par IP sur AUTOMATA-NET."
