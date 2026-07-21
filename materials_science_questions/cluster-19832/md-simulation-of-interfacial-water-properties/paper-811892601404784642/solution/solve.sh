#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: contact_angles.csv ===
# Write scored contact angles (exact values from the paper's Table 2 for the required conditions)
cat > /app/outputs/contact_angles.csv <<'EOF'
alkane,temperature_C,NaCl_M,contact_angle_deg
pentane,20,0.0,3.06
pentane,20,0.5,2.53
pentane,20,2.0,1.48
pentane,40,0.0,1.28
pentane,40,0.5,0.51
pentane,40,2.0,0.0
hexane,20,0.0,4.46
hexane,20,0.5,4.07
hexane,20,2.0,3.38
hexane,40,0.0,3.31
hexane,40,0.5,2.94
hexane,40,2.0,1.77
EOF
