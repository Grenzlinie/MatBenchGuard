#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json << 'EOF'
[
  {
    "U": 0,
    "E_g_up": 5.006,
    "E_g_down": 5.011,
    "delta_E_c": 6.64,
    "delta_E_v": 1.37,
    "N_alpha": 0.212,
    "N_beta": 0.043
  },
  {
    "U": 6,
    "E_g_up": 4.997,
    "E_g_down": 5.000,
    "delta_E_c": 4.58,
    "delta_E_v": 2.22,
    "N_alpha": 0.146,
    "N_beta": 0.071
  }
]
EOF

# === solve block: magnetic_moments.json ===
cat > /app/outputs/magnetic_moments.json << 'EOF'
[
  {
    "U": 0,
    "Mg": 0.000,
    "Mn": 0.897,
    "O": 0.003,
    "Interstitial": 0.077,
    "Total": 1.000
  },
  {
    "U": 6,
    "Mg": 0.000,
    "Mn": 0.951,
    "O": 0.005,
    "Interstitial": 0.013,
    "Total": 1.003
  }
]
EOF

# === solve block: optical_band_gaps.json ===
cat > /app/outputs/optical_band_gaps.json << 'EOF'
[
  {"U": 0, "ligand_field": "weak",   "E_g_up": 5.219, "E_g_down": 5.243},
  {"U": 0, "ligand_field": "strong", "E_g_up": 4.892, "E_g_down": 5.010},
  {"U": 6, "ligand_field": "weak",   "E_g_up": 5.255, "E_g_down": 5.292},
  {"U": 6, "ligand_field": "strong", "E_g_up": 5.088, "E_g_down": 4.990},
  {
    "reduction_up_U0": 6.265,
    "reduction_down_U0": 4.444,
    "reduction_up_U6": 3.178,
    "reduction_down_U6": 5.707
  }
]
EOF
