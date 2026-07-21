#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sh_wave_transmission.csv ===
python3 - "$OUTDIR/sh_wave_transmission.csv" <<'PYEOF'
import sys, math, csv

outpath = sys.argv[1]

# Austenitic base metal (isotropic)
rho_base = 7900.0          # kg/m^3
mu_base  = 73.0e9          # Pa
cs_base  = math.sqrt(mu_base / rho_base)   # shear wave speed

# Austenitic weld metal – modelled as isotropic with slightly lower shear modulus
rho_weld = 7900.0          # kg/m^3
mu_weld  = 72.0e9          # Pa
cs_weld  = math.sqrt(mu_weld / rho_weld)

# SH-wave reflection/transmission at a planar interface between two isotropic half-spaces.
# R = (Z1 - Z2) / (Z1 + Z2),  T = 2*Z1 / (Z1 + Z2)
# where Z1 = rho_base * cs_base * cos(theta1),  Z2 = rho_weld * cs_weld * cos(theta2)
# Snell's law: sin(theta2) = (cs_weld / cs_base) * sin(theta1)

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["angle_deg", "R", "T"])

    for angle_deg in range(0, 91):
        theta1 = math.radians(angle_deg)
        sin1 = math.sin(theta1)
        cos1 = math.cos(theta1)

        # Snell's law gives real theta2 for all angles because cs_weld < cs_base
        sin2 = (cs_weld / cs_base) * sin1
        cos2 = math.sqrt(1.0 - sin2 * sin2)

        Z1 = rho_base * cs_base * cos1
        Z2 = rho_weld * cs_weld * cos2
        denom = Z1 + Z2
        R = (Z1 - Z2) / denom
        T = 2.0 * Z1 / denom

        writer.writerow([angle_deg, R, T])
PYEOF
