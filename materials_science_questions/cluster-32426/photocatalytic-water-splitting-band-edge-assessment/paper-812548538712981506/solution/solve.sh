#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_band_properties.csv ===
cat > /app/outputs/step_01_band_properties.csv <<'FFEOF'
CBM_vacuum,Eg,VBM_vacuum,band_type,case
-4.298,2.985,-7.283,Z-scheme,uniaxial_-2%
-4.574,2.570,-7.144,Z-scheme,uniaxial_-4%
-3.615,3.673,-7.288,Z-scheme,biaxial_-2%
-4.899,0.917,-5.816,Type-II,biaxial_-6%
-5.216,0.707,-5.923,Type-II,biaxial_-8%
FFEOF

# === solve block: step_02_oer_thermodynamics.csv ===
cat > /app/outputs/step_02_oer_thermodynamics.csv <<'FFEOF'
EDF_pH0,EDF_pH7,PDS_pH0,PDS_pH7,case,feasible_pH0,feasible_pH7
1.553,1.966,0.585,0.172,uniaxial_-2%,true,true
1.414,1.827,0.639,0.226,uniaxial_-4%,true,true
1.558,1.971,0.610,0.197,biaxial_-2%,true,true
0.086,0.499,0.527,0.114,biaxial_-6%,false,true
0.193,0.606,0.607,0.194,biaxial_-8%,false,true
FFEOF
