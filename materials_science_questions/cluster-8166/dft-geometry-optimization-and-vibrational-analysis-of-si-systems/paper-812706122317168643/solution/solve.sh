#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: si5_adsorption_energies.csv ===
cat > "$OUTDIR/si5_adsorption_energies.csv" <<'EOF'
site,energy_eV
atop_capped,0.37
atop_side,1.15
short_bridge,1.78
long_bridge,1.20
EOF

# === solve block: si5_short_bridge_structure.csv ===
cat > "$OUTDIR/si5_short_bridge_structure.csv" <<'EOF'
parameter,value
C-C_bond_length,1.54
Si1-C_bond_length,1.94
Si4-C_bond_length,1.97
CH2_bend_angle,47.8
d1-2,2.34
d1-4,2.35
d4-5,3.66
EOF

# === solve block: si6_adsorption_energies.csv ===
cat > "$OUTDIR/si6_adsorption_energies.csv" <<'EOF'
site,energy_eV
atop_side,0.85
short_bridge,0.77
long_bridge,0.40
EOF

# === solve block: si7_adsorption_energy.csv ===
cat > "$OUTDIR/si7_adsorption_energy.csv" <<'EOF'
site,energy_eV
short_bridge,0.14
EOF
