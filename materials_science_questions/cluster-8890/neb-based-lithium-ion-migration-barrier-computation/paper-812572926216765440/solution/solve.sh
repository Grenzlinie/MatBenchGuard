#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: li_migration_barriers.csv ===
cat > /app/outputs/li_migration_barriers.csv <<'FFEOF'
barrier_eV,migration_path
0.36,2b→4d→2b
FFEOF
