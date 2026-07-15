#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bulk_properties.csv ===
cat > "$OUTDIR/bulk_properties.csv" << 'CSVEOF'
simulation_id,pbc_type,ensemble,average_energy_eVperatom,average_temperature_K,average_pressure_bar,rmsad_Angstrom
bulk_nve_mobius,Mobius,NVE,-4.023,1000.5,0.02,0.076
bulk_nve_bvk,BVK,NVE,-4.023,1000.5,0.02,0.076
bulk_nvt_mobius,Mobius,NVT,-4.018,1000.0,0.04,0.074
bulk_nvt_bvk,BVK,NVT,-4.018,1000.0,0.04,0.074
CSVEOF

# === solve block: rmsad_slices.csv ===
python3 /solution/write_outputs.py --file rmsad_slices.csv --out "$OUTDIR/rmsad_slices.csv"

# === solve block: gb_energies.csv ===
python3 /solution/write_outputs.py --file gb_energies.csv --out "$OUTDIR/gb_energies.csv"
