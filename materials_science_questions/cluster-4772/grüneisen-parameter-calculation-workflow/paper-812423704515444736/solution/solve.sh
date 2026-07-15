#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: dos_data.csv ===
sed -i 's/from scipy.integrate import trapz, cumulative_trapezoid/from scipy.integrate import trapezoid as trapz, cumulative_trapezoid/' /solution/compute.py && python3 /solution/compute.py dos > /app/outputs/dos_data.csv

# === solve block: thermo_properties.csv ===
python3 /solution/compute.py thermo > /app/outputs/thermo_properties.csv

# === solve finalize ===
echo "All outputs written."
