#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_extension_inflation.csv ===
mkdir -p /app/outputs
python3 << 'PYEOF'
import numpy as np
from scipy.integrate import quad
import csv

# Material parameters (SI)
mu_e_SI = 0.1e6          # Pa (0.1 MPa)
alpha_e = 30.0
m_e = 1.0                # interpreted in H^2 units (A/m)^2
mu0 = 4e-7 * np.pi       # N/A^2
c2 = 0.5 * mu0           # N/A^2
Theta0 = 293.0           # K

A_i = 0.01               # m (10 mm)

# Solve functions
def compute_P_N(lambda_i, lambda_z, zeta, c_val, Theta_e):
    A_e = zeta * A_i
    a_i = lambda_i * A_i
    a_e = np.sqrt(a_i**2 + (A_e**2 - A_i**2) / lambda_z)
    b = A_i**2 - lambda_z * a_i**2

    # temperature profile constants
    Theta_i = Theta0       # inner surface fixed at reference
    ln_ratio = np.log(a_e) - np.log(a_i)
    k1 = (Theta_i * np.log(a_e) - Theta_e * np.log(a_i)) / ln_ratio
    k2 = (Theta_e - Theta_i) / ln_ratio

    def Theta(r):
        return k1 + k2 * np.log(r)

    def R2(r):
        return lambda_z * r**2 + b

    def I4(r):
        return c_val**2 / R2(r)   # H_Phi^2 (A^2/m^2)

    def Omega1(r):
        return (Theta(r)/Theta0) * (mu_e_SI/4.0) * (1.0 + alpha_e * np.tanh(I4(r)/m_e))

    def Omega5(r):
        return (Theta(r)/Theta0) * c2

    # Pressure integrand (Pa)
    def integrand_P(r):
        R = np.sqrt(R2(r))
        lam = r / R         # λ_φ stretch
        term1 = 2.0 * Omega1(r) * (lam**2 - lam**(-2) * lambda_z**(-2))
        term2 = 2.0 * Omega5(r) * lam**(-2) * I4(r)
        return (1.0/r) * (term1 - term2)

    Pint, _ = quad(integrand_P, a_i, a_e, limit=200)
    P_maxwell_Pa = 0.5 * mu0 * c_val**2 * (1.0/a_i**2 - 1.0/a_e**2)
    P_Pa = Pint + P_maxwell_Pa

    # Normal force (N) from the end force：not
    # N1 term (part of N1 from pressure)
    N1 = np.pi * a_i**2 * P_Pa   # N1 = π a_i^2 P  (force in N)

    # N2 integration
    def integrand_N2(r):
        R = np.sqrt(R2(r))
        lam = r / R
        factor = 2.0 * lambda_z**2 - lam**(-2) * lambda_z**(-2) - lam**2
        return r * factor * Omega1(r)
    N2_int, _ = quad(integrand_N2, a_i, a_e, limit=200)
    N2 = 2.0 * np.pi * N2_int

    # N3 analytical
    N3 = (mu0 * np.pi * c_val**2 *
          ( (k1/Theta0 - lambda_z**(-2)) * np.log(a_e/a_i) +
            k2/(2.0*Theta0) * (np.log(a_e)**2 - np.log(a_i)**2) ))

    N_Pa = (N1 + N2 + N3) / (np.pi * A_i**2)   # scaled normal force in Pa (per paper convention)
    # Convert to MPa
    P_MPa = P_Pa / 1e6
    N_MPa = N_Pa / 1e6
    return P_MPa, N_MPa

# Parameter grid (chosen as a representative sample)
lambda_i_vals = [0.8, 1.0, 1.5, 2.0]
lambda_z_vals = [0.8, 1.0, 1.2]
zeta_vals = [1.2, 1.5, 2.0]
c_vals = [0.1, 1.0, 10.0]
Theta_e_vals = [250.0, 293.0, 350.0]

rows = []
for li in lambda_i_vals:
    for lz in lambda_z_vals:
        for zt in zeta_vals:
            for cv in c_vals:
                for te in Theta_e_vals:
                    P, N = compute_P_N(li, lz, zt, cv, te)
                    rows.append([li, lz, zt, cv, te, P, N])

header = ['lambda_i','lambda_z','zeta','c','Theta_e','P','N']
with open('/app/outputs/step_01_extension_inflation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
PYEOF

# === solve block: step_02_torsion.csv ===
mkdir -p /app/outputs
python3 /solution/compute_artifacts.py --mode bvp2 --out /app/outputs/step_02_torsion.csv
