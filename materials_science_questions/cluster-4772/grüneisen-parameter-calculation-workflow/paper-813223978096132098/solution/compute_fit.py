#!/usr/bin/env python3
"""Compute predicted Brillouin shifts from the paper's best-fit elastic constants."""
import numpy as np
import math
import csv

# ----------------------------------------------------------------------
# Reference elastic constants (units 1e10 dyn/cm^2 -> erg/cm^2 -> dyn/cm^2)
C11 = 2.38e10   # dyn/cm^2
C12 = 1.56e10
C44 = 1.12e10

# Density (g/cm^3)
rho = 1.629

# Optical constants
# Crystal 1: 6328.2 A, n=1.2681
# Crystals 2,3: 4879.9 A, n=1.2708
lam_6328 = 6328.2e-8   # cm
lam_4880 = 4879.9e-8
n_6328 = 1.2681
n_4880 = 1.2708

# Scattering angle 90 deg
scat_half = math.radians(45.0)
sin_scat_half = math.sin(scat_half)

# ----------------------------------------------------------------------
# Rotation matrix: Z-X-Z convention (Euler angles in degrees)
def euler_to_rot(phi_deg, theta_deg, chi_deg):
    phi   = math.radians(phi_deg)
    theta = math.radians(theta_deg)
    chi   = math.radians(chi_deg)
    c1, s1 = math.cos(phi), math.sin(phi)
    c2, s2 = math.cos(theta), math.sin(theta)
    c3, s3 = math.cos(chi), math.sin(chi)
    # Rz(phi)
    Rz1 = np.array([[ c1, s1, 0],
                    [-s1, c1, 0],
                    [  0,  0, 1]])
    # Rx(theta)
    Rx  = np.array([[1,   0,   0],
                    [0,  c2,  s2],
                    [0, -s2,  c2]])
    # Rz(chi)
    Rz3 = np.array([[ c3, s3, 0],
                    [-s3, c3, 0],
                    [  0,  0, 1]])
    R = Rz3 @ Rx @ Rz1   # v_lab = R @ v_crystal
    return R

# ----------------------------------------------------------------------
# Forward model: given elastic constants and Euler angles, return
# (T1_freq_GHz, T2_freq_GHz, L_freq_GHz) AFTER sorting ascending

def compute_frequencies(c11, c12, c44, phi, theta, chi, lam, n_refr):
    # Wavevector magnitude in vacuum: k0 = 2*pi / lam
    k0 = 2.0 * math.pi / lam
    # q magnitude (in crystal, same magnitude because refractive index scales both)
    q_mag = 2.0 * k0 * n_refr * sin_scat_half   # 1/cm
    # Lab q vector: incident along +z, scattered along +x
    # q_lab = (k, 0, -k) with k = k0 * n_refr
    k = k0 * n_refr
    # Actually q_mag = sqrt(2) * k, so k = q_mag / sqrt(2)
    k_val = q_mag / math.sqrt(2.0)
    q_lab = np.array([k_val, 0.0, -k_val])

    # Rotation matrix R (v_lab = R * v_crystal)
    R = euler_to_rot(phi, theta, chi)
    # q_crystal = R^T @ q_lab
    q_c = R.T @ q_lab
    q2 = q_c * q_c
    q_sq = np.sum(q2)

    # Build dynamical matrix lambda_ij (Eq. (2))
    lam_mat = np.zeros((3,3))
    for i in range(3):
        lam_mat[i,i] = (c11 - c44) * q2[i] + c44 * q_sq
    lam_mat[0,1] = (c12 + c44) * q_c[0] * q_c[1]
    lam_mat[1,0] = lam_mat[0,1]
    lam_mat[0,2] = (c12 + c44) * q_c[0] * q_c[2]
    lam_mat[2,0] = lam_mat[0,2]
    lam_mat[1,2] = (c12 + c44) * q_c[1] * q_c[2]
    lam_mat[2,1] = lam_mat[1,2]

    # Solve eigenvalue problem: eigenvalues of lam_mat
    eig_vals = np.linalg.eigvalsh(lam_mat)   # ascending order
    # Frequencies: omega = sqrt(eig_val / rho), then nu = omega/(2*pi)
    # eig_vals units: dyn/cm^4, rho: g/cm^3 => rad^2/s^2
    omegas = np.sqrt(eig_vals / rho)          # rad/s
    freqs_Hz = omegas / (2.0 * math.pi)       # Hz
    freqs_GHz = freqs_Hz / 1e9

    # eigvalsh returns ascending: T1, T2, L
    return freqs_GHz[0], freqs_GHz[1], freqs_GHz[2]   # T1, T2, L

