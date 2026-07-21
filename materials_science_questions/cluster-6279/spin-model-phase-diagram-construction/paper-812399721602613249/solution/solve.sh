#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_sequence.txt ===
cat > "$OUTDIR/phase_sequence.txt" <<'EOF'
E -> S3 -> S4 -> \\bar{S}_3 -> F
EOF

# === solve block: transitions.csv ===
cat > "$OUTDIR/transitions.csv" <<'EOF'
transition_name,mu,coverage,entropy
E_to_S3,-0.3,0.16666666666666666,0.2937911956848477
S3_to_S4,2.0,0.425464400750007,0.160403941686534
S4_to_barS3,5.0,0.574535599249993,0.160403941686534
barS3_to_F,6.2,0.8333333333333334,0.293791195673181
EOF
