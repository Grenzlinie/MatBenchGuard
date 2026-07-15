#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_validation_contour.csv ===
python3 /solution/compute_validation.py

# === solve block: step_02_growth_da16.csv ===
python3 /solution/generate_shapes.py da16

# === solve block: step_03_growth_da400.csv ===
python3 /solution/generate_shapes.py da400

# === solve block: step_04_fractal_dimensions.json ===
python3 /solution/compute_fractal.py

# === solve block: step_05_theoretical_critical_spacing.json ===
python3 << 'PYEOF'
import json, math, os
lam_p = 1.5
S = 1.20
lam_c = 2 * math.pi * lam_p * math.sqrt(S / (S - 1))
out = os.environ["OUTDIR"] + "/step_05_theoretical_critical_spacing.json"
with open(out, "w") as f:
    json.dump({"lambda_c": lam_c}, f)
PYEOF
