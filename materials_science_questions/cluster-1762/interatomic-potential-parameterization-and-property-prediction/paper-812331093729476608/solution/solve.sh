#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: cu_hcu7_110.csv ===
cat > /app/outputs/cu_hcu7_110.csv <<'FFEOF'
angle_deg,C,alpha_inv_sqrt
0,0.346,84
2,0.350,87
5,0.370,150
10,0.429,150
15,0.509,120
20,0.642,39
22,0.841,12
23,1.61,1.9
24,0.714,4.6
46,0.375,9.0
48,0.791,11
50,1.15,11
52,1.37,11
54.74,1.45,23
58,1.39,11
60,1.31,10
65,0.909,10
70,0.388,13
72,0.195,11
80,0.244,94
85,0.273,190
90,0.281,280
0,0.277,91
3,0.266,82
6,0.225,51
8,0.155,19
76,0.189,42
FFEOF
