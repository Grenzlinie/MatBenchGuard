import numpy as np
from scipy.optimize import brentq
import csv
import os

a = 125
b = 100
k = 0.05
D = 3.47e-3
C0 = 10.0
Ceq = 1.0
Da = k * b / D

# find positive roots of u*tan(u) - Da = 0
roots = []
for n in range(1, 40):
    low = (n-1)*np.pi + 1e-6
    high = (n-1)*np.pi + np.pi/2 - 1e-6
    def f(u):
        return u * np.tan(u) - Da
    try:
        if f(low)*f(high) < 0:
            u = brentq(f, low, high, xtol=1e-12)
            roots.append(u)
    except ValueError:
        break

roots = roots[:20]
beta_b = np.array(roots)
beta = beta_b / b

N2 = b/2 * (1 + np.sin(2*beta_b)/(2*beta_b))

x_vals = np.arange(a)
y_vals = np.arange(b)
X, Y = np.meshgrid(x_vals, y_vals, indexing='ij')
C = np.zeros((a, b))
for n in range(len(roots)):
    prefactor = np.sin(beta_b[n]) / (N2[n] * beta[n])
    C += prefactor * np.cosh(beta[n]*(X - a)) / np.cosh(beta[n]*a) * np.cos(beta[n]*Y)
C = (C0 - Ceq) * C + Ceq

out_path = os.path.join(os.environ.get('OUTDIR','/app/outputs'), 'step_01_validation_contour.csv')
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','y','concentration'])
    for i in range(a):
        for j in range(b):
            writer.writerow([i, j, C[i,j]])
