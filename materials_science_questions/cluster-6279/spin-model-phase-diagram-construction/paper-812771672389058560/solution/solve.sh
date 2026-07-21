#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: transition_lines.csv ===
python3 << 'PYEOF'
import csv, math

z_star = 1/(4*math.pi)
T_star = 0.25

# continuous (KT) line: T = T_star for z ∈ [0, z_star]
N_kt = 101
kt_points = []
for i in range(N_kt):
    z = z_star * i / (N_kt - 1)
    kt_points.append((z, T_star, 0))

# first-order line: Eq. (21) for T ∈ (0.1, 0.25]
N_fo = 200
fo_points = []
# sample T linearly from T_star down to 0.1
for i in range(N_fo):
    T = T_star - (T_star - 0.1) * i / (N_fo - 1)
    if T <= 0:
        continue
    a = 1/(4*T)
    # avoid domain issues: a > 1 for T < 0.25
    if a <= 1:
        continue  # should not happen
    # compute z = (T/π) * a**(1+a) * (a-1)**(1-a)
    try:
        z = (T/math.pi) * (a**(1+a)) * ((a-1)**(1-a))
        if z <= 1.0 and z >= z_star:
            fo_points.append((z, T, 1))
    except Exception:
        continue

# sort first-order by z ascending
fo_points.sort(key=lambda x: x[0])

# combine and sort overall
all_points = kt_points + fo_points
all_points.sort(key=lambda x: x[0])

with open('/app/outputs/transition_lines.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['z', 'T', 'transition_type'])
    for row in all_points:
        writer.writerow(row)
PYEOF

# === solve block: tricritical_point.json ===
python3 << 'PYEOF'
import json, math

z_star = 1/(4*math.pi)
T_star = 0.25

data = {"z_star": z_star, "T_star": T_star}

with open('/app/outputs/tricritical_point.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
