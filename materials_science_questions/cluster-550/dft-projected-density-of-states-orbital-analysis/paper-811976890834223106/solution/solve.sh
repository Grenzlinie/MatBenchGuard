#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"

# === solve block: energy_differences.json ===
cat > "$OUTDIR/energy_differences.json" <<'EEOF'
{
  "Fe": -0.26,
  "Co": 0.69,
  "Ni": 2.34
}
EEOF
