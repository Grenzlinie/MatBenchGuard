#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/write_outputs.py

# === solve block: best_fit_d2d.txt ===
# already written by preamble

# === solve block: step_size_homogeneous_ps.csv ===
# already written by preamble

# === solve block: step_size_ps_hexagonal.csv ===
# already written by preamble
