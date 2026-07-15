#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: parameters.json ===
cat > "$OUTDIR/parameters.json" <<'EOF'
{
  "alpha_eff": 2.0,
  "ms_a_nm": 0.9,
  "ms_delta": 0.67,
  "ms_zeta": 1.5,
  "ohmic_alpha": 2.0
}
EOF
