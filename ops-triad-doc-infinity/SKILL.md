---
name: ops-triad-doc
description: How pafoc, sentinel and blackbox chain into one disciplined workflow.
  Use at the START of any multi-step technical session.
---

# Ops Triad — pafoc × sentinel × blackbox

| Skill    | Protects against                     | When                |
|----------|--------------------------------------|---------------------|
| pafoc    | Scope creep, vague requests          | Before — framing    |
| sentinel | Irreversible changes                 | Before/during       |
| blackbox | Lost knowledge, re-debugging         | After — trace       |

## Standard workflow
Request → [1] PAFOC brief → [2] Sentinel SNAPSHOT → [3] Execute
        → [4] Verify (PAFOC O) ──fail──→ Sentinel ROLLBACK
        → [5] Blackbox entry (refs brief + snapshot)

## Minimal version (low-risk)
One-line objective (micro-PAFOC), no snapshot, one-line blackbox entry if notable.
Criterion : can the action cost >15 min to undo or rediscover? Yes → full triad.

## Cross-references
Blackbox → brief ID + snapshot path
MANIFEST → brief ID
PAFOC A  → past blackbox entries
Every intervention reconstructible from any of its three traces.
