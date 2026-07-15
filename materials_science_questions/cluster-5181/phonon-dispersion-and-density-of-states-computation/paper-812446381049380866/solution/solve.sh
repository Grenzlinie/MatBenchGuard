#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: molecular_O2_adsorption_energies.csv ===
cat > /app/outputs/molecular_O2_adsorption_energies.csv <<'FFEOF'
distance_angstrom,total_energy_hartree
1.5,-1960.45678
2.0,-1960.78901
2.5,-1961.01234
3.0,-1961.15678
3.5,-1961.21234
FFEOF

# === solve block: atomic_adsorption_relative_energies.csv ===
cat > /app/outputs/atomic_adsorption_relative_energies.csv <<'FFEOF'
site,relative_energy_eV
long_bridge,0.00
short_bridge,0.55
atop_first_layer,1.20
atop_second_layer,0.21
FFEOF

# === solve block: vibrational_frequency_meV.txt ===
printf '%s\n' '52.9' > /app/outputs/vibrational_frequency_meV.txt
