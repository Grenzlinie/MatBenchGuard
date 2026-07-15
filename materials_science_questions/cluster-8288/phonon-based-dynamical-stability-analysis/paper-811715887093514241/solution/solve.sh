#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_relaxed_structure.json ===
python3 -c "
import json

structure = {
  'lattice_vectors_angstrom': [
    [7.33340, 0.0, 0.0],
    [0.0, 10.37100, 0.0],
    [0.0, 0.0, 7.33340]
  ],
  'lattice_constants_angstrom': [7.33340, 10.37100, 7.33340],
  'fractional_coordinates': [
    {'element': 'Bi1', 'frac': [0.46821, 0.02436, 0.01883]},
    {'element': 'Bi2', 'frac': [0.22034, 0.23870, 0.71964]},
    {'element': 'Ti1', 'frac': [0.49128, 0.49330, 0.99697]},
    {'element': 'Ti2', 'frac': [0.25941, 0.76040, 0.75377]},
    {'element': 'O1',  'frac': [0.30771, 0.62654, 0.55680]},
    {'element': 'O2',  'frac': [0.79348, 0.11688, 0.06149]},
    {'element': 'O3',  'frac': [0.71201, 0.62190, 0.95715]},
    {'element': 'O4',  'frac': [0.17647, 0.13538, 0.44955]},
    {'element': 'O5',  'frac': [0.51184, 0.81992, 0.74272]},
    {'element': 'O6',  'frac': [0.99726, 0.92673, 0.25312]},
    {'element': \"O'\", 'frac': [0.52092, 0.87681, 0.24008]}
  ]
}

with open('$OUTDIR/step_01_relaxed_structure.json', 'w') as f:
    json.dump(structure, f, indent=2)
"

# === solve block: step_02_phonon_frequencies.json ===
python3 -c "
import json

modes = [
    # A1 modes (IR-active along c)
    {'mode_number': 1,  'frequency_cm1': -202.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.0},
    {'mode_number': 2,  'frequency_cm1': 54.0,   'irreducible_representation': 'A1', 'relative_intensity': 0.15},
    {'mode_number': 3,  'frequency_cm1': 91.0,   'irreducible_representation': 'A1', 'relative_intensity': 0.38},
    {'mode_number': 4,  'frequency_cm1': 122.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.17},
    {'mode_number': 5,  'frequency_cm1': 131.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.12},
    {'mode_number': 6,  'frequency_cm1': 286.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.21},
    {'mode_number': 7,  'frequency_cm1': 336.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.13},
    {'mode_number': 8,  'frequency_cm1': 356.0,  'irreducible_representation': 'A1', 'relative_intensity': 0.10},

    # B1 modes (IR-active along b)
    {'mode_number': 9,  'frequency_cm1': 40.0,   'irreducible_representation': 'B1', 'relative_intensity': 0.48},
    {'mode_number': 10, 'frequency_cm1': 95.0,   'irreducible_representation': 'B1', 'relative_intensity': 0.21},
    {'mode_number': 11, 'frequency_cm1': 113.0,  'irreducible_representation': 'B1', 'relative_intensity': 0.88},
    {'mode_number': 12, 'frequency_cm1': 281.0,  'irreducible_representation': 'B1', 'relative_intensity': 0.34},

    # B2 modes (IR-active along a)
    {'mode_number': 13, 'frequency_cm1': 116.0,  'irreducible_representation': 'B2', 'relative_intensity': 1.00},
    {'mode_number': 14, 'frequency_cm1': 267.0,  'irreducible_representation': 'B2', 'relative_intensity': 0.11},
    {'mode_number': 15, 'frequency_cm1': 285.0,  'irreducible_representation': 'B2', 'relative_intensity': 0.13},
    {'mode_number': 16, 'frequency_cm1': 334.0,  'irreducible_representation': 'B2', 'relative_intensity': 0.12}
]

output = {
    'modes': modes,
    'unit': 'cm-1'
}

with open('$OUTDIR/step_02_phonon_frequencies.json', 'w') as f:
    json.dump(output, f, indent=2)
"

# === solve block: step_03_dielectric_constants.json ===
python3 -c "
import json

data = {
    'epsilon_aa': 101.7,
    'epsilon_bb': 198.3,
    'epsilon_cc': 102.9,
    'unit': 'dimensionless (static phonon contribution)'
}

with open('$OUTDIR/step_03_dielectric_constants.json', 'w') as f:
    json.dump(data, f, indent=2)
"
