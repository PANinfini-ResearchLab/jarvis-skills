#!/bin/bash
for skill in home optimize monitor orders gpu-optimizer hardware-audit agent-orchestrator system-monitor knowledge-sync ollama-manager network-diagnostics backup-manager research-assistant security-audit network-manager nas-manager log-analyzer memory-optimizer firewall-manager bandwidth-monitor storage-optimizer log-archiver cron-manager performance-benchmark; do
    cp -r ~/.hermes/skills/$skill ~/jarvis-skills/ 2>/dev/null
done

cd ~/jarvis-skills
git add .
git diff --quiet && git diff --staged --quiet || git commit -m "Auto-sync skills $(date +%Y-%m-%d_%H:%M)" && git push origin main
