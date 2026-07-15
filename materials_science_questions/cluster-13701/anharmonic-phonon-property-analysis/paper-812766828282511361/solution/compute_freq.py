#!/usr/bin/env python3
"""Compute TO mode frequency vs temperature from anharmonic effective potential."""
import sys
import numpy as np
from scipy.integrate import simpson

def main(output_path):
    # ---------- Constants ----------
    k_B = 8.617333262145e-5   # eV/K
    c_cm_s = 2.99792458e10     # speed of light in cm/s
    # atomic masses in u
    m_Ag_u = 107.8682
    m_Cr_u = 51.9961
    m_S_u  = 32.065
    u_to_kg = 1.66053906660e-27
    eV_to_J = 1.602176634e-19
    # Convert u to eV*s^2/AA^2
    # mass in kg -> (eV*s^2)/m^2: kg / (eV/J) = kg / eV_to_J = kg * (1/eV_to_J)
    # then / (m^2 -> AA^2) => multiply by 1e-20? Actually 1 m^2 = 1e20 AA^2, 
    # so to convert denominator from m^2 to AA^2, multiply by 1e20.
    # mass_eV_s2_per_AA2 = mass_kg / eV_to_J * 1e20
    factor = 1e20 / eV_to_J
    mass_Ag = m_Ag_u * u_to_kg * factor
    mass_CrS2 = (m_Cr_u + 2*m_S_u) * u_to_kg * factor
    mu = 1.0 / (1.0/mass_Ag + 1.0/mass_CrS2)  # effective mass in eV*s^2/AA^2

    # Potential parameters
    a2, b2 = 0.17, 1.9
    a3, b3 = 0.12, 0.15
    a4, b4 = 0.22, 0.15

    # Integration grid (AA)
    L = 4.5
    N = 401   # step ~0.0225 AA
    xs = np.linspace(-L, L, N)
    ys = np.linspace(-L, L, N)
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    XX, YY = np.meshgrid(xs, ys, indexing='ij')  # shape (N,N)

    # Precompute potential and curvature on the grid
    r2 = XX**2 + YY**2
    p = XX**3 - 3*XX*YY**2
    r4 = r2**2

    # term2: f2 = 0.5*a2*(1 - exp(-b2*r2))
    eb2 = np.exp(-b2*r2)
    # Hessian of f2
    H2_xx = -a2*b2*eb2 * (1.0 - 2.0*b2*XX**2)
    H2_yy = -a2*b2*eb2 * (1.0 - 2.0*b2*YY**2)
    H2_xy = 2.0*a2*b2**2 * XX*YY * eb2

    # term3: f3 = a3*(1 - exp(-b3*p))
    eb3 = np.exp(-b3*p)
    factor3 = a3*b3*eb3
    H3_xx = factor3 * (6.0*XX - 9.0*b3*(XX**2 - YY**2)**2)
    H3_yy = factor3 * (-6.0*XX - 36.0*b3*XX**2*YY**2)
    H3_xy = factor3 * (18.0*b3*XX*YY*(XX**2 - YY**2) - 6.0*YY)

    # term4: f4 = a4*(1 - exp(-b4*(r2)^2))
    eb4 = np.exp(-b4*r4)
    factor4 = a4*b4*eb4
    H4_xx = factor4 * (-16.0*b4*XX**2*r2**2 + 4.0*r2 + 8.0*XX**2)
    H4_yy = factor4 * (-16.0*b4*YY**2*r2**2 + 4.0*r2 + 8.0*YY**2)
    H4_xy = factor4 * (-16.0*b4*XX*YY*r2**2 + 8.0*XX*YY)

    # Total Hessian
    Hxx = H2_xx + H3_xx + H4_xx
    Hyy = H2_yy + H3_yy + H4_yy
    Hxy = H2_xy + H3_xy + H4_xy

    # Radial curvatures: d^2W/dr^2 = (x^2 Hxx + y^2 Hyy + 2 x y Hxy) / r^2
    with np.errstate(divide='ignore', invalid='ignore'):
        curv = (XX**2 * Hxx + YY**2 * Hyy + 2.0*XX*YY * Hxy) / r2
    # Handle r=0: at origin, use average of Hxx and Hyy (isotropic)
    origin_mask = r2 < 1e-20
    curv[origin_mask] = (Hxx[origin_mask] + Hyy[origin_mask]) / 2.0

    # Potential energy W on the grid
    W = (0.5*a2*(1.0 - eb2) + a3*(1.0 - eb3) + a4*(1.0 - eb4))

    # Temperature loop
    T_vals = np.arange(10, 701, 10)
    freq_cm1 = []
    for T in T_vals:
        beta = 1.0 / (k_B * T)
        boltz = np.exp(-beta * W)
        Z = simpson(simpson(boltz, dx=dx, axis=1), dx=dy, axis=0)
        num = simpson(simpson(curv * boltz, dx=dx, axis=1), dx=dy, axis=0)
        phi_avg = num / Z  # eV/AA^2
        omega2 = phi_avg / mu   # 1/s^2
        if omega2 <= 0.0:
            # avoid negative due to numerical noise
            nu_cm1 = 0.0
        else:
            omega = np.sqrt(omega2)
            nu_cm1 = omega / (2.0 * np.pi * c_cm_s)
        freq_cm1.append(nu_cm1)

    # Write CSV
    with open(output_path, 'w') as f:
        f.write('T_K,frequency_cm-1\n')
        for T, nu in zip(T_vals, freq_cm1):
            f.write(f'{T},{nu:.6f}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: compute_freq.py <output_csv>')
        sys.exit(1)
    main(sys.argv[1])
