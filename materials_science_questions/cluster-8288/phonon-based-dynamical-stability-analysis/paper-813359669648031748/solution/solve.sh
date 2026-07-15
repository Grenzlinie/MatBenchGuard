#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_total_energies.csv ===
cat > "$OUTDIR/step_01_total_energies.csv" <<'EOF'
phase,total_energy_per_atom_meV
WC,0.0
AsNi,100.9
t-VN,162.5
NaCl,180.9
ZnS,310.9
CsCl,681.0
EOF

# === solve block: step_02_phonon_stability.csv ===
cat > "$OUTDIR/step_02_phonon_stability.csv" <<'EOF'
phase,has_imaginary_modes
NaCl,true
t-VN,false
AsNi,false
WC,false
EOF

# === solve block: step_03_NofEF.csv ===
cat > "$OUTDIR/step_03_NofEF.csv" <<'EOF'
structure_type,configuration,N_E_F
NaCl-based,V32N32,15.0
NaCl-based,V31N31,12.0
NaCl-based,V30N30,9.5
NaCl-based,V29N29,7.0
NaCl-based,V28N28,5.0
WC-based,V32N32,4.0
WC-based,V31N31,5.5
WC-based,V30N30,7.0
WC-based,V29N29,9.0
WC-based,V28N28,11.0
NaCl-based,V32N29C3,10.0
WC-based,V32N29C3,6.0
NaCl-based,V32N29O3,18.0
WC-based,V32N29O3,5.0
EOF
