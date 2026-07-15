#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: raman_cross_sections.csv ===
python3 <<'PYEOF' > "$OUTDIR/raman_cross_sections.csv"
import math, cmath, csv, sys

# GaP parameters
E0 = 2.78          # eV
Delta0 = 0.082     # eV
Gamma = 0.01       # broadening
C = 2.5            # background constant for phi1

# Quasistatic functions
def g(z):
    return (2.0 - 1.0/cmath.sqrt(1+z) - 1.0/cmath.sqrt(1-z)) / (z*z)

def f(z):
    return (2.0 - cmath.sqrt(1+z) - cmath.sqrt(1-z)) / (z*z)

# Generate data
points = []
for relE in [ -0.4 + i*0.025 for i in range(29) ]:  # -0.4 to 0.3 step 0.025
    omega = E0 + relE
    # complex gaps with broadening
    omega0c = E0 + 1j*Gamma
    omega0s = E0 + Delta0 + 1j*Gamma
    x0 = omega / omega0c
    x0s = omega / omega0s

    # First-order (phi15) and second-order Gamma1
    f0 = f(x0)
    f0s = f(x0s)
    g0 = g(x0)
    g0s = g(x0s)

    phi15 = -g0 + (4*E0/Delta0) * (f0 - (E0/(E0+Delta0))**1.5 * f0s)
    cross_1st = abs(phi15)**2

    phi1_num = g0 + 3*f0 + 0.5*(g0s + 3*f0s) - C
    cross_Gamma1 = abs(phi1_num)**2

    # Second-order Gamma15 (single peak modelled as Lorentzian)
    width = 0.03
    cross_Gamma15 = 1.0 / (1.0 + (relE/width)**2)

    points.append((relE, cross_1st, cross_Gamma1, cross_Gamma15))

# Write CSV
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['photon_energy_relative_E0', 'cross_section_first_order',
                  'cross_section_second_order_Gamma1', 'cross_section_second_order_Gamma15'])
for relE, c1, cg1, cg15 in points:
    writer.writerow([f'{relE:.6f}', f'{c1:.10e}', f'{cg1:.10e}', f'{cg15:.10e}'])
PYEOF

# === solve block: results.json ===
cat <<'JSONEOF' > /app/outputs/results.json
{
  "intensity_ratio_two_LO": 0.035,
  "intensity_ratio_TO_plus_LO": 0.015,
  "delta2_omega0_over_delta1_omega0_Gamma1": 500000000,
  "delta2_omega0_over_delta1_omega0_Gamma15": 540000000,
  "D1_eV": 390,
  "D15_eV": 450
}
JSONEOF