# ----------------------------------------------------------------------
# Experimental data from Table I (only orientations with L and/or T1)
data_points = [
    # (crystal, theta, phi, chi, L_shift, T1_shift, lam, n)
    (1, 297.4, 219.3, 313.7, 3.860, None, lam_6328, n_6328),
    (1, 297.9, 229.1, 313.9, 3.895, None, lam_6328, n_6328),
    (1, 297.7, 239.6, 313.9, 3.905, None, lam_6328, n_6328),
    (1, 297.5, 249.3, 313.7, 3.850, 1.572, lam_6328, n_6328),
    (1, 297.8, 259.3, 313.7, 3.764, 1.761, lam_6328, n_6328),
    (1, 297.7, 264.4, 313.4, 3.741, 1.881, lam_6328, n_6328),
    (1, 297.7, 269.5, 313.7, 3.665, 1.978, lam_6328, n_6328),
    (1, 297.7, 274.4, 313.7, 3.603, 2.085, lam_6328, n_6328),
    # Crystal 2
    (2, 208.8, 231.6, 324.0, 4.964, 2.315, lam_4880, n_4880),
    (2, 208.5, 238.3, 324.0, 4.956, 2.231, lam_4880, n_4880),
    (2, 208.7, 249.1, 323.9, 4.966, 2.093, lam_4880, n_4880),
    (2, 208.3, 262.8, 323.5, 5.022, 1.957, lam_4880, n_4880),
    (2, 208.6, 275.4, 323.4, 5.084, None, lam_4880, n_4880),
    (2, 208.1, 288.3, 323.5, 5.127, 1.997, lam_4880, n_4880),
    (2, 208.5, 297.1, 323.2, 5.120, 2.126, lam_4880, n_4880),
    (2, 208.5, 303.9, 323.1, 5.093, 2.219, lam_4880, n_4880),
    (2, 208.4, 306.9, 323.2, 5.070, 2.253, lam_4880, n_4880),
    (2, 208.0, 313.0, 323.8, 5.042, 2.318, lam_4880, n_4880),
    (2, 207.8, 318.4, 323.9, 4.995, 2.345, lam_4880, n_4880),
    (2, 208.5, 321.8, 322.8, 4.937, 2.385, lam_4880, n_4880),
    # Crystal 3
    (3, 243.5,   5.0, 309.7, 4.776, 2.648, lam_4880, n_4880),
    (3, 243.5,  16.9, 309.9, 4.847, 2.422, lam_4880, n_4880),
    (3, 243.5,  28.0, 310.1, 4.942, 2.144, lam_4880, n_4880),
    (3, 243.5,  39.0, 310.2, 5.041, 1.951, lam_4880, n_4880),
    (3, 243.5,  53.0, 310.3, 5.065, None, lam_4880, n_4880),
    (3, 243.3,  67.0, 310.3, 5.008, 1.989, lam_4880, n_4880),
    (3, 243.6,  78.1, 310.5, 4.898, 2.267, lam_4880, n_4880),
    (3, 243.0,  91.0, 310.6, 4.740, 2.607, lam_4880, n_4880),
    (3, 243.6, 100.5, 310.6, 4.617, 2.820, lam_4880, n_4880),
]

# ----------------------------------------------------------------------
# Generate fitted_frequencies.csv
output_path = "fitted_frequencies.csv"
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["crystal", "phi_deg", "mode", "measured_shift_GHz", "predicted_shift_GHz"])
    for (cry, theta, phi, chi, L_shift, T1_shift, lam, n) in data_points:
        T1_pred, T2_pred, L_pred = compute_frequencies(
            C11, C12, C44, phi, theta, chi, lam, n
        )
        if L_shift is not None:
            writer.writerow([cry, phi, "L", L_shift, round(L_pred, 4)])
        if T1_shift is not None:
            writer.writerow([cry, phi, "T1", T1_shift, round(T1_pred, 4)])

print("fitted_frequencies.csv generated.")
