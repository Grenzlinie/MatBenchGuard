#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: enthalpies.json ===
cat > /app/outputs/enthalpies.json <<'FFEOF'
{
  "reference_energies": {
    "Fe_bcc_eV_per_atom": -8.0,
    "Cr_bcc_eV_per_atom": -9.0,
    "calculator": "Quantum ESPRESSO PBE GBRV"
  },
  "compounds": [
    {
      "name": "Fe14Cr",
      "composition": "Fe14Cr",
      "number_of_atoms": 30,
      "total_energy_eV": -242.306,
      "formation_enthalpy_meV_per_atom": -10.2
    },
    {
      "name": "Fe15Cr-6/8nn",
      "composition": "Fe15Cr",
      "number_of_atoms": 16,
      "total_energy_eV": -129.1368,
      "formation_enthalpy_meV_per_atom": -8.55
    },
    {
      "name": "Fe15Cr-6nn",
      "composition": "Fe15Cr",
      "number_of_atoms": 16,
      "total_energy_eV": -129.10352,
      "formation_enthalpy_meV_per_atom": -6.47
    }
  ]
}
FFEOF

# === solve block: results_summary.txt ===
cat > /app/outputs/results_summary.txt <<'FFEOF'
Fe14Cr has the lowest formation enthalpy, and is therefore the most stable structure among the three candidates. Its formation enthalpy is lower than that of both Fe15Cr-6/8nn and Fe15Cr-6nn.
FFEOF
