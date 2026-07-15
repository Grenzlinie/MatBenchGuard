#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# The helper script /solution/generate_outputs.py writes all JSON artifacts.
# It uses only stdlib (json, math, os).

# === solve block: migration_barriers.json ===
cat > "$OUTDIR/migration_barriers.json" <<'FFEOF'
{
  "LFP_pristine_barrier_eV": 0.68,
  "LNFP_doped_local_barrier_eV": 0.38
}
FFEOF

# === solve finalize ===
echo 'All solve artifacts written.'
