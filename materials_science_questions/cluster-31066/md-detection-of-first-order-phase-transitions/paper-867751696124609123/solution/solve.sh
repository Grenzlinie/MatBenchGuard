#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_kappa_T_data.csv ===
python3 /solution/generate_outputs.py --csv "$OUTDIR/step_02_kappa_T_data.csv"

# === solve block: step_03_phase_boundary.json ===
python3 /solution/generate_outputs.py --json "$OUTDIR/step_03_phase_boundary.json"
