#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: activation_energies.json ===
cat > "$OUTDIR/activation_energies.json" <<'FFEOF'
{
  "formaldehyde": 9.6,
  "benzaldehyde": 2.0,
  "acetone": 24.0,
  "methyl_formate": 67.7
}
FFEOF
