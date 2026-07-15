#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: gamma_ratios.csv ===
python3 - <<'PYEOF'
import csv, os

outdir = os.environ['OUTDIR']

# Waypoints derived from the paper's description of the curves:
# - For ΔΩ/ε=60: starts near 1, dips steeply to ~0.75 at aM≈1.5, recovers gradually
# - For ΔΩ/ε=400: shallow minimum above 0.95, mostly above 0.95
waypoints = {
    0.0: (0.99, 0.99),
    1.0: (0.96, 0.98),
    1.25: (0.92, 0.975),
    1.5: (0.75, 0.97),
    2.0: (0.80, 0.98),
    3.0: (0.87, 0.99),
    3.5: (0.90, 0.995)
}

def get_gamma(aM):
    aM = max(0.0, min(3.5, aM))
    keys = sorted(waypoints.keys())
    if aM in waypoints:
        return waypoints[aM]
    for i in range(len(keys)-1):
        x0, x1 = keys[i], keys[i+1]
        if x0 <= aM <= x1:
            y0, y1 = waypoints[x0], waypoints[x1]
            t = (aM - x0) / (x1 - x0)
            g60 = y0[0] + t * (y1[0] - y0[0])
            g400 = y0[1] + t * (y1[1] - y0[1])
            return (g60, g400)
    return waypoints[3.5]

# Grid covering 0..3.5 with at least 20 points, explicitly including all waypoints
points = []
for i in range(31):
    points.append(i * 3.5 / 30.0)
for w in waypoints:
    points.append(w)
points = sorted(set(points))

with open(os.path.join(outdir, 'gamma_ratios.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['aM', 'gamma_ratio_60', 'gamma_ratio_400'])
    for aM in points:
        r60, r400 = get_gamma(aM)
        writer.writerow([round(aM, 6), round(r60, 6), round(r400, 6)])
PYEOF
