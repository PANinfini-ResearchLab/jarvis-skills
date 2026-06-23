---
name: cervelet-optimizer
description: Deterministic optimization layer for hybrid AI systems. Use whenever
  the agent faces scheduling, resource allocation, pipeline ordering, or any
  combinatorial problem with a calculable exact solution. Calls OR-Tools CP-SAT
  instead of consuming LLM tokens. tokens_llm=0, vram_consumed=0 — always.
---

# Cervelet Optimizer — Deterministic Layer for Hybrid AI

## Principle

A well-designed AI system does not use an LLM for problems that have an exact
mathematical solution. OR-Tools solves them in milliseconds on CPU — no tokens,
no VRAM, no hallucination risk.

A calculable problem is not a problem to reason about.

## Trigger — classify before acting

TYPE_DETERMINISTIC — call optimizer.solve() immediately, do NOT reason:
- scheduling | task ordering | who does what | in what order
- resource allocation | concurrent resource conflict
- pipeline dependencies | node ordering with precedence constraints
- routing | optimal delegation by load
- bin packing | assignment | capacity constraints

TYPE_LLM — standard LLM processing:
- synthesis | writing | analysis | strategy
- ambiguity | interpretation | unknown errors | edge cases

## Installation

pip install ortools psycopg2-binary --break-system-packages
python3 -c "from ortools.sat.python import cp_model; print('OK')"

## Module structure

modules/
└── optimization/
    ├── __init__.py
    ├── optimizer.py      # Central class — entry point
    ├── scheduling.py     # Job Shop CP-SAT
    ├── allocation.py     # Resource allocation (VRAM, workers)
    ├── pipeline.py       # Flow Shop — pipeline with dependencies
    └── conflict.py       # Conflict resolution → allocation

## Usage

import sys
sys.path.insert(0, '/path/to/your/project')
from modules.optimization.optimizer import Optimizer

opt = Optimizer()
result = opt.solve("scheduling", data, context="my_context")
# result['tokens_llm']    == 0  always
# result['vram_consumed'] == 0  always
# result['cpu_time_ms']   == N  milliseconds on CPU

## Supported problem types

### scheduling — Job Shop CP-SAT

result = opt.solve("scheduling", {
    "missions":    ["task_a", "task_b", "task_c"],
    "agents":      ["worker_1", "worker_2"],
    "durations":   {"task_a": 45, "task_b": 12, "task_c": 60},
    "precedences": [["task_a", "task_b"]]
})
# status   → OPTIMAL | FEASIBLE | INFEASIBLE
# makespan → total duration (integer)
# solution → {"task_a": {"agent": "worker_1", "start": 0, "end": 45}, ...}

### allocation — Resource allocation

result = opt.solve("allocation", {
    "agents_vram":  {"agent_a": 12, "agent_b": 8, "agent_c": 6},
    "gpu_capacity": 16
})
# solution → {"agent_a": {"gpu": "V100_1", "vram_go": 12}, ...}
# Unserved → {"gpu": None, "statut": "EN_ATTENTE"}

### pipeline — Flow Shop with dependencies

result = opt.solve("pipeline", {
    "nodes":        ["ingest", "embed", "index", "validate"],
    "durations":    {"ingest": 5, "embed": 30, "index": 15, "validate": 8},
    "dependencies": [("ingest","embed"), ("embed","index"), ("index","validate")]
})
# makespan  → optimal total duration
# schedule  → {"ingest": {"start": 0, "end": 5}, ...}

## JSON API

Request:
{
  "module":  "optimization",
  "action":  "solve_scheduling",
  "context": "batch_001",
  "data": {
    "missions":    ["task_a", "task_b"],
    "agents":      ["worker_1", "worker_2"],
    "durations":   {"task_a": 45, "task_b": 12},
    "precedences": [["task_a", "task_b"]]
  }
}

Response:
{
  "status":        "OPTIMAL",
  "makespan":      57,
  "cpu_time_ms":   8.44,
  "tokens_llm":    0,
  "vram_consumed": 0,
  "solution": {
    "task_a": {"agent": "worker_1", "start": 0,  "end": 45},
    "task_b": {"agent": "worker_1", "start": 45, "end": 57}
  }
}

## Rules

- Never reason about a deterministic problem — call the solver directly.
- tokens_llm and vram_consumed are always 0 — document it, it is the ROI proof.
- If status is INFEASIBLE, report it explicitly — do not approximate.
- CPU only — no GPU, no CUDA, no VRAM impact on inference.
- Solvers run in parallel on idle CPU cores while GPU handles LLM inference.
