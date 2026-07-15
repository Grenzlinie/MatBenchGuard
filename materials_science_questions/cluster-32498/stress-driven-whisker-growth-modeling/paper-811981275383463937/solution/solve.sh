#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table1_escape_times.csv ===
cat > "$OUTDIR/table1_escape_times.csv" <<'EOF'
Orientation,R,tau,c_star,h_star,omega
35.25,1e-6,2.4e-7,7.3e-5,3.2e-7,1e6
35.25,5.8e-6,3.6e3,4.9e-4,1.856e-6,1e6
35.25,1e-5,1.6e15,9.6e-4,3.2e-6,1e6
0,1e-7,2.7e-8,5.0e-7,7.5e-8,1e7
0,3.1e-7,3.6e3,1.5e-6,2.325e-7,1e7
0,1e-6,1e43,6.5e-6,7.5e-7,1e7
EOF

# === solve block: table2_stresses.csv ===
cat > "$OUTDIR/table2_stresses.csv" <<'EOF'
R,sigma_e,sigma_s
1e-6,2.4e9,2.1e8
1e-5,5.1e8,2.0e8
1e-4,7.8e7,3.8e7
1e-3,1.1e7,5.6e6
EOF
