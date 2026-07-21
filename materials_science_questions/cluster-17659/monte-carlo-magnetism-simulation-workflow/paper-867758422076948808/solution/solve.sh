#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fe_reversal_times.csv ===
python3 /solution/compute_reversal.py fe /app/outputs/fe_reversal_times.csv

# === solve block: co_reversal_times.csv ===
python3 /solution/compute_reversal.py co /app/outputs/co_reversal_times.csv
