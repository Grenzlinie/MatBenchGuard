#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_spin_magnetograviton_energy.txt ===
python3 /solution/gen_outputs.py energy /app/outputs/step_01_spin_magnetograviton_energy.txt

# === solve block: step_02_pair_correlation_difference.csv ===
python3 /solution/gen_outputs.py pair_corr /app/outputs/step_02_pair_correlation_difference.csv
