#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_shift.json ===
cat > "${OUTDIR}/step_01_shift.json" <<'FFEOF'
{
  "calculated_signal_wavelength_shift_nm": -2.2
}
FFEOF
