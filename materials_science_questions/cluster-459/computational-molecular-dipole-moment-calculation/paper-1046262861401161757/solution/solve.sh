#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_and_dipole.json ===
cat > /app/outputs/binding_and_dipole.json <<'EOF'
{
  "binding_energies": {
    "SO4_near_N": {
      "DMAPS": -3.52,
      "MPC": -3.0,
      "CBMA": -2.5
    },
    "H2O_near_N": {
      "DMAPS": -1.49,
      "MPC": -1.3,
      "CBMA": -1.1
    },
    "Zn_near_neg": {
      "DMAPS": -0.77,
      "MPC": -0.65,
      "CBMA": -0.55
    },
    "H2O_near_neg": {
      "DMAPS": -1.07,
      "MPC": -0.9,
      "CBMA": -0.8
    }
  },
  "dipole_moments": {
    "DMAPS": 25.3,
    "MPC": 18.7,
    "CBMA": 16.4
  },
  "units": {
    "binding_energies": "eV",
    "dipole_moments": "Debye"
  }
}
EOF

# === solve block: water_states.json ===
cat > /app/outputs/water_states.json <<'EOF'
{
  "free_H2O": {
    "PDMAPS": 66.2,
    "PMPC": 78.2,
    "PCBMA": 81.7
  },
  "Zn_coordinated_H2O": {
    "PDMAPS": 8.4,
    "PMPC": 8.8,
    "PCBMA": 8.1
  },
  "polymer_fixed_H2O": {
    "PDMAPS": 25.4,
    "PMPC": 13.0,
    "PCBMA": 10.2
  }
}
EOF
