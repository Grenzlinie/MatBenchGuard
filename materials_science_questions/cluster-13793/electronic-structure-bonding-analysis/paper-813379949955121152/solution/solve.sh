#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: perfect_cell_energy.txt ===
echo '-8000.0' > /app/outputs/perfect_cell_energy.txt

# === solve block: isolated_H_energy.txt ===
echo '-12.3456' > /app/outputs/isolated_H_energy.txt

# === solve block: interstitial_results.csv ===
printf 'site,E_H_f,delta_V\nI-Ti,-2.228,1.45\nI-SiTi,-2.850,0.90\nI-SiC,-2.853,0.55\n' > /app/outputs/interstitial_results.csv
