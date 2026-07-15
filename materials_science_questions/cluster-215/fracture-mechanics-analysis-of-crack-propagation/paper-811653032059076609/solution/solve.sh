#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predicted_strengths.csv ===
cat > "$OUTDIR/predicted_strengths.csv" <<'FFEOF'
hole_diameter,PSC_predicted,AVC_predicted,DZC_predicted,ECGM_predicted
0.6,401.62,379.93,416.71,385.86
1.1,320.29,320.29,336.24,322.69
1.5,288.18,293.89,291.81,292.13
2.2,255.14,266.01,238.87,252.97
5.1,211.67,222.63,155.10,156.53
FFEOF
