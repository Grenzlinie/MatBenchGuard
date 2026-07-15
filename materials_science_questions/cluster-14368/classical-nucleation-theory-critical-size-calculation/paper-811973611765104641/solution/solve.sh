#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
cat > /tmp/gen.py << 'PYEOF'
import math, json, csv

# compute r0 from liquid density n = 0.15 fm^{-3}
n = 0.15
r0 = (3 / (4 * math.pi * n)) ** (1/3)

# model parameters
sigma = 1.0   # MeV fm^{-2}
T = 10.0      # MeV
tau = 2.2
Svals = [1, 2, 3, 4]

# radius grid: 0.1 to 10 fm, 2000 points (dense enough to locate peaks within tolerance)
rmin, rmax = 0.1, 10.0
num_pts = 2000
dr = (rmax - rmin) / (num_pts - 1)

rows = []
peaks = {}

for S in Svals:
    lnS = math.log(S)
    best_r = None
    best_dG = None
    for i in range(num_pts):
        r = rmin + i * dr
        # ΔG = surface term + volume term + logarithmic entropy correction
        dG = 4 * math.pi * sigma * r**2 \
             - (4 / 3) * math.pi * n * T * lnS * r**3 \
             + 3 * T * tau * math.log(r / r0)
        rows.append((r, S, dG))
        if S > 1:
            if best_dG is None or dG > best_dG:
                best_dG = dG
                best_r = r
    if S > 1:
        peaks[S] = best_r

# write delta_g_vs_r.csv
with open('/app/outputs/delta_g_vs_r.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['r', 'S', 'delta_G'])
    w.writerows(rows)

# write critical_radii.json
critical = {'S2': peaks[2], 'S3': peaks[3], 'S4': peaks[4]}
with open('/app/outputs/critical_radii.json', 'w') as f:
    json.dump(critical, f, indent=2)
PYEOF

# === solve block: delta_g_vs_r.csv ===
python3 /tmp/gen.py

# === solve block: critical_radii.json ===
echo 'critical_radii.json already written by gen.py'
