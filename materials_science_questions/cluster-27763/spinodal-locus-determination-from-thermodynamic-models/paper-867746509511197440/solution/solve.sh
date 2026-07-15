#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mean_field_coexistence.csv ===
python3 /solution/gen_outputs.py mean_field_coexistence.csv

# === solve block: spinodals_hidden_binodal.csv ===
python3 /solution/gen_outputs.py spinodals_hidden_binodal.csv

# === solve block: topology_classification.txt ===
python3 /solution/gen_outputs.py topology_classification.txt

# === solve block: mc_density_distribution.csv ===
python3 /solution/gen_outputs.py mc_density_distribution.csv

# === solve finalize ===
echo 'All artifacts written successfully.'
