#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ensp_computed.csv ===
cat > "$OUTDIR/ensp_computed.csv" <<'EOF'
composition,Se_eVnm,Sn_eVnm,ENSP
Ca10VO4_6F2,736,1010,0.73
Ca10P0.5V0.5O4_6F2,775,1022,0.76
Ca10PO4_6F2,823,1043,0.79
Pb4Ca6VO4_6F2,774,1143,0.68
EOF
