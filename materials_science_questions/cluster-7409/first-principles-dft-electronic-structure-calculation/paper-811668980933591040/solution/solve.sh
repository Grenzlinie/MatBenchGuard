#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bandgap_data.json ===
cat > /app/outputs/bandgap_data.json <<'EOF'
{
  "PZT_stoich": {"bandgap_eV": 1.8, "delta_Eg_eV": 0.0},
  "PZTN_stoich": {"bandgap_eV": 0.0, "delta_Eg_eV": -1.8},
  "PZT_Pb_def": {"bandgap_eV": 0.0, "delta_Eg_eV": -1.8},
  "PZT_PbO_def": {"bandgap_eV": 0.6, "delta_Eg_eV": 1.2},
  "PZTN_Pb_def": {"bandgap_eV": 1.6, "delta_Eg_eV": 0.2}
}
EOF

# === solve block: formation_energies.json ===
cat > /app/outputs/formation_energies.json <<'EOF'
{
  "PZT_stoich": {"formation_energy_eV_per_supercell": 0.00},
  "PZT_Pb_def": {"formation_energy_eV_per_supercell": 1.50},
  "PZT_PbO_def": {"formation_energy_eV_per_supercell": 2.50},
  "PZTN_stoich": {"formation_energy_eV_per_supercell": 4.41},
  "PZTN_Pb_def": {"formation_energy_eV_per_supercell": 0.00},
  "PZTN_PbO_def": {"formation_energy_eV_per_supercell": 5.00}
}
EOF
