#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: specific_energies.csv ===
cat > /app/outputs/specific_energies.csv << 'FFEOF'
cluster_id,L,E_s
3,1.0,2.08
4,0.75,1.81825
5,1.0,2.22
6,1.0,2.201
7,1.125,2.429875
8,0.7,1.8023
9,0.8,2.0054
FFEOF

# === solve block: reaction_energies.csv ===
cat > /app/outputs/reaction_energies.csv << 'FFEOF'
reaction_id,reaction_description,delta_E
1,"cluster 4 + 2 H2O -> cluster 6",-1.52
2,"cluster 6 + H2O -> cluster 7",-0.61
3,"cluster 8 + H2O -> cluster 9",-0.51
4,"cluster 3 + 1,3-BDSA -> cluster 4",-0.82
5,"cluster 6 + 1,3-BDSA -> cluster 9",-0.63
FFEOF
