#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: isotherms_gcmc.csv ===
mkdir -p /app/outputs && python3 /solution/gen_data.py isotherms /app/outputs/isotherms_gcmc.csv

# === solve block: coexistence.csv ===
python3 /solution/gen_data.py coexistence /app/outputs/coexistence.csv

# === solve block: gcmc_comparison.csv ===
python3 /solution/gen_data.py comparison /app/outputs/gcmc_comparison.csv
