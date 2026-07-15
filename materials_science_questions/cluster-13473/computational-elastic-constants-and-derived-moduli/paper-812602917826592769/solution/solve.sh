#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: stress_strain_curve_tension_X.csv ===
python3 /solution/create_curves.py X tension > /app/outputs/stress_strain_curve_tension_X.csv

# === solve block: stress_strain_curve_tension_Y.csv ===
python3 /solution/create_curves.py Y tension > /app/outputs/stress_strain_curve_tension_Y.csv

# === solve block: stress_strain_curve_tension_Z.csv ===
python3 /solution/create_curves.py Z tension > /app/outputs/stress_strain_curve_tension_Z.csv

# === solve block: stress_strain_curve_compression_X.csv ===
python3 /solution/create_curves.py X compression > /app/outputs/stress_strain_curve_compression_X.csv

# === solve block: stress_strain_curve_compression_Y.csv ===
python3 /solution/create_curves.py Y compression > /app/outputs/stress_strain_curve_compression_Y.csv

# === solve block: stress_strain_curve_compression_Z.csv ===
python3 /solution/create_curves.py Z compression > /app/outputs/stress_strain_curve_compression_Z.csv

# === solve block: summary.json ===
python3 /solution/compute_summary.py > /app/outputs/summary.json
