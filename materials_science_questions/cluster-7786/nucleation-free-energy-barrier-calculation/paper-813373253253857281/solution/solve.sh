#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << PYEOF
import math, json
k = 1.380649e-23
T = 1000.0
S = 10.0
vA = 8.8e-30
sigma_cm = 1.0
sigma_cg = 1.0
sigma_mg = 1.0
lnS = math.log(S)
coef = 2 * math.pi * vA**2 / (3 * (k * T * lnS)**3)
g1 = coef * (2*sigma_cm + sigma_cg - sigma_mg)**3
g2 = coef * (sigma_cm**3)
DeltaF1_k = g1 * T * lnS / 2.0
DeltaF2_k = g2 * T * lnS / 2.0
res = {
    "g1_star": g1,
    "g2_star": g2,
    "DeltaF1_star": DeltaF1_k,
    "DeltaF2_star": DeltaF2_k
}
with open("$OUTDIR/results.json", "w") as f:
    json.dump(res, f)
PYEOF
