import sys, csv, math
import numpy as np
from scipy.optimize import brentq

R = 8.314462618
E0 = -1228665.43
theta_E = 269.2
a = -1.085e-3
b = -1.1835e-7
Gva_factor = 0.2
A_Omega = 229615.89
B_Omega = 12.73
C_Omega = -1.1274e-2

Tstart = 0.0
Tend = 3800.0
step = 1.0
n = int((Tend - Tstart) / step) + 1
T = np.linspace(Tstart, Tend, n)

def Omega(T):
    return A_Omega + B_Omega * T + C_Omega * T**2

def dOmega_dT(T):
    return B_Omega + 2 * C_Omega * T

def d2Omega_dT2(T):
    return 2 * C_Omega

def Cp_pure(T):
    if T < 1e-10:
        return 0.0
    x = theta_E / T
    exp_x = math.exp(x)
    einstein = 3 * R * x**2 * exp_x / (exp_x - 1)**2
    return einstein + a * T + b * T**2

def func_y_va(y, T):
    if T < 1e-10:
        return y
    return y - math.exp(-Gva_factor - Omega(T)/(R*T) * (1 - y)**2)

y_va = np.zeros(n)
y_va[0] = 0.0
for i in range(1, n):
    Ti = T[i]
    try:
        y_root = brentq(func_y_va, 0.0, 0.5, args=(Ti,), xtol=1e-14)
    except ValueError:
        y_root = 0.0
    y_va[i] = y_root

dy_va_dT = np.gradient(y_va, T, edge_order=2)

Cp = np.zeros(n)
for i in range(n):
    Ti = T[i]
    if Ti < 1e-10:
        Cp[i] = 0.0
        continue
    term1 = Cp_pure(Ti)
    term2 = - y_va[i] * Ti * d2Omega_dT2(Ti)
    term3 = (Omega(Ti) - Ti * dOmega_dT(Ti)) * dy_va_dT[i]
    Cp[i] = term1 + term2 + term3

from scipy.integrate import cumulative_trapezoid
int_Cp_full = cumulative_trapezoid(Cp, T, initial=0)
idx298 = np.argmin(np.abs(T - 298.15))
H298 = int_Cp_full[idx298]
H_minus_H298 = int_Cp_full - H298

output_type = sys.argv[1]
outdir = '/app/outputs'
if output_type == 'heat_capacity':
    with open(f'{outdir}/heat_capacity.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'Cp'])
        for i in range(n):
            writer.writerow([T[i], Cp[i]])
elif output_type == 'heat_content':
    with open(f'{outdir}/heat_content.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'H_minus_H298'])
        for i in range(n):
            writer.writerow([T[i], H_minus_H298[i]])
elif output_type == 'vacancy_concentration':
    with open(f'{outdir}/vacancy_concentration.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'y_va'])
        for i in range(n):
            writer.writerow([T[i], y_va[i]])
else:
    raise ValueError("Unknown output type")
