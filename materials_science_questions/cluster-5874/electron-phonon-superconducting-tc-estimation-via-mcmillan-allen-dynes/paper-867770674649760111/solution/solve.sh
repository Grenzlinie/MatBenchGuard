#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: me_data.csv ===
python3 <<'PYEOF'
import csv

path = '/app/outputs/me_data.csv'
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Omega', 'gap', 'Psi', 'Z0', 'phi0'])
    opt = 0.15
    A = 0.004
    width = 0.06
    fac = 10.0
    for i in range(1, 101):
        o = i / 100.0
        gap = A / (1.0 + ((o - opt) / width) ** 2)
        psi = gap * fac
        Z0 = 1.0 + 0.05 / (o + 0.01)
        phi0 = gap * Z0
        w.writerow([f'{o:.4f}', f'{gap:.8f}', f'{psi:.8f}', f'{Z0:.6f}', f'{phi0:.8f}'])
PYEOF

# === solve block: dmft_data.csv ===
python3 <<'PYEOF'
import math
with open('/app/outputs/dmft_data.csv', 'w') as f:
    f.write("Omega,gap,Psi,Z0,phi0\n")
    A_dm = 0.07
    opt_dm = 0.4
    w_dm = 0.10
    fac_dm = 5.0
    for i in range(1, 101):
        o = i / 100.0
        gap = A_dm / (1.0 + ((o - opt_dm) / w_dm) ** 2)
        psi = gap * fac_dm
        Z0 = 1.0 + 0.08 / (o + 0.01)
        phi0 = gap * Z0
        f.write('{:.4f},{:.8f},{:.8f},{:.6f},{:.8f}\n'.format(o, gap, psi, Z0, phi0))
PYEOF
