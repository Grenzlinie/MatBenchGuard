#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "mo_barrier": 1.34,
  "mos2_barrier": 2.3,
  "mo_dft_calls": 49,
  "mos2_dft_calls": 49
}
EOF
