#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
# Preamble: no installs, no downloads. OUTDIR must be set by the runner to /app/outputs.

# === solve block: dft_results.json ===
mkdir -p "$OUTDIR"
cat > "$OUTDIR/dft_results.json" << 'FFEOF'
{
  "coverage_data": [
    {
      "coverage": "1 ML",
      "E_ads_eV_per_atom": -2.40,
      "d_Ag_O_angstrom": 2.34,
      "Delta_phi_eV": 0.27,
      "mu_D": 1.12
    },
    {
      "coverage": "2 ML",
      "E_ads_eV_per_atom": -2.70,
      "d_Ag_O_angstrom": 2.39,
      "Delta_phi_eV": 1.15,
      "mu_D": 0.69
    },
    {
      "coverage": "4 ML",
      "E_ads_eV_per_atom": -2.94,
      "d_Ag_O_angstrom": 2.56,
      "Delta_phi_eV": 1.95,
      "mu_D": 0.0
    }
  ],
  "bader_charge_Ag_e": 0.1
}
FFEOF
