#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: substitution_formation_energy.txt ===
cat > "$OUTDIR/substitution_formation_energy.txt" <<'FFEOF'
5.160
FFEOF
