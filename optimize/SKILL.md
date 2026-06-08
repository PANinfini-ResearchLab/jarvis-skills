# Optimize — Infrastructure Auto-Optimization Skill

## Metadata
- **name:** optimize
- **version:** 1.0
- **author:** PAN∞ Research Lab / Claudia
- **tags:** infrastructure, gpu, performance, auto, nvidia, memory
- **trigger:** on_demand

## Description

Skill d'optimisation automatique pour les nœuds de La Forge (PAN∞ Research Lab).
Analyse l'état actuel des ressources GPU, RAM et stockage, détecte les inefficacités,
et applique des optimisations concrètes pour maximiser les performances d'ODIN.

## Instructions

Quand ce skill est chargé, exécute via ton tool terminal :

### Étape 1 — Audit ressources
```bash
nvidia-smi --query-gpu=name,memory.used,memory.free,memory.total,utilization.gpu,temperature.gpu --format=csv,noheader
free -h
df -h | grep -E "md0|JARVIS|/"
ps aux --sort=-%mem | head -10
curl -s http://localhost:11434/api/ps
```

### Étape 2 — Optimiser VRAM
Toujours garder jarvis:latest en VRAM :
```bash
curl -s http://localhost:11434/api/generate -d '{"model":"jarvis:latest","keep_alive":-1,"prompt":""}'
```
Décharger tout modèle inutile (sauf jarvis:latest).

### Étape 3 — Optimiser RAM
```bash
sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### Étape 4 — Nettoyer stockage
```bash
find ~/.hermes/logs -name "*.log" -mtime +7 -delete 2>/dev/null
find ~/.hermes/sessions -name "*.json" -mtime +30 -delete 2>/dev/null
du -sh /mnt/JARVIS-SSD/ollama/
```

### Étape 5 — Rapport
Sauvegarde un rapport dans /home/cedric/jarvis_optimize_report.md avec date, état avant/après, actions effectuées, recommandations.

### Étape 6 — Cron automatique
Planifier si pas déjà fait :
```bash
hermes cron add "0 4 * * *" "Exécute le skill optimize sur ODIN. Sauvegarde rapport dans /home/cedric/jarvis_optimize_report.md"
```

## Règles absolues
- Ne jamais décharger jarvis:latest
- Ne jamais supprimer de fichiers modèles sans autorisation HA-0
- Toujours vérifier avant ET après chaque optimisation

## Seuils d'alerte
| Ressource | Warning | Critique |
|-----------|---------|---------|
| GPU temp | > 70°C | > 80°C |
| VRAM | > 90% | > 95% |
| RAM | > 80% | > 90% |
| SSD | > 70% | > 85% |
| HDD | > 80% | > 90% |
