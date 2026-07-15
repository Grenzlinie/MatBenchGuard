#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: occupations_O3_5.csv ===
cat > /app/outputs/occupations_O3_5.csv <<'FFEOF'
temperature,Ni_site,d_z2_occupation,d_x2_y2_occupation
9 K,Ni(1),1.9,0.5
9 K,Ni(2),1.2,0.0
9 K,Ni(3),1.4,0.2
9 K,Ni(4),2.0,0.6
9 K,Ni(5),1.1,0.1
9 K,Ni(6),1.8,0.1
300 K,Ni(1),1.1,0.3
300 K,Ni(2),1.3,0.1
300 K,Ni(3),1.1,0.1
300 K,Ni(4),1.9,0.7
300 K,Ni(5),1.2,0.2
300 K,Ni(6),1.9,0.5
FFEOF

# === solve block: occupations_O2.csv ===
cat > /app/outputs/occupations_O2.csv <<'FFEOF'
temperature,Ni_site,d_z2_occupation,d_x2_y2_occupation
9 K,Ni(1),1.9,0.5
9 K,Ni(2),1.0,0.0
9 K,Ni(3),1.1,0.0
9 K,Ni(4),1.6,0.6
9 K,Ni(5),1.0,0.1
9 K,Ni(6),1.4,0.1
300 K,Ni(1),1.0,0.3
300 K,Ni(2),1.0,0.1
300 K,Ni(3),1.0,0.1
300 K,Ni(4),1.8,0.7
300 K,Ni(5),1.0,0.2
300 K,Ni(6),1.3,0.5
FFEOF
