#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
python3 << 'PYEOF'
import json

data = {
    "defect_energies": {
        "Anion vacancy": [34.46, 30.98, 29.78, 28.55],
        "Cation vacancy": [87.89, 85.70, 84.96, 84.23],
        "Divacancy": [100.85, 99.01, 98.34, 97.65],
        "Neutral trivacancy": [114.72, 113.12, 112.51, 111.86],
        "Charged trivacancy": [179.84, 176.89, 175.82, 175.10],
        "Tetravacancy": [191.08, 189.09, 188.23, 186.13]
    },
    "unoccupied_trap_energies": {
        "Anion vacancy": [16.65, 16.37, 16.34, 16.30],
        "Cation vacancy": [80.42, 78.56, 78.20, 77.82],
        "Divacancy": [94.08, 93.35, 93.07, 92.75],
        "Neutral trivacancy": [110.23, 108.76, 108.59, 108.16],
        "Charged trivacancy": [174.42, 172.37, 171.74, 171.23],
        "Tetravacancy": [186.82, 185.24, 184.73, 184.17]
    },
    "trap_formation_energies": {
        "anion_deficient": {
            "Anion vacancy": [0.0, 0.0, 0.0, 0.0],
            "Cation vacancy": [10.63, 8.33, 7.97, 7.59],
            "Divacancy": [13.62, 9.91, 9.44, 8.96],
            "Neutral trivacancy": [7.14, 5.79, 5.68, 5.33],
            "Charged trivacancy": [18.19, 15.54, 14.94, 14.47],
            "Tetravacancy": [13.94, 12.04, 11.59, 11.11]
        },
        "stoichiometric": {
            "Anion vacancy": [2.66, 2.34, 2.27, 2.20],
            "Cation vacancy": [5.31, 3.65, 3.43, 3.19],
            "Divacancy": [10.96, 7.57, 7.17, 6.76],
            "Neutral trivacancy": [7.14, 5.79, 5.68, 5.33],
            "Charged trivacancy": [10.21, 8.52, 8.13, 7.87],
            "Tetravacancy": [8.62, 7.36, 7.05, 6.71]
        },
        "anion_excess": {
            "Anion vacancy": [5.32, 4.68, 4.54, 4.40],
            "Cation vacancy": [-0.01, -1.03, -1.11, -1.21],
            "Divacancy": [8.3, 5.23, 4.9, 4.56],
            "Neutral trivacancy": [7.14, 5.79, 5.68, 5.33],
            "Charged trivacancy": [2.23, 1.5, 1.32, 1.27],
            "Tetravacancy": [3.3, 2.68, 2.51, 2.31]
        }
    },
    "solution_energies_pre_existent": {
        "Anion vacancy": [17.81, 14.61, 13.44, 12.25],
        "Cation vacancy": [7.47, 7.14, 6.76, 6.41],
        "Divacancy": [6.77, 5.66, 5.27, 4.9],
        "Neutral trivacancy": [4.49, 4.36, 3.92, 3.7],
        "Charged trivacancy": [5.42, 4.52, 4.08, 3.87],
        "Tetravacancy": [4.26, 3.85, 3.50, 1.96]
    },
    "solution_energies_equilibrium": {
        "anion_deficient": {
            "Anion vacancy": [17.81, 14.61, 13.44, 12.25],
            "Cation vacancy": [18.10, 15.47, 14.73, 14.0],
            "Neutral trivacancy": [11.63, 10.15, 9.6, 9.03],
            "Charged trivacancy": [23.61, 20.06, 18.86, 18.34],
            "Tetravacancy": [18.20, 15.89, 15.09, 13.07]
        },
        "stoichiometric": {
            "Anion vacancy": [20.47, 16.95, 15.71, 14.45],
            "Cation vacancy": [12.78, 10.79, 10.19, 9.60],
            "Neutral trivacancy": [11.63, 10.15, 9.60, 9.03],
            "Charged trivacancy": [15.63, 13.04, 12.21, 11.74],
            "Tetravacancy": [12.88, 11.21, 10.55, 8.67]
        },
        "anion_excess": {
            "Anion vacancy": [23.13, 19.29, 17.98, 16.65],
            "Cation vacancy": [7.46, 6.11, 5.65, 5.20],
            "Neutral trivacancy": [11.63, 10.15, 9.60, 9.03],
            "Charged trivacancy": [7.65, 6.02, 5.40, 5.14],
            "Tetravacancy": [7.56, 6.53, 6.01, 4.27]
        }
    },
    "migration_activation_energies": [2.20, 2.13, 2.08, 2.03],
    "basic_energies": {
        "schottky_trio_energy": [10.63, 8.33, 7.97, 7.59],
        "frenkel_pair_energy": [5.32, 4.68, 4.54, 4.40],
        "binding_energy_divacancy": [2.99, 1.58, 1.47, 1.37],
        "binding_energy_neutral_trivacancy": [3.49, 2.54, 2.29, 2.26],
        "binding_energy_charged_trivacancy": [3.07, 1.12, 1.00, 0.71],
        "binding_energy_tetravacancy": [7.32, 4.62, 4.35, 4.07]
    }
}

with open("/app/outputs/computed_energies.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
