#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relative_energies.json ===
cat > "$OUTDIR/relative_energies.json" << 'EOF'
{
  "R3c-G": 0,
  "Pnma-G": 60,
  "Pna2_1-G": 47,
  "Cc-C": 10,
  "Cm-C": 12,
  "Pc-C": 19
}
EOF
