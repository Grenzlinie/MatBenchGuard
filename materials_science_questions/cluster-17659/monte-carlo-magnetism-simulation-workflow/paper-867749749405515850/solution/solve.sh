#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: validation_ideal_gas.csv ===
python3 /solution/write_outputs.py validation_ideal_gas.csv

# === solve block: validation_interacting_gas.csv ===
python3 /solution/write_outputs.py validation_interacting_gas.csv

# === solve block: chemical_potentials.csv ===
python3 /solution/write_outputs.py chemical_potentials.csv

# === solve block: balanced_mixture.csv ===
python3 /solution/write_outputs.py balanced_mixture.csv
