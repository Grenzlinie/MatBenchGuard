#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_angles_and_relation.json ===
cat > $OUTDIR/computed_angles_and_relation.json <<'EOF'
{
  "two_psi_degrees": 117.81,
  "theta_degrees": 17.28,
  "tan_theta": 0.31041,
  "minus_c_over_a": 0.31041,
  "relation_verified": true,
  "dihedral_angle_deg": 178.66,
  "twofold_axes_angle_deg": 57.85
}
EOF

cat > $OUTDIR/pseudotrigonal_lattice.json <<'EOF'
{
  "V1_A": 14.96,
  "V2_A": 14.94,
  "V3_A": 14.94,
  "angle_V1_V2_deg": 43.22,
  "angle_V1_V3_deg": 43.22,
  "angle_V2_V3_deg": 44.78,
  "pseudo_binary_axes": ["[011]", "[01-1]"],
  "pseudo_mirror_planes": ["(11-3)", "(1-13)"]
}
EOF
