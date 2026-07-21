#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: intensity_factors.json ===
sed -i '1s/^/import scipy.integrate\n/' /solution/compute_intensity.py && sed -i 's/\bnp\.trapz\b/scipy.integrate.trapezoid/g' /solution/compute_intensity.py && python3 /solution/compute_intensity.py "$OUTDIR/intensity_factors.json"
