#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: valence_bands.json ===
cat > "$OUTDIR/valence_bands.json" <<'FFEOF'
{
  "AlIr": 6,
  "RuAl2": 14,
  "RuGa3": 34
}
FFEOF

# === solve finalize ===
echo "Oracle artifacts written successfully."
