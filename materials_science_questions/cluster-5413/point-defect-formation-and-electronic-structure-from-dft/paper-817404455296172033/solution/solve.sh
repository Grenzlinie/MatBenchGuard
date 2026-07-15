#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'FFEOF'
{
  "Fe5_Ti2": 0.226,
  "Fe3_VO_U2": -1.6774
}
FFEOF
