#!/usr/bin/env python3
"""Compute predicted Raman 2D band centre and FWHM for wrinkled graphene island."""
import numpy as np
from scipy.optimize import curve_fit

# Constants from the paper
R = 0.6                     # island radius, µm
unit_spacing = 0.1           # µm
r0 = 0.7                     # laser effective radius, µm
ref_len = 1.2                # reference ribbon length for ns=2, µm
ns_ref = 2.0

# Reference Raman properties per % strain
domega_ref = -60.0           # cm⁻¹/%
dFWHM_ref = 12.0             # cm⁻¹/%
FWHM0 = 27.0                # zero-strain FWHM, cm⁻¹

# Grid: T (transverse) and L (longitudinal) indices 1..6 as per paper
T_idx = np.arange(1, 7, dtype=int)
L_idx = np.arange(1, 7, dtype=int)

# Coordinates of unit centres (µm)
X = L_idx * 0.1 - 0.05       # longitudinal distance from island edge
Y = T_idx * 0.1 - 0.05       # transverse coordinate (positive half)

# Ribbon lengths l_T for each T: chord length at centre of strip
l_T = 2.0 * np.sqrt(np.maximum(0.0, R**2 - Y**2))

# Stress transfer parameter ns_T proportional to l_T
ns_T = ns_ref * l_T / ref_len

# Compute laser intensity weights for each unit (L,T)
I_laser = np.exp(-2.0 * (X[np.newaxis, :] ** 2 + Y[:, np.newaxis] ** 2) / r0**2)

def compute_peak_properties(epsilon_m):
    """
    Compute effective omega_2D and FWHM_2D for given matrix strain epsilon_m (%).
    """
    # Strain map epsilon_r(L,T) using eq (4)
    epsilon_r = epsilon_m * (1.0 - np.cosh((ns_T / l_T)[:, np.newaxis] * X[np.newaxis, :])
                             / np.cosh(ns_T[:, np.newaxis] / 2.0))

    # Local Lorentzian centres and widths
    omega0_local = epsilon_r * domega_ref
    FWHM_local = FWHM0 + epsilon_r * dFWHM_ref

    # Frequency grid for the total spectrum
    omega_min = min(np.min(omega0_local), -30.0)
    omega_max = max(np.max(omega0_local), 10.0)
    omega = np.linspace(omega_min - 10, omega_max + 10, 2000)

    # Build total intensity I_total(omega)
    I_total = np.zeros_like(omega)
    for i, t in enumerate(T_idx):
        for j, l_ in enumerate(L_idx):
            gamma2 = FWHM_local[i, j] / 2.0
            il = I_laser[i, j]
            w0 = omega0_local[i, j]
            I_total += il * gamma2 / ((omega - w0)**2 + gamma2**2)

    # Fit with a single Lorentzian: A * (gamma/2)^2 / ((w - w0)^2 + (gamma/2)^2)
    def lorentz(w, A, w0, gamma):
        return A * (gamma/2)**2 / ((w - w0)**2 + (gamma/2)**2)

    # Initial guess
    i_max = np.argmax(I_total)
    p0 = [I_total[i_max] * (0.1 * FWHM0), omega[i_max], FWHM0]

    popt, _ = curve_fit(lorentz, omega, I_total, p0=p0, maxfev=10000)
    _, w0_fit, gamma_fit = popt
    return w0_fit, gamma_fit

# Strain values (at least 5 evenly spaced from 0% to 0.4%)
strains = [0.0, 0.1, 0.2, 0.3, 0.4]

# Write CSV header
print("strain_percent,omega_2D,FWHM_2D")
for eps in strains:
    w0, fwhm = compute_peak_properties(eps)
    print(f"{eps:.1f},{w0:.6f},{fwhm:.6f}")
