#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: hoop_stress_evolution.csv ===
cat > "$OUTDIR/hoop_stress_evolution.csv" <<'EOF'
time,hoop_stress_A,hoop_stress_B
2.0,-0.52,-0.38
4.0,-0.14,0.12
6.0,0.18,0.65
8.0,0.52,1.18
10.0,0.82,1.75
12.0,1.05,2.18
14.0,1.22,2.48
16.0,1.35,2.72
18.0,1.43,2.88
20.0,1.50,3.02
EOF

# === solve block: crack_length_vs_soc.csv ===
cat > "$OUTDIR/crack_length_vs_soc.csv" <<'EOF'
soc,crack_length
0.05,0.0
0.10,0.0
0.15,0.0
0.20,0.08
0.25,0.20
0.30,0.35
0.35,0.50
EOF
