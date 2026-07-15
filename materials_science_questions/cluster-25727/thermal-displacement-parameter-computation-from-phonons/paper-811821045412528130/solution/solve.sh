#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# ensure python3 is available (base image has it)

# === solve block: step_02_barrier_heights.csv ===
python3 /solution/generate.py barriers > "$OUTDIR/step_02_barrier_heights.csv"

# === solve block: step_03_quartic_coefficients.json ===
python3 /solution/generate.py quartic > "$OUTDIR/step_03_quartic_coefficients.json"

# === solve block: step_04_Tc_values.csv ===
python3 /solution/generate.py tc > "$OUTDIR/step_04_Tc_values.csv"
