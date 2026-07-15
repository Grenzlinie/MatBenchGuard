import sys
import csv
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

# Constants
kB = 1.380649e-23       # J/K
e = 1.602176634e-19      # C
h = 6.62607015e-34       # J s
m_e = 9.10938356e-31     # kg
T = 300.0                # K
r = 0.5                  # scattering parameter

def fermi_integral(order, xi):
    """Compute Fermi-Dirac integral of given order at reduced chemical potential xi."""
    def integrand(x):
        return x**order / (1.0 + np.exp(x - xi))
    upper = max(200.0, xi + 100.0)
    val, _ = quad(integrand, 0.0, upper, limit=200, epsabs=1e-12, epsrel=1e-12)
    return val

def seebeck_eq(xi, S_target):
    """Return S(xi) - S_target (S_target in V/K)."""
    F_r   = fermi_integral(r, xi)           # F_0.5
    F_rp1 = fermi_integral(r + 1, xi)       # F_1.5
    S_calc = -(kB / e) * (((r + 2) * F_rp1) / ((r + 1) * F_r) - xi)
    return S_calc - S_target

# Table I: (composition, n_e in 10^21 cm^-3, mu_Hall in cm^2/V/s, S in muV/K)
data = [
    ("Ca",                   1.5, 0.33, -147),
    ("Ca0.8Sr0.2",           3.2, 0.92, -106),
    ("Ca0.5Sr0.5",           2.5, 1.3,  -123),
    ("Ca0.2Sr0.8",           3.3, 1.3,  -111),
    ("Sr",                   3.9, 4.9,  -108),
    ("Sr0.8Ba0.2",           3.0, 1.5,  -128),
    ("Sr0.5Ba0.5",           4.1, 0.97, -111),
    ("Sr0.2Ba0.8",           3.0, 0.076,-142),
    ("Ba",                   7.2, 0.068,-92),
    ("Ca0.8Sr0.2Ba0.2",      1.7, 0.14, -148),
    ("Ca0.2Sr0.8Ba0.2",      3.1, 0.37, -123),
    ("Ca0.2Sr0.2Ba0.6",      3.0, 0.10, -136),
    ("Ca0.4Sr0.4Ba0.2",      2.6, 0.44, -124),
    ("Ca0.4Sr0.2Ba0.4",      2.5, 0.34, -129),
    ("Ca0.2Sr0.4Ba0.4",      4.0, 0.56, -109),
]

results = []
for comp, n_e_in, mu_Hall, S_uV in data:
    S_target = S_uV * 1e-6          # convert muV/K to V/K

    # Find xi by root finding; search for sign change over a wide range
    xi_low, xi_high = None, None
    for low in [-200.0, -100.0, -50.0, -20.0, -10.0, -5.0, -2.0, -1.0]:
        for high in [0.0, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0]:
            if low >= high:
                continue
            fl = seebeck_eq(low, S_target)
            fh = seebeck_eq(high, S_target)
            if fl * fh < 0:
                xi_low, xi_high = low, high
                break
        if xi_low is not None:
            break
    if xi_low is None:
        raise RuntimeError(f"Could not bracket xi for {comp}")

    xi = brentq(lambda x: seebeck_eq(x, S_target), xi_low, xi_high, xtol=1e-10)

    # F_{1/2} for m_d* calculation
    F_half = fermi_integral(0.5, xi)

    # Convert n_e to m^-3: 10^21 cm^-3 = 1e27 m^-3
    n_e_m3 = n_e_in * 1e27

    # m_d* in units of m0 (first compute in kg, then divide by m_e)
    prefactor = h**2 / (2.0 * kB * T)
    m_d_kg = prefactor * (n_e_m3 / (4.0 * np.pi * F_half))**(2.0 / 3.0)
    m_d_star = m_d_kg / m_e

    # Carrier relaxation time tau = mu_Hall * m_d* / e
    # mu_Hall in cm^2/V/s -> m^2/V/s factor 1e-4
    mu_Hall_SI = mu_Hall * 1e-4
    tau_s = mu_Hall_SI * m_d_kg / e
    tau_fs = tau_s * 1e15

    # Electrical conductivity sigma = n_e * e * mu
    sigma = n_e_m3 * e * mu_Hall_SI                     # S/m

    # Thermoelectric power factor PF = S^2 * sigma  (S in V/K)
    PF = S_target**2 * sigma

    results.append([comp, n_e_in, mu_Hall, S_uV, m_d_star, tau_fs, PF])

# Write CSV to stdout
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(["composition", "n_e", "mu_Hall", "S", "m_d_star", "tau", "PF"])
for row in results:
    writer.writerow(row)
