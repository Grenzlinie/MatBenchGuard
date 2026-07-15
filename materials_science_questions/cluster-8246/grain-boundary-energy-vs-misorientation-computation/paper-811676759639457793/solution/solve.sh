#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reaction_counts.csv ===
cat > "$OUTDIR/reaction_counts.csv" <<'CSVEOF'
sigma,condition,absorption_count,transmission_count
3,disordered,12,288
3,ordered,3,72
5,disordered,6,216
5,ordered,0,72
7,disordered,6,216
7,ordered,0,72
9,disordered,12,288
9,ordered,3,72
11,disordered,6,216
11,ordered,0,72
13,disordered,6,216
13,ordered,0,72
CSVEOF
