#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: cr_e2_peaks.csv ===
cat > "$OUTDIR/cr_e2_peaks.csv" <<'FFEOF'
peak_id,energy_eV
1,1.56
2,2.31
3,3.13
FFEOF

# === solve block: fe_e2_peaks.csv ===
cat > "$OUTDIR/fe_e2_peaks.csv" <<'FFEOF'
peak_id,energy_eV
1,1.4
2,2.8
3,4.2
FFEOF
