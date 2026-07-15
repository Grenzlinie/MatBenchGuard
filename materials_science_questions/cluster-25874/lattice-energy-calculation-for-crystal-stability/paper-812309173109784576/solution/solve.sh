#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: urea_relaxed_params.json ===
cat > "$OUTDIR/urea_relaxed_params.json" <<'EOF'
{
  "a": 5.4692,
  "b": 5.4692,
  "c": 4.7266,
  "alpha": 90.0,
  "beta": 90.0,
  "gamma": 90.0,
  "U_r": -107.5
}
EOF
