#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predictions.csv ===
python3 << 'PYEOF'
import math

Em = 3.11
E_CNT = 800.0
Sm = 64.51
S_CNT = 18.0
L = 2e-6
d = 30e-9
R = L / d
fR = 1.0/6.0
fW = 0.6
alpha = 10.0
beta = 0.9

vals = []
v = 0.0
while v <= 0.07000001:
    fA = math.exp(-alpha * (v ** beta))
    # elastic modulus
    term_E = fR * fW * fA * (E_CNT / Em)
    delta_E = (term_E - 1.0) / (term_E + 2.0 * R)
    E_val = Em * (1.0 + 2.0 * R * delta_E * v) / (1.0 - delta_E * v)
    # tensile strength
    term_S = fR * fW * fA * (S_CNT / Em)
    delta_S = (term_S - 1.0) / (term_S + 2.0 * R)
    S_val = Sm * (1.0 + 2.0 * R * delta_S * v) / (1.0 - delta_S * v)
    vals.append((v, E_val, S_val))
    v += 0.002

with open("/app/outputs/predictions.csv", "w") as f:
    f.write("V_CNT,E_modulus (GPa),Tensile_strength (MPa)\n")
    for vv, ee, ss in vals:
        f.write(f"{vv:.3f},{ee:.15g},{ss:.15g}\n")
PYEOF
