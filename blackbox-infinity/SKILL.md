---
name: blackbox
description: Append-only technical journal (flight-recorder style). Use whenever an
  incident occurs, a decision is made, a bug is fixed, or a config changes — even
  if the user doesn't ask to log it.
---

# Blackbox — Technical Flight Recorder

## Configuration
| BLACKBOX_PATH | ~/.blackbox/journal.md | Journal location           |
| BLACKBOX_GIT  | false                  | If true, commit each entry |

## Entry format
## BB-YYYYMMDD-NNN · <short title>
- **Date**    : ISO 8601 + timezone
- **Type**    : INCIDENT | DECISION | FIX | CHANGE | OBSERVATION
- **Context** : system/service, state before
- **Facts**   : observations — real outputs, errors VERBATIM
- **Cause**   : root cause, marked HYPOTHESIS if unconfirmed
- **Action**  : exact commands
- **Result**  : verified result
- **Refs**    : related entries (BB-...), sentinel snapshot, commit

## Rules
1. Append-only — correction = new entry, never edit.
2. Errors verbatim (a paraphrased error is unsearchable).
3. One event = one entry ; long incident = chronological entries.
4. Log failures too — they are the most valuable (what NOT to retry).
5. Write at the moment of the event, not end of session.

## Retrieval
Before any debug : grep -i -A 12 "<keyword>" "$BLACKBOX_PATH"
If past incident found → start from its Action/Result, not from zero.
