#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sio2_p_energies.json ===
python3 -c "
import json
data = {
    'sio2_p_homo_ev': -0.41,
    'oh_sinc_homo_ev': 0.0,
    'alpha_homo_offset_ev': -0.41,
    'sio2_p_lumo_ev': 2.76,
    'oh_sinc_lumo_ev': 2.75,
    'beta_lumo_offset_ev': 0.01,
    'electron_barrier_reduction_pct': 97.0,
    'hole_barrier_reduction_pct': 85.0
}
with open('/app/outputs/sio2_p_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: sinc_p_substitutional_energies.json ===
python3 -c "
import json
data = {
    'oh_sinc_lumo_ev': 2.75,
    'substitutional_homo_relative_to_lumo_ev': 0.51,
    'ionization_energy_ev': 0.51,
    'ionization_probability_300K': 2.7e-9
}
with open('/app/outputs/sinc_p_substitutional_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: sinc_p_interstitial_energies.json ===
python3 -c "
import json
data = {
    'oh_sinc_homo_ev': 0.0,
    'oh_sinc_lumo_ev': 2.75,
    'interstitial_homo_ev': 0.57,
    'interstitial_homo_relative_to_sinc_homo_ev': 0.57,
    'interstitial_lumo_ev': 2.29,
    'interstitial_lumo_relative_to_sinc_lumo_ev': -0.46,
    'optical_transition_energy_ev': 1.72
}
with open('/app/outputs/sinc_p_interstitial_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"
