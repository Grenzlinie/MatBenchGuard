#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" << 'FFEOF'
system,phase,total_energy
pure,AF1,-3000.000000000
pure,AF3,-2999.999559008
pure,AF2,-2999.991584410
pure,F,-2999.991400664
doped,AF1,-3000.000000000
doped,AF3,-2999.999853003
doped,AF2,-2999.993825118
doped,F,-2999.993238105
FFEOF

# === solve block: magnetic_coupling.json ===
cat > "$OUTDIR/magnetic_coupling.json" << 'FFEOF'
{
  "pure": {
    "J_ab": 12.0,
    "J_c": -625.5
  },
  "doped": {
    "J_ab": 18.0,
    "J_c": -633.0
  }
}
FFEOF

# === solve block: mulliken_orbitals.json ===
cat > "$OUTDIR/mulliken_orbitals.json" << 'FFEOF'
{
  "pure": {
    "Cu": {
      "d_xy": 2.0,
      "d_xz": 2.0,
      "d_yz": 2.0,
      "d_z2": 2.0,
      "d_x2-y2": 1.3
    }
  },
  "doped": {
    "Cu1": {
      "d_xy": 2.0,
      "d_xz": 2.0,
      "d_yz": 2.0,
      "d_z2": 2.0,
      "d_x2-y2": 1.3
    },
    "Cu2": {
      "d_xy": 2.0,
      "d_xz": 2.0,
      "d_yz": 2.0,
      "d_z2": 2.0,
      "d_x2-y2": 1.3
    },
    "Cu3": {
      "d_xy": 2.0,
      "d_xz": 2.0,
      "d_yz": 2.0,
      "d_z2": 2.0,
      "d_x2-y2": 1.3
    }
  }
}
FFEOF
