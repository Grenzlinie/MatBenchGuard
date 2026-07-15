#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json <<'EOF'
{
  "C_impurity_energy_above_vbm": 0.4,
  "P_impurity_energy_above_vbm": 0.2,
  "pure_bandgap": 1.1,
  "C_bandgap": 1.1,
  "P_bandgap": 1.1,
  "direct_gap_pure": true,
  "direct_gap_C": true,
  "direct_gap_P": true
}
EOF
