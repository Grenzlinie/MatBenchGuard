import numpy as np

C_b = np.array([
    [10, 4, 2.5, 0, 0, 0],
    [4, 10, 2.5, 0, 0, 0],
    [2.5, 2.5, 6, 0, 0, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 3]
], dtype=np.float64)

def voigt_index(i, j):
    if i == j:
        return i
    elif (i == 1 and j == 2) or (i == 2 and j == 1):
        return 3
    elif (i == 0 and j == 2) or (i == 2 and j == 0):
        return 4
    elif (i == 0 and j == 1) or (i == 1 and j == 0):
        return 5
    else:
        raise ValueError("Invalid indices")

def christoffel(C, n):
    Gamma = np.zeros((3,3))
    for i in range(3):
        for k in range(3):
            s = 0.0
            for j in range(3):
                for l in range(3):
                    p = voigt_index(i, j)
                    q = voigt_index(k, l)
                    s += C[p, q] * n[j] * n[l]
            Gamma[i,k] = s
    return Gamma

def split_C(C):
    M = C[np.ix_([0,1,5], [0,1,5])]
    N = C[np.ix_([2,3,4], [2,3,4])]
    P = C[np.ix_([0,1,5], [2,3,4])]
    return M, N, P

def assemble_C(M, N, P):
    C = np.zeros((6,6))
    C[np.ix_([0,1,5], [0,1,5])] = M
    C[np.ix_([2,3,4], [2,3,4])] = N
    C[np.ix_([0,1,5], [2,3,4])] = P
    C[np.ix_([2,3,4], [0,1,5])] = P.T
    return C

def bond_matrix(R):
    a = R
    K = np.zeros((6,6))
    K[0,0] = a[0,0]**2
    K[0,1] = a[0,1]**2
    K[0,2] = a[0,2]**2
    K[0,3] = 2*a[0,1]*a[0,2]
    K[0,4] = 2*a[0,2]*a[0,0]
    K[0,5] = 2*a[0,0]*a[0,1]
    K[1,0] = a[1,0]**2
    K[1,1] = a[1,1]**2
    K[1,2] = a[1,2]**2
    K[1,3] = 2*a[1,1]*a[1,2]
    K[1,4] = 2*a[1,2]*a[1,0]
    K[1,5] = 2*a[1,0]*a[1,1]
    K[2,0] = a[2,0]**2
    K[2,1] = a[2,1]**2
    K[2,2] = a[2,2]**2
    K[2,3] = 2*a[2,1]*a[2,2]
    K[2,4] = 2*a[2,2]*a[2,0]
    K[2,5] = 2*a[2,0]*a[2,1]
    K[3,0] = a[1,0]*a[2,0]
    K[3,1] = a[1,1]*a[2,1]
    K[3,2] = a[1,2]*a[2,2]
    K[3,3] = a[1,1]*a[2,2] + a[1,2]*a[2,1]
    K[3,4] = a[1,2]*a[2,0] + a[1,0]*a[2,2]
    K[3,5] = a[1,0]*a[2,1] + a[1,1]*a[2,0]
    K[4,0] = a[2,0]*a[0,0]
    K[4,1] = a[2,1]*a[0,1]
    K[4,2] = a[2,2]*a[0,2]
    K[4,3] = a[2,1]*a[0,2] + a[2,2]*a[0,1]
    K[4,4] = a[2,2]*a[0,0] + a[2,0]*a[0,2]
    K[4,5] = a[2,0]*a[0,1] + a[2,1]*a[0,0]
    K[5,0] = a[0,0]*a[1,0]
    K[5,1] = a[0,1]*a[1,1]
    K[5,2] = a[0,2]*a[1,2]
    K[5,3] = a[0,1]*a[1,2] + a[0,2]*a[1,1]
    K[5,4] = a[0,2]*a[1,0] + a[0,0]*a[1,2]
    K[5,5] = a[0,0]*a[1,1] + a[0,1]*a[1,0]
    return K

def rotate_stiffness(C, R):
    K = bond_matrix(R)
    return K @ C @ K.T

def rot_matrix_axis_to_x3(axis):
    if axis == 0:  # x1 -> z
        return np.array([[0,0,-1],[0,1,0],[1,0,0]], dtype=np.float64)
    else:
        raise NotImplementedError("Only axis=0 supported")

def generalized_effective(C_b, C_f, h_f):
    Mb, Nb, Pb = split_C(C_b)
    Mf, Nf, Pf = split_C(C_f)
    inv_Nb = np.linalg.inv(Nb)
    inv_Nf = np.linalg.inv(Nf)
    N_e = np.linalg.inv((1-h_f)*inv_Nb + h_f*inv_Nf)
    A_left = (1-h_f)*Pb @ inv_Nb + h_f*Pf @ inv_Nf
    P_e = A_left @ N_e
    term1 = (1-h_f)*(Mb - Pb @ inv_Nb @ Pb.T)
    term2 = h_f*(Mf - Pf @ inv_Nf @ Pf.T)
    B_right = (1-h_f)*inv_Nb @ Pb.T + h_f*inv_Nf @ Pf.T
    M_e = term1 + term2 + A_left @ N_e @ B_right
    return assemble_C(M_e, N_e, P_e)

def linear_slip_effective(C_b, Z):
    Mb, Nb, Pb = split_C(C_b)
    inv_Nb = np.linalg.inv(Nb)
    N_e = np.linalg.inv(inv_Nb + Z)
    P_e = Pb @ inv_Nb @ N_e
    M_e = Mb - Pb @ inv_Nb @ Pb.T + Pb @ inv_Nb @ N_e @ inv_Nb @ Pb.T
    return assemble_C(M_e, N_e, P_e)

def generalized_effective_for_normal(C_b, C_f, h_f, axis=0):
    R = rot_matrix_axis_to_x3(axis)
    C_b_rot = rotate_stiffness(C_b, R)
    C_f_rot = rotate_stiffness(C_f, R)
    C_eff_rot = generalized_effective(C_b_rot, C_f_rot, h_f)
    R_inv = R.T
    return rotate_stiffness(C_eff_rot, R_inv)

def linear_slip_effective_for_normal(C_b, k, h_f, axis=0):
    C_f = k * C_b
    R = rot_matrix_axis_to_x3(axis)
    C_b_rot = rotate_stiffness(C_b, R)
    C_f_rot = rotate_stiffness(C_f, R)
    _, Nf_rot, _ = split_C(C_f_rot)
    Z = h_f * np.linalg.inv(Nf_rot)
    C_l_eff_rot = linear_slip_effective(C_b_rot, Z)
    R_inv = R.T
    return rotate_stiffness(C_l_eff_rot, R_inv)

def error_percentage(C_b, C_eff, C_l_eff):
    num = np.linalg.norm(C_eff - C_l_eff)
    den = np.linalg.norm(C_l_eff - C_b)
    if den == 0:
        return 0.0
    return 100.0 * num / den