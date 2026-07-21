#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: phase_diagram.csv ===
cat > "$OUTDIR/phase_diagram.csv" <<'CSVEOF'
J2,transition,Tc,order
0.5,I-H,2.16,second
0.5,H-L,1.254,first
0.7,I-H,2.16,second
0.7,H-L,1.705,first
0.8,I-H,2.13,second
0.8,H-L,1.930,first
0.9,I-L,2.110,first
1.0,I-L,2.283,first
1.2,I-L,2.53,second
CSVEOF
