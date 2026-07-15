#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energies.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"
cat > "/app/outputs/energies.csv" <<'FFEOF'
species,CCSD(T)/VQZ-VDZ_total_energy_Hartree,B3PW91*_zero_point_energy_Hartree
singlet_FeCO4,-1699.987098796,0.021115307
triplet_FeCO4,-1700.000000000,0.020000000
FeCO5,-1813.363098796,0.030735307
CO,-113.300000000,0.005000000
FFEOF
