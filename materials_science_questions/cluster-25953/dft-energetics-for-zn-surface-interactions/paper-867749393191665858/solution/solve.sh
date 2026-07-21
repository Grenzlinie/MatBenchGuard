#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p ${OUTDIR}

# === solve block: adsorption_properties.json ===
cat > ${OUTDIR}/adsorption_properties.json <<'JSONEOF'
{
  "binding_energy_Zn_meV": 130,
  "Zn_H2_distance_A": 2.9,
  "O_site_closest_distance_A": 3.4,
  "rotational_transitions_Zn_meV": [10.6, 14.0, 21.6],
  "rotational_transitions_O_meV": [11.0, 15.6, 18.5],
  "translational_frequencies_Zn_meVps": [7.1, 15.2, 17.5],
  "translational_frequencies_O_meVps": [9.5, 14.5, 21.7],
  "effective_binding_energy_Zn_meV": 100,
  "effective_binding_energy_O_meV": 90
}
JSONEOF
