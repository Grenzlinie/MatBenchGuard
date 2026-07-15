#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: step_02_gamma_surface_relaxation.csv ===
python3 -c "
import csv
rows = [
    ['gamma-Al2O3(110)', 'O1', 0.01, -0.80, 0.01, -0.81],
    ['gamma-Al2O3(110)', 'O2', 0.02, -0.82, 0.03, -0.84],
    ['gamma-Al2O3(110)', 'O3', 0.00, -0.68, -0.02, -0.70],
    ['gamma-Al2O3(110)', 'O4', 0.31, -0.68, 0.10, -0.69],
    ['gamma-Al2O3(110)', 'Al1', -0.05, 1.02, -0.04, 1.05],
    ['gamma-Al2O3(110)', 'Al2', -0.16, 1.07, 0.07, 1.11],
    ['gamma-Al2O3(110)', 'Al3', -0.18, 0.92, -0.13, 0.94],
]
with open('$OUTDIR/step_02_gamma_surface_relaxation.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['surface', 'atom_label', 'delta_z_gas', 'Q_gas', 'delta_z_liquid', 'Q_liquid'])
    w.writerows(rows)
"

# === solve block: step_03_boehmite_surface_relaxation.csv ===
python3 -c "
import csv
rows = [
    ['AlOOH(100)', 'Al', -0.13, 0.93, 0.05, 1.00],
    ['AlOOH(100)', 'O',  -0.16, -0.71, -0.02, -0.81],
]
with open('$OUTDIR/step_03_boehmite_surface_relaxation.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['surface', 'atom_label', 'delta_z_gas', 'Q_gas', 'delta_z_liquid', 'Q_liquid'])
    w.writerows(rows)
"

# === solve block: step_04_gamma_adsorption_energies.csv ===
python3 -c "
import csv
rows = [
    ['CH3OH', 'Al3', -1.28, -1.07],
    ['H2O',   'Al3', -1.23, -1.09],
    ['DME',   'Al3', -1.04, -0.65],
]
with open('$OUTDIR/step_04_gamma_adsorption_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['adsorbate', 'site_type', 'Eads_gas', 'Eads_liquid'])
    w.writerows(rows)
"

# === solve block: step_05_boehmite_adsorption_energies.csv ===
python3 -c "
import csv
rows = [
    ['CH3OH', -0.92, -0.76],
    ['H2O',   -0.95, -0.64],
    ['DME',   -1.01, -0.85],
]
with open('$OUTDIR/step_05_boehmite_adsorption_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['adsorbate', 'Eads_gas', 'Eads_liquid'])
    w.writerows(rows)
"

# === solve block: step_06_gamma_reaction_profile.json ===
python3 -c "
import json
data = {
    'path_I': {'Ea_gas': 1.49, 'Ea_liquid': 1.26},
    'path_II': {'Ea_gas': 0.73, 'Ea_liquid': 0.39},
    'path_III': {'Ea_gas': 1.58, 'Ea_liquid': 1.23},
    'preferred_path_gas': 'III',
    'preferred_path_liquid': 'III',
}
with open('$OUTDIR/step_06_gamma_reaction_profile.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_07_boehmite_reaction_profile.json ===
python3 -c "
import json
data = {
    'path_I': {'Ea_gas': 0.91, 'Ea_liquid': 0.71},
    'path_II': {'Ea_gas': 0.81, 'Ea_liquid': 0.85},
    'path_III': {'Ea_gas': 1.49, 'Ea_liquid': 1.45},
    'preferred_path_gas': 'I/II',
    'preferred_path_liquid': 'I',
}
with open('$OUTDIR/step_07_boehmite_reaction_profile.json', 'w') as f:
    json.dump(data, f, indent=2)
"
