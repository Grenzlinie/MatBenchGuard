#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: contact_coordination.csv ===
python3 -c "
import math
eps = 0.36
ratios = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]
factor = 1.0 - eps
with open(\"$OUTDIR/contact_coordination.csv\", 'w') as f:
    for r in ratios:
        c = factor * ((r + 1.0)**3 - 1.0) / (r**3)
        f.write(f'{r},{c}\n')
"

# === solve block: geometric_neighbors.txt ===
python3 -c "
import math
eps = 0.36
L_over_d = math.sqrt(2.0)
C = (1.0 - eps) * (8.0 * (L_over_d)**3 - 1.0)
with open('$OUTDIR/geometric_neighbors.txt', 'w') as f:
    f.write(f'{C}\n')
"
