#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: traction_separation_curve.csv ===
python3 - <<'PYEOF'
import numpy as np

Pc = 5.5       # MPa
zeta_c = 1.1   # mm
k = 1000.0     # MPa/mm (penalty stiffness)

cases = [
    ("zeta_b=0", 0.0),
    ("zeta_b=0.2", 0.2)
]

rows = []
for case_name, zeta_b in cases:
    Hc = Pc / (zeta_c - zeta_b)   # softening slope
    zeta = 0.0
    Q = 0.0
    # monotonic opening from 0.0 to 1.2 mm in steps of 0.01 mm
    for d in np.arange(0.0, 1.21, 0.01):
        d = round(d, 5)           # mitigate floating-point stair-step
        if zeta >= zeta_c:
            # fully open – traction drops to zero
            traction = 0.0
            zeta = d               # gap follows the applied opening
        else:
            trial = max(k * (d - zeta), 0.0)
            f_trial = trial - (Pc - Q)
            if f_trial <= 0:
                traction = trial   # elastic loading
            else:
                # plastic flow – region-based Δγ
                if zeta <= zeta_b:
                    # forward damage (plateau)
                    delta_gamma = f_trial / k
                    delta_Q = 0.0
                elif zeta < zeta_c:
                    # wake damage (softening)
                    delta_gamma = f_trial / (k - Hc)
                    delta_Q = Hc * delta_gamma
                else:
                    delta_gamma = 0.0
                    delta_Q = 0.0
                zeta += delta_gamma
                Q += delta_Q
                if zeta >= zeta_c:
                    traction = 0.0
                    Q = Pc          # enforce zero traction
                else:
                    traction = Pc - Q
        rows.append((d, traction, case_name))

# write CSV with required columns and ordering
with open("/app/outputs/traction_separation_curve.csv", "w") as f:
    f.write("opening_gap_mm,traction_MPa,case\n")
    for d, t, c in rows:
        f.write(f"{d:.2f},{t:.6f},{c}\n")
PYEOF
