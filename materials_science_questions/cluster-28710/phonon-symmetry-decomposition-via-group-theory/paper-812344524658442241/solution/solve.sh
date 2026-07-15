#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: block_decomposition.json ===
cat > /app/outputs/block_decomposition.json <<'FFEOF'
{
  "k0": [[1, 2], [2, 2], [3, 4]],
  "k_non_zone": [[4, 2], [5, 2]],
  "k_zone_boundary": [[4, 2], [5, 2]]
}
FFEOF
