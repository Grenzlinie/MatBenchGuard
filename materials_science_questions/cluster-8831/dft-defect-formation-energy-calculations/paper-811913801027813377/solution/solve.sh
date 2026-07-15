#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_enthalpies.csv ===
python3 - "$OUTDIR/step_01_formation_enthalpies.csv" << 'PYEOF'
import sys, csv
rows = [
    ['pressure_GPa', 'defect', 'charge', 'H_f_eV'],
    [0,  'C_N', -1, 2.22],
    [0,  'C_N',  0, 2.10],
    [0,  'C_N',  1, 1.92],
    [20, 'C_N', -1, 2.28],
    [20, 'C_N',  0, 2.20],
    [20, 'C_N',  1, 2.01],
    [40, 'C_N', -1, 2.44],
    [40, 'C_N',  0, 2.40],
    [40, 'C_N',  1, 2.09],
    [60, 'C_N', -1, 2.59],
    [60, 'C_N',  0, 2.57],
    [60, 'C_N',  1, 2.17],
    [0,  'C_B', -1, 8.56],
    [0,  'C_B',  0, 3.43],
    [0,  'C_B',  1, -1.10],
    [20, 'C_B', -1, 8.31],
    [20, 'C_B',  0, 3.16],
    [20, 'C_B',  1, -1.48],
    [40, 'C_B', -1, 7.92],
    [40, 'C_B',  0, 2.92],
    [40, 'C_B',  1, -1.61],
    [60, 'C_B', -1, 7.53],
    [60, 'C_B',  0, 2.49],
    [60, 'C_B',  1, -2.07],
]
with open(sys.argv[1], 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF

# === solve block: step_02_defect_level_pressure_coefficients.json ===
python3 -c '
import json, sys
data = {
    "C_B^+1": {
        "pressure_coefficient_meV_GPa": 2.0,
        "level_energies_eV": [6.5, 6.54, 6.58, 6.62]
    },
    "C_B^0": {
        "pressure_coefficient_meV_GPa": -0.5,
        "level_energies_eV": [5.0, 4.99, 4.98, 4.97]
    },
    "C_B^-1": {
        "pressure_coefficient_meV_GPa": -0.5,
        "level_energies_eV": [4.5, 4.49, 4.48, 4.47]
    },
    "C_N^+1": {
        "pressure_coefficient_meV_GPa": 0.5,
        "level_energies_eV": [0.3, 0.31, 0.32, 0.33]
    },
    "C_N^0": {
        "pressure_coefficient_meV_GPa": 0.5,
        "level_energies_eV": [0.5, 0.51, 0.52, 0.53]
    },
    "C_N^-1": {
        "pressure_coefficient_meV_GPa": -0.5,
        "level_energies_eV": [0.1, 0.09, 0.08, 0.07]
    }
}
with open(sys.argv[1], "w") as f:
    json.dump(data, f, indent=2)
' "$OUTDIR/step_02_defect_level_pressure_coefficients.json"
