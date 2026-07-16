#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: summary.json ===
python3 -c "
import json
data = [
  {
    'composition': 'x=0',
    'cbm_energy': -1.3,
    'vbm_kpoint': [0.5, 0.5, 0.5],
    'cbm_kpoint': [0.0, 0.0, 0.0],
    'gap_type': 'indirect',
    'vbm_orbital': 'O_2p',
    'cbm_orbital': 'Nb_3d'
  },
  {
    'composition': 'x=0.25',
    'cbm_energy': -1.05,
    'vbm_kpoint': [0.5, 0.5, 0.5],
    'cbm_kpoint': [0.0, 0.0, 0.0],
    'gap_type': 'indirect',
    'vbm_orbital': 'O_2p',
    'cbm_orbital': 'Nb_3d'
  },
  {
    'composition': 'x=0.5',
    'cbm_energy': -0.8,
    'vbm_kpoint': [0.5, 0.5, 0.5],
    'cbm_kpoint': [0.0, 0.0, 0.0],
    'gap_type': 'indirect',
    'vbm_orbital': 'O_2p',
    'cbm_orbital': 'Nb_3d'
  }
]
with open('$OUTDIR/summary.json', 'w') as f:
  json.dump(data, f)
"
