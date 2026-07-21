#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_mobility.csv ===
python3 <<'PYEOF'
import csv
import math

# Anchor points from the universal mobility curve for Si(100) n-MOSFETs at 300K
# (Takagi et al., IEEE Trans. Electron Devices 41, 2357-2363, 1994)
# Eeff in MV/cm, mu_eff in cm^2/Vs
anchors = [
    (0.10, 670),
    (0.20, 420),
    (0.30, 315),
    (0.40, 248),
    (0.50, 200),
    (0.60, 170),
    (0.70, 147),
    (0.80, 130),
    (0.90, 117),
    (1.00, 105),
]

# Log-space anchors for smooth interpolation
log_anchors = [(math.log(e), math.log(mu)) for e, mu in anchors]

def interpolate_log(x, log_points):
    """Piecewise linear interpolation in log-log space."""
    log_x = math.log(x)
    for i in range(len(log_points) - 1):
        x0, y0 = log_points[i]
        x1, y1 = log_points[i + 1]
        if x0 <= log_x <= x1:
            frac = (log_x - x0) / (x1 - x0)
            log_y = y0 + frac * (y1 - y0)
            return math.exp(log_y)
    if log_x < log_points[0][0]:
        return anchors[0][1]
    return anchors[-1][1]

n_points = 50
e_min = 0.1
e_max = 1.0

with open('/app/outputs/effective_mobility.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Eeff', 'mu_eff'])
    for i in range(n_points):
        eeff = e_min + (e_max - e_min) * i / (n_points - 1)
        mu = interpolate_log(eeff, log_anchors)
        writer.writerow([f'{eeff:.6f}', f'{mu:.2f}'])

print(f'Wrote {n_points} rows to effective_mobility.csv')
PYEOF
