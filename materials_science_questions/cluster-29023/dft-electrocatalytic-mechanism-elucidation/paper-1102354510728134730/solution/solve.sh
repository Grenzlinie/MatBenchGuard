#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: free_energy_profiles.json ===
cat > "$OUTDIR/free_energy_profiles.json" <<'FFEOF'
{
  "OO_adsorption_on_Nplus_delta_G_eV": -0.906,
  "ORR": [
    {"species": "*O2", "delta_G_eV": -0.2},
    {"species": "*OO*", "delta_G_eV": -0.906},
    {"species": "H2O2", "delta_G_eV": -1.5}
  ],
  "WOR": [
    {"species": "H2O", "delta_G_eV": 0.0},
    {"species": "*OH", "delta_G_eV": 1.5},
    {"species": "H2O2", "delta_G_eV": 2.0}
  ],
  "ORR_downhill": true,
  "WOR_uphill_steps": true
}
FFEOF
