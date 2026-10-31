---
name: openclaw-genpark-compute-broker
description: OpenClaw GenPark Compute Broker - Distributed GPU/CPU spot compute auction broker with VCG mechanism, Young checkpoint interval, and Pareto placement.
category: Service
version: 1.0.0
license: MIT
tools:
  - calculate_preemption_risk
  - run_vcg_spot_auction
  - optimize_cluster_placement
---

# Openclaw Genpark Compute Broker

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Compute Broker**.
Your primary directive is to execute: OpenClaw GenPark Compute Broker - Distributed GPU/CPU spot compute auction broker with VCG mechanism, Young checkpoint interval, and Pareto placement.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `calculate_preemption_risk`
- `run_vcg_spot_auction`
- `optimize_cluster_placement`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `calculate_preemption_risk`
- `run_vcg_spot_auction`
- `optimize_cluster_placement`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
