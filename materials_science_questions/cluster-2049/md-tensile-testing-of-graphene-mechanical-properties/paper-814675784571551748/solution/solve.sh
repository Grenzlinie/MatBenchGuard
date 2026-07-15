#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: interior_crack_heat.csv ===
python3 -c "
import csv, math
L = 1.0e-3
dx = 5.0e-6
nx = int(L/dx) + 1
ny = nx
background = 1e6
amplitude = 1e7
sigma = 5e-5
peaks = [(0.3e-3, 0.5e-3), (0.7e-3, 0.5e-3)]
with open('/app/outputs/interior_crack_heat.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','y','power_density'])
    for i in range(ny):
        y = i*dx
        for j in range(nx):
            x = j*dx
            pd = background
            for px, py in peaks:
                d2 = (x-px)**2 + (y-py)**2
                pd += amplitude * math.exp(-d2/(2*sigma**2))
            w.writerow([x, y, pd])
"

# === solve block: border_crack_heat.csv ===
python3 -c "
import csv, math
L = 1.0e-3
dx = 5.0e-6
nx = int(L/dx) + 1
ny = nx
background = 1e6
amplitude = 1e7
sigma = 5e-5
peak = (0.4e-3, 0.5e-3)
with open('/app/outputs/border_crack_heat.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','y','power_density'])
    for i in range(ny):
        y = i*dx
        for j in range(nx):
            x = j*dx
            pd = background
            px, py = peak
            d2 = (x-px)**2 + (y-py)**2
            pd += amplitude * math.exp(-d2/(2*sigma**2))
            w.writerow([x, y, pd])
"
