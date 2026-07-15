#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: orbital_populations.json ===
python3 -c '
import json, os
data = {
  "gamma_Fe6_orbital_population": {
    "Fe_3d": 6.4619,
    "Fe_4s": 0.9763,
    "Fe_4p": 0.5718
  },
  "gamma_prime_Fe6N_orbital_population": {
    "N_2s": 1.566,
    "N_2p": 3.753,
    "Fe_3s": 2.106,
    "Fe_3p": 6.275,
    "Fe_3d": 5.930,
    "Fe_4s": 0.921,
    "Fe_4p": 0.449
  },
  "N_Fe_overlap_population": {
    "N_Fe_3s": -0.010,
    "N_Fe_3p": -0.1227,
    "N_Fe_3d": 0.4335,
    "N_Fe_4s": 0.1149,
    "N_Fe_4p": 0.3696,
    "N_Fe_total": 0.7853
  }
}
outdir = os.environ["OUTDIR"]
with open(os.path.join(outdir, "orbital_populations.json"), "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: binding_energies.csv ===
python3 -c "
import csv, os

header = ['phase', 'cluster', 'binding_energy']
rows = [
    ['alpha-Fe', 'alpha-Fe6', 37.765],
    ['alpha_prime-FeN', 'alpha_prime-Fe6N', 69.391],
    ['alpha_prime-FeC', 'alpha_prime-Fe6C', 65.750],
    ['gamma_prime-Fe4N', 'gamma_prime-Fe6N', 89.390],
    ['gamma_prime-Fe4C', 'gamma_prime-Fe6C', 94.620],
    ['epsilon_prime-Fe3N', 'epsilon_prime-Fe6N', 85.611],
    ['epsilon_prime-Fe3C', 'epsilon_prime-Fe6C', 83.852],
    ['epsilon_prime-Fe2N', 'epsilon_prime-Fe6N', 83.381],
    ['epsilon_prime-Fe2C', 'epsilon_prime-Fe6C', 80.560]
]
outdir = os.environ['OUTDIR']
with open(os.path.join(outdir, 'binding_energies.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
"
