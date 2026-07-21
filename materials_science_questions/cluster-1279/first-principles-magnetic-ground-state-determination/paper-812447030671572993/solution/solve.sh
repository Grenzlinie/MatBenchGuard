#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: coupling_energies.csv ===
cat > "$OUTDIR/coupling_energies.csv" << 'EOFMARK'
system,n,delta_E
Fe-V,1,12.3
Fe-V,2,-5.2
Fe-V,3,0.8
Fe-V,4,-0.3
Fe-V,5,0.1
Co-Ru,1,-15.0
Co-Ru,2,7.5
Co-Ru,3,-3.0
Co-Ru,4,1.0
Co-Ru,5,-0.2
Co-Ru,6,0.05
Co-Pd,1,8.0
Co-Pd,2,3.0
Co-Pd,3,1.2
Co-Pd,4,0.5
Co-Pd,5,0.2
Fe-Cr,1,-25.0
Fe-Cr,2,5.0
Fe-Cr,3,-20.0
Fe-Cr,4,4.0
Fe-Cr,5,-18.0
EOFMARK
