#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_defect_energies.json ===
mkdir -p /app/outputs
cat > /app/outputs/step_01_defect_energies.json <<'EOF'
{
  "CdSe_Frenkel_Cd": 3.16,
  "CdSe_Frenkel_Se": 6.00,
  "PbSe_Frenkel_Pb": 3.30,
  "PbSe_Frenkel_Se": 3.80
}
EOF
