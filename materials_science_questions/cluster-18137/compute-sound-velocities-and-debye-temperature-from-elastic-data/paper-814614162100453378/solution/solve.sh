#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dispersion_curves.csv ===
python3 << 'EOF' > "$OUTDIR/dispersion_curves.csv"
import math, csv, sys

c11 = 1.68e12
c12 = 1.21e12
c44 = 0.75e12
rho = 8.96   # g/cm^3
a_ang = 3.61  # Angstrom
a_cm = a_ang * 1e-8  # cm

epsilon = c11 - c12 - 2 * c44

# k_max in 1/Angstrom as per instruction
k_max = {
    '100': math.sqrt(2) * math.pi / a_ang,
    '110': math.sqrt(5) * math.pi / a_ang,
    '111': math.sqrt(1.5) * math.pi / a_ang
}
npoints = 20
writer = csv.writer(sys.stdout)
writer.writerow(['direction', 'mode', 'k', 'frequency'])

for direction in ['100', '110', '111']:
    kmax = k_max[direction]
    for i in range(npoints):
        k = i * kmax / (npoints - 1)  # k in 1/Angstrom
        k_cm = k * 1e8  # k in cm^{-1}
        if direction == '100':
            arg = a_cm * k_cm / (2 * math.sqrt(2))  # dimensionless
            sin2 = math.sin(arg) ** 2
            pref = 8.0 / (rho * a_cm**2)
            # L mode
            omega2 = pref * sin2 * c11
            omega = math.sqrt(max(0.0, omega2))  # rad/s
            writer.writerow([direction, 'L', f"{k:.8f}", f"{omega:.8e}"])
            # T1, T2 degenerate
            omega2_T = pref * sin2 * c44
            omega_T = math.sqrt(max(0.0, omega2_T))
            writer.writerow([direction, 'T1', f"{k:.8f}", f"{omega_T:.8e}"])
            writer.writerow([direction, 'T2', f"{k:.8f}", f"{omega_T:.8e}"])
        elif direction == '110':
            arg = a_cm * k_cm / 4.0
            sin2 = math.sin(arg) ** 2
            pref = 8.0 / (rho * a_cm**2)
            # L
            term_L = 2*c11 - epsilon - (2*c11 - c44 - epsilon) * sin2
            omega2 = pref * sin2 * term_L
            omega = math.sqrt(max(0.0, omega2))
            writer.writerow([direction, 'L', f"{k:.8f}", f"{omega:.8e}"])
            # T1
            term_T1 = epsilon + 2*c44 - (c44 + epsilon) * sin2
            omega2_T1 = pref * sin2 * term_T1
            omega_T1 = math.sqrt(max(0.0, omega2_T1))
            writer.writerow([direction, 'T1', f"{k:.8f}", f"{omega_T1:.8e}"])
            # T2
            term_T2 = 2*c44 - (2*c44 - c11) * sin2
            omega2_T2 = pref * sin2 * term_T2
            omega_T2 = math.sqrt(max(0.0, omega2_T2))
            writer.writerow([direction, 'T2', f"{k:.8f}", f"{omega_T2:.8e}"])
        else:  # 111
            arg = a_cm * k_cm / math.sqrt(6.0)
            sin2 = math.sin(arg) ** 2
            pref = 2.0 / (rho * a_cm**2)
            # L
            omega2_L = pref * sin2 * (3*c11 - 2*epsilon)
            omega_L = math.sqrt(max(0.0, omega2_L))
            writer.writerow([direction, 'L', f"{k:.8f}", f"{omega_L:.8e}"])
            # T1, T2 degenerate
            omega2_T = pref * sin2 * (3*c44 + epsilon)
            omega_T = math.sqrt(max(0.0, omega2_T))
            writer.writerow([direction, 'T1', f"{k:.8f}", f"{omega_T:.8e}"])
            writer.writerow([direction, 'T2', f"{k:.8f}", f"{omega_T:.8e}"])
EOF
