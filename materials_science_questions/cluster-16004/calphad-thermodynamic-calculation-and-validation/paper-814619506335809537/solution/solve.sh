#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_parameters.json ===
cat > /app/outputs/thermodynamic_parameters.json <<'EOF'
{
  "Liquid": {
    "L0": [16713.57, 0.0]
  },
  "Fcc": {
    "L0": [-2744.77, 16.41],
    "Tc_interaction": [-4463.84],
    "beta_interaction": [-3.88]
  },
  "Hcp": {
    "L0": [7655.31, 14.9]
  }
}
EOF

# === solve block: phase_boundaries.csv ===
cat > /app/outputs/phase_boundaries.csv <<'EOF'
phase,temperature_K,composition_Os_at_frac
fcc_solvus,1300,0.05
hcp_solvus,1300,0.89
fcc_solvus,1500,0.093
hcp_solvus,1500,0.908
fcc_solvus,1700,0.112
hcp_solvus,1700,0.888
liquid,1773,0.23
EOF
