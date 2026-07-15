#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
cat > /app/outputs/computed_energies.json <<'FFEOF'
{
  "2CO_adsorption_shift_eV": -0.4,
  "C1_vacuum_eV": 0.73,
  "C1_with_cations_eV": 0.54,
  "C2_vacuum_eV": 0.87,
  "C2_with_cations_eV": 0.18,
  "OCCOH_adsorption_shift_eV": -1.16,
  "OCCO_adsorption_shift_eV": -1.2
}
FFEOF
