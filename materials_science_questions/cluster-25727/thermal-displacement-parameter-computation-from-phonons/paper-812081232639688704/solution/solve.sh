#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_ratios.csv ===
python3 << 'EOF' > $OUTDIR/predicted_ratios.csv
import math

R = 8.314
# Parameters for free interface
free_params = {
    'Fe': (0.2482, 6.42),
    'β-Sn': (0.3181, 9.25),
    'Se': (0.4366, 10.93),
    'Cu': (0.2556, 8.08),
    'Co': (0.2507, 7.83),
    'Au': (0.2884, 7.74),
    'Pb': (0.3500, 6.71),
}
# Embedded Ar params
h_Ar = 0.3650
Tm_Ar = 83.80
h_M = 0.2863
TM_Al = 933.47

def alpha_free(delS):
    return 2 * delS / (3 * R) + 1

def alpha_embedded():
    return ((h_M / h_Ar) ** 2 * Tm_Ar / TM_Al + 1) / 2

def compute_ratios(alpha, D, h, d):
    D0 = 2 * (3 - d) * h
    # All cases have D > D0, so (D/D0 - 1) > 0
    factor = (alpha - 1) / (D / D0 - 1)
    # sqrt(exp(-factor)) = exp(-factor/2)
    ThetaD_ratio = math.exp(-factor / 2)
    ThetaE_ratio = ThetaD_ratio
    alphav_ratio = math.exp(factor)
    return ThetaD_ratio, ThetaE_ratio, alphav_ratio

rows = []

# Fe free d=0 sizes 5,10,20,50
for size in [5.0, 10.0, 20.0, 50.0]:
    a = alpha_free(6.42)
    td, te, al = compute_ratios(a, size, 0.2482, 0)
    rows.append(('Fe', 0, size, 'free', td, te, al))

# β-Sn d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(9.25)
    td, te, al = compute_ratios(a, size, 0.3181, 0)
    rows.append(('β-Sn', 0, size, 'free', td, te, al))

# Se d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(10.93)
    td, te, al = compute_ratios(a, size, 0.4366, 0)
    rows.append(('Se', 0, size, 'free', td, te, al))

# Cu d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(8.08)
    td, te, al = compute_ratios(a, size, 0.2556, 0)
    rows.append(('Cu', 0, size, 'free', td, te, al))

# Co d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(7.83)
    td, te, al = compute_ratios(a, size, 0.2507, 0)
    rows.append(('Co', 0, size, 'free', td, te, al))

# Au d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(7.74)
    td, te, al = compute_ratios(a, size, 0.2884, 0)
    rows.append(('Au', 0, size, 'free', td, te, al))

# Pb d=0 sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(6.71)
    td, te, al = compute_ratios(a, size, 0.3500, 0)
    rows.append(('Pb', 0, size, 'free', td, te, al))

# Ar embedded d=0 sizes 5,10,20,50
a_emb = alpha_embedded()
for size in [5.0, 10.0, 20.0, 50.0]:
    td, te, al = compute_ratios(a_emb, size, h_Ar, 0)
    rows.append(('Ar', 0, size, 'embedded', td, te, al))

# Additional Fe nanowire (d=1) sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(6.42)
    td, te, al = compute_ratios(a, size, 0.2482, 1)
    rows.append(('Fe', 1, size, 'free', td, te, al))

# Fe thin film (d=2) sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(6.42)
    td, te, al = compute_ratios(a, size, 0.2482, 2)
    rows.append(('Fe', 2, size, 'free', td, te, al))

# Cu nanowire (d=1) sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(8.08)
    td, te, al = compute_ratios(a, size, 0.2556, 1)
    rows.append(('Cu', 1, size, 'free', td, te, al))

# Cu thin film (d=2) sizes 10,20,50
for size in [10.0, 20.0, 50.0]:
    a = alpha_free(8.08)
    td, te, al = compute_ratios(a, size, 0.2556, 2)
    rows.append(('Cu', 2, size, 'free', td, te, al))

# Write CSV
import sys
sys.stdout.write('material,dimension,size_nm,interface_type,ThetaD_ratio,ThetaE_ratio,alphav_ratio\n')
for mat, dim, size, iface, td, te, alv in rows:
    sys.stdout.write(f'{mat},{dim},{size},{iface},{td:.15f},{te:.15f},{alv:.15f}\n')
EOF
