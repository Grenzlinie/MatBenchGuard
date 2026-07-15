#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_parameters.csv ===
python3 <<'PYEOF' > /app/outputs/thermodynamic_parameters.csv
import csv
import math
import sys

# Binary mixing enthalpy parameters ΔH_ij (kJ mol⁻¹) for all i<j pairs
Omega = {
    ('Cu','Fe'): 52, ('Cu','Mn'): 16, ('Cu','Ni'): 16, ('Cu','Cr'): 48,
    ('Fe','Mn'):  0, ('Fe','Ni'): -8, ('Fe','Cr'): -4,
    ('Mn','Ni'): -32, ('Mn','Cr'): 8,
    ('Ni','Cr'): -28
}

# Atomic radii (pm)
radii = {'Cu':128, 'Fe':124, 'Mn':135, 'Ni':125, 'Cr':128}

# Valence electron counts
VEC_dict = {'Cu':11, 'Fe':8, 'Mn':7, 'Ni':10, 'Cr':6}

# Melting points (K) for Ω calculation (using T_m = Σ c_i T_m_i)
Tm = {'Cu':1358, 'Fe':1811, 'Mn':1519, 'Ni':1728, 'Cr':2180}

R = 8.314  # J K⁻¹ mol⁻¹

# Alloy compositions: x values and alloy labels
x_vals = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
alloy_names = ['0%Cr', '5%Cr', '10%Cr', '15%Cr', '20%Cr', '25%Cr']

# Elements in order (for iteration consistency)
elements = ['Cu', 'Fe', 'Mn', 'Ni', 'Cr']

out = csv.writer(sys.stdout)
out.writerow(['Alloy','Cr_content','Delta_H_mix_kJ_mol','Delta_S_mix_J_K_mol','Omega','delta_percent','VEC'])

for i, x in enumerate(x_vals):
    # atomic fractions
    c_Cr = x
    base = (1.0 - x) / 4.0
    c = {'Cu': base, 'Fe': base, 'Mn': base, 'Ni': base, 'Cr': c_Cr}
    # sanity: sum must be 1
    assert abs(sum(c.values()) - 1.0) < 1e-12

    # ΔH_mix (kJ mol⁻¹) = Σ_{i<j} c_i c_j Ω_ij
    delta_H = 0.0
    for i1 in range(len(elements)):
        for j1 in range(i1+1, len(elements)):
            e1, e2 = elements[i1], elements[j1]
            pair = (e1, e2) if (e1, e2) in Omega else (e2, e1)
            delta_H += c[e1] * c[e2] * Omega[pair]

    # ΔS_mix = -R Σ c_i ln c_i
    delta_S = -R * sum(c[e] * math.log(c[e]) for e in elements if c[e] > 0)

    # Ω = T_m ΔS_mix / |ΔH_mix|, T_m = Σ c_i T_m_i  (ΔH_mix in kJ -> J)
    T_m = sum(c[e] * Tm[e] for e in elements)
    omega = (T_m * delta_S) / (abs(delta_H) * 1000.0)   # convert kJ->J

    # δ = 100 * sqrt( Σ c_i (1 - r_i/⟨r⟩)² )
    r_avg = sum(c[e] * radii[e] for e in elements)
    var = sum(c[e] * (1.0 - radii[e]/r_avg)**2 for e in elements)
    delta_percent = 100.0 * math.sqrt(var)

    # VEC = Σ c_i VEC_i
    vec = sum(c[e] * VEC_dict[e] for e in elements)

    # Write row with appropriate precision
    out.writerow([
        alloy_names[i],
        x,
        round(delta_H, 8),
        round(delta_S, 8),
        round(omega, 8),
        round(delta_percent, 8),
        round(vec, 8)
    ])
PYEOF
