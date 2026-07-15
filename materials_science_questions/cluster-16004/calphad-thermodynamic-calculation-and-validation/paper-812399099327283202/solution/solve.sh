#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple pycalphad sympy pandas numpy scipy

# === solve block: phase_boundaries.csv ===
cat > /tmp/gen_phase.py << 'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import csv, sys

R = 8.314

cu_ni_fcc = [(9534.49, 2.83903), (424.255, -0.62595), (-1812.93, 2.12233)]
cu_ni_liq = [(32238.7, -11.1093), (-619.65, -1.08812), (-213.489, 0.97309)]
fe_ni_fcc = [(-18298.8, 5.14894), (14313.6, -7.65979)]
fe_ni_liq = [(-20292.4, 5.14137), (11924.4, -6.16329)]
cu_fe_fcc = [(48206.0, -8.44645), (-5918.0, 5.01725)]
cu_fe_liq = [(34321.3, -1.8577), (-1811.6, 1.6401), (7564.6, -2.5857), (-2418.3, 2.3472)]

ternary_fcc = (-35982, -12.0)
ternary_liq = (-45000, 0.0)

latt_stab = {
    'Cu': (13054.1, -9.6232, 4.1756e-3, 22.03),
    'Fe': (-11274.0, 163.878, 4.1756e-3, 22.03),
    'Ni': (17614.6, -10.209, 4.1756e-3, 22.03)
}

def G_pure(phase, T):
    dG = {}
    for el in ['Cu','Fe','Ni']:
        a,b,c,dval = latt_stab[el]
        dG[el] = a + b*T + c*T*T + dval*T*np.log(T)
    if phase == 'fcc':
        return {'Cu':0.0, 'Fe':0.0, 'Ni':0.0}
    else:
        return dG

def excess_energy_phase(phase, x, T):
    xCu, xFe, xNi = x
    gex = 0.0
    coeffs = cu_ni_fcc if phase == 'fcc' else cu_ni_liq
    for v, (a,b) in enumerate(coeffs):
        gex += (a + b*T) * xCu * xNi * (xCu - xNi)**v
    coeffs = fe_ni_fcc if phase == 'fcc' else fe_ni_liq
    for v, (a,b) in enumerate(coeffs):
        gex += (a + b*T) * xFe * xNi * (xFe - xNi)**v
    coeffs = cu_fe_fcc if phase == 'fcc' else cu_fe_liq
    for v, (a,b) in enumerate(coeffs):
        gex += (a + b*T) * xCu * xFe * (xCu - xFe)**v
    A, B = ternary_fcc if phase == 'fcc' else ternary_liq
    gex += (A + B*T) * xCu * xFe * xNi
    return gex

def excess_energy_phase_deriv(phase, x, T):
    xCu, xFe, xNi = x
    dG = np.zeros(3)
    coeffs = cu_ni_fcc if phase == 'fcc' else cu_ni_liq
    for v, (a,b) in enumerate(coeffs):
        g = a + b*T
        D = xCu - xNi
        dG[0] += g * (xNi * D**v + xCu*xNi * v * D**(v-1) if v>0 else 0.0)
        dG[2] += g * (xCu * D**v - xCu*xNi * v * D**(v-1) if v>0 else 0.0)
    coeffs = fe_ni_fcc if phase == 'fcc' else fe_ni_liq
    for v, (a,b) in enumerate(coeffs):
        g = a + b*T
        D = xFe - xNi
        dG[1] += g * (xNi * D**v + xFe*xNi * v * D**(v-1) if v>0 else 0.0)
        dG[2] += g * (xFe * D**v - xFe*xNi * v * D**(v-1) if v>0 else 0.0)
    coeffs = cu_fe_fcc if phase == 'fcc' else cu_fe_liq
    for v, (a,b) in enumerate(coeffs):
        g = a + b*T
        D = xCu - xFe
        dG[0] += g * (xFe * D**v + xCu*xFe * v * D**(v-1) if v>0 else 0.0)
        dG[1] += g * (xCu * D**v - xCu*xFe * v * D**(v-1) if v>0 else 0.0)
    A, B = ternary_fcc if phase == 'fcc' else ternary_liq
    gtern = A + B*T
    dG[0] += gtern * xFe * xNi
    dG[1] += gtern * xCu * xNi
    dG[2] += gtern * xCu * xFe
    return dG

def chemical_potentials_analytical(phase, x, T):
    x = np.asarray(x)
    G0 = G_pure(phase, T)
    mu_ideal = R * T * np.log(x)
    G_ex = excess_energy_phase(phase, x, T)
    dG_ex = excess_energy_phase_deriv(phase, x, T)
    mu_ex = G_ex + dG_ex - np.dot(x, dG_ex)
    mu_pure = np.array([G0['Cu'], G0['Fe'], G0['Ni']])
    return mu_pure + mu_ideal + mu_ex

T_list = [1373, 1423, 1473, 1523, 1573, 1623, 1673]
output_path = sys.argv[1]
rows = []

for T in T_list:
    init = np.array([0.5, 0.2, 0.3])
    for xNi_liq in np.linspace(0.0, 1.0, 51):
        def eq(vars):
            xCu_liq, xCu_fcc, xFe_fcc = vars
            if xCu_liq + xNi_liq > 1.0 or xCu_liq < 0:
                return [1e6]*3
            xFe_liq = 1.0 - xNi_liq - xCu_liq
            if xFe_liq < 0 or xFe_liq > 1:
                return [1e6]*3
            xNi_fcc = 1.0 - xCu_fcc - xFe_fcc
            if xNi_fcc < 0 or xNi_fcc > 1:
                return [1e6]*3
            x_liq = np.array([xCu_liq, xFe_liq, xNi_liq])
            x_fcc = np.array([xCu_fcc, xFe_fcc, xNi_fcc])
            mu_liq = chemical_potentials_analytical('liq', x_liq, T)
            mu_fcc = chemical_potentials_analytical('fcc', x_fcc, T)
            return mu_fcc - mu_liq
        try:
            sol = fsolve(eq, init, xtol=1e-8, maxfev=1000)
            xCu_liq, xCu_fcc, xFe_fcc = sol
            xFe_liq = 1.0 - xNi_liq - xCu_liq
            xNi_fcc = 1.0 - xCu_fcc - xFe_fcc
            vals = [xCu_liq, xFe_liq, xNi_liq, xCu_fcc, xFe_fcc, xNi_fcc]
            if all(0.0 <= v <= 1.0 for v in vals):
                rows.append((T, 'liq', xCu_liq, xFe_liq, xNi_liq))
                rows.append((T, 'fcc', xCu_fcc, xFe_fcc, xNi_fcc))
                init = sol
            else:
                init = np.array([0.5, 0.2, 0.3])
        except Exception:
            init = np.array([0.5, 0.2, 0.3])

with open(output_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature', 'phase', 'x_Cu', 'x_Fe', 'x_Ni'])
    for r in rows:
        w.writerow(r)
PYEOF
python3 /tmp/gen_phase.py /app/outputs/phase_boundaries.csv
