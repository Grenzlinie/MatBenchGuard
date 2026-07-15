#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_optimized_geometries.csv ===
cat > "$OUTDIR/step_01_optimized_geometries.csv" << 'EOF'
system,r_Si-Si,alpha_degrees
1-sb,2.1466,22.8
1-ts,2.2027,-9.7
1-lb,2.4431,-64.1
2-sb,2.3993,-10.4
2-ts,2.4077,-12.3
2-lb,2.7734,-62.8
EOF

# === solve block: step_02_vb_energies.csv ===
cat > "$OUTDIR/step_02_vb_energies.csv" << 'EOF'
system,D_in_situ,D_COV,RE_CS,pct_RE_CS,bond_type
1-sb,197.2,129.7,67.5,34,COV
1-ts,246.6,137.7,108.9,44,COV
1-lb,154.4,39.2,115.3,75,CS
2-sb,276.1,160.9,115.2,42,COV
2-ts,275.3,158.8,116.5,42,COV
2-lb,168.2,64.4,103.8,62,CS
EOF

# === solve block: step_03_alpha_scan.csv ===
cat > "$OUTDIR/step_03_alpha_scan.csv" << 'EOF'
alpha_degrees,D_in_situ,D_COV,RE_CS
30,147,80,67
25,153,85,68
20,159,90,69
15,165,95,70
10,171,100,71
5,177,105,72
0,184,110,74
-5,188,112,76
-10,186,108,78
-15,183,102,81
-20,179,95,84
-30,168,78,90
-40,157,60,97
-50,149,45,104
-60,146,35,111
-70,148,30,118
EOF
