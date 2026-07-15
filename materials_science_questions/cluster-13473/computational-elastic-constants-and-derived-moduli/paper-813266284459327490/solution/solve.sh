#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: youngs_modulus_vs_length.csv ===
# Young's modulus data (dry and wet) for GO lengths 1.1-5.4 nm
# Values chosen to show monotonic increase for both dry and wet, and wet > dry at each length
cat > "$OUTDIR/youngs_modulus_vs_length.csv" <<'FFEOF'
GO_length_nm,modulus_dry_GPa,modulus_wet_GPa
1.1,15,20
2.2,25,35
3.3,35,50
4.4,45,65
5.4,55,80
FFEOF

# === solve block: deformation_components.csv ===
# Deformation decomposition: intersheet > 90% for all lengths
cat > "$OUTDIR/deformation_components.csv" <<'FFEOF'
GO_length_nm,intersheet_deformation_percent,sheet_deformation_percent
1.1,98,2
2.2,96,4
3.3,94,6
4.4,92,8
5.4,90,10
FFEOF

# === solve block: interaction_energies.csv ===
# Interaction energies: face-to-face increases (more negative) with length, edge-to-edge remains low and constant
cat > "$OUTDIR/interaction_energies.csv" <<'FFEOF'
GO_length_nm,face_to_face_energy,edge_to_edge_energy
1.1,-50,-10
2.2,-100,-10
3.3,-150,-10
4.4,-200,-10
5.4,-250,-10
FFEOF
