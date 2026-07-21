#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: j_ab_values.csv ===
cat > /app/outputs/j_ab_values.csv <<'EOF'
system,method,j_ab
Cr(III)-CN-Cr(III),UHF,-232.7
Cr(III)-CN-Cr(III),DFT,0.0
Cr(III)-CN-Mn(II),UHF,-25.44
Cr(III)-CN-Mn(II),DFT,24.50
Cr(III)-CN-V(II),UHF,-143.9
Cr(III)-CN-V(II),DFT,0.0
Cr(III)-CN-Ni(II),UHF,63.73
Cr(III)-CN-Ni(II),DFT,49.91
Cr(III)-CN-V(III),UHF,-173.0
Cr(III)-CN-V(III),DFT,-34.97
EOF
