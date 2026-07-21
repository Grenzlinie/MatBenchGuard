#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: nanowire_diffusion.csv ===
cat > "/app/outputs/nanowire_diffusion.csv" <<'FFEOF'
assembly,temperature,diffusion_coefficient
5x55,300,0.0005
5x55,600,0.002
5x55,800,0.004
5x55,900,0.006
5x55,1000,0.02
5x55,1100,0.08
5x55,1200,0.25
5x55,1300,0.6
5x55,1400,1.2
10x55,300,0.0004
10x55,600,0.002
10x55,800,0.004
10x55,900,0.015
10x55,1000,0.05
10x55,1100,0.15
10x55,1200,0.4
10x55,1300,0.9
10x55,1400,1.5
5x147,300,0.0003
5x147,600,0.0015
5x147,800,0.0045
5x147,900,0.008
5x147,1000,0.03
5x147,1100,0.1
5x147,1200,0.3
5x147,1300,0.7
5x147,1400,1.2
10x147,300,0.0002
10x147,600,0.001
10x147,800,0.004
10x147,900,0.007
10x147,1000,0.015
10x147,1100,0.04
10x147,1200,0.15
10x147,1300,0.5
10x147,1400,1.0
FFEOF

# === solve block: nanofilm_planarity.csv ===
cat > "/app/outputs/nanofilm_planarity.csv" <<'FFEOF'
assembly,temperature,planarity_ratio
5x55_5x5,300,5.0
5x55_5x5,600,5.0
5x55_5x5,800,4.8
5x55_5x5,900,4.5
5x55_5x5,1000,4.0
5x55_5x5,1100,1.8
5x55_5x5,1200,1.2
5x55_5x5,1300,1.0
5x55_5x5,1400,0.9
5x147_5x5,300,4.0
5x147_5x5,600,4.0
5x147_5x5,800,3.8
5x147_5x5,900,3.5
5x147_5x5,1000,3.0
5x147_5x5,1100,1.5
5x147_5x5,1200,1.1
5x147_5x5,1300,1.0
5x147_5x5,1400,0.9
FFEOF
