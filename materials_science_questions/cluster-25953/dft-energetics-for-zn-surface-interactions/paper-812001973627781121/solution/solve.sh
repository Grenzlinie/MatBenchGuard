#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > "/app/outputs/adsorption_energies.json" <<'FFEOF'
{
  "N_Znface": -21.65,
  "N_Oface": -21.75,
  "In_Znface": -20.08,
  "In_Oface": -20.05
}
FFEOF
