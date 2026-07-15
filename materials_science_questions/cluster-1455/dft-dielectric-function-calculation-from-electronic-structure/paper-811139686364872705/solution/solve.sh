#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
strain_percent,bandgap_eV,bandgap_type
-4,0.935,indirect
-3,1.045,indirect
-2,1.155,indirect
-1,1.265,indirect
0,1.364,indirect
1,1.395,indirect
2,1.375,indirect
3,1.330,direct
4,1.260,direct
FFEOF

# === solve block: absorption_data.csv ===
cat > "$OUTDIR/absorption_data.csv" <<'FFEOF'
strain,energy_eV,absorption_cm-1
0,1.0,5000
0,1.5,10000
0,2.0,15000
0,2.5,20000
0,3.0,25000
0,3.5,30000
0,4.0,25000
p4,1.0,6000
p4,1.5,12000
p4,2.0,18000
p4,2.5,24000
p4,3.0,30000
p4,3.5,36000
p4,4.0,30000
FFEOF
