#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_stress_strain_curves.tar.gz ===
python3 /solution/generate_curves.py "$OUTDIR"
cd "$OUTDIR"
tar czf step_01_stress_strain_curves.tar.gz *.csv
rm -f *.csv
cd - > /dev/null
