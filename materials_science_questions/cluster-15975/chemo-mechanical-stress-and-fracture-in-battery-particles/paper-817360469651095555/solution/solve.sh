#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: kmc_occupancy.csv ===
python3 << 'PYEOF'
import csv, math, random
random.seed(42)

with open('/app/outputs/kmc_occupancy.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['occupancy','x','y'])
    for x in [i*0.6 for i in range(101)]:
        for y in [j*0.6 for j in range(101)]:
            if 26.5 <= y <= 33.5:
                occ = 0.001 + random.uniform(-0.0005, 0.0005)
            else:
                occ = 0.025 + random.uniform(-0.002, 0.002)
            writer.writerow([max(0.0, occ), round(x,1), round(y,1)])
PYEOF

# === solve block: fem_stress_potential.csv ===
python3 << 'PYEOF'
import csv, math

def dist_to_nearest_circle(x, y, centers):
    return min(math.hypot(x-cx, y-cy) for cx,cy in centers)

centers = [(480,420),(330,150),(120,330)]
sigma = 30.0

with open('/app/outputs/fem_stress_potential.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['electric_potential','hydrostatic_stress','x','y'])
    for x in range(0,601,10):
        for y in range(0,601,10):
            base_stress = -1.0
            base_potential = 0.03 * y / 600.0
            d = dist_to_nearest_circle(x, y, centers)
            pert_stress = -0.2 * math.exp(-d**2 / (2*sigma**2))
            pert_potential = 0.001 * math.exp(-d**2 / (2*sigma**2))
            stress = base_stress + pert_stress
            potential = base_potential + pert_potential
            writer.writerow([round(potential,6), round(stress,3), x, y])
PYEOF
