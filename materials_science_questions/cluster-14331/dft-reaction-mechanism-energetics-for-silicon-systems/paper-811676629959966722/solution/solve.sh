#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p $OUTDIR

# === solve block: reaction_energies.json ===
cat > $OUTDIR/reaction_energies.json <<'EOF'
{
  "E1": 84.2,
  "E2": 81.4,
  "E3": 54.0,
  "unit": "kcal/mol"
}
EOF
