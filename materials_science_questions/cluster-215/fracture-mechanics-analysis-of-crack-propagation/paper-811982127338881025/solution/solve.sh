#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'EOF'
{
  "high_temp_m": 0.0,
  "high_temp_M": 3.5,
  "low_temp_m": 0.53,
  "low_temp_M": 2.1
}
EOF

# === solve block: predicted_GIC_joint.csv ===
cat > /app/outputs/predicted_GIC_joint.csv <<'EOF'
temperature_C,predicted_GIC_joint_kJm2
50,1.9
37,2.3
25,3.3
0,3.0
-20,3.2
-40,2.4
EOF
