#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: barriers.json ===
cat > "$OUTDIR/barriers.json" <<'FFEOF'
{
  "MvK_barrier_0K": 0.999,
  "ER_barrier_0K": 0.557,
  "LH_barrier_0K": 0.965
}
FFEOF
