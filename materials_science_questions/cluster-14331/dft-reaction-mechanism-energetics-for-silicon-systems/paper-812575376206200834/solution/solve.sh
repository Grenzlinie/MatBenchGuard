#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: initial_decomposition_results.csv ===
cat > "$OUTDIR/initial_decomposition_results.csv" <<'EOF'
pathway,temperature_K,delta_G_forward_kcalmol,rate_constant_s-1
P1,298.15,84.38,8.30e-50
P1,1000,,4.43e-6
P1,1500,,1.57e1
P1,2000,,2.49e4
P1,2500,,2.18e6
P2,298.15,37.79,9.70e-16
P2,1000,,1.07e5
P2,1500,,9.29e7
P2,2000,,2.98e9
P2,2500,,2.52e10
P3,298.15,100.69,9.10e-62
P3,1000,,2.02e-9
P3,1500,,6.59e-2
P3,2000,,4.10e2
P3,2500,,8.15e4
P4,298.15,45.41,3.12e-21
P4,1000,,2.46e3
P4,1500,,7.52e6
P4,2000,,4.53e8
P4,2500,,5.57e9
EOF
