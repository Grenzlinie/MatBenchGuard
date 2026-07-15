#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: average_energy.csv ===
sed -i 's/\bnp\.trapz(\b/np.trapezoid(/' /solution/generate.py
python3 /solution/generate.py --output average_energy.csv

# === solve block: energy_histogram_10kVcm.csv ===
python3 /solution/generate.py --output energy_histogram_10kVcm.csv

# === solve block: dispersion_scatter_10kVcm.csv ===
python3 /solution/generate.py --output dispersion_scatter_10kVcm.csv
