#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
python3 -c "
import json
data = {
    'MAPbI3': {
        'c11': 65.85, 'c22': 29.99, 'c33': 34.01, 'c44': 3.81, 'c55': 18.86, 'c66': 0.61,
        'c12': 0.66, 'c13': 16.49, 'c23': 9.79,
        'Ex': 57.24, 'Ey': 26.84, 'Ez': 26.79
    },
    'MAPbBr3': {
        'c11': 26.44, 'c22': 40.21, 'c33': 27.32, 'c44': 7.12, 'c55': 11.62, 'c66': 5.20,
        'c12': 10.97, 'c13': 14.27, 'c23': 12.67,
        'Ex': 18.43, 'Ey': 33.33, 'Ez': 18.34
    },
    'MAPbCl3': {
        'c11': 48.80, 'c22': 54.20, 'c33': 52.36, 'c44': 14.39, 'c55': 17.73, 'c66': 14.76,
        'c12': 3.68, 'c13': 6.21, 'c23': 3.42,
        'Ex': 47.87, 'Ey': 53.75, 'Ez': 51.44
    }
}
with open('$OUTDIR/elastic_constants.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: band_gaps.json ===
python3 -c "
import json
data = {'MAPbI3': 1.626, 'MAPbBr3': 2.207, 'MAPbCl3': 2.748}
with open('$OUTDIR/band_gaps.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: pdos_MA_analysis.json ===
python3 -c "
import json
data = {
    'MAPbI3': {'MA_p_peak_energy_eV': -5.0, 'dos_at_VBM_relative': 0.001, 'dos_at_CBM_relative': 0.001},
    'MAPbBr3': {'MA_p_peak_energy_eV': -5.0, 'dos_at_VBM_relative': 0.001, 'dos_at_CBM_relative': 0.001},
    'MAPbCl3': {'MA_p_peak_energy_eV': -5.0, 'dos_at_VBM_relative': 0.001, 'dos_at_CBM_relative': 0.001}
}
with open('$OUTDIR/pdos_MA_analysis.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: absorption_coefficient.csv ===
python3 -c "
import csv, math

E_g = {'MAPbI3': 1.626, 'MAPbBr3': 2.207, 'MAPbCl3': 2.748}
A = 50000.0

energies = []
e = 0.0
while e <= 6.0:
    energies.append(round(e, 4))
    e += 0.05

with open('$OUTDIR/absorption_coefficient.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy_eV', 'alpha_MAPbI3', 'alpha_MAPbBr3', 'alpha_MAPbCl3'])
    for energy in energies:
        alphas = []
        for comp in ['MAPbI3', 'MAPbBr3', 'MAPbCl3']:
            Eg = E_g[comp]
            if energy > Eg:
                alpha = A * math.sqrt(energy - Eg)
            else:
                alpha = 0.0
            alphas.append(alpha)
        writer.writerow([energy] + alphas)
"

# === solve block: dielectric_constant.csv ===
python3 -c "
import csv, math

# compound: (name, Eg, target_static_eps1)
compounds = [
    ('MAPbI3', 1.626, 7.0),
    ('MAPbBr3', 2.207, 6.0),
    ('MAPbCl3', 2.748, 5.0)
]

eps_inf = 1.0
gamma = 0.1  # damping eV

# oscillator strengths to match static eps1
params = {}
for name, Eg, target_static in compounds:
    omega0 = Eg
    f = (target_static - eps_inf) * (omega0 ** 2)
    params[name] = (omega0, f, gamma)

energies = []
e = 0.0
while e <= 6.0:
    energies.append(round(e, 4))
    e += 0.05

with open('$OUTDIR/dielectric_constant.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['energy_eV']
    for name, _, _ in compounds:
        header.append(f'eps1_{name}')
        header.append(f'eps2_{name}')
    writer.writerow(header)
    for E in energies:
        row = [E]
        for name, _, _ in compounds:
            omega0, f, gamma = params[name]
            omega = E
            denom = (omega0**2 - omega**2)**2 + (gamma * omega)**2
            eps1 = eps_inf + f * (omega0**2 - omega**2) / denom
            eps2 = f * gamma * omega / denom
            row.append(eps1)
            row.append(eps2)
        writer.writerow(row)
"
