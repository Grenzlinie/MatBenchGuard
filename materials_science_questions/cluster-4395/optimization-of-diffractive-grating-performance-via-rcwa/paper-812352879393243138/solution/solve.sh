#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: te_polarizer_depths.csv ===
cat > /app/outputs/te_polarizer_depths.csv <<'EOF'
a_d,theta_i_deg,h_over_lambda
0.00001,35,0.250
0.00001,45,0.250
0.00001,55,0.250
0.00001,65,0.250
0.001,35,0.249
0.001,45,0.249
0.001,55,0.249
0.001,65,0.249
0.01,35,0.241
0.01,45,0.243
0.01,55,0.244
0.01,65,0.244
0.05,35,0.221
0.05,45,0.227
0.05,55,0.230
0.05,65,0.232
0.1,35,0.210
0.1,45,0.218
0.1,55,0.223
0.1,65,0.225
0.25,35,0.206
0.25,45,0.213
0.25,55,0.214
0.25,65,0.205
0.333,55,0.206
0.333,65,0.185
EOF

# === solve block: tm_polarizer_verification.json ===
cat > /app/outputs/tm_polarizer_verification.json <<'EOF'
{
  "theta_i_deg": 45,
  "a_over_d": 0.754,
  "d_over_lambda": 0.707,
  "h_over_lambda": 0.96,
  "TE_reflection": 0.0,
  "TM_reflection": 1.0
}
EOF
