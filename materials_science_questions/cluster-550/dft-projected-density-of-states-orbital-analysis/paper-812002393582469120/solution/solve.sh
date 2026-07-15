#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: heats_of_formation.json ===
cat > "$OUTDIR/heats_of_formation.json" << 'EOF'
[
  {"composition": "Sr2Si", "prototype": "oP12", "value_kJ_per_mol_at": -37.6},
  {"composition": "Sr5Si3", "prototype": "tI32-Cr5B3", "value_kJ_per_mol_at": -40.2},
  {"composition": "SrSi", "prototype": "oC8", "value_kJ_per_mol_at": -46.7},
  {"composition": "SrSi2", "prototype": "cP12", "value_kJ_per_mol_at": -35.8}
]
EOF

# === solve block: transition_pressures.json ===
cat > "$OUTDIR/transition_pressures.json" << 'EOF'
[
  {"phase": "Sr2Si", "from_lattice": "oP12", "to_lattice": "hP6", "pressure_GPa": 5.5},
  {"phase": "Sr5Si3", "from_lattice": "tI32-Cr5B3", "to_lattice": "tI32-Mo5Si3", "pressure_GPa": 19.9},
  {"phase": "SrSi", "from_lattice": "oC8", "to_lattice": "oP8", "pressure_GPa": 11.8},
  {"phase": "SrSi", "from_lattice": "oP8", "to_lattice": "tP2", "pressure_GPa": 60.0}
]
EOF

# === solve block: electronic_properties.json ===
cat > "$OUTDIR/electronic_properties.json" << 'EOF'
{
  "band_gap_Sr2Si_eV": 0.29,
  "charge_transfer": [
    {"phase": "Sr2Si", "Sr_charge": 1.48, "Si_charge": -2.97, "ionic_percent": 74},
    {"phase": "Sr5Si3", "Sr_charge": 1.52, "Si_charge": -2.53, "ionic_percent": 76},
    {"phase": "SrSi", "Sr_charge": 1.38, "Si_charge": -1.38, "ionic_percent": 69},
    {"phase": "SrSi2", "Sr_charge": 1.94, "Si_charge": -0.97, "ionic_percent": 97}
  ]
}
EOF
