#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_stoner_factors.json ===
cat > "$OUTDIR/step_01_stoner_factors.json" <<'EOF'
{
  "alpha_max_s": 0.97,
  "alpha_0_c": 0.97,
  "alpha_Q_c": 0.86
}
EOF
