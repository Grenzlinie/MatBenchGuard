#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: zt_results.json ===
cat > "$OUTDIR/zt_results.json" <<'FFEOF'
{
  "ZT_x_p_600K": 1.48,
  "ZT_y_n_600K": 1.05
}
FFEOF
