#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: interaction_energies.json ===
python3 /solution/gen_outputs.py interaction_energies.json

# === solve block: half_monolayer_IT_curve.csv ===
python3 /solution/gen_outputs.py half_monolayer_IT_curve.csv

# === solve block: quarter_monolayer_IT_curve.csv ===
python3 /solution/gen_outputs.py quarter_monolayer_IT_curve.csv

# === solve block: heat_capacity_curve.csv ===
python3 /solution/gen_outputs.py heat_capacity_curve.csv
