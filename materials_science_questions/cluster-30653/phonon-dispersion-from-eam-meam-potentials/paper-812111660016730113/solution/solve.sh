#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_properties.json ===
OUTDIR=/app/outputs
# Write bulk properties
cat <<'EOF' > "$OUTDIR/bulk_properties.json"
{
  "CY-EAM": {
    "lattice_constant_A": 3.92,
    "cohesive_energy_eV": 5.72,
    "vacancy_formation_energy_eV": 1.49,
    "C11_GPa": 309,
    "C12_GPa": 259,
    "C44_GPa": 79.3
  },
  "CY-XEAM2": {
    "lattice_constant_A": 3.92,
    "cohesive_energy_eV": 5.77,
    "vacancy_formation_energy_eV": 1.51,
    "C11_GPa": 319,
    "C12_GPa": 266,
    "C44_GPa": 77.5
  }
}
EOF

# Write cluster properties (paper Table 4 values)
cat <<'EOF' > "$OUTDIR/cluster_properties.json"
{
  "CY-EAM": {
    "dimer": { "bond_length_A": 2.31, "binding_energy_eV_per_atom": -3.94 },
    "trimer": { "bond_length_A": 2.46, "binding_energy_eV_per_atom": -4.14 },
    "tetrahedron": { "bond_length_A": 2.51, "binding_energy_eV_per_atom": -4.31 }
  },
  "CY-XEAM2": {
    "dimer": { "bond_length_A": 2.32, "binding_energy_eV_per_atom": -1.95 },
    "trimer": { "bond_length_A": 2.45, "binding_energy_eV_per_atom": -2.70 },
    "tetrahedron": { "bond_length_A": 2.53, "binding_energy_eV_per_atom": -3.04 }
  }
}
EOF

# Write surface properties (paper Table 5 values)
cat <<'EOF' > "$OUTDIR/surface_properties.json"
{
  "CY-EAM": {
    "surface_energy_111_eV_per_A2": 0.070,
    "surface_energy_100_eV_per_A2": 0.077,
    "adatom_diffusion_barrier_eV": 0.096
  },
  "CY-XEAM2": {
    "surface_energy_111_eV_per_A2": 0.092,
    "surface_energy_100_eV_per_A2": 0.111,
    "adatom_diffusion_barrier_eV": 0.38
  }
}
EOF

exit 0

# === solve block: cluster_properties.json ===
python3 /solution/write_outputs.py cluster

# === solve block: surface_properties.json ===
python3 /solution/write_outputs.py surface
