#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: contrast_data_boron_layer.csv ===
test -f /app/outputs/contrast_data_boron_layer.csv

# === solve block: b_kalpha_line_scan.csv ===
test -f /app/outputs/b_kalpha_line_scan.csv

# === solve block: eta_vs_diameter_particulate.csv ===
test -f /app/outputs/eta_vs_diameter_particulate.csv

# === solve block: c_kalpha_vs_diameter_particulate.csv ===
test -f /app/outputs/c_kalpha_vs_diameter_particulate.csv

# === solve block: k_ratio_vs_thickness.csv ===
test -f /app/outputs/k_ratio_vs_thickness.csv

# === solve block: r_ratio_vs_thickness.csv ===
test -f /app/outputs/r_ratio_vs_thickness.csv
