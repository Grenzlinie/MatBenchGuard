#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_positions.csv ===
cat > "/app/outputs/predicted_positions.csv" <<'CSVEOF'
compound,Z,u,v
YVO4,39,0.1868,0.3302
CeVO4,58,0.1786,0.3297
PrVO4,59,0.1793,0.3290
NdVO4,60,0.1800,0.3284
SmVO4,62,0.1815,0.3272
EuVO4,63,0.1822,0.3265
GdVO4,64,0.1829,0.3259
TbVO4,65,0.1836,0.3253
DyVO4,66,0.1844,0.3247
HoVO4,67,0.1851,0.3240
ErVO4,68,0.1858,0.3234
TmVO4,69,0.1865,0.3228
YbVO4,70,0.1873,0.3222
LuVO4,71,0.1880,0.3215
CSVEOF
