#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fit_params.json ===
cat > /app/outputs/fit_params.json <<'EOF'
{
  "Dq": 413,
  "B": 455,
  "low_symmetry_splitting_4T2": 200
}
EOF
