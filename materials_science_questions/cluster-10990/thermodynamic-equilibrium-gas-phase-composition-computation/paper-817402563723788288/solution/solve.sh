#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTPUT_DIR=/app/outputs
mkdir -p "$OUTPUT_DIR"

# === solve block: thermodynamic_composition.csv ===
python3 << 'PYEOF'
import math, csv, os

temperatures = [2000, 2500, 3000, 3500, 4000, 4500, 5000]

# Coefficients from Table 2 of the paper: (A, T_char)
# Units: A in atm, T_char in K, for p = p0 = 1 atm the formula reduces to p_i = A * exp(-T_char/T)
species_coeff = {
    'B':   (515000,   58800),
    'N':   (3600,     58100),
    'BN':  (359000,   65000),
    'B2N': (535000,   40700),
    'N3':  (2.9e-3,   51700),
    'B2':  (1962000,  81900),
    'B3':  (238000,   74100),
}

outdir = os.environ.get('OUTPUT_DIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
csv_path = os.path.join(outdir, 'thermodynamic_composition.csv')

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Temperature_K',
        'p_B_atm', 'p_N_atm', 'p_BN_atm', 'p_B2N_atm',
        'p_N2_atm', 'p_N3_atm', 'p_B2_atm', 'p_B3_atm'
    ])
    for T in temperatures:
        p_B   = species_coeff['B'][0]   * math.exp(-species_coeff['B'][1]   / T)
        p_N   = species_coeff['N'][0]   * math.exp(-species_coeff['N'][1]   / T)
        p_BN  = species_coeff['BN'][0]  * math.exp(-species_coeff['BN'][1]  / T)
        p_B2N = species_coeff['B2N'][0] * math.exp(-species_coeff['B2N'][1] / T)
        p_N3  = species_coeff['N3'][0]  * math.exp(-species_coeff['N3'][1]  / T)
        p_B2  = species_coeff['B2'][0]  * math.exp(-species_coeff['B2'][1]  / T)
        p_B3  = species_coeff['B3'][0]  * math.exp(-species_coeff['B3'][1]  / T)

        # N2 dominates; its partial pressure is the remainder to 1 atm
        sum_others = p_B + p_N + p_BN + p_B2N + p_N3 + p_B2 + p_B3
        p_N2 = max(0.0, 1.0 - sum_others)

        writer.writerow([T, p_B, p_N, p_BN, p_B2N, p_N2, p_N3, p_B2, p_B3])
PYEOF

# === solve block: droplet_diameter.txt ===
python3 << 'PYEOF'
import math, os

# Constants from the paper
r0 = 1.2e-10          # Wigner-Seitz radius (m)
n0 = 3.0e22           # initial boron atom density (m^-3)
T_nucl = 3200.0       # nucleation temperature (K)
T_end  = 2800.0       # BNNT formation temperature (K)
cooling_rate = 6.0e4  # cooling rate (K/s)
m_B = 1.79e-26        # mass of boron atom (kg)
k = 1.380649e-23      # Boltzmann constant (J/K)

# Equation (11): D = (2*r0)^(9/5) * n0^(2/5) * [2*pi*k*(T_nucl+T_end)/m_B]^(1/5) * [(T_nucl-T_end)/cooling_rate]^(2/5)
term1 = (2.0 * r0) ** (9.0 / 5.0)
term2 = n0 ** (2.0 / 5.0)
term3 = (2.0 * math.pi * k * (T_nucl + T_end) / m_B) ** (1.0 / 5.0)
term4 = ((T_nucl - T_end) / cooling_rate) ** (2.0 / 5.0)

D_m  = term1 * term2 * term3 * term4   # diameter in meters
D_nm = D_m / 1.0e-9                    # convert to nanometers

outdir = os.environ.get('OUTPUT_DIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
out_path = os.path.join(outdir, 'droplet_diameter.txt')
with open(out_path, 'w') as f:
    f.write(f'{D_nm}\n')
PYEOF
