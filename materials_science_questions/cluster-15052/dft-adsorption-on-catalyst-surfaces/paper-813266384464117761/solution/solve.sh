#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: physisorption_results.json ===
cat > "$OUTDIR/physisorption_results.json" << 'EOF'
{
  "pristine": {
    "adsorption_energy_eV": 0.13,
    "o2_vertical_height_A": 2.824,
    "o_o_bond_length_A": 1.263
  },
  "n_doped": {
    "adsorption_energy_eV": 0.31,
    "o1_vertical_height_A": 2.461,
    "o2_vertical_height_A": 2.775,
    "o_o_bond_length_A": 1.280
  }
}
EOF

# === solve block: chemisorption_results.json ===
python3 -c "
import json
import os
data = {
    'pristine': {
        'site': 'bridge',
        'adsorption_energy_eV': 3.97,
        'c_o_bond_lengths_A': [1.472, 1.472]
    },
    'n_doped': {
        'site': 'top',
        'adsorption_energy_eV': 4.68,
        'c_o_bond_length_A': 1.323
    }
}
with open(os.path.join('$OUTDIR', 'chemisorption_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: dissociation_results.json ===
python3 -c "
import json
import os
data = {
    'pristine': {'energy_barrier_eV': 2.39},
    'n_doped': {'energy_barrier_eV': 1.20}
}
with open(os.path.join('$OUTDIR', 'dissociation_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve finalize ===
echo 'All artifacts written successfully'
