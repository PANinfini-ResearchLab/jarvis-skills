#!/bin/bash
# Sync skills vers GitHub automatiquement
cp -r ~/.hermes/skills/home ~/jarvis-skills/ 2>/dev/null
cp -r ~/.hermes/skills/optimize ~/jarvis-skills/ 2>/dev/null
cp -r ~/.hermes/skills/monitor ~/jarvis-skills/ 2>/dev/null
cp -r ~/.hermes/skills/orders ~/jarvis-skills/ 2>/dev/null

cd ~/jarvis-skills
git add .
git diff --quiet && git diff --staged --quiet || git commit -m "Auto-sync skills $(date +%Y-%m-%d_%H:%M)" && git push origin main
