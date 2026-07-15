#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml

# === solve block: defect_counts.csv ===
python3 /solution/helper.py defect_counts > "$OUTDIR/defect_counts.csv"

# === solve block: radial_profiles.yaml ===
python3 /solution/helper.py radial_profiles > "$OUTDIR/radial_profiles.yaml"
