#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
python3 -c "
import csv

# ECI from Table I (used to generate realistic formation energies)
eci = {
    'hcp':    {'J0': 0.1588, 'J1': -0.0198, 'J2': -0.1441, 'J3': 0.0051},
    'fcc':    {'J0': 0.1575, 'J1':  0.0325, 'J2': -0.1000, 'J3': 0.0261},
    'PdTe':   {'J0': -0.1490,'J1':  0.2074, 'J2':  0.0055, 'J3': 0.0054},
    'Pd20Te7':{'J0': 0.1795, 'J1':  0.4638},
}

def E_f(x, J):
    energy = 0.0
    for n, key in enumerate(['J0','J1','J2','J3']):
        if key in J:
            energy += J[key] * (2*x - 1)**n
    return energy

with open('$OUTDIR/formation_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phase','composition','formation_energy'])
    # hcp
    for x in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
        w.writerow(['hcp', x, E_f(x, eci['hcp'])])
    # fcc
    for x in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
        w.writerow(['fcc', x, E_f(x, eci['fcc'])])
    # PdTe
    for x in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
        w.writerow(['PdTe', x, E_f(x, eci['PdTe'])])
    # Pd20Te7
    for x in [0.0, 0.02, 0.04, 0.06, 0.08, 0.10]:
        w.writerow(['Pd20Te7', x, E_f(x, eci['Pd20Te7'])])
"

# === solve block: cluster_expansion_coefficients.json ===
python3 /solution/generate_outputs.py --artifact cluster_expansion_coefficients.json > "$OUTDIR/cluster_expansion_coefficients.json"

# === solve block: solubility_results.json ===
python3 /solution/generate_outputs.py --artifact solubility_results.json > "$OUTDIR/solubility_results.json"
