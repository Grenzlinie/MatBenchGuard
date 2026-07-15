#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_lattice_parameter.txt ===
cat > "$OUTDIR/step_01_lattice_parameter.txt" <<'END_01'
lattice_parameter_angstrom = 5.030
END_01

# === solve block: step_02_elastic_constants.json ===
python3 -c "import json; print(json.dumps({'C11_GPa':144.870,'C12_GPa':64.205,'C44_GPa':76.393}))" > "$OUTDIR/step_02_elastic_constants.json"

# === solve block: step_03_polycrystalline_moduli.json ===
python3 -c "
import json, math
C11=144.870; C12=64.205; C44=76.393
# Compliance constants for cubic
S11 = (C11+C12)/((C11-C12)*(C11+2*C12))
S12 = -C12/((C11-C12)*(C11+2*C12))
S44 = 1.0/C44
# Voigt averages
BV = (C11+2*C12)/3
GV = (C11-C12+3*C44)/5
# Reuss averages
BR = 1/(3*S11+6*S12)
GR = 5/(4*S11-4*S12+3*S44)
# VRH averages
B = (BV+BR)/2
G = (GV+GR)/2
E = 9*B*G/(3*B+G)
nu = (3*B-2*G)/(2*(3*B+G))
G_B = G/B
# Directional Young's moduli for cubic using compliance formula: 1/E = S11 - 2*(S11-S12-0.5*S44)*(l1^2 l2^2 + l2^2 l3^2 + l1^2 l3^2)
# For [100]: l=(1,0,0) -> l1^2 l2^2+...=0 -> E_100 = 1/S11
# For [110]: l=(1/sqrt2,1/sqrt2,0) -> l1^2 l2^2+0+0 = 0.5*0.5=0.25; cross term = 0.25, so 1/E = S11 - 2*(S11-S12-0.5*S44)*0.25
# For [111]: l=(1/sqrt3,1/sqrt3,1/sqrt3) -> l1^2 l2^2+... = (1/3)*(1/3)*3 = 1/3; cross term = 1/3
E_100 = 1/S11
inv_E_110 = S11 - 2*(S11-S12-0.5*S44)*0.25
E_110 = 1/inv_E_110 if inv_E_110 != 0 else float('inf')
inv_E_111 = S11 - 2*(S11-S12-0.5*S44)*(1.0/3)
E_111 = 1/inv_E_111 if inv_E_111 != 0 else float('inf')
result = {
    'B_VRH_GPa': round(B,3),
    'G_VRH_GPa': round(G,3),
    'E_VRH_GPa': round(E,3),
    'Poisson_ratio': round(nu,3),
    'G_B_ratio': round(G_B,3),
    'E_100_GPa': round(E_100,3),
    'E_110_GPa': round(E_110,3),
    'E_111_GPa': round(E_111,3)
}
print(json.dumps(result))
" > "$OUTDIR/step_03_polycrystalline_moduli.json"

# === solve block: step_07_derived_properties.json ===
python3 /solution/compute_derived.py 5.030 144.870 64.205 76.393 > "$OUTDIR/step_07_derived_properties.json"

# === solve block: step_04_tensile_strength.json ===
python3 -c "import json; print(json.dumps({'direction':'[100]','ideal_tensile_strength_GPa':36.9,'failure_strain_percent':67.3}))" > "$OUTDIR/step_04_tensile_strength.json"

# === solve block: step_05_phonon_frequencies.json ===
python3 -c "import json; print(json.dumps({'T1u_DFPT_THz':31.148,'T1u_finite_displacement_THz':28.520,'T2g_DFPT_THz':39.106,'T2g_finite_displacement_THz':32.530}))" > "$OUTDIR/step_05_phonon_frequencies.json"

# === solve block: step_06_thermodynamic_properties.csv ===
python3 /solution/generate_thermo.py > "$OUTDIR/step_06_thermodynamic_properties.csv"
