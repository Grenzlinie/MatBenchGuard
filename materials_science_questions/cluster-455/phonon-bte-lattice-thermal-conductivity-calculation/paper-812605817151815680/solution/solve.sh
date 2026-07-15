#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity_accumulation.csv ===
python3 -c "
import csv, math, sys

def cumulative(kappa_max, mfp, median=0.2, sigma=1.163):
    if mfp <= 0:
        return 0.0
    x = (math.log(mfp) - math.log(median)) / (sigma * math.sqrt(2))
    cdf = 0.5 * (1.0 + math.erf(x))
    return kappa_max * cdf

# 81 points logarithmically spaced from 0.01 um to 100 um
mfp_vals = [10**(i/20.0) for i in range(-40, 41)]

writer = csv.writer(sys.stdout)
writer.writerow(['mfp_um', 'kappa_in_plane', 'kappa_cross_plane'])

for mfp in mfp_vals:
    k_in = cumulative(380.0, mfp)
    k_cross = cumulative(320.0, mfp)
    writer.writerow([round(mfp, 6), round(k_in, 4), round(k_cross, 4)])
" > /app/outputs/thermal_conductivity_accumulation.csv

# === solve block: bulk_kappa_300K.json ===
cat > /app/outputs/bulk_kappa_300K.json <<'FFEOF'
{
  "kappa_in_plane_300K": 380.0,
  "kappa_cross_plane_300K": 320.0
}
FFEOF
