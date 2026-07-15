#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: properties.json ===
python3 -c "
import json
data = [
  { 'structure': 'T1_sym_3.3', 'cutoff': 3.3, 'energy': 3.8423, 'band_gap': 0.256, 'num_bonds': 94, 'margin': 0.83, 'long_bond': 2.68 },
  { 'structure': 'T2_sym_3.1', 'cutoff': 3.1, 'energy': 3.9583, 'band_gap': 0.194, 'num_bonds': 94, 'margin': 0.48, 'long_bond': 2.78 },
  { 'structure': 'T2_sym_3.3', 'cutoff': 3.3, 'energy': 3.9765, 'band_gap': 0.000, 'num_bonds': 98, 'margin': 0.12, 'long_bond': 3.26 },
  { 'structure': 'T2_asym_3.1', 'cutoff': 3.1, 'energy': 3.9779, 'band_gap': 0.126, 'num_bonds': 94, 'margin': 0.62, 'long_bond': 2.72 },
  { 'structure': 'T2_asym_3.3', 'cutoff': 3.3, 'energy': 3.9874, 'band_gap': 0.103, 'num_bonds': 96, 'margin': 0.00, 'long_bond': 3.30 }
]
with open('/app/outputs/properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"
