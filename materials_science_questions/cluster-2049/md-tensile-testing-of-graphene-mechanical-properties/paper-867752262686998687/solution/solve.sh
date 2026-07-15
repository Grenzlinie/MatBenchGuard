#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: geometric_parameters.json ===
cat > "$OUTDIR/geometric_parameters.json" <<'EOF'
{
  "a_graphene": 2.44,
  "a_sym": 2.79,
  "a_asym": 2.50,
  "corrugation_asym": 0.45,
  "bond_length_C_C": 1.52,
  "bond_angle_C_C_C": 111.6,
  "bond_angle_H_C_C": 107.3
}
EOF

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'EOF'
{
  "E_f_sym_0": -1.044,
  "E_f_asym_0": -2.847,
  "E_f_sym_strained": -1.606,
  "E_f_asym_strained": -3.517
}
EOF
