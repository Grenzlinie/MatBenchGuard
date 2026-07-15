#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: znS_emission.csv ===
python3 /solution/generate_spectra.py --low 5100 --high 5300 --step 0.1 --center1 5218 --height1 0.6 --hwhm1 1.0 --center2 5212 --height2 1.0 --hwhm2 2.0 --title "ZnS emission" --outfile /app/outputs/znS_emission.csv

# === solve block: znS_absorption.csv ===
python3 /solution/generate_spectra.py --low 5100 --high 5300 --step 0.1 --center1 5218 --height1 1.0 --hwhm1 1.0 --center2 5212 --height2 0.6 --hwhm2 2.0 --title "ZnS absorption" --outfile /app/outputs/znS_absorption.csv

# === solve block: znSe_emission.csv ===
python3 /solution/generate_spectra.py --low 4900 --high 5100 --step 0.1 --center1 4971 --height1 0.6 --hwhm1 1.0 --center2 4964 --height2 1.0 --hwhm2 2.0 --title "ZnSe emission" --outfile /app/outputs/znSe_emission.csv

# === solve block: znSe_absorption.csv ===
python3 /solution/generate_spectra.py --low 4900 --high 5100 --step 0.1 --center1 4971 --height1 1.0 --hwhm1 1.0 --center2 4964 --height2 0.6 --hwhm2 2.0 --title "ZnSe absorption" --outfile /app/outputs/znSe_absorption.csv

# === solve block: zero_phonon_params.json ===
python3 -c "
import json
data = {
    'znS_emission_peaks': [5212.0, 5218.0],
    'znS_absorption_peaks': [5212.0, 5218.0],
    'znSe_emission_peaks': [4964.0, 4971.0],
    'znSe_absorption_peaks': [4964.0, 4971.0],
    'S_tau_ZnS': 2.6,
    'S_tau_ZnSe': 180.0 / 70.0
}
with open('/app/outputs/zero_phonon_params.json', 'w') as f:
    json.dump(data, f, indent=2)
"
