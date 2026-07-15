import csv
import os

a0 = 3.9789
c0 = 6.5824

def a_func(T):
    if T <= 42:
        eps = -4.71e-7 * T + 1.71e-9 * T**3
    else:
        T42 = 42.0
        eps42 = -4.71e-7 * T42 + 1.71e-9 * T42**3
        deps42 = -4.71e-7 + 3 * 1.71e-9 * T42**2
        dT = T - T42
        B = deps42
        eps300 = 0.0023
        C = (eps300 - eps42 - B * 258) / (258**2)
        eps = eps42 + B * dT + C * dT**2
    return a0 * (1 + eps)

def c_func(T):
    if T <= 42:
        eps = -2e-6 * T + 7.86e-9 * T**2
    else:
        T42 = 42.0
        eps42 = -2e-6 * T42 + 7.86e-9 * T42**2
        deps42 = -2e-6 + 2 * 7.86e-9 * T42
        dT = T - T42
        B = deps42
        eps300 = 0.002
        C = (eps300 - eps42 - B * 258) / (258**2)
        eps = eps42 + B * dT + C * dT**2
    return c0 * (1 + eps)

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, 'step_04_lattice_parameters_vs_T.csv')
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T(K)', 'a(Å)', 'c(Å)'])
    for T in range(0, 301, 5):
        a_val = a_func(T)
        c_val = c_func(T)
        writer.writerow([T, f'{a_val:.8f}', f'{c_val:.8f}'])
