---
name: research-pipeline
description: End-to-end academic publishing pipeline — search prior work, prepare
  deposits (Zenodo, HAL), track DOIs, sync ORCID. Use when the user wants to
  publish, deposit, or track academic work.
---

# Research Pipeline — Academic Publishing

## Configuration
| RP_ORCID         | (required) | Your ORCID identifier                     |
| RP_ZENODO_TOKEN  | (required) | Zenodo personal access token              |
| RP_HAL_USER      | (optional) | HAL username for direct deposit           |
| RP_ARCHIVE_PATH  | ~/research/archive.md | Local DOI ledger             |

## Stage 1 — Prior-work search
Search OpenAlex + arXiv + HAL via knowledge-sources before any deposit.
Output : table (title, year, DOI, relevance).
Flag duplicates BEFORE depositing — a duplicate deposit wastes a DOI.

## Stage 2 — Metadata preparation
Required fields :
- title, authors + ORCID per author
- abstract, keywords, language
- license (CC BY 4.0 recommended for open science)
- version (semantic : 1.0, 1.1, 2.0)
- related identifiers (cites, isPartOf, isVersionOf)

Rule : one deposit = one DOI. Never a "general DOI".
Use concept DOI for the family, version DOI per release.

## Stage 3 — Deposit

### Zenodo
POST https://zenodo.org/api/depositions
  Authorization: Bearer $RP_ZENODO_TOKEN
PUT  /api/depositions/<id> (metadata)
POST /api/depositions/<id>/files (upload)
POST /api/depositions/<id>/actions/publish

### HAL
With credentials → SWORD/AOfr API.
Without credentials → generate XML, hand to user for manual upload.

## Stage 4 — Ledger and ORCID sync
Append to $RP_ARCHIVE_PATH :
| date | title | version | DOI | repository | status |

Verify DOI resolves : curl -sI https://doi.org/<doi> → expect 302
Check ORCID public API after 48h : https://pub.orcid.org/v3.0/$RP_ORCID/works
Flag if work absent after 48h.

## Rules
1. DOI verified by resolving it — never assume it works
2. Ledger = source of truth for numbering — consult before any internal reference (anti-collision)
3. New version → Zenodo "new version" action, never an orphan record
4. Never deposit without Stage 1 prior-work check
