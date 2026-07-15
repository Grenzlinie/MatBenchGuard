#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: strip_ledge_energies.csv ===
cat > "$OUTDIR/strip_ledge_energies.csv" << 'EOF'
ledge_type,gamma_large_spacing
[2-1-1]_U,-0.050
[2-1-1]_L,0.146
[211]_U,0.051
[211]_L,0.251
[2-1-1]_avg,0.050
[211]_avg,0.150
EOF

# === solve block: triangular_cluster_energies.csv ===
cat > "$OUTDIR/triangular_cluster_energies.csv" << 'EOF'
N_c,Delta_E_ex,total_ledge_length,gamma_l
3,0.9975,19.95,0.15
6,0.3764,28.23,0.08
13,-0.03196,41.55,-0.01
19,0.05286,50.22,0.02
25,0.06912,57.6,0.03
37,0.0663,70.08,0.035
49,0.0608,80.64,0.037
61,0.0560,90.0,0.038
79,0.0499,102.42,0.0385
100,0.04494,115.23,0.039
-1,,,0.039
EOF
