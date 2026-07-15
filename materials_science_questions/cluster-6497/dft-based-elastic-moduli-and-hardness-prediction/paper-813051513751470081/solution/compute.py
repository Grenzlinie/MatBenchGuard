#!/usr/bin/env python3
"""Compute all properties for naphthalene P2_1/a (LDA, PBE, PL/2)."""
import sys
import csv
import math

# ----------------------------------------------------------------------
# Paper data: elastic constants (GPa) and unit-cell volumes (Å³)
# Order: C11,C22,C33,C12,C13,C23,C44,C55,C66,C15,C25,C35,C46
# ----------------------------------------------------------------------
LDA_C = [23.51, 27.51, 32.63, 11.76, 12.34, 10.89,
         12.53,  7.16, 10.54, -1.43,  2.60, -5.26,  2.10]
PBE_C = [ 3.36,  5.81,  5.85,  3.11,  1.88,  2.69,
          1.34,  0.40,  2.05,  0.09,  0.63, -0.68,  0.90]
LDA_VOL = 299.9
PBE_VOL = 401.7
PL2_VOL = (LDA_VOL + PBE_VOL) / 2.0

M = 128.17          # g/mol (C10H8)
N_A = 6.02214076e23
Z = 2               # molecules per unit cell

# Physical constants
H_BAR = 1.054571817e-34   # J·s
K_B   = 1.380649e-23      # J/K

# ----------------------------------------------------------------------
def build_C(ec):
    """Construct 6x6 stiffness matrix from 13 independent constants."""
    c11,c22,c33,c12,c13,c23,c44,c55,c66,c15,c25,c35,c46 = ec
    C = [[0.0]*6 for _ in range(6)]
    C[0][0] = c11
    C[1][1] = c22
    C[2][2] = c33
    C[0][1] = C[1][0] = c12
    C[0][2] = C[2][0] = c13
    C[1][2] = C[2][1] = c23
    C[3][3] = c44
    C[4][4] = c55
    C[5][5] = c66
    C[0][5] = C[5][0] = c15
    C[1][5] = C[5][1] = c25
    C[2][5] = C[5][2] = c35
    C[3][4] = C[4][3] = c46
    return C

def mat_mult(A, B):
    """Multiply two square matrices (lists of lists)."""
    n = len(A)
    C = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            if aik == 0.0:
                continue
            Bk = B[k]
            Ci = C[i]
            for j in range(n):
                Ci[j] += aik * Bk[j]
    return C

def inv_mat(M):
    """Invert 6x6 matrix by Gauss-Jordan with partial pivoting."""
    n = len(M)
    # Augment
    A = [row[:] + [float(i==j) for j in range(n)] for i,row in enumerate(M)]
    for col in range(n):
        # Find pivot
        pivot_row = max(range(col, n), key=lambda r: abs(A[r][col]))
        if abs(A[pivot_row][col]) < 1e-15:
            raise ValueError("Singular matrix")
        A[col], A[pivot_row] = A[pivot_row], A[col]
        piv = A[col][col]
        for j in range(2*n):
            A[col][j] /= piv
        for i in range(n):
            if i == col:
                continue
            factor = A[i][col]
            for j in range(2*n):
                A[i][j] -= factor * A[col][j]
    return [row[n:] for row in A]

def compute_moduli(ec):
    """Return (B_V, G_V, B_R, G_R) for given elastic constants."""
    C = build_C(ec)
    # Voigt
    c11,c22,c33,c12,c13,c23,c44,c55,c66,_,_,_,_ = ec
    B_V = (c11 + c22 + c33 + 2.0*(c12 + c13 + c23)) / 9.0
    G_V = (c11 + c22 + c33 + 3.0*(c44 + c55 + c66) - (c12 + c13 + c23)) / 15.0
    # Reuss via compliance
    S = inv_mat(C)
    s11,s22,s33 = S[0][0],S[1][1],S[2][2]
    s12,s13,s23 = S[0][1],S[0][2],S[1][2]
    s44,s55,s66 = S[3][3],S[4][4],S[5][5]
    B_R = 1.0 / (s11 + s22 + s33 + 2.0*(s12 + s13 + s23))
    G_R = 15.0 / (4.0*(s11 + s22 + s33) - 4.0*(s12 + s13 + s23) + 3.0*(s44 + s55 + s66))
    return B_V, G_V, B_R, G_R

def mechanical_properties(ec):
    """Return (B, G, E, mu, H)."""
    B_V, G_V, B_R, G_R = compute_moduli(ec)
    B = (B_V + B_R) / 2.0
    G = (G_V + G_R) / 2.0
    E = (9.0 * B * G) / (3.0 * B + G)
    mu = (3.0 * B - 2.0 * G) / (2.0 * (3.0 * B + G))
    H = 0.92 * (G / B) ** 1.137 * G ** 0.708
    return B, G, E, mu, H

