#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: li_adsorption_energies.json ===
cat > "$OUTDIR/li_adsorption_energies.json" <<'FFEOF'
{
  "bowl_C30H10_inner": -2.51,
  "flat_C30H14": -1.88,
  "C60_inner": -2.41,
  "C60_outer": -2.31,
  "C54N4_all_N5": -5.56,
  "C54N4_two_N5_two_N6": -6.03
}
FFEOF
