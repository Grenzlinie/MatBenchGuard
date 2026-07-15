#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: step_01_simulation_results.csv ===
# already written by preamble

# === solve block: step_02_summary.json ===
# already written by preamble
