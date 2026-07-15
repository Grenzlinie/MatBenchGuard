#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: electronic_structure.json ===
python3 -c "
import json
data = {
    'bands': {'a': -1.3, 'b': -0.3, 'c': 1.6, 'd': -2.6},
    'orbital_characters': {
        'c': ['d_xy', 'd_xz', 'd_z2'],
        'd': ['d_z2']
    }
}
with open('$OUTDIR/electronic_structure.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: phonon_analysis.json ===
python3 -c "
import json
data = {
    'phonon_modes': {'A1g': 200.0, 'Eg': 128.0},
    'phonon_DOS_comparison': 'A1g higher than Eg'
}
with open('$OUTDIR/phonon_analysis.json', 'w') as f:
    json.dump(data, f, indent=2)
"
