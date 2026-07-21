#!/usr/bin/env python3
"""Reference oracle: compute peak peel and shear stresses for the smart
composite pipe joint (FOST state-space model) and write peak_stresses.csv.

The script implements the electro-mechanical analytical model from the
instruction: laminate stiffness integration, state-space matrices [A] and [B]
from the paper's appendix, matrix-exponential solution of the linear BVP,
and stress extraction along the adhesive overlap.
"""

import numpy as np
from scipy.linalg import expm
import csv
import os

# =============================================================================
# 1. Material properties and geometry (SI units)
# =============================================================================

# --- Composite lamina (E-glass/Derakane 470) ---
E1_c = 25.2e9       # Pa
E2_c = 7.5e9        # Pa
G12_c = 2.4e9       # Pa
nu12_c = 0.32
nu21_c = nu12_c * E2_c / E1_c

# --- Epoxy adhesive ---
Ea = 0.96e9          # Pa
Ga = 0.34e9          # Pa

# --- Piezoelectric material (PZT) ---
E_pzt = 84e9         # Pa
nu_pzt = 0.22
d31 = -310e-12       # m/V
d32 = -310e-12       # m/V

# --- Geometry ---
R_pi = 50.8e-3       # m, pipe inner radius
h_p  = 2.54e-3       # m, pipe wall thickness
h_c  = 2.54e-3       # m, coupler wall thickness
h_a  = 0.0127e-3     # m, adhesive thickness
l1   = 25.4e-3       # m, overlap length
l2   = 127e-3        # m, bare pipe length

# Applied axial force
F_applied = 25000.0  # N (25 kN)

# Derived radii
R_p  = R_pi + h_p/2                     # pipe mid-plane radius
R_c  = R_pi + h_p + h_a + h_c/2         # coupler mid-plane radius
R_po = R_pi + h_p                       # pipe outer radius
R_ci = R_pi + h_p + h_a                 # coupler inner radius

# Shear correction factor
K = 5.0/6.0

# =============================================================================
# 2. Lamina stiffness matrices (plane-stress reduced)
# =============================================================================

denom_c = 1.0 - nu12_c * nu21_c
Q11_c = E1_c / denom_c
Q22_c = E2_c / denom_c
Q12_c = nu12_c * E2_c / denom_c
Q66_c = G12_c
Q55_c = G12_c   # transverse shear stiffness (use G12 as approximation)

# PZT: isotropic
Q11_p = E_pzt / (1.0 - nu_pzt**2)
Q22_p = Q11_p
Q12_p = nu_pzt * E_pzt / (1.0 - nu_pzt**2)
Q66_p = E_pzt / (2.0 * (1.0 + nu_pzt))
Q55_p = Q66_p

# Piezoelectric stress coefficients e31, e32
# e_3i = d_3i * (Q_i1 + Q_i2)  for in-plane isotropic PZT
e31_p = d31 * (Q11_p + Q12_p)   # C/m^2 = N/(V*m)
e32_p = d32 * (Q11_p + Q12_p)

# =============================================================================
# 3. Laminate stiffness resultants (A, B, D, E, F, A55)
# =============================================================================

