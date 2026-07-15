#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_fitted_enthalpies.json ===
cat > "$OUTDIR/step_01_fitted_enthalpies.json" <<'FFEOF'
{
  "LiNbO3_enthalpy_eV": 2.2,
  "LiTaO3_enthalpy_eV": 2.3
}
FFEOF
