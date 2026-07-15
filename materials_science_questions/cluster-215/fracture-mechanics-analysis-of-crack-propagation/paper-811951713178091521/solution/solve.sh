#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 - <<'PYEOF'
import math
import json

# given parameters
s = 0.6
nu = 0.3
alpha = 0.5
beta = 0.2
G_IC = 200.0
M = 1000.0

# -- twist drill baseline F_A
F_A = math.pi * math.sqrt(32.0 * G_IC * M)

# -- C1, C2 for saw drill
lns = math.log(s)
term = 3.0 + 2.0 * lns
s2 = s * s
s4 = s2 * s2
s6 = s4 * s2

C1 = 1.0 - term * s2 + term * s4 - s6
C2 = (1.0 + 2.0 * lns) * s2 - (2.0 + 2.0 * lns) * s4 + s6

den_SD = C1 + nu * C2
F_SD = F_A / math.sqrt(den_SD)
ratio_SD = 1.0 / math.sqrt(den_SD)

# -- candle stick drill
term_CD = 1.0 + (alpha * alpha) * den_SD
F_CD = (1.0 + alpha) * F_A / math.sqrt(term_CD)
ratio_CD = (1.0 + alpha) / math.sqrt(term_CD)

# -- core drill coefficients
# precomputations
b1 = 1.0 - beta
b1_sq = b1 * b1
linprod = beta * (2.0 - beta)
ln1mb = math.log(b1)
factor = (2.0 * b1_sq) / linprod
A = factor * ln1mb

A_coeff = 2.0 - 2.0 * beta + beta * beta   # (2 - 2β + β^2)
term1_coeff = 2.0 - 2.0 * beta + 1.5 * beta * beta   # 2 - 2β + 1.5 β^2
Q = term1_coeff + 2.0*lns + A
term1_C3 = -Q * s2   # note C3 formula: 1 - Q*s^2 + ...
# second term in C3
inner_C3 = (2.0 - beta + beta*beta) / 2.0 + lns + (b1_sq / linprod) * ln1mb
term2_C3_coeff = A_coeff * inner_C3
term2_C3 = term2_C3_coeff * s4
# third term in C3
term3_C3 = -(A_coeff * A_coeff / 4.0) * s6
C3 = 1.0 + term1_C3 + term2_C3 + term3_C3

# C4
# first term in C4
first_C4 = (2.0*lns - A) * s2
# second term in C4
inner_C4 = -0.5 - lns + (b1_sq / linprod) * ln1mb
term2_C4 = A_coeff * inner_C4 * s4
# third term in C4
term3_C4 = (A_coeff * A_coeff / 4.0) * s6
C4 = first_C4 + term2_C4 + term3_C4

den_RD = C3 + nu * C4
F_RD = F_A / math.sqrt(den_RD)
ratio_RD = 1.0 / math.sqrt(den_RD)

results = {
    "saw_drill": {
        "F_SD": F_SD,
        "F_A": F_A,
        "ratio_SD": ratio_SD
    },
    "candle_stick_drill": {
        "F_CD": F_CD,
        "F_A": F_A,
        "ratio_CD": ratio_CD
    },
    "core_drill": {
        "F_RD": F_RD,
        "F_A": F_A,
        "ratio_RD": ratio_RD
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