def compute_laminate_stiffness(z_bounds, Q11_list, Q12_list, Q22_list, Q55_list, R):
    """
    Integrate through laminate thickness to get stiffness resultants.
    z_bounds: array of layer boundary z-coordinates (from -h/2 to h/2)
    Q**_list: list of lamina stiffnesses per layer
    R: mid-plane radius for the (R+z)/R factor
    
    Returns: A11, A12, A21, A22, A55, B11, B21, D11, E12, E22, F12
    """
    n_layers = len(z_bounds) - 1
    A11 = A12 = A21 = A22 = A55 = 0.0
    B11 = B21 = D11 = 0.0
    E12 = E22 = F12 = 0.0
    
    for k in range(n_layers):
        z_low = z_bounds[k]
        z_high = z_bounds[k+1]
        Q11 = Q11_list[k]
        Q12 = Q12_list[k]
        Q22 = Q22_list[k]
        Q55 = Q55_list[k]
        
        # Analytic integration with (R+z)/R factor
        # ∫(R+z)/R dz = z + z^2/(2R)
        # ∫(R+z)/R * z dz = z^2/2 + z^3/(3R)
        # ∫(R+z)/R * z^2 dz = z^3/3 + z^4/(4R)
        # For w/(R+z) terms: ∫(R+z)/R * 1/(R+z) dz = ∫1/R dz = dz/R
        # For z*w/(R+z): ∫(R+z)/R * z/(R+z) dz = ∫z/R dz = z^2/(2R)
        
        def int_1(z):
            return z + z**2 / (2.0 * R)
        def int_z(z):
            return z**2 / 2.0 + z**3 / (3.0 * R)
        def int_z2(z):
            return z**3 / 3.0 + z**4 / (4.0 * R)
        
        I1  = int_1(z_high) - int_1(z_low)
        Iz  = int_z(z_high) - int_z(z_low)
        Iz2 = int_z2(z_high) - int_z2(z_low)
        dz  = z_high - z_low
        
        A11 += Q11 * I1
        A12 += Q12 * I1
        A21 += Q12 * I1    # Q21 = Q12
        A22 += Q22 * I1
        B11 += Q11 * Iz
        B21 += Q12 * Iz
        D11 += Q11 * Iz2
        
        # E and F from w/(R+z) terms
        E12 += Q12 * dz / R
        E22 += Q22 * dz / R
        F12 += Q12 * (z_high**2 - z_low**2) / (2.0 * R)
        
        # Shear stiffness (without K factor yet)
        A55 += Q55 * dz
    
    A55 *= K  # Apply shear correction factor
    
    return A11, A12, A21, A22, A55, B11, B21, D11, E12, E22, F12


# Coupler: 6 layers [Comp/PZT/Comp/Comp/PZT/Comp], equal thickness h_c/6
z_c_bounds = np.linspace(-h_c/2, h_c/2, 7)
Q11_c_list = [Q11_c, Q11_p, Q11_c, Q11_c, Q11_p, Q11_c]
Q12_c_list = [Q12_c, Q12_p, Q12_c, Q12_c, Q12_p, Q12_c]
Q22_c_list = [Q22_c, Q22_p, Q22_c, Q22_c, Q22_p, Q22_c]
Q55_c_list = [Q55_c, Q55_p, Q55_c, Q55_c, Q55_p, Q55_c]

(A_c11, A_c12, A_c21, A_c22, A_c55, B_c11, B_c21, D_c11, E_c12, E_c22, F_c12
 ) = compute_laminate_stiffness(z_c_bounds, Q11_c_list, Q12_c_list, Q22_c_list,
                                Q55_c_list, R_c)

# Pipe: homogeneous composite wall of thickness h_p
z_p_bounds = np.array([-h_p/2, h_p/2])
Q11_p_list = [Q11_c]
Q12_p_list = [Q12_c]
Q22_p_list = [Q22_c]
Q55_p_list = [Q55_c]

(A_p11, A_p12, A_p21, A_p22, A_p55, B_p11, B_p21, D_p11, E_p12, E_p22, F_p12
 ) = compute_laminate_stiffness(z_p_bounds, Q11_p_list, Q12_p_list, Q22_p_list,
                                Q55_p_list, R_p)

# For convenience, define the denominator used in many matrix entries
den_c = A_c11 * D_c11 - B_c11**2
den_p = A_p11 * D_p11 - B_p11**2

# =============================================================================
# 4. Build state-space matrices [A] (12x12) and [B] (6x6)
# =============================================================================

A_mat = np.zeros((12, 12))
B_mat = np.zeros((6, 6))

# --- [A] matrix entries (from paper appendix) ---
A_mat[0, 1] = 1.0
A_mat[2, 3] = 1.0
A_mat[4, 5] = 1.0
A_mat[6, 7] = 1.0
A_mat[8, 9] = 1.0
A_mat[10, 11] = 1.0

