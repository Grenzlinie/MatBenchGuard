#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: nhc_properties.json ===
cat > "$OUTDIR/nhc_properties.json" <<'FFEOF'
{
  "homo_lumo_gap_kcal_mol": 138.4,
  "casscf_b3b1_energy_kcal_mol": 92.8,
  "casscf_b1b1_energy_kcal_mol": 139.2
}
FFEOF

# === solve block: sigma_bde.csv ===
cat > "$OUTDIR/sigma_bde.csv" <<'FFEOF'
TM,multiplicity_gs,BDE_B3LYP,BDE_CCSDT
Sc,2,20.5,16.6
Ti,3,21.4,18.7
V,6,26.0,14.0
Cr,7,14.4,14.6
Mn,6,0.6,0.5
Fe,3,11.3,34.6
Co,2,21.9,12.1
Ni,1,29.7,34.0
Cu,2,24.3,25.7
Zn,1,1.4,5.0
FFEOF
