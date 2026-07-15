#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_constants.json ===
cat > "$OUTDIR/lattice_constants.json" <<'FFEOF'
{
  "a_nm": 0.48,
  "c_nm": 0.327
}
FFEOF

# === solve block: band_gap.json ===
cat > "$OUTDIR/band_gap.json" <<'FFEOF'
{
  "band_gap_eV": 3.1
}
FFEOF

# === solve block: transport_summary.json ===
cat > "$OUTDIR/transport_summary.json" <<'FFEOF'
{
  "relaxation_time_s": 7.36e-16,
  "n_type_600K": {
    "Seebeck_peak_uVK": -2336
  },
  "p_type_600K": {
    "Seebeck_peak_uVK": 2391
  },
  "900K": {
    "n_type": {
      "chem_pot_eV": 1.63,
      "carrier_conc_cm3": 8.77e19,
      "Seebeck_uVK": -160,
      "sigma_Ohmm": 3400,
      "power_factor_WmK2": 0.0000876,
      "ZT_e": 1.0
    },
    "p_type": {
      "chem_pot_eV": -1.62,
      "carrier_conc_cm3": 1.2e20,
      "Seebeck_uVK": 180,
      "sigma_Ohmm": 6500,
      "power_factor_WmK2": 0.00021,
      "ZT_e": 1.0
    }
  }
}
FFEOF
