#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_oer_energies.json ===
cat > "$OUTDIR/dft_oer_energies.json" <<'FFEOF'
{
  "systems": {
    "MIL-59(Fe)@Fe": [1.33, 1.34, 0.40, 1.84],
    "MIL-59(Ni)@Ni": [1.46, 1.87, -0.30, 1.89],
    "MIL-59(FeNi)@Fe": [1.07, 1.66, 0.39, 1.80],
    "MIL-59(FeNi)@Ni": [1.61, 2.01, -0.67, 1.97]
  },
  "rate_determining_step_barriers": {
    "MIL-59(Fe)@Fe": 1.84,
    "MIL-59(Ni)@Ni": 1.89,
    "MIL-59(FeNi)@Fe": 1.80,
    "MIL-59(FeNi)@Ni": 1.97
  },
  "mulliken_charge_difference_fe_ooH": 0.01
}
FFEOF
