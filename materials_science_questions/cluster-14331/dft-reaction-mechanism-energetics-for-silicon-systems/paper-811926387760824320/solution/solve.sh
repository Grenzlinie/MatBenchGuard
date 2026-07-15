#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: barriers_and_heats.csv ===
cat > "$OUTDIR/barriers_and_heats.csv" <<'EOF'
channel,forward_barrier,reverse_barrier,heat_of_reaction
abstraction,9.25,86.99,-77.78
frontside,12.18,85.10,-72.93
backside,21.76,94.38,-72.93
EOF

# === solve block: rate_constants_298K.csv ===
cat > "$OUTDIR/rate_constants_298K.csv" <<'EOF'
channel,rate_constant
k1,1.12e-12
k2a,2.03e-13
k2b,6.28e-16
k_total,1.32e-12
EOF
