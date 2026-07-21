#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_03_ionic_pair_distances.json ===
cat > "$OUTDIR/step_03_ionic_pair_distances.json" <<'FFEOF'
{
  "Z1": 3.95,
  "Z2": 3.52,
  "Z3": 3.98
}
FFEOF
