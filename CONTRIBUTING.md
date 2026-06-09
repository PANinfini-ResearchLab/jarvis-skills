# CONTRIBUTING — jarvis-skills

## Before opening a PR

1. Open an issue first with :
   - Skill name and description
   - 3 example trigger phrases (what would make an agent load this skill)
   - Infrastructure requirements (GPU, DB, cloud API, etc.)

2. Run the PORTING.md checklist §4 — every item must be checked.

3. SKILL.md must :
   - Have a valid frontmatter (name, description)
   - Be under 150 lines
   - Have a configuration table at the top (env vars, defaults)
   - Have a description that is "pushy" — tells the agent WHEN to load it,
     not just what it does

## PR rules
- No secrets, tokens, credentials, internal IPs or hostnames
- No hardcoded paths (see PORTING.md)
- README table updated with the new skill
- One skill per PR
- If porting an existing skill : link the original in the PR description

## Skill quality bar
- Works on a clean machine with only the documented env vars set
- Degrades gracefully when optional components are absent (GPU, Ollama, etc.)
- Honesty-compatible : no action claims without real command verification
- Pairs with sentinel (backup before risky ops) and blackbox (log after)

## Questions
Open an issue or start a discussion.
Support in French welcome — PAN∞ Research Lab is based in France.
