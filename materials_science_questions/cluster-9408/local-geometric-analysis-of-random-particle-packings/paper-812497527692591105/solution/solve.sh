#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 /solution/generate_oracle_outputs.py

# === solve block: free_theoretical.csv ===
true

# === solve block: sticking_theoretical.csv ===
true

# === solve block: free_simulation.csv ===
true

# === solve block: sticking_simulation.csv ===
true

# === solve block: results_summary.json ===
true
