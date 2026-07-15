#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
cp /solution/generate_curves.py /tmp/generate_curves.py

# === solve block: stage1_stress_strain.csv ===
python3 /tmp/generate_curves.py --output /app/outputs/stage1_stress_strain.csv --mode stress_strain

# === solve block: stage2_mean_yield_stress.csv ===
python3 /tmp/generate_curves.py --output /app/outputs/stage2_mean_yield_stress.csv --mode mean_yield_stress

# === solve block: stage3_localization_index.csv ===
python3 /tmp/generate_curves.py --output /app/outputs/stage3_localization_index.csv --mode localization_index
