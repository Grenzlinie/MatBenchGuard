#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'EOF'
{
  "PBE_band_gap_eV": 1.7,
  "HSE06_band_gap_eV": 2.8
}
EOF

# === solve block: defect_formation_energies.json ===
cat > /app/outputs/defect_formation_energies.json <<'EOF'
[
  {"defect": "V_Li-", "energy_eV": 0.77},
  {"defect": "V_S2_2plus", "energy_eV": 2.02},
  {"defect": "p_minus", "energy_eV": 1.43},
  {"defect": "p_plus", "energy_eV": 0.77}
]
EOF

# === solve block: diffusion_barriers.json ===
cat > /app/outputs/diffusion_barriers.json <<'EOF'
[
  {"defect": "V_Li-", "direction": "[100]", "barrier_eV": 0.95},
  {"defect": "V_Li-", "direction": "[010]", "barrier_eV": 0.83},
  {"defect": "V_Li-", "direction": "[001]-in", "barrier_eV": 0.026},
  {"defect": "V_Li-", "direction": "[001]-out", "barrier_eV": 0.148},
  {"defect": "V_S2_2plus", "direction": "[001]", "barrier_eV": 0.46},
  {"defect": "V_S2_2plus", "direction": "[100]", "barrier_eV": 0.71},
  {"defect": "V_S2_2plus", "direction": "[010]", "barrier_eV": 1.20},
  {"defect": "p_minus", "direction": "[001]", "barrier_eV": 0.69},
  {"defect": "p_minus", "direction": "[100]", "barrier_eV": 0.71},
  {"defect": "p_minus", "direction": "[010]", "barrier_eV": 0.89},
  {"defect": "p_plus", "direction": "[001]", "barrier_eV": 0.013},
  {"defect": "p_plus", "direction": "[100]", "barrier_eV": 0.006},
  {"defect": "p_plus", "direction": "[010]", "barrier_eV": 0.006}
]
EOF

# === solve block: mobility_conductivity.json ===
cat > /app/outputs/mobility_conductivity.json <<'EOF'
{
  "T_K": 300,
  "mobility_V_Li_minus_cm2_Vs": 1e-15,
  "mobility_p_plus_cm2_Vs": 0.1,
  "ionic_conductivity_S_cm": 1.5e-25,
  "electronic_conductivity_S_cm": 1.5e-10
}
EOF
