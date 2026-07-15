#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: step_01_dft_results.json ===
python3 -c "
import json, os

data = [
    {
        'stoichiometry': 'graphite_AB',
        'g_band_frequency_cm1': 1585,
        'k_point_crossing_energy_eV': 0.0,
        'intercalation_voltage_V': None
    },
    {
        'stoichiometry': 'NaC48',
        'g_band_frequency_cm1': 1570,
        'k_point_crossing_energy_eV': 0.05,
        'intercalation_voltage_V': 0.55
    },
    {
        'stoichiometry': 'NaC24',
        'g_band_frequency_cm1': 1555,
        'k_point_crossing_energy_eV': 0.02,
        'intercalation_voltage_V': 0.25
    },
    {
        'stoichiometry': 'NaC12',
        'g_band_frequency_cm1': 1535,
        'k_point_crossing_energy_eV': -0.05,
        'intercalation_voltage_V': -0.20
    },
    {
        'stoichiometry': 'NaC6',
        'g_band_frequency_cm1': 1500,
        'k_point_crossing_energy_eV': -0.15,
        'intercalation_voltage_V': -0.60
    }
]

os.makedirs('$OUTDIR', exist_ok=True)
with open('$OUTDIR/step_01_dft_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve finalize ===
# all pieces written, no further steps
