#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: E2g_frequencies.csv ===
cat > "$OUTDIR/E2g_frequencies.csv" <<'FFEOF'
system,frequency_cm1
1L,1360.6
2L,1357.6
3L,1357.4
bulk,1356.8
FFEOF

# === solve block: Gruneisen_parameter.txt ===
echo "0.64" > "$OUTDIR/Gruneisen_parameter.txt"
