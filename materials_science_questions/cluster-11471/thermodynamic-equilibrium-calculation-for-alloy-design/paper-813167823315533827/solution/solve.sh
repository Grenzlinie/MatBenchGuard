#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_thermal_expansion.csv ===
python3 /solution/compute_thermal_expansion.py
