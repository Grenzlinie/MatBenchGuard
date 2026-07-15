import json
import math
import numpy as np
from scipy.special import k0, k1

G = 5e10
nu = 0.3
omega = 0.01
R_trunc = 2e-6
b = 2.5e-10
rho0 = 1e14
T_ext = 1.6e-9

D = G / (2 * math.pi * (1 - nu))
rd = 1.0 / math.sqrt(math.pi * rho0 * b**2 * D / T_ext)
Ic = omega / (math.pi * b * rd)

r_d = rd
I_c = Ic

N = 501
lim = 4 * r_d
x = np.linspace(-lim, lim, N)
y = np.linspace(-lim, lim, N)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)
r_safe = np.maximum(r, 1e-20)

sigma_yy = -D * omega * (np.cosh(Y / r_d) * k0(r_safe / r_d) + np.sinh(Y / r_d) * (Y / r_safe) * k1(r_safe / r_d))
sigma_xx = -D * omega * (np.cosh(Y / r_d) * k0(r_safe / r_d) - np.sinh(Y / r_d) * (Y / r_safe) * k1(r_safe / r_d))
sigma_xy = -D * omega * np.sinh(Y / r_d) * (X / r_safe) * k1(r_safe / r_d)
I = I_c * np.sinh(Y / r_d) * k0(r_safe / r_d)

fields = {
    "x": x.tolist(),
    "y": y.tolist(),
    "I": I.tolist(),
    "sigma_xx": sigma_xx.tolist(),
    "sigma_yy": sigma_yy.tolist(),
    "sigma_xy": sigma_xy.tolist(),
    "r_d": r_d,
    "I_c": I_c,
    "D": D,
    "omega": omega,
    "b": b,
    "R": R_trunc
}
with open("/app/outputs/step_01_fields.json", "w") as f:
    json.dump(fields, f, indent=2)

W_unscreened = D * omega**2 * R_trunc**2 / 8
W_screened = (math.sqrt(math.pi) / 4) * D * omega**2 * rd**2 * math.sqrt(R_trunc / rd)
ratio = W_screened / W_unscreened
energy = {
    "W_unscreened": W_unscreened,
    "W_screened": W_screened,
    "ratio": ratio
}
with open("/app/outputs/step_02_energy.json", "w") as f:
    json.dump(energy, f, indent=2)
