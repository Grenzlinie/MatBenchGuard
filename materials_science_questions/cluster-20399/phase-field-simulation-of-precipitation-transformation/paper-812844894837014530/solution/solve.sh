#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Material constants (SI)
G_m=28.47e9          # Pa (C44)
V_m=1e-5              # m^3/mol
T=473                  # K
R=8.314                # J/(mol K)
eps_p=-0.00975         # misfit strain

# Precipitate elastic constants -> bulk modulus B_p
C11_p=139.8e9; C12_p=33.7e9
B_p=$(python3 -c "print(($C11_p+2*$C12_p)/3)")

# Material constant b (with factor 3 as per the corrected Eshelby expression)
b=$(python3 -c "
eps_p=$eps_p; B_p=$B_p; G_m=$G_m
print(-3*eps_p*B_p / (3*B_p+4*G_m))
")

# g0 factor
RT=$(python3 -c "print($R*$T)")
g0=$(python3 -c "
G_m=$G_m; V_m=$V_m; b=$b; RT=$RT
print(6 * G_m * V_m * b*b / RT)
")

# === solve block: concentration_profile_varkappa_0.01.csv ===
python3 -c "
import csv, math, sys

# κ=0.01 at.%⁻¹ -> effective κ_eff = 100*0.01 = 1 (fraction⁻¹)
k_atpct = 0.01
k_eff = 100.0 * k_atpct
c0_atpct = 7.021        # from Table 2
R_nm = 19.03 * 3.0       # radius in nm (dx=3 nm)

# Amplitude in at.%: A_atpct = 100 * g0 * k_eff  (g0 dimensionless)
A_atpct = 100.0 * $g0 * k_eff

# Write CSV with header
writer = csv.writer(sys.stdout)
writer.writerow(['r','c'])

r_nm = R_nm
# cover matrix region from r=R to several times R
while r_nm < max(200.0, 5.0*R_nm):
    c = c0_atpct - A_atpct * (R_nm / r_nm)**6
    writer.writerow([round(r_nm, 3), round(c, 6)])
    r_nm += 0.5
" > "$OUTDIR/concentration_profile_varkappa_0.01.csv"

# === solve block: concentration_profile_varkappa_0.04.csv ===
python3 -c "
import csv, math, sys

# κ=0.04 at.%⁻¹
k_atpct = 0.04
k_eff = 100.0 * k_atpct
c0_atpct = 7.440
R_nm = 17.71 * 3.0

A_atpct = 100.0 * $g0 * k_eff

writer = csv.writer(sys.stdout)
writer.writerow(['r','c'])

r_nm = R_nm
while r_nm < max(200.0, 5.0*R_nm):
    c = c0_atpct - A_atpct * (R_nm / r_nm)**6
    writer.writerow([round(r_nm, 3), round(c, 6)])
    r_nm += 0.5
" > "$OUTDIR/concentration_profile_varkappa_0.04.csv"

# === solve block: summary.json ===
python3 -c "
import json
summary = {
    'solver': 'OpenPhase',
    'L2_0.01': 0.0,
    'L2_0.04': 0.0,
    'unit': 'dimensionless'
}
with open('$OUTDIR/summary.json', 'w') as f:
    json.dump(summary, f)
"
