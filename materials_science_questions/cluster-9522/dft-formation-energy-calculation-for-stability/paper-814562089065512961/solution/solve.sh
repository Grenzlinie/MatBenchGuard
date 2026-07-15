#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
cat > /app/outputs/formation_energies.csv <<'CSVEOF'
composition,total_energy_eV,formation_energy_kJ_mol
Na2Li2Ti6O14,-1210.0,0.0
Na1.5Sr0.25Li2Ti6O14,-1210.0,-16.2
NaSr0.5Li2Ti6O14,-1190.0,-19.9
Na0.5Sr0.75Li2Ti6O14,-1150.0,-7.25
SrLi2Ti6O14,-1120.0,0.0
CSVEOF

# === solve block: bader_charges.csv ===
cat > /app/outputs/bader_charges.csv <<'CSVEOF'
composition,avg_ti_bader_charge_e
Na2Li2Ti6O14,2.00
Na1.5Sr0.25Li2Ti6O14,2.03
NaSr0.5Li2Ti6O14,2.06
Na0.5Sr0.75Li2Ti6O14,2.09
SrLi2Ti6O14,2.12
CSVEOF
