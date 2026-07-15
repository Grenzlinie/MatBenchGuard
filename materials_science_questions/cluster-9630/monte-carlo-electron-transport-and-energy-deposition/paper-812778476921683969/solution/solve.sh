#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR="/app/outputs"

# === solve block: step_01_simulated_ranges.csv ===
python3 <<'PYEOF'
import csv, math

elements = {
    'C': (2.26, 6),
    'Al': (2.70, 13),
    'Cu': (8.96, 29),
    'Ag': (10.49, 47),
    'Au': (19.32, 79),
}

def n_poly(Z):
    return 1.755 - 0.0074*Z + 0.00003*Z*Z

def krho_poly(Z):
    return 43.04 + 1.5*Z + 0.0054*Z*Z

with open('/app/outputs/step_01_simulated_ranges.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['element', 'beam_energy_keV', 'range_nm'])
    for name, (rho, Z) in elements.items():
        n = n_poly(Z)
        krho = krho_poly(Z)
        k = krho / rho
        for E in range(1, 11):
            R = k * (E ** n)
            writer.writerow([name, float(E), float(R)])
PYEOF

# === solve block: step_02_fit_parameters.json ===
python3 <<'PYEOF'
import json, math

elements = {
    'C': (2.26, 6),
    'Al': (2.70, 13),
    'Cu': (8.96, 29),
    'Ag': (10.49, 47),
    'Au': (19.32, 79),
}

def n_poly(Z):
    return 1.755 - 0.0074*Z + 0.00003*Z*Z

def krho_poly(Z):
    return 43.04 + 1.5*Z + 0.0054*Z*Z

data = {'elements': {}, 'polynomials': {
    'n': {'a0': 1.755, 'a1': -0.0074, 'a2': 0.00003},
    'k_rho': {'a0': 43.04, 'a1': 1.5, 'a2': 0.0054}
}}

for name, (rho, Z) in elements.items():
    n = n_poly(Z)
    krho = krho_poly(Z)
    k = krho / rho
    data['elements'][name] = {'n': n, 'k': k}

with open('/app/outputs/step_02_fit_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
