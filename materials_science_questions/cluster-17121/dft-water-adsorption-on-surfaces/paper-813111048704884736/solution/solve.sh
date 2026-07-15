#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: oxygen_relative_energies.csv ===
printf '%b' 'termination,de\nI,0.00\nII,-50.00\nIII,-27.00\nIV,-32.00\nVI,80.00\nX,-20.00\n' > "$OUTDIR/oxygen_relative_energies.csv"

# === solve block: hydrogen_relative_energies.csv ===
cat > "$OUTDIR/hydrogen_relative_energies.csv" <<'FFEOF'
termination,de
bare_H1,10.57
bare_H2,46.83
bare_H3,40.92
chromyl_OH,-124.00
chromyl_H2O,-142.00
FFEOF

# === solve block: water_relative_energies.csv ===
cat > "$OUTDIR/water_relative_energies.csv" <<'FFEOF'
termination,de
Cr-O3-H-Cr-OH,-39.20
Cr-O3-H-Cr-OH(H2O),-91.10
Cr-O3-H-Cr-OH(H2O)2,-132.00
Cr-Cr-O2-H,9.77
Cr-Cr-O3-H3,-99.40
FFEOF

# === solve block: chemical_potential_crossings.json ===
cat > "$OUTDIR/chemical_potential_crossings.json" <<'FFEOF'
{
  "I_II_crossing": -1.0,
  "II_IV_crossing": 0.2
}
FFEOF
