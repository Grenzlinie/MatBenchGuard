#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: specific_impulse.csv ===
cat > /app/outputs/specific_impulse.csv <<'EOF'
compound,N,delta_H_comb,Tc,Is,relative_Is
HMX,0.0338,-2000.40,6166.49,14.43,1.000
MN,0.0357,-521.89,5805.33,14.40,0.998
EGDN,0.0329,-1044.36,6414.10,14.52,1.006
NG,0.0319,-1464.74,6414.59,14.31,0.992
ETN,0.0314,-1903.63,6474.96,14.27,0.989
XPN,0.0312,-2324.11,6464.44,14.19,0.983
MHN,0.0310,-2781.21,6539.36,14.23,0.986
VHN,0.0308,-3174.90,6470.97,14.12,0.979
ONO,0.0307,-3624.14,6513.98,14.15,0.981
EOF
