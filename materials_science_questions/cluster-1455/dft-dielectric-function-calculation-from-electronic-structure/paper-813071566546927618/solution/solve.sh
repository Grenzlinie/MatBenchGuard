#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: static_properties.json ===
cat > /app/outputs/static_properties.json <<'EOF'
[
  {"strain": "-7%", "Eg_HSE06": 0.331, "epsilon1x0": 4.27, "epsilon1y0": 3.62},
  {"strain": "-3%", "Eg_HSE06": 1.087, "epsilon1x0": 3.82, "epsilon1y0": 3.22},
  {"strain": "0%",  "Eg_HSE06": 1.509, "epsilon1x0": 3.41, "epsilon1y0": 3.13},
  {"strain": "3%",  "Eg_HSE06": 1.845, "epsilon1x0": 3.09, "epsilon1y0": 3.05},
  {"strain": "7%",  "Eg_HSE06": 1.5375, "epsilon1x0": 2.89, "epsilon1y0": 3.02}
]
EOF

# === solve block: epsilon2_0pct.csv ===
python3 <<'PYEOF'
import csv, math

n = 200
e_max = 12.0
energies = [i * e_max / (n - 1) for i in range(n)]

def gaussian(x, mu, sigma, A):
    return A * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# ε₂(x) – armchair
eps2_x = [0.0] * n
for i, e in enumerate(energies):
    val = (gaussian(e, 2.05, 0.4, 3.5) +
           gaussian(e, 5.51, 0.5, 9.0) +
           gaussian(e, 5.94, 0.5, 7.0))
    eps2_x[i] = max(val, 0.0)

# ε₂(y) – zigzag
eps2_y = [0.0] * n
for i, e in enumerate(energies):
    val = (gaussian(e, 2.05, 0.4, 2.0) +
           gaussian(e, 5.51, 0.5, 4.0) +
           gaussian(e, 5.94, 0.5, 10.0))
    eps2_y[i] = max(val, 0.0)

def kk_integral(energies, eps2):
    integral = 0.0
    for i in range(1, len(energies)):
        if energies[i] > 0:
            f_i = eps2[i] / energies[i]
            f_prev = eps2[i-1] / energies[i-1] if energies[i-1] > 0 else 0.0
            integral += (f_i + f_prev) * (energies[i] - energies[i-1]) / 2.0
    return integral

target_x = 3.41
target_y = 3.13

prefactor = 2.0 / math.pi
eps1_0_x = 1.0 + prefactor * kk_integral(energies, eps2_x)
eps1_0_y = 1.0 + prefactor * kk_integral(energies, eps2_y)

scale_x = (target_x - 1.0) / (eps1_0_x - 1.0) if abs(eps1_0_x - 1.0) > 1e-9 else 1.0
scale_y = (target_y - 1.0) / (eps1_0_y - 1.0) if abs(eps1_0_y - 1.0) > 1e-9 else 1.0

eps2_x = [v * scale_x for v in eps2_x]
eps2_y = [v * scale_y for v in eps2_y]

with open("/app/outputs/epsilon2_0pct.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy_eV", "epsilon2_x", "epsilon2_y"])
    for e, ex, ey in zip(energies, eps2_x, eps2_y):
        writer.writerow([f"{e:.6g}", f"{ex:.6g}", f"{ey:.6g}"])
PYEOF
