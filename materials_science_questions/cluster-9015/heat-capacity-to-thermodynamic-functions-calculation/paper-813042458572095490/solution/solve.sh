#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thermodynamic_functions.csv ===
python3 - "$OUTDIR/thermodynamic_functions.csv" << 'PYEOF'
import math, csv, sys

# Fundamental constants
h = 6.62607015e-34          # J·s
c = 2.99792458e10           # cm/s
k = 1.380649e-23            # J/K
R = 8.314462618             # J/(mol·K)
NA = 6.02214076e23           # mol⁻¹
p = 1e5                     # Pa (1 bar)

# Atomic masses (g/mol -> kg/mol)
Y_mass = 88.90585
F_mass = 18.9984032

# Molecular masses in kg per molecule
m_YF3  = (Y_mass + 3*F_mass) * 1e-3 / NA
m_Y2F6 = (2*Y_mass + 6*F_mass) * 1e-3 / NA

# Product of moments of inertia: paper gives IA*IB*IC in  g³ cm⁶ × 10⁻¹¹⁷
# Convert to kg³ m⁶: 1 g³ cm⁶ = 1e-21 kg³ m⁶
IAIBIC_YF3  = 15.3e3 * 1e-117 * 1e-21    # = 15.3e-135? Actually 15.3e-114 * 1e-21 = 1.53e-133? We'll just evaluate directly.
IAIBIC_Y2F6 = 245.1e4 * 1e-117 * 1e-21

# Symmetry numbers
sigma_YF3  = 6
sigma_Y2F6 = 4

# Vibrational frequencies (cm⁻¹) and degeneracies
freqs_YF3 = [(575,1), (95,1), (595,2), (140,2)]
freqs_Y2F6 = [(611,1), (579.8,1), (593,1), (554.7,1), (425,1), (414,1),
              (361,1), (360,1),   (201,1),   (196,1),   (133,1), (125,1),
              (110,1), (105,1),   (94,1),    (69,1),    (55,1),  (38,1)]

def compute(mol_mass, product_inertia, sigma, freqs, temperatures):
    results = []
    for T in temperatures:
        # Translational contribution
        V = k*T / p                              # volume per molecule (m³)
        qt = (2*math.pi*mol_mass*k*T / h**2)**1.5 * V
        S_trans = R * (math.log(qt) + 2.5)
        H_trans = 2.5 * R * T                    # H(T)-H(0) for translation

        # Rotational contribution (non‑linear rigid rotor)
        fac = (8 * math.pi**2 * k * T / h**2) ** 1.5
        q_rot = (1.0/sigma) * fac * math.sqrt(math.pi * product_inertia)
        S_rot  = R * (math.log(q_rot) + 1.5)
        H_rot  = 1.5 * R * T

        # Vibrational contribution (harmonic oscillator)
        S_vib = 0.0
        H_vib = 0.0
        Cv_vib = 0.0
        for nu, g in freqs:
            u = h * c * nu / (k * T)
            expu = math.exp(u)
            # energy above zero‑point
            H_vib += R * g * u / (expu - 1)
            S_vib += R * g * (u/(expu - 1) - math.log(1 - math.exp(-u)))
            Cv_vib += R * g * (u**2 * expu) / (expu - 1)**2

        # Total enthalpy increment (J/mol) -> kJ/mol
        H_minus_H0 = (H_trans + H_rot + H_vib) / 1000.0

        # Total entropy
        S_total = S_trans + S_rot + S_vib

        # Heat capacity at constant pressure (J/(mol·K))
        Cp = 4*R + Cv_vib

        # Reduced Gibbs energy
        Phi = S_total - (H_trans + H_rot + H_vib) / T

        results.append((T, Cp, S_total, Phi, H_minus_H0))
    return results

# Temperatures required (K)
Ts = [298.15, 1000, 2000, 3000]

# Compute for both molecules
res_YF3  = compute(m_YF3,  IAIBIC_YF3,  sigma_YF3,  freqs_YF3,  Ts)
res_Y2F6 = compute(m_Y2F6, IAIBIC_Y2F6, sigma_Y2F6, freqs_Y2F6, Ts)

# Write CSV
outpath = sys.argv[1]
with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['molecule','T','Cp','S','Phi','H_minus_H0'])
    for T, Cp, S, Phi, H in res_YF3:
        w.writerow(['YF3', round(T,2), round(Cp,6), round(S,6), round(Phi,6), round(H,6)])
    for T, Cp, S, Phi, H in res_Y2F6:
        w.writerow(['Y2F6', round(T,2), round(Cp,6), round(S,6), round(Phi,6), round(H,6)])
PYEOF