# Row 2 (index 1): d^2 u0c / dx^2 equation
A_mat[1, 0] = (D_c11 * R_ci * Ga / (R_c * h_a) + (h_c * B_c11 * R_ci * Ga) / (2.0 * R_c * h_a)) / den_c
A_mat[1, 2] = (-D_c11 * (h_c * R_ci * Ga) / (2.0 * R_c * h_a) - B_c11 * (A_c55 + h_c**2 * R_ci * Ga / (4.0 * R_c * h_a))) / den_c
A_mat[1, 5] = (D_c11 * (R_ci * Ga / (2.0 * R_c) - E_c12) - B_c11 * (A_c55 - h_c * R_ci * Ga / (4.0 * R_c) - F_c12)) / den_c
A_mat[1, 6] = (-D_c11 * R_ci * Ga / (R_c * h_a) - B_c11 * (h_c * R_ci * Ga) / (2.0 * R_c * h_a)) / den_c
A_mat[1, 8] = (-D_c11 * (h_p * R_ci * Ga) / (2.0 * R_c * h_a) - B_c11 * (h_c * h_p * R_ci * Ga) / (4.0 * R_c * h_a)) / den_c
A_mat[1, 11] = (D_c11 * R_ci * Ga / (2.0 * R_c) + B_c11 * (h_c * R_ci * Ga) / (4.0 * R_c)) / den_c

# Row 4 (index 3): d^2 phi_c / dx^2 equation
A_mat[3, 0] = (-A_c11 * (h_c * R_ci * Ga) / (2.0 * R_c * h_a) - B_c11 * R_ci * Ga / (R_c * h_a)) / den_c
A_mat[3, 2] = (A_c11 * (A_c55 + h_c**2 * R_ci * Ga / (4.0 * R_c * h_a)) + B_c11 * (h_c * R_ci * Ga) / (2.0 * R_c * h_a)) / den_c
A_mat[3, 5] = (A_c11 * (A_c55 - h_c * R_ci * Ga / (4.0 * R_c) - F_c12) - B_c11 * (R_ci * Ga / (2.0 * R_c) - E_c12)) / den_c
A_mat[3, 6] = (A_c11 * (h_c * R_ci * Ga) / (2.0 * R_c * h_a) + B_c11 * R_ci * Ga / (R_c * h_a)) / den_c
A_mat[3, 8] = (A_c11 * (h_c * h_p * R_ci * Ga) / (4.0 * R_c * h_a) + B_c11 * (h_p * R_ci * Ga) / (2.0 * R_c * h_a)) / den_c
A_mat[3, 11] = (-A_c11 * (h_c * R_ci * Ga) / (4.0 * R_c) - B_c11 * R_ci * Ga / (2.0 * R_c)) / den_c

# Row 6 (index 5): d^2 w_c / dx^2 equation
A_mat[5, 1] = A_c21 / (R_c * A_c55)
A_mat[5, 3] = (B_c21 / R_c - A_c55) / A_c55
A_mat[5, 4] = (E_c22 / R_c + R_ci * Ea / (R_c * h_a)) / A_c55
A_mat[5, 10] = -R_ci * Ea / (R_c * h_a * A_c55)

# Row 8 (index 7): d^2 u0p / dx^2 equation
A_mat[7, 0] = (-D_p11 * R_po * Ga / (R_p * h_a) + B_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a)) / den_p
A_mat[7, 2] = (D_p11 * (h_c * R_po * Ga) / (2.0 * R_p * h_a) - B_p11 * (h_c * h_p * R_po * Ga) / (4.0 * R_p * h_a)) / den_p
A_mat[7, 5] = (-D_p11 * R_po * Ga / (2.0 * R_p) + B_p11 * (h_p * R_po * Ga) / (4.0 * R_p)) / den_p
A_mat[7, 6] = (D_p11 * R_po * Ga / (R_p * h_a) - B_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a)) / den_p
A_mat[7, 8] = (D_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a) - B_p11 * (A_p55 + h_p**2 * R_po * Ga / (4.0 * R_p * h_a))) / den_p
A_mat[7, 11] = (-D_p11 * (E_p12 + R_po * Ga / (2.0 * R_p)) - B_p11 * (A_p55 - F_p12 - h_p * R_po * Ga / (4.0 * R_p))) / den_p

