#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
# Write the DFT results JSON
cat > "$OUTDIR/dft_results.json" <<'FFEOF'
{
  "pristine_CoN4_U": 0.83,
  "defect_CoN4_U": 1.00,
  "defect_O2_to_OOH_deltaG_at_0_83": -0.20
}
FFEOF
