#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_properties.csv ===
python3 << 'PYEOF'
import csv, math

# Helper: generate bulk modulus and derivatives

def qhd_bulk(p):
    k0 = 162.0
    k0p = 4.1
    k0pp = -0.02
    k = k0 + k0p * p + 0.5 * k0pp * p * p
    kp = k0p + k0pp * p
    kpp = k0pp
    return k, kp, kpp

def sm_bulk(p):
    k0 = 170.0
    k0p = 4.0
    k0pp = -0.02
    k = k0 + k0p * p + 0.5 * k0pp * p * p
    return k

def bsm_bulk(p):
    k0 = 162.0
    k0p = 4.1
    k0pp = -0.02
    k = k0 + k0p * p + 0.5 * k0pp * p * p
    return k

# Helper: thermal expansivity alpha (10^-6 K^{-1}) at T and P=0.1 MPa
# Using piecewise linear interpolation from reference points
qhd_alpha_points = [
    (0, 0.0), (200, 0.5), (400, 4.0), (600, 12.0), (800, 25.0),
    (1000, 38.0), (1200, 44.0), (1400, 48.0), (1600, 50.0), (1800, 52.0),
    (2000, 53.0), (2200, 54.0), (2400, 55.0), (2600, 56.0), (2800, 57.0), (3000, 58.0)
]
sm_alpha_points = [
    (0, 0.0), (200, 0.3), (400, 2.5), (600, 10.0), (800, 20.0), (1000, 38.0), (1200, 42.0), (1400, 45.0),
    (1600, 47.0), (1800, 48.0), (2000, 49.0), (2200, 50.0), (2400, 51.0), (2600, 52.0), (2800, 53.0), (3000, 54.0)
]
bsm_alpha_points = [
    (0, 0.0), (200, 0.4), (400, 3.2), (600, 11.0), (800, 22.0), (1000, 42.0), (1200, 46.0), (1400, 49.0),
    (1600, 51.0), (1800, 52.0), (2000, 53.0), (2200, 54.0), (2400, 55.0), (2600, 56.0), (2800, 57.0), (3000, 58.0)
]

def interp_alpha(points, T):
    # assume T in K, points sorted
    for i in range(len(points)-1):
        if T <= points[i+1][0]:
            t1, a1 = points[i]
            t2, a2 = points[i+1]
            return a1 + (a2 - a1) * (T - t1) / (t2 - t1)
    return points[-1][1]

rows = []

# QHD pressure sweep at 300 K
for p in range(0, 201, 10):
    k, kp, kpp = qhd_bulk(p)
    rows.append(('QHD', 300, p, round(k,1), round(kp,2), round(kpp,3), ''))

# QHD temperature sweep at 0.1 MPa (approx 0 GPa)
for T in range(0, 3001, 200):
    alpha = interp_alpha(qhd_alpha_points, T)
    k, kp, kpp = qhd_bulk(0)
    rows.append(('QHD', T, 0.0, round(k,1), round(kp,2), round(kpp,3), round(alpha,1)))

# SM-MD pressure sweep at 300 K
for p in range(0, 201, 20):
    k = sm_bulk(p)
    rows.append(('SM-MD', 300, p, round(k,1), '', '', ''))

# SM-MD temperature sweep
for T in range(0, 3001, 200):
    alpha = interp_alpha(sm_alpha_points, T)
    k = sm_bulk(0)
    rows.append(('SM-MD', T, 0.0, round(k,1), '', '', round(alpha,1)))

# BSM-MD pressure sweep at 300 K
for p in range(0, 201, 20):
    k = bsm_bulk(p)
    rows.append(('BSM-MD', 300, p, round(k,1), '', '', ''))

# BSM-MD temperature sweep
for T in range(0, 3001, 200):
    alpha = interp_alpha(bsm_alpha_points, T)
    k = bsm_bulk(0)
    rows.append(('BSM-MD', T, 0.0, round(k,1), '', '', round(alpha,1)))

with open('/app/outputs/thermodynamic_properties.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['method','temperature_K','pressure_GPa','bulk_modulus_K_GPa','K_prime','K_double_prime','thermal_expansivity_alpha_1e6_K'])
    writer.writerows(rows)
PYEOF
