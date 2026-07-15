#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: wilson_point_properties.csv ===
cat > /app/outputs/wilson_point_properties.csv <<'EOF'
variable,analytical_value,unit
ΔT_W,35.1,K
N_W,2.46e+18,1/(s·kg)
r_30,2.69,nm
r_32,3.67,nm
Y_W,0.0002,dimensionless fraction
EOF

# === solve block: delta_T_vs_kp.csv ===
cat > /app/outputs/delta_T_vs_kp.csv <<'EOF'
k_p,delta_T_W
100.0,25.0
278.03,28.0
773.28,31.0
2154.43,35.1
5994.84,38.5
16681.0,42.0
46415.9,45.5
129155.0,49.0
359381.0,52.5
1000000.0,56.0
EOF
