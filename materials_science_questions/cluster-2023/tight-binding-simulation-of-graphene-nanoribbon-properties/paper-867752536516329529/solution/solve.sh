#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap_curvature.csv ===
cat > "$OUTDIR/band_gap_curvature.csv" <<'FFEOF'
curvature,EG,NEG
0.0,0.60,1.20
0.02,0.60,1.22
0.04,0.60,1.25
0.05,0.58,1.28
0.0625,0.55,1.30
0.0769,0.53,1.25
0.100,0.53,1.15
0.111,0.45,1.05
0.125,0.38,0.95
0.1429,0.30,0.85
0.1667,0.20,0.75
FFEOF

# === solve block: identification_of_critical_curvatures.txt ===
cat > "$OUTDIR/identification_of_critical_curvatures.txt" <<'FFEOF'
kappa0: 0.04
kappac1: 0.0625
kappac2: 0.100
FFEOF

# === solve block: edge_gap_width_flat.csv ===
cat > "$OUTDIR/edge_gap_width_flat.csv" <<'FFEOF'
n,EG,delta_EC,delta_EV
9,0.73,0.02,0.06
10,0.66,0.08,0.24
11,0.62,0.12,0.36
12,0.72,0.02,0.06
13,0.65,0.07,0.21
14,0.61,0.10,0.30
15,0.71,0.02,0.06
16,0.64,0.06,0.18
17,0.60,0.09,0.27
18,0.70,0.02,0.06
19,0.63,0.06,0.18
20,0.59,0.08,0.24
21,0.69,0.02,0.06
22,0.62,0.05,0.15
23,0.58,0.07,0.21
24,0.68,0.02,0.06
FFEOF

# === solve block: excitontable.csv ===
cat > "$OUTDIR/excitontable.csv" <<'FFEOF'
radius,Eg,EA,Eb,EAtriplet,DeltaST
inf,1.98,0.57,1.41,0.35,0.22
13,1.91,0.50,1.41,0.30,0.20
9,1.88,0.50,1.38,0.30,0.20
6,1.47,0.33,1.14,0.28,0.05
FFEOF
