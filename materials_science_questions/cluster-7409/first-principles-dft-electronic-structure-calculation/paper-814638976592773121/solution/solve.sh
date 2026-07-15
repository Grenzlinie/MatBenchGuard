#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_edge_shifts.csv ===
cat > /app/outputs/band_edge_shifts.csv <<'FFEOF'
defect,def_state_min,def_state_max,ΔE_V,ΔE_C,ΔE_g,p_z
O-H,-6.09,-5.97,0.68,0.67,-0.01,2.21
O-vac,-6.37,-6.08,0.38,0.36,-0.02,1.26
Ti-int,-6.76,-6.38,0.33,0.36,0.03,1.30
FFEOF
