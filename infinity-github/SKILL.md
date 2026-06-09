# SKILL : INFINITY-GITHUB
Advanced GitHub Management — Multi-remote, Dual-version workflow
Ref. : PAN-RL-434D-InfinityHermesSkill-0626-0002 · v1.0 · CC BY-SA 4.0
Bifurcated from : PanHermesSkill-0626-0002 (pan-github)

## DESCRIPTION
This skill extends the bundled GitHub skills with advanced workflows :
multi-remote management, dual-version skill production, and structured releases.
Do NOT duplicate bundled skills — load them instead for standard operations.

## MULTI-REMOTE SETUP
git remote add origin git@github.com:YOUR_ORG/your-skills-public.git
git remote add private git@github.com:YOUR_ORG/your-skills-private.git

Verify : git remote -v
Push public : git push origin main
Push private : git push private main
Push both : git push origin main && git push private main

Always use SSH. Never hardcode HTTPS tokens in remote URLs.

## COMMIT CONVENTIONS
Format : type(scope): short description
         Optional ref: Ref. [YOUR-REF]

Types : feat / fix / refactor / docs / chore

Examples :
feat(skills): my-skill v1.0
feat(public-skills): infinity-myskill v1.0
fix(rag): fix database connection
refactor(skills): split public/private repos

## DUAL-VERSION SKILL WORKFLOW
Every skill has two versions :
- Internal version : tested on real infra, full config
- Public version : portable, no hardcoded paths or credentials
After bifurcation, the two versions evolve independently. NEVER sync after bifurcation.

Step 1 — Internal version :
1. Create skills/[name]/SKILL.md
2. Test on your real infrastructure
3. Push to private repo :
   cp -r skills/[name] /path/to/private-repo/
   git add [name] && git commit -m "feat(internal): [name] v1.0"
   git push private main

Step 2 — Public version :
1. Copy internal version as base
2. Remove ALL environment-specific refs :
   - Hardcoded paths (/home/user/, /mnt/disk/)
   - Internal IPs or hostnames
   - Credentials or tokens
   - Personal identifiers
3. Replace with configurable variables
4. Push to public repo :
   cp -r skills/infinity-[name] /path/to/public-repo/
   git add infinity-[name] && git commit -m "feat(public): infinity-[name] v1.0"
   git push origin main

Step 3 — Freeze bifurcation. Document the date. No cross-sync ever.

## RELEASES
Tag format : v[MAJOR].[MINOR].[PATCH]-[YYMM]
Examples : v1.0.0-2406, v0.3.0-2405

git tag -a v1.0.0-2406 -m "Release v1.0.0 — June 2024"
git push origin v1.0.0-2406

gh release create v1.0.0-2406 \
  --title "Skills v1.0.0 — June 2024" \
  --notes "Included skills : skill-a, skill-b"

## BIFURCATION CHECKLIST
Before pushing to public repo :
- No hardcoded paths (/home/user/, /mnt/disk/)
- No internal IPs or hostnames
- No credentials in plain text
- No personal identifiers
- Configurable variables documented
- Generic description

## BUNDLED SKILLS TO LOAD
Authentication → github-auth
Repo management → github-repo-management
Pull requests → github-pr-workflow
Code review → github-code-review
Issues → github-issues
Code analysis → codebase-inspection

*INFINITY-GITHUB v1.0 · CC BY-SA 4.0*
*Ref. PAN-RL-434D-InfinityHermesSkill-0626-0002*
*Bifurcated from PAN-RL-434D-PanHermesSkill-0626-0002*
