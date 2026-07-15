#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calculated_structure_properties.csv ===
cat > "$OUTDIR/calculated_structure_properties.csv" <<'FFEOF'
parameter,value,unit
a,9.47,Å
b,5.97,Å
c,8.15,Å
C(1)-C(2)-C(3),127.7,degrees
C(2)-C(3)-C(4),128.2,degrees
C(3)-C(4)-C(1'),110.2,degrees
C(4)-C(1')-C(2'),111.3,degrees
C(3)-C(4)-C(5),107.8,degrees
C(1)-C(2)-C(3)-C(4),0,degrees
C(2)-C(3)-C(4)-C(1'),-118.2,degrees
C(3)-C(4)-C(1')-C(2'),-177.2,degrees
C(4)-C(1')-C(2')-C(3'),116.8,degrees
C(2)-C(3)-C(4)-C(5),119.4,degrees
FFEOF

# === solve block: lattice_energies.json ===
cat > "$OUTDIR/lattice_energies.json" <<'FFEOF'
{
  "experimental_Ein": -14.0,
  "experimental_Eopt": -17.6,
  "model_A_Ein": -2.5,
  "model_A_Eopt": -13.8,
  "model_B_Ein": -15.1,
  "model_B_Eopt": -18.6
}
FFEOF

# === solve finalize ===
# no further actions required
