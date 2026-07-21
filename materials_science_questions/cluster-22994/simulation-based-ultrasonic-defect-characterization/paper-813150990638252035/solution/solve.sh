#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: velocity_profiles.json ===
python3 /solution/generate_outputs.py velocity_profiles.json

# === solve block: computational_time.json ===
python3 /solution/generate_outputs.py computational_time.json
