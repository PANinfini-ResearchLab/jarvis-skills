# Home — Infrastructure Self-Awareness Skill

## Metadata
- **name:** home
- **version:** 1.0
- **author:** PAN∞ Research Lab / Claudia
- **tags:** infrastructure, auto, dynamic, universal
- **trigger:** on_load

## Description

Skill universel pour tous les agents Hermès IAU. Au premier chargement sur une nouvelle machine, l'agent scanne son propre environnement matériel, enregistre son profil dans sa mémoire persistante, et vérifie sa connectivité au réseau AUTOMATA-NET via BIFROST.

## Instructions

Au chargement de ce skill, tu DOIS exécuter via ton tool terminal :

```bash
hostname
ip -o -4 addr show up | grep scope\ global | awk '{print $4}' | head -1
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null || echo "No NVIDIA GPU"
free -h | awk 'NR==2{print $2}'
ping -c 3 bifrost.automata-net.local 2>/dev/null || ping -c 3 192.168.10.1
```

Compile les résultats dans ta mémoire persistante. Ton IP est fixe — ne jamais la modifier sans autorisation HA-0.

## Réseau AUTOMATA-NET
- Domaine : automata-net.local
- Firewall : bifrost.automata-net.local (192.168.10.1)
- Plage IP : 192.168.10.x

## Nœuds La Forge
| Nœud | IP | Agent |
|------|----|-------|
| ODIN | 192.168.10.34 | HA-0 Jarvis |
| Z230 | 192.168.10.20 | Contrôle |
| BIFROST | 192.168.10.1 | Firewall |
