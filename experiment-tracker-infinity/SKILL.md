---
name: experiment-tracker
description: 100% local ML/AI experiment tracking — runs, params, metrics,
  artifacts — file-based, offline, sovereign. No cloud API required.
  Use when the user runs model training, evaluation, or benchmarks.
---

# Experiment Tracker — Local Run Tracking

## Configuration
| XT_ROOT    | ~/experiments | Root directory for all runs |
| XT_PROJECT | default       | Project name (subdirectory) |

## Directory structure
$XT_ROOT/$XT_PROJECT/YYYYMMDD-HHMM_<label>/
  ├── run.json        ← params, env, status, summary metrics
  ├── metrics.jsonl   ← one JSON line per step
  ├── artifacts/      ← models, plots, outputs
  └── notes.md        ← free-form observations

## run.json schema
{
  "id": "20260609-1402_qwen-q4-batch8",
  "project": "default",
  "status": "running|done|failed|aborted",
  "started": "ISO8601",
  "ended": "ISO8601 or null",
  "params": {"model": "...", "quant": "...", "batch": 8},
  "env": {"gpu": "auto-detected via nvidia-smi -L", "driver": "...", "host": "..."},
  "metrics_summary": {"loss": 0.42, "throughput_tps": 120},
  "tags": [],
  "parent_run": null
}

WARNING : env fields captured by real commands (nvidia-smi, uname), never declared.

## metrics.jsonl format
{"step": 100, "loss": 0.45, "throughput": 110, "ts": "ISO8601"}
{"step": 200, "loss": 0.42, "throughput": 120, "ts": "ISO8601"}

## Operations

### Start a run
mkdir -p $XT_ROOT/$XT_PROJECT/$RUN_ID/artifacts
echo '{"id":"'$RUN_ID'","status":"running",...}' > $XT_ROOT/$XT_PROJECT/$RUN_ID/run.json

### Log a metric
echo '{"step":'$STEP',"loss":'$LOSS',"ts":"'$(date -Iseconds)'"}' \
  >> $XT_ROOT/$XT_PROJECT/$RUN_ID/metrics.jsonl

### Finish a run
jq '.status="done" | .ended="'$(date -Iseconds)'"' run.json > run.json.tmp && mv run.json.tmp run.json

### Compare runs
jq -s '[.[] | {id, status, params, metrics_summary}]' \
  $XT_ROOT/$XT_PROJECT/*/run.json

### Best run on a metric
jq -s 'map(select(.status=="done")) | sort_by(.metrics_summary.loss) | first | .id' \
  $XT_ROOT/$XT_PROJECT/*/run.json

## Rules
1. Every reported metric traces back to a line in metrics.jsonl
2. A crashed run = failed, kept — failed runs are data
3. Changed parameter → new run with parent_run set, never overwrite
4. env captured at run start by real commands, never assumed
