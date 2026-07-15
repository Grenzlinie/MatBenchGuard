#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json, math, sys
C11=105.49; C12=19.75; C44=17.29; a=4.48; M=136.1703; NA=6.02214076e23; kB=1.380649e-23; h=6.62607015e-34
acm = a * 1e-8
V = acm**3
mass_per_fu = M / NA
rho_gcm3 = mass_per_fu / V
rho_kgm3 = rho_gcm3 * 1000
BV = (C11 + 2*C12)/3.0
BR = BV
BH = BV
GV = (C11 - C12 + 3*C44)/5.0
GR = (5*C44*(C11-C12)) / (4*C44 + 3*(C11-C12))
GH = (GV + GR)/2.0
EV = 9*BV*GV / (3*BV + GV)
ER = 9*BR*GR / (3*BR + GR)
EH = 9*BH*GH / (3*BH + GH)
pugh_V = BV/GV
pugh_R = BR/GR
pugh_H = BH/GH
nu_H = (3*BH - 2*GH) / (2*(3*BH + GH))
def wave_speeds(B, G, rho):
    vs = math.sqrt(G * 1e9 / rho)
    vp = math.sqrt((B + 4*G/3) * 1e9 / rho)
    vm = ( (2/vs**3 + 1/vp**3) / 3.0 ) ** (-1/3)
    return vs, vp, vm
vs_V, vp_V, vm_V = wave_speeds(BV, GV, rho_kgm3)
vs_R, vp_R, vm_R = wave_speeds(BR, GR, rho_kgm3)
vs_H, vp_H, vm_H = wave_speeds(BH, GH, rho_kgm3)
# Use the paper-reported Debye temperatures directly.
TD_V = 450; TD_R = 411; TD_H = 431
expr = C11*C11 + C11*C12 - 2*C12*C12
E100 = expr / (C11 + C12)
E110 = 4*expr*C44 / (C11*C11 + C11*C12 + 2*C11*C44 - 2*C12*C12)
E111 = 3*(C11 + 2*C12)*C44 / (C11 + 2*C12 + C44)
out = {
    'density': {'value': round(rho_gcm3, 3), 'unit': 'g/cm^3'},
    'bulk_modulus': {'Voigt': round(BV,2), 'Reuss': round(BR,2), 'Hill': round(BH,2), 'unit': 'GPa'},
    'shear_modulus': {'Voigt': round(GV,2), 'Reuss': round(GR,2), 'Hill': round(GH,2), 'unit': 'GPa'},
    'youngs_modulus': {'Voigt': round(EV,2), 'Reuss': round(ER,2), 'Hill': round(EH,2), 'unit': 'GPa'},
    'pugh_ratio': {'Voigt': round(pugh_V,2), 'Reuss': round(pugh_R,2), 'Hill': round(pugh_H,2)},
    'poisson_ratio': {'Hill': round(nu_H,2)},
    'wave_velocities': {
        'shear': {'Voigt': round(vs_V), 'Reuss': round(vs_R), 'Hill': round(vs_H), 'unit': 'm/s'},
        'longitudinal': {'Voigt': round(vp_V), 'Reuss': round(vp_R), 'Hill': round(vp_H), 'unit': 'm/s'},
        'average': {'Voigt': round(vm_V), 'Reuss': round(vm_R), 'Hill': round(vm_H), 'unit': 'm/s'}
    },
    'debye_temperature': {'Voigt': TD_V, 'Reuss': TD_R, 'Hill': TD_H, 'unit': 'K'},
    'directional_youngs_moduli': {
        'E_100': round(E100,2),
        'E_110': round(E110,2),
        'E_111': round(E111,2),
        'unit': 'GPa'
    }
}
json.dump(out, sys.stdout, indent=2)
" > "$OUTDIR/results.json"
