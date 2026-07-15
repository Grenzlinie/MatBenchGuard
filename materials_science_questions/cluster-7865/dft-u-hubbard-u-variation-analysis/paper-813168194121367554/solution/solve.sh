#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_structural_parameters.csv ===
cat > "$OUTDIR/step_01_structural_parameters.csv" <<'EOF'
compound,a (Å),b (Å),c (Å),z_R,z_As,Fe_As_1 (Å),Fe_As_2 (Å)
Pr,5.6290,5.5507,8.4213,0.1460,0.6570,2.3773,2.3778
Nd,5.6643,5.5977,8.4117,0.1432,0.6552,2.3801,2.3807
Sm,5.6520,5.6446,8.4917,0.1401,0.6521,2.3754,2.3763
Gd,5.5673,5.4734,8.3048,0.1393,0.6599,2.3601,2.3606
EOF

# === solve block: step_02_magnetic_moments.csv ===
cat > "$OUTDIR/step_02_magnetic_moments.csv" <<'EOF'
compound,method,R_moment (μ_B),Fe_moment (μ_B)
Pr,GGA,1.95,1.95
Pr,GGA+U2,2.00,2.63
Pr,GGA+U3,2.01,2.80
Nd,GGA,3.09,2.02
Nd,GGA+U2,3.01,2.68
Nd,GGA+U3,3.02,2.81
Sm,GGA,5.13,2.03
Sm,GGA+U2,4.93,2.62
Sm,GGA+U3,4.94,2.78
Gd,GGA,6.82,1.72
Gd,GGA+U2,6.93,2.56
Gd,GGA+U3,6.93,2.73
EOF

# === solve block: step_03_dos_gap.csv ===
cat > "$OUTDIR/step_03_dos_gap.csv" <<'EOF'
compound,U_Fe (eV),gap
Pr,3,0.25
Nd,3,0.25
Sm,3,metallic
Gd,3,0.25
EOF
