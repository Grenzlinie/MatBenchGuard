#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_magnetic.csv ===
cat > $OUTDIR/structural_magnetic.csv <<'EOF'
compound,a0_angstrom,B0_GPa,deltaH_eV,total_magnetic_moment_mu_B,exchange_constant_N0alpha_eV,exchange_constant_N0beta_eV
HgCr2S4,10.37,90.15,-0.98,6.0,-0.34,0.26
HgCr2Se4,10.89,72.83,-0.84,6.0,-0.30,0.22
EOF

# === solve block: transport_properties.csv ===
# Write transport_properties.csv
cat > /app/outputs/transport_properties.csv <<'EOF'
compound,temperature_K,Seebeck_uV_K,power_factor_arb_units
HgCr2S4,200,170,5.5
HgCr2S4,400,240,12.0
HgCr2S4,600,290,20.0
HgCr2Se4,200,120,3.5
HgCr2Se4,400,180,7.5
HgCr2Se4,600,230,11.0
EOF

# === solve finalize ===
echo "Oracle artifacts written successfully"
