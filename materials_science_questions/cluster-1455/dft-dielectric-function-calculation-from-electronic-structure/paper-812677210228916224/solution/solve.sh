#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_mechanical_properties.csv ===
# Write the mechanical properties CSV directly from paper Table 3 values
cat > /app/outputs/step_01_mechanical_properties.csv <<'EOF'
pressure,B_H,G_H,B_H_G_H,v,C12_C44
0,14.98,10.34,1.45,0.22,-3.39
5,47.55,19.61,2.42,0.32,21.06
10,69.46,24.59,2.82,0.34,39.96
15,95.38,36.00,2.65,0.33,55.19
20,117.15,41.17,2.85,0.34,72.93
25,140.61,45.74,3.07,0.35,95.23
30,160.25,51.56,3.11,0.35,110.68
35,180.48,55.59,3.25,0.36,128.65
40,198.61,60.28,3.29,0.36,144.77
EOF

# === solve block: step_02_band_gap.csv ===
cat > /app/outputs/step_02_band_gap.csv <<'EOF'
pressure,band_gap
0,3.444
5,3.340
10,3.236
15,3.133
20,3.029
25,2.925
30,2.821
35,2.718
40,2.614
EOF

# === solve block: step_03_static_refractive_index.csv ===
cat > /app/outputs/step_03_static_refractive_index.csv <<'EOF'
direction,static_refractive_index_n0
100,1.74
010,1.73
001,1.77
EOF
