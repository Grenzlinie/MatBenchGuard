#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > "$OUTDIR/adsorption_energies.json" << 'EOF'
{
  "O2_Mo_term": {
    "configuration_id": "1 (V_C/V_C)",
    "PBE_Eads": -8.98,
    "RPBE_Eads": -8.46,
    "Mo_O_distances": [1.988, 2.039, 2.063],
    "O_O_distance": 3.003
  },
  "O2_C_term": {
    "configuration_id": "8 (H_C/H_C)",
    "PBE_Eads": -5.78,
    "RPBE_Eads": -5.36,
    "Mo_O_distances": [2.087, 2.044, 2.099],
    "O_O_distance": 3.007
  },
  "CO_Mo_term": {
    "configuration_id": "17 (V_C, \u03bc\u00b3-form)",
    "PBE_Eads": -2.65,
    "RPBE_Eads": -2.23,
    "C_O_distance": 1.255,
    "Mo_C_distance": 1.961
  },
  "CO_C_term": {
    "configuration_id": "21 (Atop at C)",
    "PBE_Eads": -1.97,
    "RPBE_Eads": -1.74,
    "C_O_distance": 1.172,
    "C_C_distance": 1.302
  },
  "O_atom_Mo_term": {
    "configuration_id": "12 (V_C)",
    "PBE_Eads": -4.62,
    "RPBE_Eads": -4.39,
    "Mo_O_distances": [2.013, 2.051, 2.017]
  },
  "O_atom_C_term": {
    "configuration_id": "15 (H_C)",
    "PBE_Eads": -3.09,
    "RPBE_Eads": -2.85,
    "Mo_O_distances": [2.009, 2.069, 2.122]
  }
}
EOF
