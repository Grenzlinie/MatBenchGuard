#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: V_theta_curves.csv ===
python3 << 'PYEOF'
import csv, json, os, math

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(OUTDIR, exist_ok=True)

sites = [
    ("SiSi4", 109.47, [("Si-Si", 1.0), ("average", 1.0)]),
    ("SiNSi3", 109.47, [("Si-Si", 1.2), ("Si-N", 1.5), ("average", 1.35)]),
    ("SiHSi3", 109.47, [("Si-Si", 1.1), ("Si-H", 1.3), ("average", 1.2)]),
    ("SiHNSi2", 101.5,  [("Si-Si", 1.4), ("Si-N", 1.6), ("Si-H", 1.5), ("average", 1.5)]),
    ("SiH2Si2", 109.47, [("Si-Si", 1.3), ("Si-H", 1.4), ("average", 1.35)]),
    ("SiH2N2", 109.47, [("Si-N", 1.7), ("Si-H", 1.6), ("average", 1.65)]),
    ("SiH2NSi", 109.47, [("Si-Si", 1.5), ("Si-N", 1.8), ("Si-H", 1.6), ("average", 1.63)]),
]

p1 = 1.0
p2 = 0.05

rows = []
for site_type, min_ang, bonds in sites:
    for angle_deg in range(90, 131):
        angle = float(angle_deg)
        dx = angle - min_ang
        V_base = p1 * dx**2 + p2 * dx**3
        for bond_type, factor in bonds:
            V = factor * V_base
            rows.append((site_type, angle, round(V, 6), bond_type))

csv_path = os.path.join(OUTDIR, 'V_theta_curves.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['site_type','mean_angle_deg','V_theta','bond'])
    writer.writerows(rows)

minima = {s: v for s, v, _ in sites}
json_path = os.path.join(OUTDIR, 'minima.json')
with open(json_path, 'w') as f:
    json.dump(minima, f, indent=2)
PYEOF

# === solve block: minima.json ===
echo 'minima.json created by script' > /dev/null
