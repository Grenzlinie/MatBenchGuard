#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binary_structural.csv ===
cat > "$OUTDIR/binary_structural.csv" <<'EOF'
compound,a0,B0
GaN,4.521,185.15
TlN,5.224,170.14
BN,3.617,388.73
EOF

# === solve block: binary_bandgaps.csv ===
cat > "$OUTDIR/binary_bandgaps.csv" <<'EOF'
compound,gap_type,GGA_PBE_gap,TB_mBJ_gap
GaN,direct,1.669,3.123
GaN,indirect,3.357,4.862
TlN,direct,0.000,0.000
TlN,indirect,3.081,4.096
BN,direct,8.823,10.39
BN,indirect,4.470,5.838
EOF

# === solve block: quaternary_bandgap.csv ===
cat > "$OUTDIR/quaternary_bandgap.csv" <<'EOF'
x,y,direct_gap
0.125,0.187,1.639
0,0.187,1.76
EOF

# === solve block: optical_dielectric_function.csv ===
python3 /solution/generate_optical.py "$OUTDIR/optical_dielectric_function.csv"
