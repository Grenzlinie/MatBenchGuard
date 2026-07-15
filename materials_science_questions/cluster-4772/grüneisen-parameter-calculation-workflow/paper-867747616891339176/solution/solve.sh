#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: thermal_expansion_coefficient.txt ===
python3 -c "
import math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
d_c = 1
k0   = 1.0
g0   = 0.05
eta  = 0.8
alpha = -d_c / (8 * math.pi * k0) * (2/eta + math.log(1/g0))
with open(os.path.join(outdir, 'thermal_expansion_coefficient.txt'), 'w') as f:
    f.write(f'{alpha:.8f}\n')
"
