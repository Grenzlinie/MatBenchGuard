#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monolayer_results.json ===
cat > /app/outputs/monolayer_results.json <<'HEREDOC'
{
  "bond_lengths": {
    "C1-1": 1.950,
    "C2-1": 1.936,
    "C2-1'": 1.951,
    "C3-1'": 1.903,
    "C3-C3": 1.534,
    "C1-H": 1.135
  },
  "bond_angles": {
    "C3C31'": 143.4,
    "C31'C2": 122.8,
    "1C11": 134.2,
    "HC1H": 96.4
  },
  "tilt_angles": {
    "HC1H": 0.0,
    "HC2H": 0.89,
    "HC3H": 18.57
  },
  "displacements": [
    {"atom": "1", "dx": 0.124, "dz": -0.018},
    {"atom": "1'", "dx": 0.374, "dz": 0.098},
    {"atom": "2", "dx": 0.043, "dz": -0.072},
    {"atom": "2'", "dx": 0.091, "dz": 0.034},
    {"atom": "3", "dx": 0.0, "dz": -0.063},
    {"atom": "3''", "dx": 0.0, "dz": 0.094},
    {"atom": "4", "dx": 0.0, "dz": -0.049},
    {"atom": "4''", "dx": 0.0, "dz": 0.040}
  ],
  "electron_densities": {
    "C1C2C3": 4.016,
    "1 1'": 3.893,
    "2 2'": 4.089,
    "3 3' 3''": 3.993,
    "4 4' 4''": 3.972
  }
}
HEREDOC

# === solve block: three_layer_results.json ===
cat > /app/outputs/three_layer_results.json <<'HEREDOC'
{
  "bond_lengths": {
    "C11": 1.927,
    "C3C3": 1.614,
    "Si1C4": 1.874,
    "C21": 1.911,
    "Si2C4": 1.889,
    "C21'": 1.972,
    "Si2C5": 1.847,
    "C31'": 1.912,
    "Si3C5": 1.855,
    "Si1C1": 2.164,
    "Si3C6": 1.838,
    "Si2C2": 2.122,
    "C6H": 1.126,
    "Si3C3": 2.207
  },
  "bond_angles": {
    "C3C31'": 142.4,
    "C31'C2": 124.3,
    "1C11": 134.5,
    "Si1C1Si1": 130.6,
    "C4Si1C4": 118.4,
    "Si1C4Si2": 122.5,
    "C4Si2C5": 112.6,
    "Si2C5Si3": 116.7,
    "C5Si3C6": 111.2,
    "Si3C6Si3": 87.3,
    "HC6H": 96.9
  },
  "tilt_angles": {
    "Si1C1Si1": 0.0,
    "Si2C2Si2": 11.9,
    "Si3C3Si3": 29.1
  },
  "displacements": [
    {"atom": "1", "dx": 0.143, "dz": 0.024},
    {"atom": "1'", "dx": 0.402, "dz": 0.270},
    {"atom": "2", "dx": 0.037, "dz": -0.134},
    {"atom": "2'", "dx": 0.088, "dz": 0.023},
    {"atom": "3", "dx": 0.0, "dz": -0.063},
    {"atom": "3''", "dx": 0.0, "dz": 0.094},
    {"atom": "4", "dx": 0.0, "dz": -0.049},
    {"atom": "4''", "dx": 0.0, "dz": 0.040}
  ],
  "electron_densities": {
    "C4C5C6": 4.201,
    "Si1Si2Si3": 3.590,
    "C1C2C3": 4.240,
    "1 1'": 3.454,
    "2 2'": 4.603,
    "3 3' 3''": 3.891,
    "4 4' 4''": 4.051
  }
}
HEREDOC
