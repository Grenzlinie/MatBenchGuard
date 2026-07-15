#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_structure.json ===
cat > "$OUTDIR/step_01_structure.json" <<'EOF'
{
  "phase": "1T",
  "lattice_constant_a": 3.47,
  "bond_length_Fe_Cl": 2.45,
  "bond_length_Cl_Cl": 2.84,
  "angle_Cl_Fe_Cl": 90.15,
  "total_magnetic_moment": 4.0,
  "Bader_charge_Fe": -1.20,
  "Bader_charge_Cl": 0.60,
  "cohesive_energy_per_atom": 2.64,
  "total_energy": -30.0
}
EOF

# === solve block: step_04_band_gap.json ===
cat > "$OUTDIR/step_04_band_gap.json" <<'EOF'
{
  "minority_gap": 4.4,
  "majority_has_bands_at_Fermi": true
}
EOF

# === solve block: step_02_phonon_frequencies.json ===
cat > "$OUTDIR/step_02_phonon_frequencies.json" <<'EOF'
[
  {"branch": "ZA",  "frequency": 0.0,  "Raman_active": false, "IR_active": false},
  {"branch": "TA",  "frequency": 0.0,  "Raman_active": false, "IR_active": false},
  {"branch": "LA",  "frequency": 0.0,  "Raman_active": false, "IR_active": false},
  {"branch": "E'",  "frequency": 130.0, "Raman_active": true,  "IR_active": false},
  {"branch": "E'",  "frequency": 130.0, "Raman_active": true,  "IR_active": false},
  {"branch": "E'",  "frequency": 179.0, "Raman_active": true,  "IR_active": false},
  {"branch": "E'",  "frequency": 179.0, "Raman_active": true,  "IR_active": false},
  {"branch": "A1'", "frequency": 237.0, "Raman_active": true,  "IR_active": false},
  {"branch": "A2''","frequency": 279.0, "Raman_active": false, "IR_active": true}
]
EOF

# === solve block: step_03_magnetic_energy.json ===
cat > "$OUTDIR/step_03_magnetic_energy.json" <<'EOF'
{
  "energy_FM": -120.0,
  "energy_AFM": -119.628,
  "energy_difference_per_primitive_cell": 93.0,
  "exchange_parameter_J": 0.97,
  "Curie_temperature": 17.0
}
EOF

# === solve finalize ===
echo "All artifacts written successfully."
