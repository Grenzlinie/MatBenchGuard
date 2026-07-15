#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: angular_functions.csv ===
python3 - <<'PYEOF'
import csv, math

kappas = [0.2, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]
thetas_deg = list(range(0, 181))   # 0..180 inclusive

with open('/app/outputs/angular_functions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['kappa', 'theta_deg', 'R_c', 'R_s'])
    for kappa in kappas:
        for deg in thetas_deg:
            theta = math.radians(deg)
            cos = math.cos(theta)
            sin = math.sin(theta)
            denom = cos*cos + kappa*kappa * sin*sin
            # R_c = sqrt( (sqrt(cos^2 + k^2 sin^2) + cos) / (2*(cos^2 + k^2 sin^2)) )
            R_c = math.sqrt((math.sqrt(denom) + cos) / (2.0 * denom))
            # R_s(kappa, theta) = R_c(kappa, 180° - theta)
            theta2 = math.radians(180 - deg)
            cos2 = math.cos(theta2)
            sin2 = math.sin(theta2)
            denom2 = cos2*cos2 + kappa*kappa * sin2*sin2
            R_s = math.sqrt((math.sqrt(denom2) + cos2) / (2.0 * denom2))
            writer.writerow([kappa, deg, R_c, R_s])
PYEOF
