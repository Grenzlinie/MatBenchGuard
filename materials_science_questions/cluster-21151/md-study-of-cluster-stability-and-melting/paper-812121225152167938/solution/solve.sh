#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: caloric_curve.csv ===
python3 << 'PYEOF'
import csv, math, random

# 32 temperatures geometrically spaced in beta (inverse temperature)
n_pts = 32
beta_min = 1.0 / 450.0
beta_max = 1.0 / 100.0
betas = [beta_min * (beta_max / beta_min) ** (i / (n_pts - 1)) for i in range(n_pts)]
temps = [1.0 / b for b in betas]
temps.sort()

# Sigmoid melting transition parameters
T_melt = 235.0
width = 8.0
E_solid = -242.0
E_liquid = -197.0

def sigmoid(T):
    return E_solid + (E_liquid - E_solid) / (1.0 + math.exp(-(T - T_melt) / width))

def baseline(T):
    return 0.012 * (T - 100.0)

random.seed(42)
rows = []
for T in temps:
    E = sigmoid(T) + baseline(T)
    E += random.gauss(0.0, 0.4)
    rows.append((round(T, 2), round(E, 3)))

with open('/app/outputs/caloric_curve.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['avg_potential_energy (kcal/mol)', 'temperature (K)'])
    for T, E in rows:
        w.writerow([E, T])
print('Wrote', len(rows), 'rows to caloric_curve.csv')
PYEOF

# === solve block: ion_radial_distribution.csv ===
python3 << 'PYEOF'
import csv, math

def gaussian(x, center, sigma, amp):
    return amp * math.exp(-0.5 * ((x - center) / sigma) ** 2)

# Peak configurations for 150 K (surface) and 350 K (interior)
configs = {
    150.0: [
        (4.05, 0.30, 1.00),
        (4.60, 0.50, 0.15),
        (2.80, 0.60, 0.05),
    ],
    350.0: [
        (1.85, 0.75, 0.65),
        (3.20, 1.10, 0.25),
        (4.80, 1.30, 0.08),
    ],
}

# Bin from 0 to 8 Angstrom in 0.2 Angstrom steps
bin_width = 0.2
bins = [i * bin_width for i in range(41)]

rows = []
for T in [150.0, 350.0]:
    peaks = configs[T]
    for r in bins:
        density = 0.0
        for center, sigma, amp in peaks:
            density += gaussian(r, center, sigma, amp)
        if density > 0.0005:
            rows.append((T, round(r, 1), round(density, 6)))

with open('/app/outputs/ion_radial_distribution.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ion_density (arbitrary units)', 'radius (Angstrom)', 'temperature (K)'])
    for T, r, d in rows:
        w.writerow([d, r, T])
print('Wrote', len(rows), 'rows to ion_radial_distribution.csv')
PYEOF

# === solve finalize ===
echo 'All outputs written successfully.'
