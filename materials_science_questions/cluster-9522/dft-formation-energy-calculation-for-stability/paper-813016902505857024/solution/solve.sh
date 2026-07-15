#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_energies.json ===
cat > /app/outputs/total_energies.json <<'FFEOF'
{
  "binary_total_energies": {
    "CsBr": -5.0,
    "PbBr2": -10.0,
    "MAI": -8.0,
    "PbI2": -12.0
  },
  "ternary_total_energies": {
    "CsPbBr3": -15.22,
    "MAPbI3": -20.06
  },
  "slab_total_energies": [
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 1, "relaxation": "ideal", "energy_eV": -20.00},
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 1, "relaxation": "relaxed", "energy_eV": -20.05},
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 2, "relaxation": "ideal", "energy_eV": -35.10},
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 2, "relaxation": "relaxed", "energy_eV": -35.16},
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 3, "relaxation": "ideal", "energy_eV": -50.18},
    {"compound": "CsPbBr3", "termination": "AX", "thickness": 3, "relaxation": "relaxed", "energy_eV": -50.34},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 1, "relaxation": "ideal", "energy_eV": -24.80},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 1, "relaxation": "relaxed", "energy_eV": -24.90},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 2, "relaxation": "ideal", "energy_eV": -39.85},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 2, "relaxation": "relaxed", "energy_eV": -39.90},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 3, "relaxation": "ideal", "energy_eV": -54.86},
    {"compound": "CsPbBr3", "termination": "BX2", "thickness": 3, "relaxation": "relaxed", "energy_eV": -54.98},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 1, "relaxation": "ideal", "energy_eV": -27.69},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 1, "relaxation": "relaxed", "energy_eV": -28.09},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 2, "relaxation": "ideal", "energy_eV": -47.76},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 2, "relaxation": "relaxed", "energy_eV": -48.16},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 3, "relaxation": "ideal", "energy_eV": -67.72},
    {"compound": "MAPbI3", "termination": "AX", "thickness": 3, "relaxation": "relaxed", "energy_eV": -68.20},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 1, "relaxation": "ideal", "energy_eV": -31.65},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 1, "relaxation": "relaxed", "energy_eV": -31.70},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 2, "relaxation": "ideal", "energy_eV": -51.41},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 2, "relaxation": "relaxed", "energy_eV": -51.46},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 3, "relaxation": "ideal", "energy_eV": -71.22},
    {"compound": "MAPbI3", "termination": "BX2", "thickness": 3, "relaxation": "relaxed", "energy_eV": -71.30}
  ]
}
FFEOF
