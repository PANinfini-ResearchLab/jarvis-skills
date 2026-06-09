---
name: logs-rag
description: Semantic search over agent and system logs. Use when the user asks
  "when did X fail", "have we seen this error before", or wants incidents
  correlated across time.
---

# Logs RAG — Semantic Log Search

## Configuration
Inherits rag-local variables, plus :
| LOGS_RAG_SOURCES | ~/.hermes/logs | Dirs/files to index (colon-separated) |
| LOGS_RAG_TABLE   | logs           | Dedicated table (do not mix)          |
| LOGS_RAG_WINDOW  | 50             | Lines per chunk                       |
| LOGS_RAG_SINCE   | 30d            | Ingestion horizon                     |

## Log-aware chunking
1. Windows of LOGS_RAG_WINDOW lines
2. Never cut a stack trace — extend the window to its end
3. Prefix each chunk with its time range [ts_start → ts_end]
4. metadata : {file, ts_start, ts_end, service}

## Sources
- Flat log files
- journalctl -u <service> --since <date>
- docker logs --since <date>
Ingest on timer (cron/systemd), dedup on (file, ts_start, ts_end).

## Answering rules
1. Every claim about the past cites a real timestamped log line
2. "Last Tuesday" = vector search + filter ts_start BETWEEN
3. Empty retrieval → say so, never reconstruct a plausible history
4. Recurring error → full timeline of occurrences, not just the latest

## Schema addition vs rag-local
ALTER TABLE logs ADD COLUMN IF NOT EXISTS ts_start TIMESTAMPTZ;
ALTER TABLE logs ADD COLUMN IF NOT EXISTS ts_end TIMESTAMPTZ;
ALTER TABLE logs ADD COLUMN IF NOT EXISTS service TEXT;
CREATE INDEX IF NOT EXISTS idx_logs_ts ON logs(ts_start);
