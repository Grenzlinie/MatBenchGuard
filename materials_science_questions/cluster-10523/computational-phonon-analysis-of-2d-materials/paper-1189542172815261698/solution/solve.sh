#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_parameters.csv ===
python3 /solution/generate_outputs.py lattice > /app/outputs/lattice_parameters.csv

# === solve block: poisson_ratios.csv ===
python3 /solution/generate_outputs.py poisson > /app/outputs/poisson_ratios.csv

# === solve block: diffuse_line_cuts.csv ===
python3 /solution/generate_outputs.py linecuts > /app/outputs/diffuse_line_cuts.csv

# === solve block: fitting_results.csv ===
python3 /solution/generate_outputs.py fitting > /app/outputs/fitting_results.csv
