#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.csv ===
python3 /solution/generate_outputs.py fitted_parameters.csv

# === solve block: pr_vs_pressure.csv ===
python3 /solution/generate_outputs.py pr_vs_pressure.csv

# === solve block: crossover_pressure.txt ===
python3 /solution/generate_outputs.py crossover_pressure.txt
