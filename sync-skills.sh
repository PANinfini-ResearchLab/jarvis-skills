#!/bin/bash
for skill in home optimize monitor orders gpu-optimizer hardware-audit agent-orchestrator system-monitor knowledge-sync ollama-manager network-diagnostics backup-manager research-assistant security-audit network-manager nas-manager log-analyzer memory-optimizer firewall-manager bandwidth-monitor storage-optimizer log-archiver cron-manager performance-benchmark hardware-inventory ha-tool-core hermes-memory hermes-datetime honesty; do
    cp -r ~/.hermes/skills/$skill ~/jarvis-skills/ 2>/dev/null
done

# Ajouter les fichiers ha-tool-core Python
mkdir -p ~/jarvis-skills/ha-tool-core
cp /home/cedric/.hermes/ha-tool-core/*.py ~/jarvis-skills/ha-tool-core/ 2>/dev/null

cd ~/jarvis-skills
git add .
git diff --quiet && git diff --staged --quiet || git commit -m "Auto-sync skills $(date +%Y-%m-%d_%H:%M)" && git push origin main
