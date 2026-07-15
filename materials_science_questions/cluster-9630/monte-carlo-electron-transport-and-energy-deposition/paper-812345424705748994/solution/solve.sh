#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: secondary_yield.csv ===
cat > /app/outputs/secondary_yield.csv <<'CEOF'
grain_material,grain_diameter_um,beam_energy_eV,secondary_yield
melamine_formaldehyde,2.35,1000,0.38
melamine_formaldehyde,2.35,2000,0.28
melamine_formaldehyde,2.35,5000,0.12
melamine_formaldehyde,2.35,10000,0.05
melamine_formaldehyde,9.78,1000,0.38
melamine_formaldehyde,9.78,2000,0.28
melamine_formaldehyde,9.78,5000,0.12
melamine_formaldehyde,9.78,10000,0.05
SiO2,1.2,1000,0.35
SiO2,1.2,2000,0.25
SiO2,1.2,5000,0.10
SiO2,1.2,10000,0.04
CEOF

# === solve block: grain_potential.csv ===
cat > /app/outputs/grain_potential.csv <<'CEOF'
grain_material,grain_diameter_um,beam_energy_eV,potential_V
melamine_formaldehyde,2.35,1000,2.6
melamine_formaldehyde,2.35,2000,2.0
melamine_formaldehyde,2.35,5000,1.2
melamine_formaldehyde,2.35,10000,3.5
melamine_formaldehyde,9.78,1000,2.1
melamine_formaldehyde,9.78,2000,1.2
melamine_formaldehyde,9.78,5000,0.0
melamine_formaldehyde,9.78,10000,0.0
SiO2,1.2,1000,1.7
SiO2,1.2,2000,0.9
SiO2,1.2,5000,0.0
SiO2,1.2,10000,2.2
CEOF

# === solve finalize ===
echo "All outputs written."
