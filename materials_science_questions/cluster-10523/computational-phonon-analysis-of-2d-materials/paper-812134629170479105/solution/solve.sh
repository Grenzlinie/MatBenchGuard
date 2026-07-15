#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ka_slopes.json ===
cat > "$OUTDIR/ka_slopes.json" <<'FFEOF'
{
  "alpha_Gamma_LO": 397,
  "alpha_K": 973
}
FFEOF
