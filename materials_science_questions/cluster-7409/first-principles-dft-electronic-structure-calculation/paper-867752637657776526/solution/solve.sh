#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_magnetic_properties.json ===
python3 -c "
import json
data = {
    'magnetic_orders': ['NM', 'FM', 'A-AFM', 'C-AFM', 'G-AFM'],
    'relative_energies_meV_per_Ti': [124, 0, -13, 17, -18],
    'magnetic_moments_muB_per_Ti': [0.0, 0.86, 0.80, 0.77, 0.75]
}
with open('$OUTDIR/bulk_magnetic_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: strained_cases_energy_differences.json ===
python3 /solution/write_ref_outputs.py strained_cases_energy_differences.json

# === solve block: band_gap_values.json ===
python3 /solution/write_ref_outputs.py band_gap_values.json