def density(V_ang3):
    """kg/m³ from cell volume in Å³."""
    M_kg = M * 1e-3  # kg/mol
    mass = Z * M_kg / N_A
    return mass / (V_ang3 * 1e-30)

def acoustic_properties(B_GPa, G_GPa, V_ang3):
    """Return (v_s, v_p, v_avg, Theta_D, gamma_a)."""
    B = B_GPa * 1e9
    G = G_GPa * 1e9
    rho = density(V_ang3)
    v_s = math.sqrt(G / rho)
    v_p = math.sqrt((B + 4.0 * G / 3.0) / rho)
    v_avg = ( (1.0/3.0) * (2.0 / v_s**3 + 1.0 / v_p**3) ) ** (-1.0/3.0)
    n_atoms = 18
    conc = (6.0 * math.pi**2 * n_atoms * N_A * rho / (M * 1e-3)) ** (1.0/3.0)
    Theta_D = (H_BAR / K_B) * conc * v_avg
    gamma_a = (9.0/2.0) * (v_p**2 - 4.0/3.0 * v_s**2) / (v_p**2 + 2.0 * v_s**2)
    return v_s, v_p, v_avg, Theta_D, gamma_a

def write_elastic():
    writer = csv.writer(sys.stdout)
    writer.writerow(["functional", "C11", "C22", "C33", "C12", "C13", "C23",
                     "C44", "C55", "C66", "C15", "C25", "C35", "C46"])
    for name, ec in [("LDA", LDA_C), ("PBE", PBE_C)]:
        row = [name] + [f"{v:.4f}" for v in ec]
        writer.writerow(row)
    pl2 = [(l + p) / 2.0 for l, p in zip(LDA_C, PBE_C)]
    row = ["PL/2"] + [f"{v:.4f}" for v in pl2]
    writer.writerow(row)

def write_mechanical():
    writer = csv.writer(sys.stdout)
    writer.writerow(["functional", "B", "G", "E", "mu", "H"])
    for name, ec in [("LDA", LDA_C), ("PBE", PBE_C)]:
        B, G, E, mu, H = mechanical_properties(ec)
        writer.writerow([name, f"{B:.2f}", f"{G:.2f}", f"{E:.2f}",
                         f"{mu:.4f}", f"{H:.4f}"])
    pl2 = [(l + p) / 2.0 for l, p in zip(LDA_C, PBE_C)]
    B, G, E, mu, H = mechanical_properties(pl2)
    writer.writerow(["PL/2", f"{B:.2f}", f"{G:.2f}", f"{E:.2f}",
                     f"{mu:.4f}", f"{H:.4f}"])

def write_acoustic():
    writer = csv.writer(sys.stdout)
    writer.writerow(["functional", "v_s", "v_p", "v_avg",
                     "Theta_D", "gamma_a"])
    # LDA
    B, G, _, _, _ = mechanical_properties(LDA_C)
    v_s, v_p, v_avg, Theta_D, gamma_a = acoustic_properties(B, G, LDA_VOL)
    writer.writerow(["LDA", f"{v_s:.2f}", f"{v_p:.2f}", f"{v_avg:.2f}",
                     f"{Theta_D:.2f}", f"{gamma_a:.4f}"])
    # PBE
    B, G, _, _, _ = mechanical_properties(PBE_C)
    v_s, v_p, v_avg, Theta_D, gamma_a = acoustic_properties(B, G, PBE_VOL)
    writer.writerow(["PBE", f"{v_s:.2f}", f"{v_p:.2f}", f"{v_avg:.2f}",
                     f"{Theta_D:.2f}", f"{gamma_a:.4f}"])
    # PL/2
    pl2 = [(l + p) / 2.0 for l, p in zip(LDA_C, PBE_C)]
    B, G, _, _, _ = mechanical_properties(pl2)
    v_s, v_p, v_avg, Theta_D, gamma_a = acoustic_properties(B, G, PL2_VOL)
    writer.writerow(["PL/2", f"{v_s:.2f}", f"{v_p:.2f}", f"{v_avg:.2f}",
                     f"{Theta_D:.2f}", f"{gamma_a:.4f}"])

# ----------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: compute.py <elastic|mechanical|acoustic>")
    mode = sys.argv[1]
    if mode == "elastic":
        write_elastic()
    elif mode == "mechanical":
        write_mechanical()
    elif mode == "acoustic":
        write_acoustic()
    else:
        sys.exit("Unknown mode")
