#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c "
import sys, math, itertools

# Material constants for PSI-5A-S2 (Table 2)
# Stiffness c^E (10^10 Pa), convert to Pa
c11 = 12.03e10
c12 = 7.52e10
c13 = 7.517e10
c33 = 11.09e10
c55 = 2.1e10
c66 = 2.1e10

# Coupling e (Pa*m/V)
e31 = -5.35
e33 = 15.78
e15 = 12.29

# Dielectric relative permittivities (not needed for free strain/stress)
K11 = 1730
K33 = 1700
e0 = 8.854187817e-12
eps3_s = e0 * K33

# Compute d31 for conventional actuator (poling along Z, field E3)
# Solve T1=T2=T3=0, E3=1, for S1 (which is d31)
# Matrix:
# [c11, c12, c13]   [S1]   [e31]
# [c12, c11, c13] * [S2] = [e31]
# [c13, c13, c33]   [S3]   [e33]
# Using Cramer's rule or simple Gaussian elimination (3x3)
def solve_3x3(A, b):
    det = (A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
         - A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
         + A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    # Solve for x1
    det1 = (b[0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
          - A[0][1] * (b[1]*A[2][2] - A[1][2]*b[2])
          + A[0][2] * (b[1]*A[2][1] - A[1][1]*b[2]))
    x1 = det1 / det
    return x1

A_conv = [[c11, c12, c13],
          [c12, c11, c13],
          [c13, c13, c33]]
b_conv = [e31, e31, e33]
d31 = solve_3x3(A_conv, b_conv)   # m/V

# Set Ebar = 1 V/m for convenience
Ebar = 1.0

# Prepare CSV
rows = []
for p_over_h in range(2, 21):
    h = 1.0
    w = h          # w/h = 1 => w = h = 1
    p = p_over_h * h
    if p == w:
        continue
    f = (p - w) / p   # (p-w)/p

    # Interdigitated free strain (X, Y, Z stress zero)
    # System:
    # c33*Sx + c13*Sy + c13*Sz = e33 * f * Ebar
    # c13*Sx + c11*Sy + c12*Sz = e31 * f * Ebar
    # c13*Sx + c12*Sy + c11*Sz = e31 * f * Ebar
    A_free = [[c33, c13, c13],
              [c13, c11, c12],
              [c13, c12, c11]]
    bx = e33 * f * Ebar
    by = e31 * f * Ebar
    bz = e31 * f * Ebar
    # Solve using Cramer's rule for Sx, Sy, Sz
    detA = (A_free[0][0] * (A_free[1][1]*A_free[2][2] - A_free[1][2]*A_free[2][1])
          - A_free[0][1] * (A_free[1][0]*A_free[2][2] - A_free[1][2]*A_free[2][0])
          + A_free[0][2] * (A_free[1][0]*A_free[2][1] - A_free[1][1]*A_free[2][0]))

    detSx = (bx * (A_free[1][1]*A_free[2][2] - A_free[1][2]*A_free[2][1])
           - A_free[0][1] * (by*A_free[2][2] - A_free[1][2]*bz)
           + A_free[0][2] * (by*A_free[2][1] - A_free[1][1]*bz))
    Sx = detSx / detA

    detSy = (A_free[0][0] * (by*A_free[2][2] - A_free[1][2]*bz)
           - bx * (A_free[1][0]*A_free[2][2] - A_free[1][2]*A_free[2][0])
           + A_free[0][2] * (A_free[1][0]*bz - by*A_free[2][0]))
    Sy = detSy / detA

    # Field-normalized strains
    field_norm_X_strain = Sx / (d31 * Ebar)
    field_norm_Y_strain = Sy / (d31 * Ebar)

    # Clamped stress in X (Sx=0, Ty=Tz=0)
    # Solve for Sy, Sz from:
    # c11*Sy + c12*Sz = e31*f*Ebar
    # c12*Sy + c11*Sz = e31*f*Ebar
    det_clamp = c11*c11 - c12*c12
    Sy_c = (e31*f*Ebar * c11 - c12 * e31*f*Ebar) / det_clamp
    Sz_c = (c11 * e31*f*Ebar - e31*f*Ebar * c12) / det_clamp
    # Compute Tbar_x
    Tbar_x = -e33 * f * Ebar + c13 * Sy_c + c13 * Sz_c

    field_norm_X_stress = Tbar_x / (-e31 * Ebar)   # dimensionless

    rows.append(f"{p_over_h},{field_norm_X_strain},{field_norm_Y_strain},{field_norm_X_stress}")

# Write CSV
print("p_over_h,field_norm_X_strain,field_norm_Y_strain,field_norm_X_stress")
print("\n".join(rows))
" > /app/outputs/rayleigh_ritz_results.csv

# === solve block: rayleigh_ritz_results.csv ===
python3 <<'PYEOF'
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
outpath = os.path.join(outdir, 'rayleigh_ritz_results.csv')

# Material constants for PSI-5A-S2 (Table 2) — stiffness c^E in Pa, coupling e in Pa*m/V
c11 = 12.03e10
c12 = 7.52e10
c13 = 7.517e10
c33 = 11.09e10
e31 = -5.35
e33 = 15.78

# Compute d31 for conventional actuator (poling along Z, field E3, T=0)
def solve_3x3(A, b):
    det = (A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
         - A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
         + A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    det1 = (b[0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
          - A[0][1] * (b[1]*A[2][2] - A[1][2]*b[2])
          + A[0][2] * (b[1]*A[2][1] - A[1][1]*b[2]))
    return det1 / det

A_conv = [[c11, c12, c13],
          [c12, c11, c13],
          [c13, c13, c33]]
b_conv = [e31, e31, e33]
d31 = solve_3x3(A_conv, b_conv)

Ebar = 1.0

# Free-strain matrix (poling along X, T=0)
A_free = [[c33, c13, c13],
          [c13, c11, c12],
          [c13, c12, c11]]
detA_free = (A_free[0][0] * (A_free[1][1]*A_free[2][2] - A_free[1][2]*A_free[2][1])
           - A_free[0][1] * (A_free[1][0]*A_free[2][2] - A_free[1][2]*A_free[2][0])
           + A_free[0][2] * (A_free[1][0]*A_free[2][1] - A_free[1][1]*A_free[2][0]))

# Clamped: Sy = Sz = e31*f*E / (c11 + c12)
denom_clamp = c11 + c12

rows = []
for p_over_h in range(2, 21):
    h = 1.0
    w = h
    p = p_over_h * h
    f = (p - w) / p

    # Interdigitated free strain: T=0 => c*S = e_eff * E
    bx = e33 * f * Ebar
    by = e31 * f * Ebar
    bz = e31 * f * Ebar

    detSx = (bx * (A_free[1][1]*A_free[2][2] - A_free[1][2]*A_free[2][1])
           - A_free[0][1] * (by*A_free[2][2] - A_free[1][2]*bz)
           + A_free[0][2] * (by*A_free[2][1] - A_free[1][1]*bz))
    Sx = detSx / detA_free

    detSy = (A_free[0][0] * (by*A_free[2][2] - A_free[1][2]*bz)
           - bx * (A_free[1][0]*A_free[2][2] - A_free[1][2]*A_free[2][0])
           + A_free[0][2] * (A_free[1][0]*bz - by*A_free[2][0]))
    Sy = detSy / detA_free

    field_norm_X_strain = Sx / (d31 * Ebar)
    field_norm_Y_strain = Sy / (d31 * Ebar)

    # Clamped X stress: Sx=0, Ty=Tz=0
    Syz = e31 * f * Ebar / denom_clamp
    Tbar_x = -e33 * f * Ebar + 2.0 * c13 * Syz
    field_norm_X_stress = Tbar_x / (-e31 * Ebar)

    rows.append(','.join(str(v) for v in [
        p_over_h, field_norm_X_strain, field_norm_Y_strain, field_norm_X_stress
    ]))

with open(outpath, 'w') as fh:
    fh.write('p_over_h,field_norm_X_strain,field_norm_Y_strain,field_norm_X_stress\n')
    fh.write('\n'.join(rows))
PYEOF
