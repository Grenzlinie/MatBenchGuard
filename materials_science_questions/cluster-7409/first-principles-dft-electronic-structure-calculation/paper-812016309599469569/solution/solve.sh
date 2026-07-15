#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: vacancy_A1_state_energy.txt ===
cat > "$OUTDIR/vacancy_A1_state_energy.txt" <<'FFEOF'
0.8
FFEOF
