#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thin_film_stress_alpha.csv ===
python3 /solution/generate_all.py thin_film > /app/outputs/thin_film_stress_alpha.csv

# === solve block: spherical_lithiation_evolution.csv ===
python3 /solution/generate_all.py spherical > /app/outputs/spherical_lithiation_evolution.csv

# === solve block: equilibrium_core_radius.csv ===
python3 /solution/generate_all.py equilibrium > /app/outputs/equilibrium_core_radius.csv

# === solve block: energy_release_rate.csv ===
python3 /solution/generate_all.py energy > /app/outputs/energy_release_rate.csv

# === solve block: gmax_vs_R.csv ===
python3 /solution/generate_all.py gmax > /app/outputs/gmax_vs_R.csv
