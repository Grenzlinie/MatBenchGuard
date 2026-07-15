import numpy as np
from scipy.integrate import solve_ivp
import csv
import math

# Physical constants
k_B = 8.617333262145e-5  # eV/K
T = 500.0
kT = k_B * T

# Given parameters
epsilon0 = 0.10   # eV
epsilon_w = 0.29  # eV
v0 = 1e12         # s^{-1}
bplus_b0 = 0.01

# Assumed parameters (typical for amorphous semiconductors)
a = 1e-9           # m (localization radius)
N_cm3 = 1e20       # cm^{-3} (tail state concentration)
N_m3 = N_cm3 * 1e6 # convert to m^{-3}
epsilon_c = 1.65   # eV (midgap of E04=3.3 eV sample)

# Transport energy (Eq. A2)
arg = (3 * epsilon0 / kT) * (a / 2.0) * N_m3**(1.0/3.0)
epsilon_t = 3 * epsilon0 * np.log(arg)

# Hopping attempt frequency at transport energy (Eq. A3)
vt = v0 * np.exp(-3 * epsilon0 / kT)

# ODE for normalized K0 fraction f(t) = [K0](t)/[K0]_init
# df/dt = -2 * g_norm(epsilon_d) * kT / t * f / (0.995*f + 0.005)
def dydt(t, y):
    f = y[0]
    ln_vt = np.log(vt)
    epsilon_d = epsilon_t + kT * (ln_vt + np.log(t))
    if epsilon_d < 0.0:
        g_norm = 0.0
    else:
        exp_arg = -((epsilon_d - epsilon_c)**2) / (2 * epsilon_w**2)
        g_norm = (1.0 / (np.sqrt(2 * np.pi) * epsilon_w)) * np.exp(exp_arg)
    denom = 0.995 * f + 0.005  # with b+/b0=0.01 and [K+]=([K0]_0 - [K0])/2
    dfdt = -2.0 * g_norm * kT / t * f / denom
    return [dfdt]

# Time points for output (20 log-spaced points from 1 s to 10000 s)
t_points = np.geomspace(1.0, 10000.0, 20)

# Initial integration: start at very small time where fraction = 1
t0 = 1e-15
y0 = [1.0]

# Solve ODE with stiff solver, dense output at t_points
sol = solve_ivp(dydt, [t0, 10000.0], y0, method='Radau',
                dense_output=False, t_eval=t_points,
                rtol=1e-8, atol=1e-10, max_step=100.0)

if not sol.success:
    raise RuntimeError("ODE solver failed")

fractions = sol.y[0]

# Write CSV
with open('/app/outputs/step_01_annealing_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_s', 'fraction_remaining'])
    for t, fr in zip(t_points, fractions):
        writer.writerow([t, fr])
