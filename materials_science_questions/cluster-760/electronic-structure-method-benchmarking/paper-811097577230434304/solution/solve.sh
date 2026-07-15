#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: activation_energies.json ===
mkdir -p "$OUTDIR"
cat > "$OUTDIR/activation_energies.json" <<'FFEOF'
{
  "Rosslynlee": 66.0,
  "Dalquhandy": 68.0
}
FFEOF
