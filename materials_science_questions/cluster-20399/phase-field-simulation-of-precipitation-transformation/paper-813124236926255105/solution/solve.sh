#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/gen_curves.py

# === solve block: stress_strain_curves.csv ===
true

# === solve block: temperature_evolution.csv ===
true

# === solve block: band_angle.json ===
true
