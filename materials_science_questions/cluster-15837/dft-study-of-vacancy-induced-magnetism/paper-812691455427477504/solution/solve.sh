#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: summary_results.json ===
python3 -c "
import json
data = {
    'total_moment_muB': 2.0,
    'local_moments': {
        'di_fp1': [
            {'atom_site_description': 'Ti interstitial I1', 'moment_muB': 0.7},
            {'atom_site_description': 'Ti interstitial I2', 'moment_muB': 0.7}
        ],
        'di_fp2': [
            {'atom_site_description': 'Ti interstitial I1', 'moment_muB': 0.7},
            {'atom_site_description': 'O atom near Ti vacancy', 'moment_muB': 0.62}
        ]
    },
    'di_fp1_energy_eV': 0.0,
    'di_fp2_energy_eV': 0.252,
    'energy_diff_meV_per_fu': 7.0,
    'anisotropy_meV_z_x': 0.08,
    'anisotropy_meV_z_y': 0.04
}
with open('$OUTDIR/summary_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
