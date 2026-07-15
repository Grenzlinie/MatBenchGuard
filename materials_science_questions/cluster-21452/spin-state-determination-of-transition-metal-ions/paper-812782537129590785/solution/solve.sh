#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "CoH_D0": 51.5,
  "CoNH2_doublet_D0": 52.0,
  "CoNH2_quartet_D0": 66.7,
  "CoNH2_spin_gap": -14.7,
  "CoNH3_D0": 52.1
}
FFEOF
