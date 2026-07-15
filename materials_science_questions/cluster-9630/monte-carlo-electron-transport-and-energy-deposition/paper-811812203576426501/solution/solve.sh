#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: radial_profile.csv ===
python3 <<'PY' > /app/outputs/radial_profile.csv
import math, csv
sigma = 13.5 / (2 * math.sqrt(2 * math.log(2)))
with open('/dev/stdout', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r0_um', 'Jprime_A'])
    r = 0.0
    while r <= 40.0:
        val = math.exp(-((r-18.0)**2) / (2 * sigma**2))
        writer.writerow([f'{r:.1f}', f'{val:.6f}'])
        r += 0.1
PY

# === solve block: angular_distribution.csv ===
python3 <<'PY' > /app/outputs/angular_distribution.csv
import math, csv
alpha = 2.614
with open('/dev/stdout', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta_deg', 'I_theta'])
    theta = 0.0
    while theta <= 90.0:
        val = math.exp(-theta / alpha)
        writer.writerow([f'{theta:.1f}', f'{val:.6f}'])
        theta += 0.1
PY
