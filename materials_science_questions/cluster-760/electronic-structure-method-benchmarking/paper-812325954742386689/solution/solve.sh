#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: geometries.csv ===
cat > "$OUTDIR/geometries.csv" << 'EOF'
Radical,Method,R_C1O2,R_O2O3,Angle_C1O2O3,Torsion_X4,Torsion_X5,Torsion_X6
CH3O2,MP2,1.4489,1.3117,110.04,-180.00,60.61,-60.61
CH3O2,B3LYP,1.4493,1.3227,110.72,180.00,60.51,-60.51
CH2ClO2,MP2,1.4546,1.3129,108.20,180.00,60.90,60.90
CH2ClO2,B3LYP,1.4538,1.3228,108.43,180.00,61.24,-61.24
CHCl2O2,MP2,1.4362,1.3231,111.68,180.00,63.06,-63.06
CHCl2O2,B3LYP,1.4412,1.3253,110.30,0.00,118.97,-118.97
CCl3O2,MP2,1.4554,1.3194,111.14,180.00,61.11,-61.11
CCl3O2,B3LYP,1.4601,1.3184,112.22,180.00,61.05,-61.05
CFCl2O2,MP2,1.4397,1.3212,111.30,180.00,62.83,-62.83
CFCl2O2,B3LYP,1.4451,1.3198,112.80,180.00,62.34,-62.34
CF2ClO2,MP2,1.4242,1.3329,108.60,180.00,59.55,-59.55
CF2ClO2,B3LYP,1.4352,1.3315,109.36,180.00,60.02,-60.02
CHFClO2,MP2,1.4239,1.3291,110.44,-177.20,63.67,-58.48
CHFClO2,B3LYP,1.4296,1.3289,111.70,-175.82,66.20,-55.94
EOF

# === solve block: charge_spin_dipole.json ===
python3 /solution/write_outputs.py charge_spin_dipole

# === solve block: CH_BDEs.csv ===
python3 /solution/write_outputs.py CH_BDEs

# === solve block: CO_BDEs.csv ===
python3 /solution/write_outputs.py CO_BDEs

# === solve block: EAs.csv ===
python3 /solution/write_outputs.py EAs
