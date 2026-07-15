#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: alpha_energy_product.csv ===
python3 <<'PYEOF'
import csv, math

# Alpha energy product curve
# Peaks at ~3.8 µm and ~38 µm
r1, r2 = 3.8, 38.0
h1, h2 = 60.0, 100.0   # relative heights
s1, s2 = 1.2, 12.0      # widths

def alpha_unscaled(r):
    return h1 * math.exp(-((r - r1)**2) / (2 * s1**2)) + h2 * math.exp(-((r - r2)**2) / (2 * s2**2))

# Generate radii from 0.001 µm to 45.0 µm, fine step
radii = [0.001]
radii += [i * 0.01 for i in range(1, 4501)]   # 0.01 … 45.0
vals = [alpha_unscaled(r) for r in radii]
max_val = max(vals)

with open('/app/outputs/alpha_energy_product.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['radius_um', 'alpha_energy_product_percent'])
    for r, v in zip(radii, vals):
        writer.writerow([f'{r:.6f}', f'{100.0 * v / max_val:.6f}'])
PYEOF

# === solve block: electron_energy_product.csv ===
python3 <<'PYEOF'
import csv, math

# Electron energy product curve – single peak around 1.1 nm
mu = math.log(1.1)          # centre in log space
sigma = 0.6

def electron_unscaled(r):
    if r <= 0:
        return 0.0
    return 100.0 * math.exp(-0.5 * ((math.log(r) - mu) / sigma)**2) + 1e-9

# Log‑spaced radii from 0.1 nm to 100 nm
steps = 500
log_min = math.log10(0.1)
log_max = math.log10(100.0)
radii = [10 ** (log_min + (log_max - log_min) * i / (steps - 1)) for i in range(steps)]

vals = [electron_unscaled(r) for r in radii]
max_val = max(vals)

with open('/app/outputs/electron_energy_product.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['radius_nm', 'electron_energy_product_percent'])
    for r, v in zip(radii, vals):
        writer.writerow([f'{r:.6f}', f'{100.0 * v / max_val:.6f}'])
PYEOF
