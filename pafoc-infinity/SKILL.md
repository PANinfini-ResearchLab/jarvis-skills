---
name: pafoc
description: Surgical briefing format for delegating a coding or sysadmin task to an
  AI agent. Trigger for any "fix this", "add this feature", "change this config".
---

# PAFOC — Surgical Brief for Coding Agents

## Brief template
# PAFOC · <task title>

## P — Problem      : observed symptom, facts only, errors verbatim
## A — Analysis     : known context, files, versions, past attempts
                      (link blackbox entries), hypotheses marked
## F — Fix expected : the exact change. Files to touch — and ONLY them
## O — Objective    : the test that proves success : command + expected output.
                      "It should work" is not an objective.
## C — Constraints  : what must NOT change (API, formats, deps, other files),
                      environment limits

## Rules — executing agent
1. Stay inside the brief. File outside F = read-only. Need to touch it → stop + report.
2. O is the contract. Run the verification, paste the real output.
3. Snapshot first (sentinel before), blackbox after.
4. Ambiguity blocks. P/F/O missing → ask, never guess the scope.

## Rules — brief author
- One brief = one intervention. Two problems → two briefs.
- Real paths and errors pasted, never from memory.
- An unwritten constraint is a constraint the agent will break.
