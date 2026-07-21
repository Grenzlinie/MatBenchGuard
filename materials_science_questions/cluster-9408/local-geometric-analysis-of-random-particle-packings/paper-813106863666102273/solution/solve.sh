#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: percolation_curves_chi0.5.csv ===
python3 /solution/write_outputs.py --output /app/outputs/percolation_curves_chi0.5.csv --chi 0.5

# === solve block: percolation_curves_chi0.1.csv ===
python3 /solution/write_outputs.py --output /app/outputs/percolation_curves_chi0.1.csv --chi 0.1

# === solve block: percolation_curves_chi0.9.csv ===
python3 /solution/write_outputs.py --output /app/outputs/percolation_curves_chi0.9.csv --chi 0.9

# === solve block: fractal_dimension_chi0.5.txt ===
python3 /solution/write_outputs.py --output /app/outputs/fractal_dimension_chi0.5.txt --fractal
