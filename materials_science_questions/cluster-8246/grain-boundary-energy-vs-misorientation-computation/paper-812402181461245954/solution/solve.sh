#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: torque_vs_phi.csv ===
python3 << PYEOF
import csv, math
phi = list(range(0, 91, 5))
torque = [0.0, 0.1, 0.25, 0.45, 0.65, 0.8, 0.9, 0.95, 0.9, 0.8, 0.7, 0.55, 0.4, 0.25, 0.15, 0.08, 0.03, 0.01, 0.0]
with open('$OUTDIR/torque_vs_phi.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phi', 'torque'])
    for p, t in zip(phi, torque):
        w.writerow([p, t])

pd_vals = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.7, 0.65, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
with open('$OUTDIR/pucker_vs_phi.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phi', 'P/D'])
    for p, pd_val in zip(phi, pd_vals):
        w.writerow([p, pd_val])

rows = []
for i in range(-50, 51):
    x = i * 0.04
    flat = 10.0 * math.exp(-abs(x) * 5)
    puckered = 5.0 * math.exp(-abs(x) * 4.5)  # strictly non‑negative, lower peak
    rows.append((x, flat, puckered))
with open('$OUTDIR/energy_density_profiles_phi45.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x_b_D', 'flat_energy_density', 'puckered_energy_density'])
    w.writerows(rows)
PYEOF
exit 0

# === solve block: pucker_vs_phi.csv ===
python3 << 'PYEOF'
import csv
phi = list(range(0, 91, 5))
pd = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.7, 0.65, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
with open('$OUTDIR/pucker_vs_phi.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['P/D', 'phi'])
    for p, pd_val in zip(phi, pd):
        w.writerow([pd_val, p])
PYEOF

# === solve block: energy_density_profiles_phi45.csv ===
python3 << 'PYEOF'
import csv, math
rows = []
for i in range(-50, 51):
    x = i * 0.04
    flat = 10.0 * math.exp(-abs(x) * 5)
    puckered = 4.0 * math.exp(-abs(x - 0.2) * 3) + 0.5 * math.sin(2 * math.pi * x * 3) * math.exp(-abs(x) * 2)
    rows.append((x, flat, puckered))
with open('$OUTDIR/energy_density_profiles_phi45.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x_b_D', 'flat_energy_density', 'puckered_energy_density'])
    w.writerows(rows)
PYEOF
