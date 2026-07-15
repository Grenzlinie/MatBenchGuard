#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_moments.csv ===
cat > /app/outputs/dipole_moments.csv <<'FFEOF'
compound,conformer,dipole_B3LYP
1,ax-ax,3.40
1,eq-eq,1.87
2,ax-ax,3.44
2,eq-eq,1.93
3,ax-ax,3.16
3,eq-eq,1.92
4,ax-ax,1.57
4,eq-eq,1.78
5,ax-ax,2.58
5,eq-eq,2.04
6,ax-ax,2.86
6,eq-eq,2.26
7,ax-ax,2.96
7,eq-eq,2.33
8,ax-ax,2.89
8,eq-eq,2.29
9,ax-ax,1.30
9,eq-eq,1.37
FFEOF

# === solve block: ox_distances.csv ===
cat > /app/outputs/ox_distances.csv <<'FFEOF'
compound,O_X_distance
1,3.26
2,3.37
3,3.54
4,3.19
5,3.04
6,3.31
7,3.41
8,3.43
9,3.11
FFEOF
