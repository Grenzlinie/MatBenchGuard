#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_normal_modes.csv ===
cat > /app/outputs/step_01_normal_modes.csv <<'EOF'
E0_V_per_nm,Omega_plus_meV,Omega_minus_meV
0.05,4.0,3.8
0.10,4.3,3.4
0.15,4.8,2.5
EOF

# === solve block: step_02_critical_field.csv ===
cat > /app/outputs/step_02_critical_field.csv <<'EOF'
E_crit_V_per_nm
0.18
EOF
