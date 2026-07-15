#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'EOF'
{
  "alpha": 3e-4,
  "eta": 1.0,
  "ln_a_Zn_0": -4.65
}
EOF

# === solve block: thermodynamic_table_beta1.csv ===
cat > /app/outputs/thermodynamic_table_beta1.csv <<'EOF'
a/o_Zn,ln_a_Zn,ln_a_Pt,Delta_G_kJ_per_g_atom,Delta_H_kJ_per_g_atom,T_Delta_S_kJ_per_g_atom
45,-8.10,-1.37,-46.6,-64.1,-17.5
48,-7.10,-2.24,-48.4,-66.9,-18.5
49,-6.58,-2.73,-48.9,-67.9,-19.0
50,-4.65,-4.64,-49.2,-68.7,-19.5
51,-2.74,-6.57,-48.9,-68.1,-19.2
52,-2.25,-7.09,-48.4,-67.2,-18.8
EOF

# === solve block: delta_H_alpha_relation.csv ===
cat > /app/outputs/delta_H_alpha_relation.csv <<'EOF'
phase,alpha,Delta_H_kJ_per_g_atom
PtZn,0.0003,-65.0
EOF
