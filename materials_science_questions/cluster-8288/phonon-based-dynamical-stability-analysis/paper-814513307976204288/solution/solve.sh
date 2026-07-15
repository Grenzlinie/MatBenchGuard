#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/generate_artifacts.py

# === solve block: phonon_dispersion.csv ===
# written by preamble

# === solve block: dynamical_stability.json ===
# written by preamble

# === solve block: thermal_conductivity.csv ===
# written by preamble

# === solve block: thermal_fit.json ===
# written by preamble

# === solve block: stress_strain_data.csv ===
# written by preamble

# === solve block: mechanical_properties.json ===
# written by preamble
