#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: shape_nominal.csv ===
python3 /solution/compute.py shape 1e-6 0.2 /app/outputs/shape_nominal.csv

# === solve block: max_amplitude_vs_delta.csv ===
python3 /solution/compute.py delta_sweep 1e-6 /app/outputs/max_amplitude_vs_delta.csv

# === solve block: max_amplitude_vs_epsilon.csv ===
python3 /solution/compute.py epsilon_sweep 0.2 /app/outputs/max_amplitude_vs_epsilon.csv
