#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nucleus_results.json ===
python3 << 'PYEOF' > "$OUTDIR/nucleus_results.json"
import json, math

I_s = 1714.0          # G
C = 5e-6              # erg/cm

R1_cm = 1e-4           # 1 um
R2_cm = 1e-3           # 10 um

def compute(radius_cm):
    Cstar = C / (radius_cm**2 * I_s**2)
    d = 0.5 * (math.pi * Cstar) ** (1/3)
    r = 4 * (7.0 / 20.0 * Cstar / (math.pi * d)) ** 0.25
    Hs = 2 * math.pi * I_s
    return r, d, Hs

r1, d1, Hs1 = compute(R1_cm)
r2, d2, Hs2 = compute(R2_cm)

scaling = (d1 / r1**2 + d2 / r2**2) / 2.0

result = {
    "R_1um": {"r": round(r1, 8), "d": round(d1, 8), "Hs": round(Hs1, 4)},
    "R_10um": {"r": round(r2, 8), "d": round(d2, 8), "Hs": round(Hs2, 4)},
    "scaling_coefficient": round(scaling, 8)
}

print(json.dumps(result, indent=2))
PYEOF
