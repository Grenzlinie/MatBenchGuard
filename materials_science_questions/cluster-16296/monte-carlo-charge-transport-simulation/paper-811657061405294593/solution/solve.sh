#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_drift_velocity.csv ===
cat > /app/outputs/bulk_drift_velocity.csv <<'EOF'
electric_field_kV_cm,drift_velocity_cm_s
0.5,2000000
1.0,4000000
2.0,8000000
4.0,14000000
8.0,19000000
12.0,18000000
16.0,15000000
20.0,13000000
25.0,11000000
30.0,10000000
EOF

# === solve block: device_iv_curve.csv ===
cat > /app/outputs/device_iv_curve.csv <<'EOF'
bias_voltage_V,current_density_A_cm2
0.0,0
0.2,600
0.5,1100
0.8,1600
1.0,2000
1.2,2300
1.5,2700
1.8,3100
2.0,3400
2.2,3700
2.5,4000
EOF
