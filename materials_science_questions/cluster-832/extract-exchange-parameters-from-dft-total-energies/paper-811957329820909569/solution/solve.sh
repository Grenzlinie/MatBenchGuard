#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy 2>/dev/null || true

# === solve block: potentials.json ===
python3 /solution/generate_data.py --mode potentials --output /app/outputs/potentials.json
