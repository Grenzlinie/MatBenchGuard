#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: graphene_roughness_data.csv ===
cat > "$OUTDIR/graphene_roughness_data.csv" <<'FFEOF'
E_ad,Sq_Fe,Sq_Gr,epsilon_mean_top10
148.0,2.0,2.09,0.0095
130.4,4.0,3.666,0.01318
112.8,6.0,5.242,0.01686
FFEOF

# === solve block: per_atom_strains_sq6.json ===
python3 /solution/generate_strains.py > "$OUTDIR/per_atom_strains_sq6.json"