# Row 10 (index 9): d^2 phi_p / dx^2 equation
A_mat[9, 0] = (-A_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a) + B_p11 * R_po * Ga / (R_p * h_a)) / den_p
A_mat[9, 2] = (A_p11 * (h_c * h_p * R_po * Ga) / (4.0 * R_p * h_a) - B_p11 * (h_c * R_po * Ga) / (2.0 * R_p * h_a)) / den_p
A_mat[9, 5] = (-A_p11 * (h_p * R_po * Ga) / (4.0 * R_p) + B_p11 * R_po * Ga / (2.0 * R_p)) / den_p
A_mat[9, 6] = (A_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a) - B_p11 * R_po * Ga / (R_p * h_a)) / den_p
A_mat[9, 8] = (A_p11 * (A_p55 + h_p**2 * R_po * Ga / (4.0 * R_p * h_a)) - B_p11 * (h_p * R_po * Ga) / (2.0 * R_p * h_a)) / den_p
A_mat[9, 11] = (A_p11 * (A_p55 - F_p12 - h_p * R_po * Ga / (4.0 * R_p)) + B_p11 * (E_p12 + R_po * Ga / (2.0 * R_p))) / den_p

# Row 12 (index 11): d^2 w_p / dx^2 equation
A_mat[11, 4] = -R_po * Ea / (R_p * h_a * A_p55)
A_mat[11, 7] = A_p21 / (R_p * A_p55)
A_mat[11, 9] = (B_p21 / R_p - A_p55) / A_p55
A_mat[11, 10] = R_po * Ea / (R_p * h_a * A_p55)
A_mat[11, 11] = E_p22 / (R_p * A_p55)

# --- [B] matrix for bare pipe ---
B_mat[0, 1] = 1.0
B_mat[2, 3] = 1.0
B_mat[4, 5] = 1.0

B_mat[1, 2] = -B_p11 * A_p55 / den_p
B_mat[1, 5] = (-D_p11 * E_p12 - B_p11 * (A_p55 - F_p12)) / den_p
B_mat[3, 2] = A_p11 * A_p55 / den_p
B_mat[3, 5] = (A_p11 * (A_p55 - F_p12) + B_p11 * E_p12) / den_p
B_mat[5, 1] = A_p21 / (R_p * A_p55)
B_mat[5, 3] = (B_p21 / R_p - A_p55) / A_p55
B_mat[5, 4] = E_p22 / (R_p * A_p55)

# =============================================================================
# 5. Piezoelectric resultants (for boundary conditions)
# =============================================================================

def compute_pzt_resultants(E3):
    """
    Compute N_xc^PZT, M_xc^PZT, N_sc^PZT for given E3 (V/m).
    PZT layers are at positions 2 and 5 (0-indexed 1 and 4) in the 6-layer stack.
    """
    Nx_pzt = 0.0
    Mx_pzt = 0.0
    Ns_pzt = 0.0
    
    # PZT layers: indices 1 and 4 (0-indexed)
    pzt_indices = [1, 4]
    
    for k in pzt_indices:
        z_low = z_c_bounds[k]
        z_high = z_c_bounds[k+1]
        
        # ∫ (R+z)/R * e31 * E3 dz
        # = e31 * E3 * [z + z^2/(2R)]_{z_low}^{z_high}
        I1 = (z_high + z_high**2/(2*R_c)) - (z_low + z_low**2/(2*R_c))
        Iz = (z_high**2/2 + z_high**3/(3*R_c)) - (z_low**2/2 + z_low**3/(3*R_c))
        I1_s = (z_high + z_high**2/(2*R_c)) - (z_low + z_low**2/(2*R_c))  # same as I1
        
        Nx_pzt += e31_p * E3 * I1
        Mx_pzt += e31_p * E3 * Iz
        Ns_pzt += e32_p * E3 * I1_s
    
    return Nx_pzt, Mx_pzt, Ns_pzt


# =============================================================================
# 6. BVP solution via matrix exponentials
# =============================================================================

