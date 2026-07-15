#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: heat_curves.csv ===
mkdir -p /app/outputs
python3 /solution/compute_heat.py > /app/outputs/heat_curves.csv
