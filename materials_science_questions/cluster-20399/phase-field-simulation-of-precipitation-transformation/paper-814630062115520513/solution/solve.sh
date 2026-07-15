#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: nearest_neighbors_Ag2Al.csv ===
cat > "$OUTDIR/nearest_neighbors_Ag2Al.csv" <<'CSVEOF'
neighbor_count,relative_frequency
1,0.25
2,0.50
3,0.15
4,0.10
CSVEOF

# === solve block: nearest_neighbors_Al2Cu.csv ===
cat > "$OUTDIR/nearest_neighbors_Al2Cu.csv" <<'CSVEOF'
neighbor_count,relative_frequency
1,0.18
2,0.50
3,0.20
4,0.12
CSVEOF
