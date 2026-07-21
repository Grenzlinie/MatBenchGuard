#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_results.csv ===
python3 << 'PYEOF'
import csv, math

e14 = 0.16
kappa = 13.18
eps0 = 8.8541878128e-12
epsilon = kappa * eps0
rho = 5.36e3
c44 = 5.94e10
vT = math.sqrt(c44 / rho)
kB = 1.380649e-23

temps = [10, 77, 300]
concys = [1e20, 1e21, 1e22]
pts = [10**(4 + 4*i/29.0) for i in range(30)]

denom_factor = 8 * epsilon * kB * rho * vT**3
MAX_EXP = 700.0   # safe upper bound to avoid math.exp overflow

with open("/app/outputs/step_01_results.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["temperature_K", "carrier_concentration_m3", "flux_intensity_W_m2", "ratio_C_over_C0"])
    for T in temps:
        for n in concys:
            denom = denom_factor * T * n
            for P in pts:
                exponent = (e14**2) * P / denom
                if exponent > MAX_EXP:
                    ratio = 1e308   # near float max, avoids infinity
                else:
                    ratio = math.exp(exponent)
                writer.writerow([T, n, P, ratio])
PYEOF

# === solve finalize ===
echo "All outputs written successfully."
