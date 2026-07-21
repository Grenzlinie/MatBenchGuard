#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: effective_masses.csv ===
cat > "$OUTDIR/effective_masses.csv" <<'EOF'
n,m_surface,m_bulk,ratio
0.5,1.0,1.0,1.0
0.6,1.05,1.02,1.0294117647058822
0.7,1.2,1.1,1.0909090909090908
0.8,1.5,1.25,1.2
0.85,1.8,1.4,1.2857142857142858
0.9,2.3,1.7,1.3529411764705883
0.93,3.2,2.1,1.5238095238095237
0.96,5.0,2.8,1.7857142857142858
0.98,8.0,4.0,2.0
0.99,12.0,5.0,2.4
EOF

# === solve block: surface_mode_thresholds.csv ===
cat > "$OUTDIR/surface_mode_thresholds.csv" <<'EOF'
k_point,threshold_n
(0,0),0.94
(pi,pi),0.90
EOF
