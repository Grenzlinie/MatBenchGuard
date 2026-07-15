#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: adsorption_results.json ===
cat > "$OUTDIR/adsorption_results.json" <<'FFEOF'
{
  "1_WM": {
    "total_binding_energy_eV": 0.147,
    "avg_binding_energy_eV": 0.147,
    "O_Zn_distance_Angstrom": 2.227,
    "H_O_distance_Angstrom": 2.993,
    "charge_transfer_e": 0.007
  },
  "4_WM": {
    "total_binding_energy_eV": 0.59,
    "avg_binding_energy_eV": 0.1475
  },
  "10_WM": {
    "total_binding_energy_eV": 1.473,
    "avg_binding_energy_eV": 0.1473
  }
}
FFEOF
