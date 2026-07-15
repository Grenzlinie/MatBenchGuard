#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: antimonene_sw_data.json ===
python3 -c "
import json

data = {
    'structures': [
        {
            'name': 'ZbNT',
            'diameter_ang': 17.742,
            'tube_length_ang': 19.031,
            'd_Sb_Sb_min_ang': 2.916,
            'd_Sb_Sb_max_ang': 2.935,
            'orientation_angle_deg': 0.0,
            'formation_energy_eV': 0.0,
            'band_gap_eV': 1.489
        },
        {
            'name': 'SW1-ZbNT',
            'diameter_ang': 17.512,
            'tube_length_ang': 19.048,
            'd_Sb_Sb_min_ang': 2.902,
            'd_Sb_Sb_max_ang': 3.008,
            'orientation_angle_deg': 20.969,
            'formation_energy_eV': 0.582,
            'band_gap_eV': 1.336
        },
        {
            'name': 'SW2-ZbNT',
            'diameter_ang': 17.688,
            'tube_length_ang': 19.025,
            'd_Sb_Sb_min_ang': 2.869,
            'd_Sb_Sb_max_ang': 3.017,
            'orientation_angle_deg': 32.307,
            'formation_energy_eV': 0.724,
            'band_gap_eV': 1.404
        },
        {
            'name': 'ASbNT',
            'diameter_ang': 15.579,
            'tube_length_ang': 14.420,
            'd_Sb_Sb_min_ang': 2.921,
            'd_Sb_Sb_max_ang': 2.937,
            'orientation_angle_deg': 0.0,
            'formation_energy_eV': 0.0,
            'band_gap_eV': 1.391
        },
        {
            'name': 'SW1-ASbNT',
            'diameter_ang': 15.491,
            'tube_length_ang': 14.437,
            'd_Sb_Sb_min_ang': 2.854,
            'd_Sb_Sb_max_ang': 2.987,
            'orientation_angle_deg': 49.556,
            'formation_energy_eV': 0.754,
            'band_gap_eV': 1.299
        },
        {
            'name': 'SW2-ASbNT',
            'diameter_ang': 15.511,
            'tube_length_ang': 14.265,
            'd_Sb_Sb_min_ang': 2.891,
            'd_Sb_Sb_max_ang': 3.055,
            'orientation_angle_deg': 11.815,
            'formation_energy_eV': 0.788,
            'band_gap_eV': 1.212
        }
    ]
}
with open('$OUTDIR/antimonene_sw_data.json', 'w') as f:
    json.dump(data, f, indent=2)
"
