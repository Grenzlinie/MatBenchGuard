#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_U_values.csv ===
cat > "$OUTDIR/step_01_U_values.csv" <<'EOF'
compound,U_type,U_value
La,d,0.531
Ce,f,1.619
Pr,f,2.332
Nd,f,2.403
EOF

# === solve block: step_02_lattice_constants.csv ===
cat > "$OUTDIR/step_02_lattice_constants.csv" <<'EOF'
compound,method,a,c,volume
La5Ge3,LSDA+U,8.872,6.774,461.708
Ce5Ge3,LSDA+U,8.726,6.055,399.286
Pr5Ge3,LSDA+U,8.917,6.137,422.598
Nd5Ge3,LSDA+U,8.718,6.382,420.112
EOF

# === solve block: step_03_magnetic_moments.csv ===
cat > "$OUTDIR/step_03_magnetic_moments.csv" <<'EOF'
compound,method,total_moment,RE1_moment,RE2_moment,Ge_moment
Ce5Ge3,LSDA+U+SO,2.742,0.111,0.367,-0.016
Pr5Ge3,LSDA+U+SO,24.378,2.336,2.170,-0.022
Nd5Ge3,LSDA+U+SO,34.793,3.262,3.228,-0.046
EOF
