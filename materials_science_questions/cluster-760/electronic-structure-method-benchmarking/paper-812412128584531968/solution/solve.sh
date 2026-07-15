#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "CH3_bond_length_Becke3LYP": 1.082,
  "CH3_bond_length_MP2": 1.079,
  "CH4_bond_length_Becke3LYP": 1.093,
  "CH4_bond_length_MP2": 1.090,
  "activation_energy_Becke3LYP": 14.38,
  "activation_energy_MP2": 22.13
}
EOF
