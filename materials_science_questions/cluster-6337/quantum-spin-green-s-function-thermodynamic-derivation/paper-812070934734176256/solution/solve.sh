#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: dispersion_k.csv ===
python3 /solution/compute_reference.py --mode dispersion --output /app/outputs/dispersion_k.csv

# === solve block: critical_temperature.json ===
python3 /solution/compute_reference.py --mode critical --output /app/outputs/critical_temperature.json
