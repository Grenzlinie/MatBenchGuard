#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > "/app/outputs/results.csv" <<'FFEOF'
phase,n_n,a_Oy,K_ratio,m_star_ratio,S_F_ratio
lasagna,0.0735,23.71,1.0698,1.0307,0.9878
lasagna,0.0749,23.07,1.0664,1.0286,0.9885
lasagna,0.0773,22.23,1.0605,1.0251,0.9896
lasagna,0.0792,21.84,1.0526,1.0196,0.9910
hexagonal_spaghetti,0.0581,27.17,1.4102,1.3471,0.8898
hexagonal_spaghetti,0.0630,25.77,1.2972,1.2425,0.9145
hexagonal_spaghetti,0.0678,24.62,1.2225,1.1744,0.9322
hexagonal_spaghetti,0.0716,23.97,1.1668,1.1239,0.9471
square_spaghetti,0.0581,27.17,1.4673,1.4016,0.8778
square_spaghetti,0.0630,25.77,1.3231,1.2673,0.9085
square_spaghetti,0.0678,24.62,1.2124,1.1647,0.9347
square_spaghetti,0.0716,23.97,1.1473,1.1051,0.9524
FFEOF
