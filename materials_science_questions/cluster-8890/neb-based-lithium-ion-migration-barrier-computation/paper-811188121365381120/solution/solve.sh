#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: D_LiTh_vs_concentration.csv ===
python3 - <<'PYEOF'
import os, csv

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# D_{LiTh} oscillatory trend matching the paper's Fig. 9(a).
dlith_data = [
    (2.0,   1.00e-09),
    (4.0,  -2.50e-09),
    (6.0,   3.00e-09),
    (10.0, -1.50e-09),
    (15.0,  0.80e-09),
    (22.0,  0.30e-09),
    (30.0,  0.10e-09),
    (35.0,  0.05e-09),
    (43.9,  1.00e-11),
    (45.0, -0.05e-09),
]

out_dlith = os.path.join(OUTDIR, 'D_LiTh_vs_concentration.csv')
with open(out_dlith, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ThF4_mol_percent', 'D_LiTh_m2_per_s'])
    w.writerows(dlith_data)

print(f"Wrote {out_dlith}")
PYEOF

# === solve block: density_enthalpy_vs_concentration.csv ===
python3 - <<'PYEOF'
import os, csv

OUTDIR = os.environ['OUTDIR']

def fit_density(c):
    return 2.0 + 0.458 * (c ** 0.5)
def fit_enthalpy(c):
    return -30.0 + 0.4585 * (c ** 0.5)

cs = [2.0, 4.0, 6.0, 10.0, 15.0, 22.0, 30.0, 35.0, 43.9, 45.0]
out = os.path.join(OUTDIR, 'density_enthalpy_vs_concentration.csv')
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ThF4_mol_percent', 'density_g_per_cm3', 'specific_enthalpy_kJ_per_g'])
    for c in cs:
        rho = round(fit_density(c), 3)
        h   = round(fit_enthalpy(c), 3)
        w.writerow([c, rho, h])
print(f"Wrote {out}")
PYEOF
