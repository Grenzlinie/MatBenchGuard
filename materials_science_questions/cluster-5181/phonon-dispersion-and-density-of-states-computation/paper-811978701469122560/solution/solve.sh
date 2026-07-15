#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mean_square_displacements.json ===
python3 -c "
import json

data = {
    'NH4Cl': [
        {'T_K': 85, 'Cl_u2': 6.54, 'N_u2': 7.99, 'H_perp_u2': 31.2, 'H_par_u2': 13.0},
        {'T_K': 105, 'Cl_u2': 7.57, 'N_u2': 8.93, 'H_perp_u2': 32.3, 'H_par_u2': 14.0},
        {'T_K': 125, 'Cl_u2': 8.67, 'N_u2': 9.96, 'H_perp_u2': 33.6, 'H_par_u2': 15.0},
        {'T_K': 145, 'Cl_u2': 9.80, 'N_u2': 11.05, 'H_perp_u2': 35.0, 'H_par_u2': 16.1},
        {'T_K': 165, 'Cl_u2': 10.96, 'N_u2': 12.19, 'H_perp_u2': 36.7, 'H_par_u2': 17.2}
    ],
    'ND4Cl': [
        {'T_K': 85, 'Cl_u2': 6.64, 'N_u2': 7.75, 'D_perp_u2': 23.6, 'D_par_u2': 11.0},
        {'T_K': 105, 'Cl_u2': 7.57, 'N_u2': 8.74, 'D_perp_u2': 25.0, 'D_par_u2': 11.9},
        {'T_K': 125, 'Cl_u2': 8.67, 'N_u2': 9.81, 'D_perp_u2': 26.6, 'D_par_u2': 13.0},
        {'T_K': 145, 'Cl_u2': 9.80, 'N_u2': 10.94, 'D_perp_u2': 28.4, 'D_par_u2': 14.2},
        {'T_K': 165, 'Cl_u2': 10.96, 'N_u2': 12.10, 'D_perp_u2': 30.3, 'D_par_u2': 15.3}
    ],
    'NH_bond_amplitude': 5.76,
    'ND_bond_amplitude': 4.16
}

with open('/app/outputs/mean_square_displacements.json', 'w') as f:
    json.dump(data, f, indent=2)
"