def solve_bvp(E3):
    """
    Solve the BVP for given E3 (V/m).
    Returns x_points (overlap), q(x), tau(x).
    """
    Nx_pzt, Mx_pzt, Ns_pzt = compute_pzt_resultants(E3)
    
    # Matrix exponentials
    M = expm(A_mat * l1)   # 12x12: Z(l1) = M @ Z(0)
    P = expm(B_mat * l2)   # 6x6:  X(l2) = P @ X(0)
    
    # X(0) = pipe part of Z at l1 = Z[6:12](l1)
    # So X(l2) = P @ M[6:12, :] @ Z(0)
    M_pipe = M[6:12, :]   # rows 6..11 of M (pipe variables at l1)
    
    # Build linear system for Z(0): C @ Z(0) = b
    # 12 unknowns, 12 equations
    C = np.zeros((12, 12))
    b = np.zeros(12)
    
    eq = 0  # equation counter
    
    # --- BCs at x=0 ---
    # 1) u0_c(0) = 0  -> Z[0] = 0
    C[eq, 0] = 1.0
    b[eq] = 0.0
    eq += 1
    
    # 2) w_c'(0) = 0  -> Z[5] = 0
    C[eq, 5] = 1.0
    b[eq] = 0.0
    eq += 1
    
    # 3) Q_xc(0) = 0  -> A_c55*(Z[2] + Z[5]) = 0; since Z[5]=0, Z[2]=0
    C[eq, 2] = 1.0
    b[eq] = 0.0
    eq += 1
    
    # 4) N_xp(0) = 0  -> A_p11*Z[7] + B_p11*Z[9] + E_p12*Z[10] = 0
    C[eq, 7] = A_p11
    C[eq, 9] = B_p11
    C[eq, 10] = E_p12
    b[eq] = 0.0
    eq += 1
    
    # 5) M_xp(0) = 0  -> B_p11*Z[7] + D_p11*Z[9] + F_p12*Z[10] = 0
    C[eq, 7] = B_p11
    C[eq, 9] = D_p11
    C[eq, 10] = F_p12
    b[eq] = 0.0
    eq += 1
    
    # 6) Q_xp(0) = 0  -> Z[8] + Z[11] = 0
    C[eq, 8] = 1.0
    C[eq, 11] = 1.0
    b[eq] = 0.0
    eq += 1
    
    # --- BCs at x=l1 (coupler free end) ---
    # These involve Z(l1) = M @ Z(0)
    # 7) N_xc(l1) = N_xc^PZT
    #    A_c11*Z2(l1) + B_c11*Z4(l1) + E_c12*Z5(l1) = Nx_pzt
    row_Nx = np.zeros(12)
    row_Nx[1] = A_c11   # Z2 = u0_c'
    row_Nx[3] = B_c11   # Z4 = phi_c'
    row_Nx[4] = E_c12   # Z5 = w_c
    # Apply to Z(l1): row_Nx @ Z(l1) = row_Nx @ M @ Z(0) = Nx_pzt
    C[eq, :] = row_Nx @ M
    b[eq] = Nx_pzt
    eq += 1
    
    # 8) M_xc(l1) = M_xc^PZT
    #    B_c11*Z2(l1) + D_c11*Z4(l1) + F_c12*Z5(l1) = Mx_pzt
    row_Mx = np.zeros(12)
    row_Mx[1] = B_c11
    row_Mx[3] = D_c11
    row_Mx[4] = F_c12
    C[eq, :] = row_Mx @ M
    b[eq] = Mx_pzt
    eq += 1
    
    # 9) Q_xc(l1) = 0  -> Z3(l1) + Z6(l1) = 0
    row_Qx = np.zeros(12)
    row_Qx[2] = 1.0   # phi_c
    row_Qx[5] = 1.0   # w_c'
    C[eq, :] = row_Qx @ M
    b[eq] = 0.0
    eq += 1
    
    # --- BCs at x2=l2 (bare pipe loaded end) ---
    # X(l2) = P @ X(0) = P @ M_pipe @ Z(0)
    # 10) N_xb(l2) = F_applied / (2*pi*R_p)   [force per unit circumference]
    #     A_p11*X2(l2) + B_p11*X4(l2) + E_p12*X5(l2) = N0
    N0 = F_applied / (2.0 * np.pi * R_p)
    row_Nxb = np.zeros(6)
    row_Nxb[1] = A_p11   # X2 = u0_b'
    row_Nxb[3] = B_p11   # X4 = phi_b'
    row_Nxb[4] = E_p12   # X5 = w_b
    C[eq, :] = row_Nxb @ P @ M_pipe
    b[eq] = N0
    eq += 1
    
    # 11) M_xb(l2) = 0
    #     B_p11*X2(l2) + D_p11*X4(l2) + F_p12*X5(l2) = 0
    row_Mxb = np.zeros(6)
    row_Mxb[1] = B_p11
    row_Mxb[3] = D_p11
    row_Mxb[4] = F_p12
    C[eq, :] = row_Mxb @ P @ M_pipe
    b[eq] = 0.0
    eq += 1
    
    # 12) Q_xb(l2) = 0  -> X3(l2) + X6(l2) = 0
    row_Qxb = np.zeros(6)
    row_Qxb[2] = 1.0   # phi_b
    row_Qxb[5] = 1.0   # w_b'
    C[eq, :] = row_Qxb @ P @ M_pipe
    b[eq] = 0.0
    eq += 1
    
    # Solve for Z(0)
    try:
        Z0 = np.linalg.solve(C, b)
    except np.linalg.LinAlgError:
        # Fallback: least squares if singular
        Z0, _, _, _ = np.linalg.lstsq(C, b, rcond=None)
    
    # Compute Z(x) and stresses at evaluation points along overlap
    n_points = 500
    x_eval = np.linspace(0, l1, n_points)
    q_vals = np.zeros(n_points)
    tau_vals = np.zeros(n_points)
    
    for i, x in enumerate(x_eval):
        Zx = expm(A_mat * x) @ Z0
        
        # q(x) = (Ea/ha) * (w_c - w_p) = (Ea/ha) * (Z[4] - Z[10])
        q_vals[i] = (Ea / h_a) * (Zx[4] - Zx[10])
        
        # tau(x) = -Ga/ha*Z0 + Ga*hc/(2ha)*Z2 - Ga/2*Z5 + Ga/ha*Z6 + Ga*hp/(2ha)*Z8 - Ga/2*Z11
        # Z indices: Z0=u0c, Z2=phi_c, Z5=w_c', Z6=u0p, Z8=phi_p, Z11=w_p'
        tau_vals[i] = (-Ga/h_a * Zx[0]
                       + Ga * h_c / (2.0 * h_a) * Zx[2]
                       - Ga / 2.0 * Zx[5]
                       + Ga / h_a * Zx[6]
                       + Ga * h_p / (2.0 * h_a) * Zx[8]
                       - Ga / 2.0 * Zx[11])
    
    return x_eval, q_vals, tau_vals


# =============================================================================
# 7. Compute for both cases and write CSV
# =============================================================================

cases = [
    ("Case 1", 0.0, 0.0),        # E3 = 0 V/mm
    ("Case 1", -500.0, -500e6),  # E3 = -500 V/mm = -500e6 V/m
]

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)

results = []

for case_name, e3_V_per_mm, E3_V_per_m in cases:
    x_eval, q_vals, tau_vals = solve_bvp(E3_V_per_m)
    peel_max = np.max(np.abs(q_vals))
    shear_max = np.max(np.abs(tau_vals))
    results.append((case_name, e3_V_per_mm, peel_max, shear_max))

# Write CSV
csv_path = os.path.join(output_dir, "peak_stresses.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["case", "e3_V_per_mm", "peel_stress_max_Pa", "shear_stress_max_Pa"])
    for row in results:
        writer.writerow(row)

print(f"Written {csv_path}")
for row in results:
    print(f"  {row[0]}, E3={row[1]:.1f} V/mm: peel_max={row[2]:.3e} Pa, shear_max={row[3]:.3e} Pa")
