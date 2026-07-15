#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_structural.csv ===
cat > "$OUTDIR/step_01_structural.csv" <<'EOF'
material,a_A,B_GPa,B_prime,E_coh_eV_per_atom
HoAs,5.80,76.75,3.88,6.37
HoP,5.64,86.57,3.70,7.20
EOF

# === solve block: step_02_elastic.csv ===
cat > "$OUTDIR/step_02_elastic.csv" <<'EOF'
material,C11_GPa,C12_GPa,C44_GPa
HoAs,114.27,57.99,10.68
HoP,126.89,66.41,12.71
EOF

# === solve block: step_03_derived_elastic.csv ===
cat > "$OUTDIR/step_03_derived_elastic.csv" <<'EOF'
material,A,nu,E_GPa,G_GPa
HoAs,0.38,0.40,44.71,15.93
HoP,0.42,0.40,50.85,18.13
EOF

# === solve block: step_04_thermodynamic.csv ===
cat > "$OUTDIR/step_04_thermodynamic.csv" <<'EOF'
material,Cv_300K_J_per_mol_K,Debye_T_0K_K,gamma_0K
HoAs,49.16,165.74,1.905
HoP,48.90,192.62,1.778
EOF
