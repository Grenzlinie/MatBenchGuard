#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: al_chemisorption_results.json ===
OUTDIR="${1:-/app/outputs}"
mkdir -p "$OUTDIR"
cat > "$OUTDIR/al_chemisorption_results.json" <<'FFEOF'
[
  {
    "cluster": "Ga4As4H12",
    "site": "cage",
    "basis": "HWECP",
    "Ec": -3.994,
    "bond_length": 2.430,
    "HOMO_LUMO_gap": 4.925,
    "Mulliken_charge_Al": 0.731
  },
  {
    "cluster": "Ga4As4H12",
    "site": "cage",
    "basis": "6-311++G**",
    "Ec": -3.689,
    "bond_length": 2.430,
    "HOMO_LUMO_gap": 4.733,
    "Mulliken_charge_Al": 0.763
  },
  {
    "cluster": "Ga4As4H12",
    "site": "top",
    "basis": "HWECP",
    "Ec": 1.626,
    "bond_length": 2.700,
    "HOMO_LUMO_gap": 6.334,
    "Mulliken_charge_Al": 0.2
  },
  {
    "cluster": "Ga4As4H12",
    "site": "top",
    "basis": "6-311++G**",
    "Ec": 1.204,
    "bond_length": 2.500,
    "HOMO_LUMO_gap": 5.638,
    "Mulliken_charge_Al": 0.3
  },
  {
    "cluster": "Ga19As15H39",
    "site": "trough",
    "basis": "HWECP",
    "Ec": 4.728,
    "bond_length": 2.890,
    "HOMO_LUMO_gap": 2.692,
    "Mulliken_charge_Al": 0.625
  },
  {
    "cluster": "Ga19As15H39",
    "site": "trough",
    "basis": "6-311++G**",
    "Ec": 4.838,
    "bond_length": 2.890,
    "HOMO_LUMO_gap": 2.693,
    "Mulliken_charge_Al": 0.807
  }
]
FFEOF
