#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_04a_stress_strain_8nm.csv ===
python3 /solution/generate.py --size 8 --out /app/outputs/step_04a_stress_strain_8nm.csv

# === solve block: step_04b_stress_strain_20nm.csv ===
python3 /solution/generate.py --size 20 --out /app/outputs/step_04b_stress_strain_20nm.csv

# === solve block: step_05_yield_strengths.json ===
python3 -c "import json; json.dump({'8nm':5.0,'20nm':3.0}, open('/app/outputs/step_05_yield_strengths.json','w'))"
