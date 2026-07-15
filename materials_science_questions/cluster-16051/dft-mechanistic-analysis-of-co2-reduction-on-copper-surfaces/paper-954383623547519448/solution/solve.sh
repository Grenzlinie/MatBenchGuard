#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_selectivity_result.json ===
cat > /app/outputs/dft_selectivity_result.json <<'EOF'
[
  {"motif": "pristine Cu2Sb(100)", "delta_R1G_eV": -0.34, "delta_R2G_eV": 0.14, "delta_R3G_eV": -1.05},
  {"motif": "S_Sb1/Cu2Sb(100)", "delta_R1G_eV": -0.23, "delta_R2G_eV": 0.15, "delta_R3G_eV": -0.94},
  {"motif": "S_Sb2/Cu2Sb(100)", "delta_R1G_eV": -0.71, "delta_R2G_eV": -0.15, "delta_R3G_eV": -0.99},
  {"motif": "V_Cu2/Cu2Sb(100)", "delta_R1G_eV": -0.25, "delta_R2G_eV": 0.33, "delta_R3G_eV": -1.08}
]
EOF
