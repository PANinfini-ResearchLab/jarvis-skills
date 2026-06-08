---
name: system-monitor
description: Surveille les ressources système (CPU, GPU, RAM, stockage, réseau) et envoie des alertes Telegram si des seuils sont dépassés.
version: 1.0
author: Cédric Maret
toolsets: ["terminal", "web"]
---

# Skill: System Monitor
## Fonctions
- **`start_monitoring`** : Lance la surveillance en continu (toutes les 5 min).
- **`stop_monitoring`** : Arrête la surveillance.
- **`set_threshold <resource> <value>`** : Définit un seuil d'alerte.
- **`send_alert`** : Envoie une alerte manuelle via Telegram.

## Seuils par défaut
- CPU : > 90%
- GPU : > 80%
- RAM : > 85%
- Stockage : > 90%

## Alertes Telegram
- Bot : @jarvis_paninfini_bot
- Chat ID : 8664542027

## Exemples d'utilisation
- "Démarre la surveillance système avec alertes Telegram."
- "Définis un seuil d'alerte pour la VRAM à 90%."
- "Envoie une alerte : GPU 0 à 95% d'utilisation."
