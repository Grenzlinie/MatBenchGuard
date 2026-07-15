#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'EOF'
x,r_c_PAA,E_total,B,delta_H
0.0,2.8522,-0.35661,1.032,0.0
0.1,2.8007,-0.36095,1.087,0.088
0.2,2.7492,-0.36540,1.144,0.061
0.3,2.6999,-0.36977,1.203,0.113
0.4,2.6530,-0.37404,1.263,0.274
0.5,2.6060,-0.37842,1.327,0.318
0.6,2.5590,-0.38291,1.395,0.252
0.7,2.5120,-0.38752,1.469,0.070
0.8,2.4672,-0.39202,1.542,0.006
0.9,2.4248,-0.39639,1.617,0.055
1.0,2.3823,-0.40087,1.696,0.0
EOF
