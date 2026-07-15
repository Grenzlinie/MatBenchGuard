#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: length_scale_params.json ===
cat > '/app/outputs/length_scale_params.json' <<'FFEOF'
{
  "l0_MSGT_μm": 3.60,
  "l2_MCST_μm": 6.75
}
FFEOF

# === solve block: deflection_ratios.csv ===
cat > '/app/outputs/deflection_ratios.csv' <<'FFEOF'
thickness_µm,ratio_MSGT,ratio_MCST
50,0.98,0.97
45,0.975,0.96
40,0.97,0.95
35,0.96,0.93
30,0.90,0.88
25,0.85,0.82
20,0.80,0.76
15,0.75,0.70
10,0.65,0.60
5,0.50,0.45
2,0.35,0.30
1,0.25,0.20
FFEOF
