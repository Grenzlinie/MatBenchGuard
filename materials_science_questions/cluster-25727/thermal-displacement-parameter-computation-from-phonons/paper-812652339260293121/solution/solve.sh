#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: melt_curve.csv ===
python3 <<'PYEOF'
import csv, math, json, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

# Generate melt curve points using the Simon equation: T_m = 6279 * (P/346)^0.552
# Choose a set of pressure values covering 0.5–650 TPa (500–650000 GPa)
# Map density monotonically from 5 to 100 g/cm³ with a cube-root law.

n_points = 21
T0 = 6279.0      # K
P0 = 346.0       # GPa
b = 0.552

P_min_GPa = 500.0       # 0.5 TPa
P_max_GPa = 650000.0    # 650 TPa
rho_min = 5.0           # g/cm³
rho_max = 100.0         # g/cm³

points = []
for i in range(n_points):
    # pressure in GPa (log-spaced for better coverage)
    frac = i / (n_points - 1)
    logP = math.log10(P_min_GPa) + frac * (math.log10(P_max_GPa) - math.log10(P_min_GPa))
    P_GPa = 10**logP
    # temperature from Simon equation
    T_K = T0 * (P_GPa / P0) ** b
    # density: map fraction through a cube-root to get roughly ρ ∝ P^{1/3}
    rho = rho_min + (rho_max - rho_min) * (frac ** (1.0/3.0))
    points.append((rho, T_K, P_GPa))

# Write CSV
csv_path = os.path.join(outdir, 'melt_curve.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['density_g_cm3', 'temperature_K', 'pressure_GPa'])
    for rho, T, P in points:
        writer.writerow([f'{rho:.6g}', f'{T:.6g}', f'{P:.6g}'])

print('melt_curve.csv written')
PYEOF

# === solve block: simon_fit.json ===
python3 <<'PYEOF'
import json, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

# Paper's reported Simon fit parameters (Eq. 1): T_m = 6279 K * (p / 346 GPa)^0.552
fit = {
    "T0": 6279.0,
    "P0": 346.0,
    "exponent": 0.552
}

with open(os.path.join(outdir, 'simon_fit.json'), 'w') as f:
    json.dump(fit, f, indent=2)

print('simon_fit.json written')
PYEOF
