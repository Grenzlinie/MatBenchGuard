#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: migration_barriers.csv ===
cat > /app/outputs/migration_barriers.csv <<'FFEOF'
composition,barrier_eV
Li₆SbS₅I,0.41
Li₆.₆Si₀.₆Sb₀.₄S₅I,0.25
FFEOF
