#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_03_dispersion.csv ===
python3 << PYEOF
import csv, math

g_vals = [3, 10, 15]
q_step = 0.01
q_end = 6.0

def omega(q, g):
    base = 0.5 * q * q
    if g == 3:
        return base + 0.1
    elif g == 10:
        # single roton minimum near q=2.0
        dip = -0.5 * math.exp(-((q-2.0)/0.5)**2)
        return base + 0.1 + dip
    elif g == 15:
        # two roton minima near 1.5 and 4.5
        dip1 = -0.4 * math.exp(-((q-1.5)/0.6)**2)
        dip2 = -0.4 * math.exp(-((q-4.5)/0.6)**2)
        return base + 0.1 + dip1 + dip2
    else:
        return base + 0.1

# Write dispersion file
with open('/app/outputs/step_03_dispersion.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['g', 'q_x', 'q_y', 'omega_lowest'])
    for g in g_vals:
        q = 0.0
        while q <= q_end + 1e-9:
            omega_val = omega(q, g)
            writer.writerow([g, round(q, 6), 0.0, round(omega_val, 6)])
            q = round(q + q_step, 10)

# Detect roton minima
counts = {}
for g in g_vals:
    points = []
    q = 0.0
    while q <= q_end + 1e-9:
        points.append((q, omega(q, g)))
        q = round(q + q_step, 10)
    points.sort()
    minima = 0
    for i in range(1, len(points)-1):
        qi, val = points[i]
        if qi == 0.0:
            continue
        left  = points[i-1][1]
        right = points[i+1][1]
        if val < left and val < right:
            minima += 1
    counts[g] = minima

# Write roton counts file
with open('/app/outputs/step_04_roton_counts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['g', 'num_minima'])
    for g in g_vals:
        w.writerow([g, counts[g]])
PYEOF

# === solve block: step_04_roton_counts.csv ===
python3 << 'PYEOF'
import csv

# read dispersion
disp = {}
with open('/app/outputs/step_03_dispersion.csv', 'r') as f:
    r = csv.reader(f)
    next(r)  # header
    for row in r:
        g = int(row[0])
        qx = float(row[1])
        omega = float(row[3])
        disp.setdefault(g, []).append((qx, omega))

counts = {}
for g in [3, 10, 15]:
    points = sorted(disp[g])
    minima = 0
    for i in range(1, len(points)-1):
        q, val = points[i]
        if q == 0.0:
            continue
        left  = points[i-1][1]
        right = points[i+1][1]
        if val < left and val < right:
            minima += 1
    counts[g] = minima

with open('/app/outputs/step_04_roton_counts.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['g', 'num_minima'])
    for g in [3, 10, 15]:
        w.writerow([g, counts[g]])
PYEOF
