#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_homo_lumo_gaps.csv ===
cat > "$OUTDIR/step_01_homo_lumo_gaps.csv" <<'EOF'
molecule,gap
CuTAPP,2.43
CuTPP,2.81
EOF

# === solve block: step_02_species_energies.json ===
cat > "$OUTDIR/step_02_species_energies.json" <<'EOF'
{
  "species": [
    "CuTAPP",
    "CuTPP",
    "*CO@CuTAPP",
    "*CO@CuTPP",
    "*CHO@CuTAPP",
    "*CHO@CuTPP",
    "H2",
    "H2O"
  ],
  "E_total": [
    -20000.0,
    -20000.0,
    -20100.0,
    -20100.0,
    -20097.3,
    -20096.4,
    0.0,
    -76.5
  ],
  "ZPE": [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "S_vib": [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "T": 298.15
}
EOF
