import numpy as np
import math
import sys

def compute_for_pressure(p):
    # pressure-dependent exchanges (meV)
    J = 5.5 - 0.14 * p
    J1 = 0.43 + 0.075 * p
    J2 = 3.16 + 0.075 * p
    J3 = 0.91 + 0.075 * p
    # effective coupling (calibrated to produce a self-consistent order)
    C = 2.0 * (J1 + J2 + J3)   # meV
    gmuBH = 0.1158 * 14.0      # meV (g~2, muB~0.0579 meV/T, H=14 T)

    # Diagonal parts of the 4x4 Hamiltonian (basis: |1,1>, |1,0>, |1,-1>, |0,0>)
    J_term = np.diag([J/4, J/4, J/4, -3*J/4])
    H_z_term = -gmuBH * np.diag([1.0, 0.0, -1.0, 0.0])

    # Operator O = S_l^x - S_r^x in the same basis
    O = np.zeros((4,4))
    O[0,1] = 0.5; O[1,0] = 0.5
    O[1,2] = -0.5; O[2,1] = -0.5
    O[0,3] = -np.sqrt(2); O[3,0] = -np.sqrt(2)
    O[2,3] = np.sqrt(2); O[3,2] = np.sqrt(2)

    # Matrices for S_l^z, S_r^z
    Sz_total_diag = np.diag([1.0, 0.0, -1.0, 0.0])
    S_l_z = np.diag([0.5, 0.0, -0.5, 0.0])
    S_r_z = np.diag([0.5, 0.0, -0.5, 0.0])

    # Matrices for S_l^x, S_r^x  (P = S_l^x + S_r^x)
    P_mat = (1/np.sqrt(2)) * np.array([[0,1,0,0],
                                       [1,0,1,0],
                                       [0,1,0,0],
                                       [0,0,0,0]])
    S_l_x = 0.5 * (P_mat + O)
    S_r_x = 0.5 * (P_mat - O)

    # Operator for the y-component of the vector spin chirality
    Y_op = S_l_z @ S_r_x - S_l_x @ S_r_z

    # Self-consistent loop for the staggered field h_s
    h_s = 1.0   # initial guess (meV)
    for _ in range(200):
        H_mat = J_term + H_z_term - h_s * O
        eigvals, eigvecs = np.linalg.eigh(H_mat)
        gs = eigvecs[:, 0]          # ground state
        m_sx = 0.5 * (gs.conj().T @ O @ gs).real
        h_s_new = C * m_sx
        if abs(h_s_new - h_s) < 1e-6:
            break
        h_s = 0.5 * h_s + 0.5 * h_s_new   # damping

    # Compute ordered parts
    m_z = 0.5 * (gs.conj().T @ Sz_total_diag @ gs).real
    ordered = 2.0 * abs(m_sx * m_z)

    # Total chirality magnitude = |<Y_op>|
    total_chirality = abs((gs.conj().T @ Y_op @ gs).real)
    fluctuation = total_chirality - ordered

    # Entanglement entropy
    u = gs[3].real   # C1
    a = gs[0].real   # C2
    c = gs[2].real   # C3
    v = np.sqrt(a**2 + c**2)
    if v > 1e-12:
        f = -a / v
        g = -c / v
    else:
        f = 1.0; g = 0.0
    C_tilde = np.array([[-v*f, u/np.sqrt(2)], [-u/np.sqrt(2), -v*g]])
    M = C_tilde @ C_tilde.T
    qvals = np.linalg.eigvalsh(M)
    qvals = np.clip(qvals, 1e-12, None)
    ent = -np.sum(qvals * np.log(qvals))

    return total_chirality, ordered, fluctuation, ent

if __name__ == "__main__":
    pressures = [0, 2, 4, 6, 8, 10]
    print("pressure_kbar,total_chirality,ordered_contribution,fluctuation_contribution,entanglement_entropy")
    for p in pressures:
        tot, ord_, fluc, ent = compute_for_pressure(p)
        print(f"{p},{tot:.6f},{ord_:.6f},{fluc:.6f},{ent:.6f}")
