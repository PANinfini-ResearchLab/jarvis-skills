---
name: hermes-datetime
description: Gestion date/heure avec triple validation, synchronisation Paris (Europe/Paris), et affichage au format français JJ/MM/AAAA HH:MM:SS.
version: 1.0
author: Cédric Maret
toolsets: ["terminal"]
---

# Skill: Hermes DateTime

## Fonctions
- **`now`** : Heure actuelle Paris format FR
- **`validate <datetime>`** : Triple validation (Native + ISO + Format FR)
- **`timestamp`** : Timestamp complet validé avec offset DST
- **`format <type>`** : short_date / short_time / full / long / relative

## Formats
- JJ/MM/AAAA HH:MM:SS → "08/06/2026 14:30:45"
- JJ/MM/AAAA → "08/06/2026"
- Long → "lundi 8 juin 2026"
- Relatif → "il y a 2 heures"

## Stockage recommandé
- Stocker en UTC
- Afficher en Europe/Paris
- DST auto-détecté (UTC+1 hiver / UTC+2 été)

## Exemples
- "Quelle heure est-il à Paris ?"
- "Valide la date 08/06/2026 14:30"
- "Horodate cette action en format français"
