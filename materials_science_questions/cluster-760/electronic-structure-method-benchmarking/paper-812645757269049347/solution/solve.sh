#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/write_outputs.py

# === solve block: step_03_enthalpies.csv ===
echo 'step_03_enthalpies.csv already produced by preamble' > /dev/null

# === solve block: step_04_summary.csv ===
echo 'step_04_summary.csv already produced by preamble' > /dev/null
