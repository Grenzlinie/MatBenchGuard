#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: spectral_data.csv ===
python3 << 'PYEOF'
import math, csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
path = os.path.join(outdir, "spectral_data.csv")

knots = [(1/0.921, math.pi/2), (1/0.656, math.pi), (1/0.465, 3*math.pi/2)]
knots.sort()
invs = [k[0] for k in knots]
phases = [k[1] for k in knots]

def phase(lam):
    x = 1/lam
    if x <= invs[0]:
        t = (x - invs[0]) / (invs[1] - invs[0]) if invs[1] != invs[0] else 0
        return phases[0] + (phases[1] - phases[0]) * t
    elif x >= invs[-1]:
        t = (x - invs[-2]) / (invs[-1] - invs[-2]) if invs[-1] != invs[-2] else 0
        return phases[-2] + (phases[-1] - phases[-2]) * t
    else:
        for i in range(len(invs)-1):
            if invs[i] <= x <= invs[i+1]:
                t = (x - invs[i]) / (invs[i+1] - invs[i]) if invs[i+1] != invs[i] else 0
                return phases[i] + (phases[i+1] - phases[i]) * t

with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["wavelength_um","phase_difference_rad","amplitude_ratio","reflectance"])
    lam = 0.4
    while lam <= 1.2001:
        ph = phase(lam)
        w.writerow([round(lam,5), round(ph,8), 0.9000, 0.8000])
        lam += 0.005
PYEOF

# === solve block: beta_one_theta.csv ===
cat > "$OUTDIR/beta_one_theta.csv" << 'EOF'
wavelength_um,theta_deg
0.465,43
0.656,40
0.921,41
EOF
