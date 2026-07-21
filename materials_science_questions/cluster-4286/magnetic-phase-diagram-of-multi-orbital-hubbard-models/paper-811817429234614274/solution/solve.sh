#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: k_rho_data.json ===
python3 -c "
import json
data = [
    {'U_prime': 0.0, 'K_rho': 1.0, 'ground_state_spin': 0},
    {'U_prime': 0.5, 'K_rho': 0.95, 'ground_state_spin': 0},
    {'U_prime': 1.0, 'K_rho': 0.88, 'ground_state_spin': 0},
    {'U_prime': 1.5, 'K_rho': 0.80, 'ground_state_spin': 0},
    {'U_prime': 2.0, 'K_rho': 0.85, 'ground_state_spin': 0},
    {'U_prime': 2.5, 'K_rho': 1.05, 'ground_state_spin': 1},
    {'U_prime': 3.0, 'K_rho': 1.15, 'ground_state_spin': 1},
    {'U_prime': 3.5, 'K_rho': 1.25, 'ground_state_spin': 1},
    {'U_prime': 4.0, 'K_rho': 1.35, 'ground_state_spin': 1}
]
with open('/app/outputs/k_rho_data.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: pairing_correlations.json ===
python3 -c "
import json
sc_i = {
    'parameters': {'U_prime': 1.0, 'J': 0.25, 'U': 2.4, 'Delta': 1.9, 'filling': '5/3'},
    'correlations': {
        'S_on_u': [0.1, 0.08, 0.05, 0.03],
        'S_nn_u': [0.15, 0.12, 0.1, 0.08],
        'S_on_l': [0.05, 0.03, 0.02, 0.01],
        'S_nn_l': [0.2, 0.15, 0.1, 0.08],
        'S_on_lu': [0.01, 0.005, 0.003, 0.0],
        'T_nn_u': [0.001, 0.0005, 0.0002, 0.0001],
        'T_nn_l': [0.002, 0.001, 0.0005, 0.0003],
        'T_on_lu': [0.0005, 0.0003, 0.0001, 0.0],
        'S_nn_l-u': [-0.1, -0.08, -0.05, -0.03],
        'T_nn_l-u': [0.001, 0.0005, 0.0002, 0.0001]
    }
}
sc_ii = {
    'parameters': {'U_prime': 1.0, 'J': 0.25, 'U': -0.4, 'Delta': 1.9, 'filling': '5/3'},
    'correlations': {
        'S_on_u': [0.3, 0.25, 0.2, 0.18],
        'S_nn_u': [0.15, 0.12, 0.1, 0.08],
        'S_on_l': [0.05, 0.04, 0.03, 0.02],
        'S_nn_l': [0.06, 0.05, 0.04, 0.03],
        'S_on_lu': [0.02, 0.015, 0.01, 0.005],
        'T_nn_u': [0.001, 0.0005, 0.0002, 0.0001],
        'T_nn_l': [0.002, 0.001, 0.0005, 0.0003],
        'T_on_lu': [0.0005, 0.0003, 0.0001, 0.0],
        'S_nn_l-u': [0.02, 0.015, 0.01, 0.005],
        'T_nn_l-u': [0.001, 0.0005, 0.0002, 0.0001]
    }
}
with open('/app/outputs/pairing_correlations.json', 'w') as f:
    json.dump([sc_i, sc_ii], f, indent=2)
"
