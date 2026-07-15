#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: formation_energies.json ===
python3 -c "
import json

data = {
    'c-OsN2_GGA': 0.5217,
    'N-vacancy_GGA': 0.5562,
    'O-substitution_GGA': 0.4816
}
with open('/app/outputs/formation_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: elastic_properties.json ===
python3 -c "
import json

data = {
    'c-OsN2_GGA': {
        'C11': 744, 'C12': 175, 'C13': 278, 'C22': 908,
        'C33': 575, 'C44': 132, 'C55': 339, 'C66': 173,
        'B': 363, 'G': 256, 'v': 0.215, 'G_B': 0.705
    },
    'N-vacancy_GGA': {
        'C11': 675, 'C12': 159, 'C13': 270, 'C22': 823,
        'C33': 507, 'C44': 114, 'C55': 289, 'C66': 136,
        'B': 340, 'G': 213, 'v': 0.241, 'G_B': 0.626
    },
    'O-substitution_GGA': {
        'C11': 698, 'C12': 182, 'C13': 256, 'C22': 854,
        'C33': 489, 'C44': 127, 'C55': 296, 'C66': 166,
        'B': 340, 'G': 233, 'v': 0.221, 'G_B': 0.685
    }
}
with open('/app/outputs/elastic_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"
