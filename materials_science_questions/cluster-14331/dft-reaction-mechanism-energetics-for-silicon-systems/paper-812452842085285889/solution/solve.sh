#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: sif4_binding_curve.csv ===
python3 /solution/generate.py sif4_binding_curve /app/outputs/sif4_binding_curve.csv

# === solve block: hf2_dissociation_surface.csv ===
python3 /solution/generate.py hf2_dissociation_surface /app/outputs/hf2_dissociation_surface.csv

# === solve block: desorption_energy_surface_without_Hplus.csv ===
python3 /solution/generate.py desorption_surface_without_hplus /app/outputs/desorption_energy_surface_without_Hplus.csv

# === solve block: desorption_energy_surface_with_Hplus.csv ===
python3 /solution/generate.py desorption_surface_with_hplus /app/outputs/desorption_energy_surface_with_Hplus.csv

# === solve block: activation_energy_report.json ===
python3 /solution/generate.py activation_energy_report /app/outputs/activation_energy_report.json

# === solve block: angle_population_trend.csv ===
python3 /solution/generate.py angle_population_trend /app/outputs/angle_population_trend.csv
