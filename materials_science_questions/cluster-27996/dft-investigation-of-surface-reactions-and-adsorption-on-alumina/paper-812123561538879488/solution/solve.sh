#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: dft_adsorption_energies.json ===
cat > "$OUTDIR/dft_adsorption_energies.json" <<'JSONEOF'
{
  "para": -37,
  "meta": -30,
  "ortho": -33
}
JSONEOF

# === solve block: van_der_waals_correction.json ===
cat > "$OUTDIR/van_der_waals_correction.json" <<'JSONEOF'
{
  "E_VdW": -95
}
JSONEOF

# === solve block: corrected_adsorption_energies.json ===
cat > "$OUTDIR/corrected_adsorption_energies.json" <<'JSONEOF'
{
  "para": -132,
  "meta": -125,
  "ortho": -128
}
JSONEOF
