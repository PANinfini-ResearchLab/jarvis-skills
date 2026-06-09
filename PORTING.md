# PORTING.md — How to port an internal skill to a public Infinity skill

## 1. The 4 contamination patterns

| Pattern              | Internal example              | Public replacement                      |
|----------------------|-------------------------------|-----------------------------------------|
| Hardcoded path       | /home/cedric/backups          | ${BACKUP_ROOT:-~/.backups}              |
| Internal hostname/IP | bifrost.automata-net.local    | ${TARGET_HOST} documented               |
| Hardware assumption  | "the two Tesla P100"          | auto-detect via nvidia-smi -L           |
| Fixed threshold      | "alert above 80 GB"           | ${THRESHOLD_*} with default             |

## 2. Env var conventions
- One prefix per skill (SENTINEL_, RAG_, ALERT_, XT_, RP_...)
- Every var : default OR "required" clearly documented
- Table at the top of SKILL.md

## 3. Optional hardware
Probe before using (nvidia-smi, pg_isready, curl $OLLAMA_URL/api/tags).
Announce degraded mode explicitly, never crash on absent component.

## 4. Pre-publish checklist
- [ ] grep -rn "home/[a-z]*\|192\.168\.\|\.local" skill/ → empty
- [ ] Zero username/hostname/internal network/hardware model as assumption
- [ ] All tunables = documented env vars
- [ ] Tested on a machine that is NOT the origin machine
- [ ] SKILL.md frontmatter description : what + when to trigger

## 5. Internal vs public
Skills that stay internal : nas-manager, firewall-manager, agent-orchestrator.
Internal skills may be kept as reference in paninfini/ (read-only).
