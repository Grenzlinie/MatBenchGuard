#!/usr/bin/env python3
"""Compute C_V(T) for diamond, Si, Ge using the Morse‐potential anharmonic model."""
import sys
import numpy as np
from scipy.integrate import simpson

# Fundamental constants
hbar = 1.054571817e-34    # J·s
k_B  = 1.380649e-23       # J/K
R    = 8.314462618        # J/(mol·K)
eV_to_J = 1.602176634e-19


def compute_cv(theta_D, D_eV, T_range, step=10):
    """
    Compute isochoric heat capacity C_V(T) for one material.
    theta_D: Debye temperature in K
    D_eV:    Morse potential well depth in eV
    T_range: (T_min, T_max) in K
    step:    output temperature step in K
    Returns (T_out, Cv_out) arrays.
    """
    D_J = D_eV * eV_to_J
    N = int(np.floor(4 * D_J / (k_B * theta_D) - 0.5))
    omega_D = k_B * theta_D / hbar

    # Fine temperature grid for differentiation
    dT_fine = 0.5  # K
    T_fine = np.arange(T_range[0], T_range[1] + 2, dT_fine)

    # Frequency grid for integration
    n_omega = 5000
    omega_vals = np.linspace(0, omega_D, n_omega)

    # n+1/2 array
    n_plus_half = np.arange(N + 1) + 0.5

    # Energy E_n(ω) – shape (n_omega, N+1)
    omega_grid = omega_vals[:, None]          # (n_omega, 1)
    n_ph = n_plus_half[None, :]              # (1, N+1)
    energy = (hbar * omega_grid * n_ph
              - (hbar**2 * omega_grid**2 / (4 * D_J)) * (n_ph**2))

    # Process only T > 0 (T=0 will be handled separately)
    mask = T_fine > 0
    T_nonzero = T_fine[mask]

    # Exponent for all frequencies, levels, and non‑zero temperatures
    exponent = energy[:, :, None] / (k_B * T_nonzero[None, None, :])
    # Log‑sum‑exp stabilisation: subtract max over levels
    max_exp = np.max(-exponent, axis=1, keepdims=True)
    Z = np.sum(np.exp(-exponent - max_exp), axis=1)   # (n_omega, n_T_nonzero)
    log_Z = np.log(Z) + max_exp[:, 0, :]

    # Integrand ω² ln Z
    omega_sq = omega_vals**2
    integrand = omega_sq[:, None] * log_Z
    I = simpson(integrand, omega_vals, axis=0)        # shape (n_T_nonzero,)

    # Mean free energy F(T) = –(9·R·T / ω_D³) · I(T)
    F = np.zeros_like(T_fine)
    F[mask] = - (9 * R * T_nonzero / omega_D**3) * I

    # Second derivative → C_V
    dFdT = np.gradient(F, dT_fine)
    d2FdT2 = np.gradient(dFdT, dT_fine)
    Cv_fine = -T_fine * d2FdT2
    Cv_fine[0] = 0.0   # physical limit

    # Interpolate to output grid
    T_out = np.arange(T_range[0], T_range[1] + step, step)
    Cv_out = np.interp(T_out, T_fine, Cv_fine)

    return T_out, Cv_out


def main():
    outfile = sys.argv[1] if len(sys.argv) > 1 else "/app/outputs/cv_curves.csv"

    materials = [
        ("diamond",  2239.6, 3.68, (0, 2000)),
        ("silicon",   648.9, 2.32, (0, 1500)),
        ("germanium", 373.4, 1.94, (0, 1500)),
    ]

    rows = []
    for name, theta_D, D_eV, T_range in materials:
        T, Cv = compute_cv(theta_D, D_eV, T_range, step=10)
        for t, cv in zip(T, Cv):
            rows.append((name, f"{t:.1f}", f"{cv:.6f}"))

    with open(outfile, "w") as f:
        f.write("material,temperature_K,Cv_J_per_mol_K\n")
        for row in rows:
            f.write(",".join(row) + "\n")


if __name__ == "__main__":
    main()
