#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: buckling_onset_strains.csv ===
cat > /app/outputs/buckling_onset_strains.csv <<'FFEOF'
H_coverage,buckling_onset_strain
0,1.7
0.15,1.1
1,0.9
5,0.8
10,0.7
15,0.7
20,0.7
25,0.7
30,0.8
40,1.0
50,1.0
FFEOF
