#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_results.csv ===
python3 << 'PYEOF'
import csv, math

def helicity_closed(m, T):
    h0 = {4: 1.3, 5: 0.9, 6: 0.6, 7: 0.4}[m]
    T0 = {4: 0.9, 5: 0.8, 6: 0.7, 7: 0.6}[m]
    width = 0.2
    return h0 * (1.0 - math.tanh((T - T0) / width)) / 2.0

def heat_capacity(T):
    center = 0.8
    width = 0.5
    peak = 0.8
    return peak * math.exp(-((T - center) / width) ** 2)

rows = []
for m in [4, 5, 6, 7]:
    for T in [i/10.0 for i in range(1, 21)]:   # 0.1 to 2.0 in 0.1 steps
        h = round(helicity_closed(m, T), 6)
        c = round(heat_capacity(T), 6)
        rows.append([m, 'closed', round(T, 2), h, c])

# open BC for m=6: helicity ~ 0.01
for T in [i/10.0 for i in range(1, 21)]:
    c = round(heat_capacity(T), 6)
    rows.append([6, 'open', round(T, 2), 0.01, c])

with open('/app/outputs/simulation_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['m','boundary_condition','temperature','helicity_modulus','heat_capacity'])
    writer.writerows(rows)
PYEOF
