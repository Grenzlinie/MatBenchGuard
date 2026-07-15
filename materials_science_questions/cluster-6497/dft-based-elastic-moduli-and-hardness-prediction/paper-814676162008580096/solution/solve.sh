#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: eos_data.json ===
python3 -c "
import json
data = {
  'beta': {
    'E0': -7.627,
    'V0': 12.053,
    'K': 185,
    'K_prime': 3.7
  },
  'gamma': {
    'E0': -7.577,
    'V0': 9.730,
    'K': 240,
    'K_prime': 4.5
  }
}
with open('/app/outputs/eos_data.json', 'w') as f:
  json.dump(data, f, indent=2)
"

# === solve block: structural_data.json ===
python3 -c "
import json
data = {
  'beta': {
    'lattice_constants': {'a': 7.987, 'c': 3.054},
    'internal_coordinates': [
      {'atom': 'Ge', 'site_label': '6h', 'x': 0.1696, 'y': 0.7628, 'z': 0.25},
      {'atom': 'N', 'site_label': '6h', 'x': 0.3304, 'y': 0.0257, 'z': 0.25},
      {'atom': 'N', 'site_label': '2c', 'x': 0.3333333333333333, 'y': 0.6666666666666666, 'z': 0.25}
    ]
  },
  'gamma': {
    'lattice_constants': {'a': 8.1676},
    'internal_coordinates': [
      {'atom': 'Ge', 'site_label': '8a', 'x': 0.0, 'y': 0.0, 'z': 0.0},
      {'atom': 'Ge', 'site_label': '16d', 'x': 0.625, 'y': 0.625, 'z': 0.625},
      {'atom': 'N', 'site_label': '32e', 'x': 0.1330, 'y': 0.1330, 'z': 0.1330}
    ]
  }
}
with open('/app/outputs/structural_data.json', 'w') as f:
  json.dump(data, f, indent=2)
"

# === solve block: band_gap.json ===
python3 -c "
import json
data = {
  'beta': {'LDA_gap': 2.45},
  'gamma': {'LDA_gap': 2.17}
}
with open('/app/outputs/band_gap.json', 'w') as f:
  json.dump(data, f, indent=2)
"

# === solve block: phonon_frequencies.json ===
python3 -c "
import json
beta = [
  {'frequency_cm-1': 0, 'symmetry_label': 'A_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 0, 'symmetry_label': 'E_1u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 106, 'symmetry_label': 'E_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 108, 'symmetry_label': 'A_g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 129, 'symmetry_label': 'E_1g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 137, 'symmetry_label': 'B_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 169, 'symmetry_label': 'E_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 172, 'symmetry_label': 'B_g', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 247, 'symmetry_label': 'A_u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 254, 'symmetry_label': 'B_g', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 271, 'symmetry_label': 'E_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 275, 'symmetry_label': 'E_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 306, 'symmetry_label': 'B_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 309, 'symmetry_label': 'A_g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 339, 'symmetry_label': 'E_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 365, 'symmetry_label': 'B_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 373, 'symmetry_label': 'E_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 443, 'symmetry_label': 'A_g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 703, 'symmetry_label': 'A_u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 721, 'symmetry_label': 'E_1g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 735, 'symmetry_label': 'E_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 739, 'symmetry_label': 'E_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 753, 'symmetry_label': 'B_g', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 781, 'symmetry_label': 'A_g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 791, 'symmetry_label': 'E_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 878, 'symmetry_label': 'E_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 878, 'symmetry_label': 'E_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 896, 'symmetry_label': 'B_u', 'ir_active': False, 'raman_active': False}
]

gamma = [
  {'frequency_cm-1': 0, 'symmetry_label': 'T_1u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 153, 'symmetry_label': 'T_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 224, 'symmetry_label': 'T_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 245, 'symmetry_label': 'T_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 245, 'symmetry_label': 'E_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 406, 'symmetry_label': 'T_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 453, 'symmetry_label': 'T_1g', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 455, 'symmetry_label': 'A_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 467, 'symmetry_label': 'E_g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 475, 'symmetry_label': 'T_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 535, 'symmetry_label': 'T_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 576, 'symmetry_label': 'T_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 656, 'symmetry_label': 'T_1u', 'ir_active': True, 'raman_active': False},
  {'frequency_cm-1': 667, 'symmetry_label': 'E_u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 710, 'symmetry_label': 'T_2g', 'ir_active': False, 'raman_active': True},
  {'frequency_cm-1': 806, 'symmetry_label': 'A_2u', 'ir_active': False, 'raman_active': False},
  {'frequency_cm-1': 830, 'symmetry_label': 'A_1g', 'ir_active': False, 'raman_active': True}
]

data = {'beta': beta, 'gamma': gamma}
with open('/app/outputs/phonon_frequencies.json', 'w') as f:
  json.dump(data, f, indent=2)
"

# === solve block: transition_pressure.txt ===
echo '3.7' > /app/outputs/transition_pressure.txt
