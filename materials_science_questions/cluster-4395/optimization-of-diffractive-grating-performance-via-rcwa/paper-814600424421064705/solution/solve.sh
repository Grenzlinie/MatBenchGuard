#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: cggf1_spectrum.csv ===
python3 /solution/synthesize.py --device I --output /app/outputs/cggf1_spectrum.csv

# === solve block: cggf2_spectrum.csv ===
python3 /solution/synthesize.py --device II --output /app/outputs/cggf2_spectrum.csv

# === solve block: peak_summary.json ===
python3 -c "
import json

data = {
    'ccgf1_peaks': [
        {
            'peak_label': 'A',
            'central_wavelength_nm': 608.5,
            'peak_reflectivity': 0.527,
            'FWHM_nm': 13.5
        },
        {
            'peak_label': 'B',
            'central_wavelength_nm': 700.5,
            'peak_reflectivity': 0.519,
            'FWHM_nm': 18.0
        }
    ],
    'ccgf2_peaks': [
        {
            'peak_label': 'C',
            'central_wavelength_nm': 639.5,
            'peak_reflectivity': 0.535,
            'FWHM_nm': 12.0
        },
        {
            'peak_label': 'D',
            'central_wavelength_nm': 722.0,
            'peak_reflectivity': 0.504,
            'FWHM_nm': 10.0
        }
    ]
}

with open('/app/outputs/peak_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
"
