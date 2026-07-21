#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs && python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: cluster_distributions.json ===
python3 /solution/generate_cluster.py > /app/outputs/cluster_distributions.json

# === solve block: magnetization_curves.json ===
python3 /solution/generate_mag.py > /app/outputs/magnetization_curves.json
