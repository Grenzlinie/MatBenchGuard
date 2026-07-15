#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_ufg_vs_E.csv ===
cat > /app/outputs/step_01_ufg_vs_E.csv <<'FFEOF'
E,Ufg_no_ni,Ufg_with_ni
0,0.0,0.0
1,0.7,0.7
2,1.4,1.4
3,2.1,2.1
4,2.8,2.8
5,3.5,3.5
6,4.5,4.0
7,5.5,4.5
8,6.5,5.0
9,7.5,5.5
10,8.5,5.9
11,9.5,6.3
12,10.5,6.7
13,11.5,7.1
14,12.5,7.5
15,13.5,7.9
16,14.5,8.3
FFEOF
