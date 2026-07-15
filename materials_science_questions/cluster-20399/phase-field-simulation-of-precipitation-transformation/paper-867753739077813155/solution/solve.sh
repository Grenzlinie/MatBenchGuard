#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple jsonschema 2>/dev/null || true

# === solve block: velocities.csv ===
python3 /solution/compute_velocities.py > /app/outputs/velocities.csv
