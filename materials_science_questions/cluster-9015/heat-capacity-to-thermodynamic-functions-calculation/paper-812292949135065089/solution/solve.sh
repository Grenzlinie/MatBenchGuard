#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: entropy.txt ===
cat > "$OUTDIR/entropy.txt" <<'FFEOF'
18.73
FFEOF

# === solve block: heat_content_table.csv ===
cat > "$OUTDIR/heat_content_table.csv" <<'FFEOF'
T,H_diff,S_diff
350,860,2.65
400,1800,5.16
420,2180,6.09
500,3540,9.05
600,5350,12.35
700,7210,15.22
800,9090,17.73
900,11000,19.98
1000,12970,22.05
FFEOF
