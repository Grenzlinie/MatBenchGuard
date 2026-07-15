#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_deposition_powerlaw.csv ===
python3 /solution/generate_outputs.py energy "$OUTDIR/energy_deposition_powerlaw.csv"

# === solve block: ion_production_oct1989.csv ===
python3 /solution/generate_outputs.py oct "$OUTDIR/ion_production_oct1989.csv"

# === solve block: ion_production_jun1989.csv ===
python3 /solution/generate_outputs.py jun "$OUTDIR/ion_production_jun1989.csv"
