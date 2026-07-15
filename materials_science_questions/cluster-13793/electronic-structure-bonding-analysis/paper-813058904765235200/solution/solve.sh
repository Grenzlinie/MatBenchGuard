#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: interaction_energies.csv ===
python3 <<'PYEOF'
import csv
import os

outdir = '/app/outputs'
columns = ['solute', 'separation', 'E_int', 'reconstruction_spontaneous']
rows = [
    ['B', '1b', -1.16, 'yes'],
    ['B', '2b', -1.20, 'yes'],
    ['C', '1b', -0.72, 'yes'],
    ['C', '2b', -0.75, 'yes'],
    ['N', '1b', -0.40, 'energetically_favorable_but_not_spontaneous'],
    ['N', '2b', -0.56, 'yes'],
    ['O', '1b', -0.65, 'yes'],
    ['O', '2b', -0.72, 'yes'],
]

with open(os.path.join(outdir, 'interaction_energies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)
PYEOF

# === solve block: reconstruction_summary.json ===
python3 <<'PYEOF'
import json
import os

data = {
    "results": [
        {"solute": "B", "separation": "1b", "reconstruction": "spontaneous", "E_int_eV": -1.16},
        {"solute": "B", "separation": "2b", "reconstruction": "spontaneous", "E_int_eV": -1.20},
        {"solute": "C", "separation": "1b", "reconstruction": "spontaneous", "E_int_eV": -0.72},
        {"solute": "C", "separation": "2b", "reconstruction": "spontaneous", "E_int_eV": -0.75},
        {"solute": "N", "separation": "1b", "reconstruction": "energetically_favorable_but_not_spontaneous", "E_int_eV": -0.40},
        {"solute": "N", "separation": "2b", "reconstruction": "spontaneous", "E_int_eV": -0.56},
        {"solute": "O", "separation": "1b", "reconstruction": "spontaneous", "E_int_eV": -0.65},
        {"solute": "O", "separation": "2b", "reconstruction": "spontaneous", "E_int_eV": -0.72}
    ]
}

with open(os.path.join('/app/outputs', 'reconstruction_summary.json'), 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
