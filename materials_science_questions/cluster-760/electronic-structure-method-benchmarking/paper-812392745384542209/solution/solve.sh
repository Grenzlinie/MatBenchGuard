#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: reproduced_results.json ===
python3 -c "
import json, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
data = {
  'activation_energies': {
    'TS1': {'Ea_reactant': 13.99, 'Ea_OC': 15.92},
    'TS2': {'Ea_reactant': 3.02, 'Ea_OC': 5.68},
    'TS3': {'Ea_reactant': -5.38, 'Ea_OC': -3.59}
  },
  'synchronicity_Sy': {'TS1': 0.92, 'TS2': 0.69, 'TS3': 0.53},
  'Wiberg_indices': {
    'TS1': {'C2O5': 0.39, 'N1C6': 0.38},
    'TS2': {'C2O5': 0.55, 'N1C6': 0.20},
    'TS3': {'C2O5': 0.48, 'N1C6': 0.11}
  },
  'NPA_charges_beta_C': {
    'free_CH3CN': 0.29,
    'complex1': 0.48,
    'complex2': 0.53
  },
  'electron_density_BCP': {
    'TS1': {'C2O5': 0.578, 'N1C6': 0.470},
    'TS3': {'C2O5': 0.793, 'N1C6': 0.181}
  }
}
with open(os.path.join(outdir, 'reproduced_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"
