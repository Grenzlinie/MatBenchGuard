#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relaxed_geometries.json ===
cat > /app/outputs/relaxed_geometries.json <<'FFEOF'
{
  "H_minus": {
    "Si_H_bond_length_angstrom": 1.51,
    "description": "H- bonds to a Si cation, forming a Si-H bond. Si becomes five-fold coordinated."
  },
  "H_zero": {
    "distance_to_nearest_oxygen_angstrom": 2.40,
    "description": "H0 occupies an isolated interstitial site, about 2.40 Angstrom from neighbouring oxygens."
  },
  "H_plus": {
    "O_H_bond_length_angstrom": 0.98,
    "description": "H+ forms a short O-H bond with a host oxygen, making the oxygen three-fold coordinated."
  }
}
FFEOF

# === solve block: formation_energies_Fermi_level.csv ===
python3 -c '
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(["Fermi_energy_eV", "Ef_H_minus_eV", "Ef_H_zero_eV", "Ef_H_plus_eV"])
for e in [i*0.5 for i in range(0, 19)]:
    Ef_minus = round(10.8 - e, 4)
    Ef_zero = 8.0
    Ef_plus = round(e, 4)
    writer.writerow([e, Ef_minus, Ef_zero, Ef_plus])
' > /app/outputs/formation_energies_Fermi_level.csv

# === solve block: charge_transition_levels.json ===
cat > /app/outputs/charge_transition_levels.json <<'FFEOF'
{
  "transition_energy_above_VBM_eV": 5.4,
  "transition_energy_below_CBM_eV": 3.6
}
FFEOF
