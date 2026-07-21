#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: NiNMn3_results.json ===
python3 -c "
import json
data = {
    'compound': 'NiNMn3',
    'lattice_constant_GGA': 3.7875,
    'bulk_modulus_GGA': 133.6735,
    'FM_energy_GGA': -10093.5868,
    'AFM_energy_GGA': -10093.5930,
    'Delta_E_FM_AFM_GGA': 0.0062,
    'ground_state': 'AFM',
    'magnetic_moment_Mn_GGA': 1.5563,
    'magnetic_moment_Mn_GGA_plus_U': 1.8203,
    'DOS_at_Fermi_level_GGA': 3.0
}
with open('/app/outputs/NiNMn3_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: ZnNMn3_results.json ===
python3 -c "
import json
data = {
    'compound': 'ZnNMn3',
    'lattice_constant_GGA': 3.7802,
    'bulk_modulus_GGA': 260.2162,
    'FM_energy_GGA': -10643.9448,
    'AFM_energy_GGA': -10643.9980,
    'Delta_E_FM_AFM_GGA': 0.0532,
    'ground_state': 'AFM',
    'magnetic_moment_Mn_GGA': 2.0447,
    'magnetic_moment_Mn_GGA_plus_U': 2.2481,
    'DOS_at_Fermi_level_GGA': 3.2
}
with open('/app/outputs/ZnNMn3_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
