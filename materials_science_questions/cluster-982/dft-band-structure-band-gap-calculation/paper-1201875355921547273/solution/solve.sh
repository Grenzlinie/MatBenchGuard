#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: hybrid_ZT.csv ===
cat > "$OUTDIR/hybrid_ZT.csv" <<'FFEOF'
Temperature (K),ZT_SnSe_hBN,ZT_SnSe_CsPbI3
100,0.985,0.991
200,0.966,0.980
300,0.950,0.961
400,0.933,0.944
500,0.912,0.930
600,0.888,0.913
700,0.861,0.889
800,0.832,0.876
900,0.802,0.865
1000,0.773,0.854
FFEOF

# === solve block: layered_ZT.csv ===
cat > "$OUTDIR/layered_ZT.csv" <<'FFEOF'
Layer,Temperature_K,ZT_elec
monolayer,650,1.6
bilayer,200,1.6
three-layer,150,2.5
four-layer,150,2.49
FFEOF
