#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
data = {
  'SrFeAsF': {
    'lattice_a': 4.0055,
    'lattice_c': 8.8049,
    'z_As': 0.6397,
    'z_A': 0.1665,
    'Fe_d_DOS_EF': 1.188,
    'As_DOS_EF': 0.039,
    'total_DOS_EF': 1.540,
    'atomic_charges': {
      'Sr': 8.465,
      'Fe': 7.741,
      'As': 5.950,
      'F': 7.843
    },
    'layer_charges': {
      'AF': 16.309,
      'FeAs': 15.585
    },
    'interlayer_charge_transfer': 0.309,
    'gamma': 3.630,
    'chi': 0.496
  },
  'CaFeAsF': {
    'lattice_a': 3.9049,
    'lattice_c': 8.3565,
    'z_As': 0.6525,
    'z_A': 0.1588,
    'Fe_d_DOS_EF': 1.529,
    'As_DOS_EF': 0.040,
    'total_DOS_EF': 1.895,
    'atomic_charges': {
      'Ca': 6.411,
      'Fe': 7.734,
      'As': 5.986,
      'F': 7.869
    },
    'layer_charges': {
      'AF': 14.280,
      'FeAs': 15.603
    },
    'interlayer_charge_transfer': 0.280,
    'gamma': 4.466,
    'chi': 0.610
  }
}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
