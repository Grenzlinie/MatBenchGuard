#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "LiV_first": -0.89,
  "LiV_second": -0.7,
  "KV_first": -0.69,
  "KV_second": -0.6
}
FFEOF
