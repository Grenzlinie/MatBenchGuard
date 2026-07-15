#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: monolayer_properties.json ===
cat > /app/outputs/monolayer_properties.json <<'FFEOF'
{
  "As": {"lattice_constant_A": 3.607, "bond_length_A": 2.506, "bandgap_eV": 2.234, "gap_type": "indirect"},
  "GaS": {"lattice_constant_A": 3.624, "bond_length_A": 2.360, "bandgap_eV": 3.279, "gap_type": "indirect"},
  "GaSe": {"lattice_constant_A": 3.803, "bond_length_A": 2.690, "bandgap_eV": 2.751, "gap_type": "indirect"}
}
FFEOF

# === solve block: heterostructure_properties.json ===
cat > /app/outputs/heterostructure_properties.json <<'FFEOF'
{
  "As/GaS": {
    "binding_energy_meV_per_Ang2": -28.5,
    "interlayer_distance_A": 3.803,
    "bandgap_eV": 1.852,
    "CBM_energy_eV": -4.05,
    "VBM_energy_eV": -5.902,
    "CBO_eV": 0.341,
    "VBO_eV": 0.110,
    "bader_charge_transfer_e": 0.0081,
    "potential_drop_eV": 4.215,
    "typeII_confirmed": true
  },
  "As/GaSe": {
    "binding_energy_meV_per_Ang2": -59.2,
    "interlayer_distance_A": 3.291,
    "bandgap_eV": 2.120,
    "CBM_energy_eV": -3.85,
    "VBM_energy_eV": -5.97,
    "CBO_eV": 1.255,
    "VBO_eV": 1.654,
    "bader_charge_transfer_e": 0.0101,
    "potential_drop_eV": 1.317,
    "typeII_confirmed": true
  }
}
FFEOF

# === solve block: st_hydrogen_efficiency.json ===
cat > /app/outputs/st_hydrogen_efficiency.json <<'FFEOF'
{
  "As": {"eta_abs": 36.42, "eta_cu": 28.40, "eta_STH": 10.34},
  "GaS": {"eta_abs": 10.42, "eta_cu": 34.78, "eta_STH": 3.61},
  "GaSe": {"eta_abs": 28.64, "eta_cu": 38.95, "eta_STH": 11.13},
  "As/GaS": {"eta_abs": 73.88, "eta_cu": 34.55, "eta_STH": 25.46},
  "As/GaSe": {"eta_abs": 60.92, "eta_cu": 40.92, "eta_STH": 24.91}
}
FFEOF
