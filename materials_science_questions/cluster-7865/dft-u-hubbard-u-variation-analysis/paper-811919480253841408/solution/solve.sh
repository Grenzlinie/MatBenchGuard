#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.csv ===
cat > /app/outputs/band_gaps.csv <<'EOF'
concentration,U,Delta_E_VI_plus,Delta_E_I_plus,Delta_E_IC_plus,Delta_E_VC_minus
1/32,0,0.24,0.31,1.22,1.56
1/32,3,0.24,0.37,1.16,1.57
1/32,6,0.21,0.41,1.16,1.56
2/32,0,0.19,0.52,1.10,1.68
2/32,3,0.16,0.53,1.11,1.66
2/32,6,0.13,0.55,1.12,1.64
EOF

# === solve block: integrated_dos_IB.csv ===
cat > /app/outputs/integrated_dos_IB.csv <<'EOF'
concentration,U,DOS_below_Ef,DOS_above_Ef
1/32,0,2,1
1/32,3,2,1
1/32,6,2,1
2/32,0,4,2
2/32,3,4,2
2/32,6,4,2
EOF
