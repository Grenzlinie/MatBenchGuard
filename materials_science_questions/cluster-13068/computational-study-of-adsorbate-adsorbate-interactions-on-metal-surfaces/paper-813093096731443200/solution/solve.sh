#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > /app/outputs/adsorption_energies.json <<'FFEOF'
{
  "terrace_monomer": -1.72,
  "terrace_rhombic_dimer": -1.96,
  "terrace_linear_dimer": -1.11,
  "step_monomer": -2.68,
  "step_rhombic_dimer": -3.06,
  "step_linear_dimer": -2.86
}
FFEOF
