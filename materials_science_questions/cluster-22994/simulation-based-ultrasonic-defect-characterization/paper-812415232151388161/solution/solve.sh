#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.csv ===
python3 /solution/compute.py csv /app/outputs/computed_results.csv

# === solve block: threshold_and_worstcase.txt ===
python3 /solution/compute.py txt /app/outputs/threshold_and_worstcase.txt
