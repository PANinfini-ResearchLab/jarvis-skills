# jarvis-skills

**Portable skills for Hermes Agent — operational discipline, sovereign RAG, research tooling.**

Developed and battle-tested at PAN∞ Research Lab (Seyches, France) on a multi-GPU
Ubuntu home-lab, then de-coupled from that infrastructure so they run anywhere:
a laptop, a single VPS, or a rack. Everything is configured through environment
variables; nothing requires a cloud API.

🇫🇷 Skills développés par PAN∞ Research Lab. Documentation en anglais pour la
communauté Hermès ; support en français bienvenu dans les issues.

## Installation

git clone https://github.com/PANinfini-ResearchLab/jarvis-skills
cp -r jarvis-skills/core/* jarvis-skills/rag/* ~/.hermes/skills/

## Skills

### core/ — operational discipline (zero infra dependencies)

| Skill         | Description                                                                     |
|---------------|---------------------------------------------------------------------------------|
| honesty       | Anti-hallucination rules: real execution, real output, fact/hypothesis labeling |
| sentinel      | Snapshot-act-verify backup protocol; every risky change becomes reversible      |
| blackbox      | Append-only technical journal; never debug the same problem twice               |
| pafoc         | Surgical briefing format for delegating tasks to coding agents                  |
| ops-triad-doc | How pafoc x sentinel x blackbox chain into one workflow                         |

### rag/ — sovereign retrieval

| Skill              | Description                                                      |
|--------------------|------------------------------------------------------------------|
| rag-local          | Local RAG on PostgreSQL + pgvector with local embeddings         |
| logs-rag           | Semantic search over logs with timestamped evidence              |
| knowledge-sources  | Routing catalog of open, keyless knowledge APIs                  |

### research/

| Skill               | Description                                                                  |
|---------------------|------------------------------------------------------------------------------|
| research-pipeline   | arXiv/OpenAlex search → Zenodo/HAL deposit → DOI ledger → ORCID sync        |
| experiment-tracker  | File-based, offline run tracking (params, metrics, artifacts)                |

### tools/

| Skill    | Description                                                                    |
|----------|--------------------------------------------------------------------------------|
| alerting | Telegram / email / ntfy notifications with thresholds, dedup, recovery alerts |

### infra/ — *Being ported, see PORTING.md*
gpu-optimizer, system-monitor, backup-manager, hardware-inventory, ollama-manager...

## Design principles
1. Sovereign by default — local models, local storage, no mandatory cloud.
2. Configurable, not hardcoded — every path, host, threshold = documented env var.
3. Honest agents — no claim without real command output.
4. Degrade gracefully — missing GPU/service → reduced mode, stated explicitly.

## Contributing
See CONTRIBUTING.md and PORTING.md.

## License
MIT — PAN∞ Research Lab, Cédric MARET (ORCID 0009-0006-6399-9132)
