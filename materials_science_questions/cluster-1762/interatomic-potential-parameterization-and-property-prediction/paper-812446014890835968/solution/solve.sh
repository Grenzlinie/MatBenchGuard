#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: raman_frequencies.json ===
cat > "$OUTDIR/raman_frequencies.json" <<'EOF'
{
  "CaF2": 314.7,
  "SrF2": 284.9,
  "BaF2": 247.2
}
EOF
