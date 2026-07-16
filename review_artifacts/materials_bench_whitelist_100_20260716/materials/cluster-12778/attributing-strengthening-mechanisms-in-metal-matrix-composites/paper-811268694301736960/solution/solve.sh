#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: predicted_strengths_250C.csv ===
python3 <<'PYEOF'
import csv, math

def compute_HP(d_m):
    return 0.12 / math.sqrt(d_m)

def compute_Or(wt_oxygen):
    rho_Al = 2.70          # g/cm3
    rho_Al2O3 = 3.95       # g/cm3
    M_Al2O3 = 101.96       # g/mol
    M_O = 16.00            # g/mol
    f = (rho_Al / rho_Al2O3) * (M_Al2O3 / (3.0 * M_O)) * (wt_oxygen / 100.0)
    
    d_p = 50e-9            # particle diameter (m)
    lam = d_p * (math.sqrt(math.pi / (6.0 * f)) - 1.0)
    
    G = 26.4e9             # shear modulus at 250 °C (Pa)
    b = 0.286e-9            # Burgers vector (m)
    M = 3.06               # Taylor factor
    nu = 0.33              # Poisson's ratio
    
    factor = (0.81 * G * b * M) / (2.0 * math.pi * math.sqrt(1.0 - nu))
    sigma_Or_Pa = factor * (1.0 / lam) * math.log(d_p / b)
    return sigma_Or_Pa * 1e-6   # convert to MPa

alloys = [
    ("BL", 5.15e-6, 0.15),
    ("BM", 3.16e-6, 0.33),
]

rows = []
for name, d, ox in alloys:
    hp = compute_HP(d)
    orowan = compute_Or(ox)
    total = hp + orowan + 25.0
    rows.append([name, round(total, 2)])

with open('/app/outputs/predicted_strengths_250C.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alloy', 'predicted_YS_MPa'])
    writer.writerows(rows)
print("Done writing predicted_strengths_250C.csv")
PYEOF
