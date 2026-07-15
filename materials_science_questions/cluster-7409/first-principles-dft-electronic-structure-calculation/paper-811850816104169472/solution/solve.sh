#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relaxation_metrics.json ===
cat > "${OUTDIR}/relaxation_metrics.json" << 'FFEOF'
{
  "surface_Ti_displacement": -0.253,
  "interlayer_relaxation_d12": -29.66,
  "interlayer_relaxation_d23": 1.55,
  "outermost_Ti-O_bond_contraction": -9.14,
  "subsurface_Ti-O_bond_expansion": 2.17,
  "rumpling_second_PbO3_layer": 0.448,
  "layer_displacements": [
    {"layer": 1, "atom_type": "Ti", "displacement": -0.253},
    {"layer": 2, "atom_type": "Pb", "displacement": -0.249},
    {"layer": 2, "atom_type": "O", "displacement": 0.199},
    {"layer": 3, "atom_type": "Ti", "displacement": 0.069},
    {"layer": 4, "atom_type": "Pb", "displacement": -0.215},
    {"layer": 4, "atom_type": "O", "displacement": 0.141},
    {"layer": 5, "atom_type": "Ti", "displacement": 0.027},
    {"layer": 6, "atom_type": "Pb", "displacement": -0.111},
    {"layer": 6, "atom_type": "O", "displacement": 0.035},
    {"layer": 7, "atom_type": "Ti", "displacement": 0.0}
  ]
}
FFEOF
