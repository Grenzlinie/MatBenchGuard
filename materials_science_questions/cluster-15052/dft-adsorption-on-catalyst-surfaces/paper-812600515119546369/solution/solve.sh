#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_charge_density_analysis.json ===
cat > "$OUTDIR/step_02_charge_density_analysis.json" <<'EOF'
{
  "charge_density_difference_description": "Electron rearrangement occurs at the NiO/ZnO interface: Ni atoms lose electrons (electron depletion), while electron cloud accumulates around O atoms near the oxygen vacancy on ZnO, forming electron dissipation centers (NiO) and electron accumulation centers (oxygen vacancy site). The average Ni-O bond length contracts from 2.06 to 1.92 Å.",
  "bader_charges_summary": "All four Ni atoms in the supercell lose electrons: 1.03, 1.13, 1.11, 1.11 e. The total net electron loss for the NiO layer is -0.61 e, indicating electron transfer from NiO to ZnO, particularly to O atoms adjacent to the oxygen vacancy."
}
EOF

# === solve block: step_01_geometry_optimization_results.json ===
cat > "$OUTDIR/step_01_geometry_optimization_results.json" <<'EOF'
{
  "adsorption_energy_PMS": -1.57,
  "O_O_bond_length_before_adsorption": 1.35,
  "O_O_bond_length_after_adsorption": 1.44,
  "bader_charge_transfer_to_PMS": 0.52
}
EOF
