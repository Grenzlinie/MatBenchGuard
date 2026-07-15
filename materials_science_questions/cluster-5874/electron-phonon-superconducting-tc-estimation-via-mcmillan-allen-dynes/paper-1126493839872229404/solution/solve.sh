#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: step_01_specific_heat.csv ===
python3 /solution/generate_artifacts.py "$OUTDIR/step_01_specific_heat.csv"

# === solve block: step_02_impurity_spectral.csv ===
python3 /solution/generate_artifacts.py "$OUTDIR/step_02_impurity_spectral.csv"

# === solve block: step_03_thermal_conductivity.csv ===
python3 /solution/generate_artifacts.py "$OUTDIR/step_03_thermal_conductivity.csv"
