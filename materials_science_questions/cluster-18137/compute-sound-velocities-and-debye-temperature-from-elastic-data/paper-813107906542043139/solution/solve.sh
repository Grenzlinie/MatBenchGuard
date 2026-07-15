#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.csv ===
cat > "$OUTDIR/elastic_constants.csv" << 'EOF'
composition,C11,C12,C44
0.6,254,124.5,135.3
1.0,235.9,118.6,137.8
EOF

# === solve block: polycrystalline_moduli.csv ===
cat > "$OUTDIR/polycrystalline_moduli.csv" << 'EOF'
composition,B,G,E,v,A_Z,B_over_G
1.0,157.7,97.8,243.2,0.243,2.35,1.61
EOF

# === solve block: debye_temperature.csv ===
cat > "$OUTDIR/debye_temperature.csv" << 'EOF'
composition,theta_D,vL,vT,vm
1.0,542,6421,3743,4150
EOF

# === solve block: ideal_tensile_strength.csv ===
cat > "$OUTDIR/ideal_tensile_strength.csv" << 'EOF'
composition,sigma_max,epsilon_max
1.0,7.7,0.09
EOF

# === solve block: curie_temperature.csv ===
cat > "$OUTDIR/curie_temperature.csv" << 'EOF'
composition,T_C
1.0,463
EOF
