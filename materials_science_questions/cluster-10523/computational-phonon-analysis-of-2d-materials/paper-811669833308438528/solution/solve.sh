#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_moments.csv ===
cat > /app/outputs/magnetic_moments.csv <<'FFEOF'
x,magnetic_moment
0.00,1.370
0.05,1.274
0.10,1.136
0.15,0.947
0.20,0.640
0.25,0.351
0.30,0.000
FFEOF

# === solve block: dos_fermi.csv ===
cat > /app/outputs/dos_fermi.csv <<'FFEOF'
x,dos_fermi
0.00,0.7
0.05,0.9
0.10,1.5
0.15,2.2
0.20,1.8
0.25,1.2
0.30,0.5
FFEOF

# === solve block: lambda.csv ===
cat > /app/outputs/lambda.csv <<'FFEOF'
x,lambda
0.00,0.03
0.05,0.06
0.10,0.10
0.15,0.11
0.20,0.07
0.25,0.04
0.30,0.01
FFEOF
