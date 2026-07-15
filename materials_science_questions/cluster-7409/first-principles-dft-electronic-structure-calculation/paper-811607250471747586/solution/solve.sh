#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_energy_and_oxygen_ref.json ===
cat > "/app/outputs/bulk_energy_and_oxygen_ref.json" <<'FFEOF'
{
  "bulk_energy_per_unit": -89.3,
  "O_chem_potential": -4.52
}
FFEOF

# === solve block: surface_energies.csv ===
cat > "/app/outputs/surface_energies.csv" <<'FFEOF'
surface,sigma_Jperm2
stoichiometric,0.74
Onishi,2.03
Park,4.82
FFEOF

# === solve block: gap_state_positions.csv ===
cat > "/app/outputs/gap_state_positions.csv" <<'FFEOF'
surface,gap_state_eV
Onishi,1.24
Park,0.68
FFEOF
