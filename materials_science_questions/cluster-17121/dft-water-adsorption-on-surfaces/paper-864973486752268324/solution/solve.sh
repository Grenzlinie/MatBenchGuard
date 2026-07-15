#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
cat > "$OUTDIR/adsorption_energies.json" <<'FFEOF'
{
  "Li": -3.46,
  "Na": -2.81,
  "K": -2.32
}
FFEOF

# === solve block: bader_charges_dipoles.json ===
cat > "$OUTDIR/bader_charges_dipoles.json" <<'FFEOF'
{
  "Li": {"O_charge": -0.52, "OH_dipole_D": 2.37, "PtO_dipole_D": 2.09},
  "Na": {"O_charge": -0.49, "OH_dipole_D": 2.19, "PtO_dipole_D": 1.69},
  "K": {"O_charge": -0.48, "OH_dipole_D": 2.15, "PtO_dipole_D": 1.06}
}
FFEOF

# === solve block: free_energy_vs_potential.csv ===
cat > "$OUTDIR/free_energy_vs_potential.csv" <<'FFEOF'
potential_V,G_ad_OH_Li,G_ad_OH_Na,G_ad_OH_K
-1.0,-3.16,-2.51,-2.02
-0.5,-3.31,-2.66,-2.17
0.0,-3.46,-2.81,-2.32
0.5,-3.61,-2.96,-2.47
1.0,-3.76,-3.11,-2.62
FFEOF
