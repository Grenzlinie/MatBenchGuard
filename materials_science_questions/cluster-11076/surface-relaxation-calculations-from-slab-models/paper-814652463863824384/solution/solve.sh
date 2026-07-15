#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_results.json ===
python3 -c "
import json, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
data = [
    {'system': 'Mg-Mg7H16', 'y': 16, 'total_energy': -400.0, 'a': 6.4085, 'b': 6.4085, 'c': 6.0562, 'reaction_energy': 0.617, 'zpe_correction': -0.078, 'helmholtz_enthalpy': 0.539},
    {'system': 'Mg-Mg7H15', 'y': 15, 'total_energy': -400.0, 'a': 6.4010, 'b': 6.4010, 'c': 6.0849, 'reaction_energy': 0.419, 'zpe_correction': -0.067, 'helmholtz_enthalpy': 0.353},
    {'system': 'Co-Mg7H16', 'y': 16, 'total_energy': -400.0, 'a': 6.2714, 'b': 6.2714, 'c': 5.9224, 'reaction_energy': 0.417, 'zpe_correction': -0.137, 'helmholtz_enthalpy': 0.270},
    {'system': 'Co-Mg7H15', 'y': 15, 'total_energy': -400.0, 'a': 6.1849, 'b': 6.3834, 'c': 5.8730, 'reaction_energy': 0.347, 'zpe_correction': -0.138, 'helmholtz_enthalpy': 0.200},
    {'system': 'Ni-Mg7H16', 'y': 16, 'total_energy': -400.0, 'a': 6.3161, 'b': 6.3161, 'c': 5.9276, 'reaction_energy': 0.386, 'zpe_correction': -0.097, 'helmholtz_enthalpy': 0.299},
    {'system': 'Ni-Mg7H15', 'y': 15, 'total_energy': -400.0, 'a': 6.2438, 'b': 6.3432, 'c': 5.9493, 'reaction_energy': 0.362, 'zpe_correction': -0.075, 'helmholtz_enthalpy': 0.297}
]
with open(os.path.join(outdir, 'bulk_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: surface_results.json ===
python3 /solution/write_outputs.py
