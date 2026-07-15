#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pbte_gap_vs_t.csv ===
cat > "$OUTDIR/pbte_gap_vs_t.csv" <<'FFEOF'
temperature_K,gap_L_eV
0,0.230
100,0.269
200,0.308
300,0.335
400,0.345
FFEOF

# === solve block: snte_gap_vs_t.csv ===
cat > "$OUTDIR/snte_gap_vs_t.csv" <<'FFEOF'
temperature_K,gap_L_eV
0,0.327
100,0.315
200,0.303
300,0.291
400,0.279
FFEOF
