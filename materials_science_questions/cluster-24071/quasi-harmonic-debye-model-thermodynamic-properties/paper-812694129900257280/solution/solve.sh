#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# No additional setup needed – python3 with stdlib is sufficient.

# === solve block: alpha_calc.csv ===
python3 /solution/compute_alphas.py /app/outputs/alpha_calc.csv

# === solve finalize ===
# Nothing to finalize after alpha_calc.csv is written.
