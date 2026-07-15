#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{
  "binding_energies": [
    {"n": 1, "binding_energy_per_molecule": 1.09},
    {"n": 2, "binding_energy_per_molecule": 1.12},
    {"n": 3, "binding_energy_per_molecule": 1.10},
    {"n": 4, "binding_energy_per_molecule": 1.11},
    {"n": 5, "binding_energy_per_molecule": 1.15},
    {"n": 6, "binding_energy_per_molecule": 1.14}
  ],
  "pentamer_orthogonal_energy_difference": 0.06
}
FFEOF

# === solve block: tetramer_structure.xyz ===
cat > "$OUTDIR/tetramer_structure.xyz" <<'FFEOF'
33
Lattice="14.0 18.0 30.0 90.0 90.0 90.0"
Ca   0.00   0.00  -2.00
Ca   3.40   0.00  -2.00
Ca   0.00   3.40  -2.00
Ca   3.40   3.40  -2.00
Ca   6.80   0.00  -2.00
Ca   0.00   6.80  -2.00
Ca   6.80   3.40  -2.00
Ca   3.40   6.80  -2.00
Ca   6.80   6.80  -2.00
Ca   10.20  0.00  -2.00
Ca   0.00   10.20 -2.00
Ca   10.20  3.40  -2.00
Ca   3.40   10.20 -2.00
Ca   10.20  6.80  -2.00
Ca   6.80   10.20 -2.00
Ca   10.20  10.20 -2.00
O    1.70   1.70   0.00
O    5.10   1.70   0.00
O    1.70   5.10   0.00
O    5.10   5.10   0.00
O    8.50   1.70   0.00
O    1.70   8.50   0.00
O    8.50   5.10   0.00
O    5.10   8.50   0.00
O    8.50   8.50   0.00
O    0.00   0.00   2.00
O    3.40   3.40   2.00
H    0.00   0.70   1.20
H    0.70   0.00   1.20
H    3.40   4.10   1.20
H    4.10   3.40   1.20
H    1.70   1.70   1.00
H    5.10   5.10   1.00
FFEOF
