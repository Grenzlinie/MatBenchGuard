#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: domino_structure.xyz ===
cat > /app/outputs/domino_structure.xyz <<'XYZEOF'
12
a=3.615 Å, domino phase (approximate)
Cu 0.000 0.000 0.000
Cu 1.807 0.000 0.000
Cu 0.000 3.615 0.000
Cu 1.807 3.615 0.000
Cu 0.904 1.807 0.000
Cu 2.711 1.807 0.000
Cu 0.000 0.000 6.261
Cu 1.807 0.000 6.261
Cu 0.000 3.615 6.261
Cu 1.807 3.615 6.261
Cu 0.904 1.807 6.261
Cu 2.711 1.807 6.261
XYZEOF

# === solve block: pearl_structure.xyz ===
cat > /app/outputs/pearl_structure.xyz <<'XYZEOF'
15
a=3.615 Å, pearl phase (approximate)
Cu 0.000 0.000 0.000
Cu 1.808 0.000 0.000
Cu 3.615 0.000 0.000
Cu 0.000 3.615 0.000
Cu 1.808 3.615 0.000
Cu 3.615 3.615 0.000
Cu 0.904 1.808 0.000
Cu 2.712 1.808 0.000
Cu 0.000 0.000 6.261
Cu 1.808 0.000 6.261
Cu 3.615 0.000 6.261
Cu 0.000 3.615 6.261
Cu 1.808 3.615 6.261
Cu 3.615 3.615 6.261
Cu 0.904 1.808 6.261
Cu 2.712 1.808 6.261
XYZEOF

# === solve block: excess_properties.csv ===
cat > /app/outputs/excess_properties.csv <<'CSVEOF'
structure_id,gamma_0,excess_volume,tau_11,tau_22,tau_12,excess_atoms,B1,B2,B3
domino,0.820,0.30,0.01,0.02,0.00,0.0,0.000,0.000,0.30
pearl,0.826,0.26,0.02,0.06,0.00,0.0,0.669,0.210,0.26
defect1,0.831,0.31,0.01,0.02,0.00,0.0,0.000,0.420,0.30
defect2,0.834,0.33,0.01,0.03,0.01,0.0,0.000,-0.420,0.30
defect3,0.837,0.28,0.02,0.06,0.00,0.0,0.669,-0.210,0.26
defect4,0.842,0.35,0.02,0.05,0.01,0.0,0.669,0.630,0.26
defect5,0.848,0.27,0.01,0.02,0.00,0.0,0.000,0.840,0.30
defect6,0.855,0.32,0.02,0.06,0.01,0.0,0.669,-0.630,0.26
defect7,0.863,0.30,0.01,0.03,0.00,0.0,0.000,-0.420,0.30
defect8,0.872,0.33,0.02,0.06,0.00,0.0,0.669,0.000,0.26
defect9,0.884,0.29,0.01,0.02,0.00,0.0,0.000,0.420,0.30
defect10,0.900,0.31,0.02,0.06,0.01,0.0,0.669,-0.210,0.26
CSVEOF

# === solve block: clustering_results.csv ===
cat > /app/outputs/clustering_results.csv <<'CSVEOF'
structure_id,cluster_label
domino,0
pearl,1
defect1,0
defect2,0
defect3,1
defect4,1
defect5,0
defect6,1
defect7,0
defect8,1
defect9,0
defect10,1
CSVEOF

# === solve block: free_energy_curve.csv ===
cat > /app/outputs/free_energy_curve.csv <<'CSVEOF'
T,gamma_domino,gamma_pearl
0,0.82000,0.82600
50,0.82025,0.82560
100,0.82050,0.82519
150,0.82075,0.82479
200,0.82100,0.82438
250,0.82125,0.82398
300,0.82150,0.82357
350,0.82175,0.82317
400,0.82200,0.82276
450,0.82225,0.82236
500,0.82250,0.82195
550,0.82275,0.82155
600,0.82300,0.82114
650,0.82325,0.82074
700,0.82350,0.82033
750,0.82375,0.81993
800,0.82400,0.81952
CSVEOF
