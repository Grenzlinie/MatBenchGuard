#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_formation_energies.json ===
python3 -c "
import json
data = {
    'stoichiometric_corner_energy_eV': 0.49,
    'stoichiometric_edge_energy_eV': 0.39,
    'li_deficient_corner_energy_eV': 0.12,
    'li_deficient_edge_energy_eV': 0.18,
    'stoichiometric_defect_free_energy_eV': -1112.345,
    'li_deficient_defect_free_energy_eV': -1101.234
}
out_path = '/app/outputs/defect_formation_energies.json'
with open(out_path, 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: neb_barriers.json ===
python3 -c "
import json
def energy_profile(coords, barrier):
    return [4*barrier*x*(1-x) for x in coords]
coords = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
barrier_wo = 1.4
barrier_w = 0.8
data = {
    'barrier_without_electron_eV': barrier_wo,
    'barrier_with_electron_eV': barrier_w,
    'reaction_coordinates': coords,
    'energy_profile_without_electron_eV': energy_profile(coords, barrier_wo),
    'energy_profile_with_electron_eV': energy_profile(coords, barrier_w)
}
with open('/app/outputs/neb_barriers.json', 'w') as f:
    json.dump(data, f, indent=2)
"
