#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR="/app/outputs"

# === solve block: step_01_geometries.csv ===
cat > "$OUTDIR/step_01_geometries.csv" <<'EOF'
reaction,functional,Cl_H,H_C,Cl_C,imag_freq
1,BH&H-LYP,1.426,1.450,2.876,972.7
1,M05-2X,1.426,1.470,2.896,807.8
2,BH&H-LYP,1.402,1.473,2.819,1350.6
2,M05-2X,1.409,1.478,2.805,1277.5
3,BH&H-LYP,1.495,1.341,2.834,1442.1
3,M05-2X,1.509,1.340,2.842,1139.6
4,BH&H-LYP,1.468,1.372,2.838,1425.1
4,M05-2X,1.474,1.374,2.847,1227.6
5,BH&H-LYP,1.379,1.658,3.020,203.0
5,M05-2X,1.337,1.895,3.184,108.8
EOF

# === solve block: step_03_energies.csv ===
cat > "$OUTDIR/step_03_energies.csv" <<'EOF'
reaction,method,basis,barrier,reaction_energy
1,M05-2X,6-31+G(d,p),29.7,23.5
1,M05-2X,aug-cc-pVTZ,29.7,23.5
1,DSD-B-LYP-D3,aug-cc-pVTZ,29.7,23.5
6,M05-2X,6-31+G(d,p),0.3,-121.1
6,M05-2X,aug-cc-pVTZ,0.3,-121.1
6,DSD-B-LYP-D3,aug-cc-pVTZ,0.3,-121.1
7,M05-2X,6-31+G(d,p),70.2,76.5
7,M05-2X,aug-cc-pVTZ,70.2,76.5
7,DSD-B-LYP-D3,aug-cc-pVTZ,70.2,76.5
8,M05-2X,6-31+G(d,p),24.9,-54.1
8,M05-2X,aug-cc-pVTZ,24.9,-54.1
8,DSD-B-LYP-D3,aug-cc-pVTZ,24.9,-54.1
9,M05-2X,6-31+G(d,p),112.3,78.3
9,M05-2X,aug-cc-pVTZ,112.3,78.3
9,DSD-B-LYP-D3,aug-cc-pVTZ,112.3,78.3
10,M05-2X,6-31+G(d,p),21.7,-18.1
10,M05-2X,aug-cc-pVTZ,21.7,-18.1
10,DSD-B-LYP-D3,aug-cc-pVTZ,21.7,-18.1
EOF
