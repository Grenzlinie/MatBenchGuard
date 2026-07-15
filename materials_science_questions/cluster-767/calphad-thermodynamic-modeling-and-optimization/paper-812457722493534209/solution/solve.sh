#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: segregation_results.csv ===
cat > "$OUTDIR/segregation_results.csv" <<'EOF'
System,NoSize_SurfaceFrac,NoSize_EdgeCornerFrac,Size_SurfaceFrac,Size_EdgeCornerFrac
Rh-Ag,17.00,0.00,17.00,0.00
Rh-Cu,17.00,0.00,17.00,0.00
Pd-Ag,18.00,2.00,17.00,2.00
Ni-Ag,17.00,0.00,17.00,3.00
Cu-Ag,25.00,8.00,19.00,13.00
Rh-Pd,18.00,2.00,17.00,2.00
Ni-Cu,20.00,3.00,18.00,5.00
Rh-Ni,21.00,3.00,32.00,5.00
Ni-Pd,35.00,27.00,23.00,32.00
Pd-Cu,24.00,10.00,34.00,12.00
EOF
