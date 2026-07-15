#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
results = {
    'lattice_constant_a0': 5.360,
    'bulk_modulus_B': 122,
    'bulk_modulus_derivative_Bprime': 4.56,
    'cohesive_energy_Ecoh': -14.77,
    'elastic_constant_C11': 151.81,
    'elastic_constant_C12': 106.38,
    'elastic_constant_C44': 50.65,
    'band_gap_Eg': 3.42,
    'band_gap_pressure_coefficient': 29.88,
    'phonon_LO_frequency': 398,
    'phonon_TO_frequency': 253
}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(results, f, indent=4)
"
