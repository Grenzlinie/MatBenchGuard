#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: adsorption_energies.json ===
# block: adsorption_energies.json
python3 -c "
import json
data = {
    'Glycine': -3515.05,
    'Serine': -3980.74,
    'Glutamate': -4882.87,
    'Arginine': -5562.87
}
with open('$OUTDIR/adsorption_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: mulliken_charges.json ===
# block: mulliken_charges.json
python3 -c "
import json
data = [
    {'amino_acid': 'Glycine', 'COO_charge': -0.39, 'NH3_charge': -0.33},
    {'amino_acid': 'Serine', 'COO_charge': -0.41, 'NH3_charge': -0.21},
    {'amino_acid': 'Glutamate', 'COO_charge': -0.31, 'NH3_charge': -0.24},
    {'amino_acid': 'Arginine', 'COO_charge': -0.41, 'NH3_charge': -0.31}
]
with open('$OUTDIR/mulliken_charges.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: vb_dominance.txt ===
# block: vb_dominance.txt
cat > "$OUTDIR/vb_dominance.txt" << 'FFEOF'
O-2p4 states dominate the top of the valence band. Therefore, direct coupling of AA terminal groups to surface O-2p4 orbitals is the principal adsorption driver.
FFEOF
