---
name: sentinel
description: Universal operational backup protocol. Use BEFORE any risky operation —
  config edits, service changes, migrations, deletions, upgrades — even if the user
  doesn't ask for a backup.
---

# Sentinel — Operational Backup Protocol
Three phases : SNAPSHOT → ACT → VERIFY.

## Configuration
| SENTINEL_ROOT      | ~/.sentinel | Where snapshots are stored          |
| SENTINEL_RETENTION | 30          | Days before snapshots are pruned    |
| SENTINEL_REMOTE    | (empty)     | Optional rsync/git remote, off-host |

## Phase 1 — SNAPSHOT
1. Timestamped dir : $SENTINEL_ROOT/$(date +%Y%m%d-%H%M%S)-<label>/
2. cp -a of each file that will be modified
3. State capture : services, versions, ports, disk
4. MANIFEST.md : what/why, captured list, rollback procedure as copy-pasteable commands

## Phase 2 — ACT
One logical operation per snapshot. If scope grows → stop, new snapshot.

## Phase 3 — VERIFY
1. Confirm new state (real commands — cf. honesty)
2. Confirm rollback is still possible (files readable, checksums)
3. Append SUCCESS / ROLLED BACK / PARTIAL to MANIFEST

## Rules
- No snapshot → no risky operation.
- Snapshots append-only, never edited.
- SENTINEL_REMOTE defined → push before Phase 2.
