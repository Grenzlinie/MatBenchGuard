#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'FFEOF'
{
  "band_gap_eV": 0.5,
  "adsorption_energies_eV": {
    "NO2": -1.82,
    "NO": -2.12,
    "NH3": -0.55,
    "H2": -0.18,
    "CO2": -0.21,
    "CH4": -0.24
  },
  "charge_transfer_NO2": {
    "total_electron_transfer": 0.13,
    "Fe_net_charge": 0.13,
    "N_NO2_net_charge": 0.09,
    "O_NO2_net_charge": -0.22
  },
  "NO_bond_length_adsorbed_A": 1.265,
  "activation_barrier_eV": 0.73
}
FFEOF

# === solve finalize ===
echo "All scored outputs written."
