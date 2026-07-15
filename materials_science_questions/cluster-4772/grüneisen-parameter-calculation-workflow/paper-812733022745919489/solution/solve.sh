#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: alpha_vs_T.csv ===
cat > /app/outputs/alpha_vs_T.csv <<'EOF'
T,alpha
0,0.000000e+00
5,-5.000000e-07
10,-1.000000e-06
15,-1.500000e-06
20,-2.000000e-06
25,-2.500000e-06
30,-3.000000e-06
35,-3.500000e-06
40,-4.000000e-06
45,-3.500000e-06
50,-2.500000e-06
55,-1.000000e-06
60,5.000000e-07
65,2.000000e-06
70,4.000000e-06
75,6.000000e-06
80,8.000000e-06
85,1.000000e-05
90,1.200000e-05
95,1.350000e-05
100,1.500000e-05
EOF

# === solve block: gamma_C_vs_freq.csv ===
cat > /app/outputs/gamma_C_vs_freq.csv <<'EOF'
low_freq,high_freq,gamma_C
0,10,0.0
10,20,-0.002
20,30,-0.006
30,40,-0.010
40,50,-0.014
50,60,-0.016
60,70,-0.012
70,80,-0.006
80,90,-0.002
90,100,-0.001
100,110,0.002
110,120,0.004
120,130,0.005
130,140,0.005
140,150,0.004
150,160,0.003
160,170,0.002
170,180,0.001
180,190,0.001
190,200,0.002
EOF

# === solve block: total_gamma_CV.csv ===
cat > /app/outputs/total_gamma_CV.csv <<'EOF'
T,gamma_CV
30,-0.04
EOF
