#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: bulk_properties.csv ===
cat > "$OUTDIR/bulk_properties.csv" <<'EOF'
material,a0_angstrom,mu_muB,easy_axis,E_g_ind_eV,E_g_dir_eV
MnO,4.37,4.53,"(111) plane",1.9,2.6
FeO,4.24,4.34,"[111]",2.0,2.6
CoO,4.15,3.69,"~[-1-1 1.5], [-110]",2.1,2.3
NiO,4.07,1.71,"(111) plane",2.2,2.7
EOF
