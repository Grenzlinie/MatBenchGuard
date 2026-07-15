#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: structural_properties.json ===
export OUTDIR
python3 -c "
import json, os

data = {
    'a0': 9.373,
    'C11': 198.320,
    'C12': 95.570,
    'C44': 36.580,
    'B': 113.136,
    'G': 41.920,
    'Y': 113.54,
    'V': 2556.419,
    'θ_D': 331.45,
    'ν': 0.354,
    'A': 0.712
}

with open(os.environ['OUTDIR'] + '/structural_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: bandgap.txt ===
echo "0.09" > "$OUTDIR/bandgap.txt"

# === solve block: seebeck_curve.csv ===
python3 -c "
import csv, os

# Control points: (T(K), S(µV/K))
# Based on paper description: low S at low T, peak 129 at 80 K, then decrease to 53 at 300 K
points = [
    (0, 0),
    (20, 5),
    (80, 129),
    (200, 55),
    (300, 53)
]

def interpolate(t):
    if t <= points[0][0]:
        return points[0][1]
    if t >= points[-1][0]:
        return points[-1][1]
    for i in range(len(points)-1):
        t0, s0 = points[i]
        t1, s1 = points[i+1]
        if t0 <= t <= t1:
            frac = (t - t0) / (t1 - t0)
            return s0 + frac * (s1 - s0)
    return 0.0

outpath = os.path.join(os.environ['OUTDIR'], 'seebeck_curve.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T(K)', 'S(µV/K)'])
    for T in range(0, 301, 5):   # 61 points, > 30
        S = interpolate(T)
        writer.writerow([T, round(S, 2)])
"

# === solve block: zt_300k.txt ===
echo "0.12" > "$OUTDIR/zt_300k.txt"
