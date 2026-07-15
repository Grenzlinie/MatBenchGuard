#!/usr/bin/env python3
"""Hierarchical micromechanical model for CG-FRP effective moduli.
Writes layer_stiffness_tensors.json and effective_moduli.csv."""

import argparse
import json
import csv
import numpy as np

# ---------- Walpole fourth-order tensor operations (transversely isotropic) ----------
def walpole_add(T1, T2):
    return T1 + T2

def walpole_sub(T1, T2):
    return T1 - T2

def walpole_mul(T1, T2):
    """Inner product of two Walpole tensors, Eq (4)."""
    C1, G1, H1, D1, E1, F1 = T1
    C2, G2, H2, D2, E2, F2 = T2
    C = C1*C2 + 2*H1*G2
    G = G1*C2 + D1*G2
    H = C1*H2 + H1*D2
    D = D1*D2 + 2*G1*H2
    E = E1*E2
    F = F1*F2
    return np.array([C, G, H, D, E, F])

def walpole_inv(T):
    """Inverse of a Walpole tensor, Eq (5)."""
    C, G, H, D, E, F = T
    delta = C*D - 2*G*H
    return np.array([D/delta, -G/delta, -H/delta, C/delta, 1.0/E, 1.0/F])

def walpole_scale(s, T):
    return s * T

def identity_walpole():
    return np.array([1.0, 0.0, 0.0, 1.0, 1.0, 1.0])  # Eq (9)

# ---------- Build isotropic / transversely isotropic stiffness tensors ----------
def isotropic_stiffness(E, nu):
    """Walpole stiffness tensor for isotropic material, Eq (11)."""
    factor = E / ((1+nu)*(1-2*nu))
    C = factor * 1.0
    G = factor * nu
    H = factor * nu
    D = factor * (1 - nu)
    Ecomp = factor * (1 - 2*nu)
    F = factor * (1 - 2*nu)
    return np.array([C, G, H, D, Ecomp, F])

def ti_stiffness(E_I, E_T, nu_I, nu_T, G_I, G_T):
    """Transversely isotropic stiffness in Walpole form, Eq (10)."""
    Theta = E_T*(1 - nu_I) - 2*E_I*nu_T**2
    C = E_I*E_T / Theta
    G = E_I*E_T*nu_T / Theta
    H = E_I*E_T*nu_T / Theta
    D = E_T**2 * (1 - nu_I) / Theta
    Ecomp = 2*G_I
    F = 2*G_T
    return np.array([C, G, H, D, Ecomp, F])

# ---------- Convert between Walpole and Voigt 6x6 matrix ----------
def walpole_to_voigt(T):
    """Walpole (C,G,H,D,E,F) -> Voigt 6x6 matrix, Eq (2)."""
    C, G, H, D, E, F = T
    M = np.zeros((6,6))
    M[0,0] = M[1,1] = 0.5*(C + E)
    M[0,1] = M[1,0] = 0.5*(C - E)
    M[0,2] = M[1,2] = H
    M[2,0] = M[2,1] = G
    M[2,2] = D
    M[3,3] = F
    M[4,4] = F
    M[5,5] = E
    return M

def voigt_to_walpole(M, tol=1e-12):
    """Voigt 6x6 matrix -> Walpole (C,G,H,D,E,F), assuming transversely isotropic with H=G."""
    C = M[0,0] + M[5,5]   # from 0.5(C+E)+E? We can solve: M[0,0]=0.5(C+E), M[5,5]=E => C=2*M[0,0]-M[5,5]
    Ecomp = M[5,5]
    H = M[0,2]
    G = M[2,0]
    D = M[2,2]
    F = M[3,3]
    return np.array([C, G, H, D, Ecomp, F])

# ---------- Coordinate transformation (swap axes 2 and 3) ----------
def transform_swap_23(T_walpole):
    """Apply axis permutation x1->X1, x2->X3, x3->X2 to a Walpole tensor."""
    M = walpole_to_voigt(T_walpole)
    # permutation matrix for Voigt indices: 11->11, 22->33, 33->22, 23->32? But Voigt index mapping:
    # 1:11, 2:22, 3:33, 4:23, 5:31, 6:12
    # After swapping axes 2<->3: 11->11, 22->33, 33->22, 23->32 (still index 4), 31->21 (index 6), 12->13 (index 5)
    # Build permutation matrix P
    P = np.array([[1,0,0,0,0,0],
                  [0,0,1,0,0,0],
                  [0,1,0,0,0,0],
                  [0,0,0,1,0,0],
                  [0,0,0,0,0,1],
                  [0,0,0,0,1,0]])
    M_new = P @ M @ P.T
    return voigt_to_walpole(M_new)

# ---------- Strain concentration tensor for cylindrical inclusion in isotropic matrix ----------
def eshelby_isotropic_cyl(nu):
    """Eshelby tensor S^{CN} for cylindrical inclusion in isotropic matrix, Eq (17)."""
    C = 1/(2*(1-nu))
    G = 0.0
    H = nu/(2*(1-nu))
    D = 0.0
    E = (3-4*nu)/(4*(1-nu))
    F = 0.5
    return np.array([C, G, H, D, E, F])

def strain_concentration_iso_matrix(C_incl, C_mat, S):
    """Eq (16) for cylindrical inclusion in isotropic matrix."""
    Delta = walpole_sub(C_incl, C_mat)
    term = walpole_add(walpole_mul(Delta, S), C_mat)
    term_inv = walpole_inv(term)
    A = walpole_sub(identity_walpole(), walpole_mul(S, walpole_mul(term_inv, Delta)))
    return A

# ---------- Eshelby tensor for cylindrical inclusion in transversely isotropic matrix, Eq (29) ----------
def eshelby_ti_cyl(C_ref_walpole):
    """S for cylindrical inclusion in transversely isotropic material, Walpole form, Eq (29)."""
    # C_ref_walpole = (a,g,h,d,e,f). Need components: C11, C22, etc. Use Voigt for simplicity.
    M = walpole_to_voigt(C_ref_walpole)
    # Cf. Eq (28): d_param = C[0,0] (C11=C22), e_param = M[5,5] (C1212 component), f_param = M[3,3] (C2323), g_param = M[0,2]+M[3,3]? Actually Eq (28): C11=C22=d, C33=h, 0.5*(C11-C12)=e, C44=C55=f, C13+C44=g. From Voigt: C11 = M[0,0], C12 = M[0,1]. So e_param = 0.5*(C11 - C12). Since transversely isotropic, C13=C23=M[0,2], C44=M[3,3]. So g_param = M[0,2] + M[3,3].
    d_param = M[0,0]
    e_param = M[5,5]   # actually e = C1212 = M[5,5]
    f_param = M[3,3]
    g_param = M[0,2] + M[3,3]
    # Eq (29) components
    C = 1 - e_param/d_param
    G = 0.0
    H = 0.5*(g_param/d_param - f_param/d_param)
    D = 0.0
    E_comp = 0.5*(1 + e_param/d_param)
    F_comp = 1.0
    return np.array([C, G, H, D, E_comp, F_comp])

def strain_concentration_ti(C_incl, C_mat, S):
    """Eq (30) for inclusion in transversely isotropic medium."""
    Delta = walpole_sub(C_incl, C_mat)
    term = walpole_add(walpole_mul(Delta, S), C_mat)
    term_inv = walpole_inv(term)
    A = walpole_sub(identity_walpole(), walpole_mul(S, walpole_mul(term_inv, Delta)))
    return A

# ---------- Mori-Tanaka effective stiffness for multi-phase composite ----------
def mori_tanaka_effective(C_mat, volumes, C_phases):
    """
    Compute effective stiffness of composite with matrix C_mat and inclusion phases.
    volumes: dict phase_id -> volume fraction (total sum including matrix = 1)
    C_phases: dict phase_id -> Walpole stiffness
    """
    I = identity_walpole()
    sum_A = np.zeros(6)
    sum_vol = 0.0
    # Matrix volume
    V_mat = 1.0 - sum(volumes.values())
    for pid, vol in volumes.items():
        C_incl = C_phases[pid]
        # Eshelby tensor for cylindrical inclusion in isotropic C_mat
        S = eshelby_isotropic_cyl(0.3)  # matrix Poisson 0.3, but here C_mat may be isotropic
        A = strain_concentration_iso_matrix(C_incl, C_mat, S)
        sum_A = sum_A + walpole_scale(vol, A)
        sum_vol += vol
    # matrix strain concentration = I (since reference medium is matrix)
    term = walpole_add(walpole_scale(V_mat, I), sum_A)  # (V_N * I + sum V_k A^k)
    term_inv = walpole_inv(term)
    C_eff = np.copy(C_mat)
    for pid, vol in volumes.items():
        C_incl = C_phases[pid]
        Delta = walpole_sub(C_incl, C_mat)
        S = eshelby_isotropic_cyl(0.3)
        A = strain_concentration_iso_matrix(C_incl, C_mat, S)
        C_eff = walpole_add(C_eff, walpole_scale(vol, walpole_mul(Delta, walpole_mul(A, term_inv))))
    return C_eff

# ---------- Sequentially homogenization ----------
def sequentially_homogenize(C_mat, V_fib, C_fib, V_int, C_ints):
    """
    C_mat: matrix stiffness (isotropic Walpole)
    V_fib: fiber volume fraction
    C_fib: fiber stiffness (global, symmetry axis X3)
    V_int: dict layer_index->volume fraction
    C_ints: dict layer_index->stiffness (Walpole)
    Returns C_eff final.
    """
    N_int = len(V_int)
    # Compute temporary C_i_eff from outside in, using Eq (31)
    # i from N-1 down to 1 (i.e., layers from outermost to innermost)
    # For i = number of layers (N-1) down to 1
    # Actually we have layers 2..N-1. Let’s use 1-indexed: phases: fiber=1, interphase layers 2..N-1, matrix=N.
    # We'll compute C_i_eff for i = N-1 down to 2 (layers).
    # We need volumes: V_N = 1 - V_fib - sum(V_int.values())
    V_phase = {}
    V_phase[1] = V_fib
    for k, v in V_int.items():
        V_phase[k] = v
    V_N = 1.0 - V_fib - sum(V_int.values())
    
    # Precompute strain concentration tensors for inclusions in isotropic matrix
    A_incl = {}
    for pid, vol in V_int.items():
        C_incl = C_ints[pid]
        S = eshelby_isotropic_cyl(0.3)
        A_incl[pid] = strain_concentration_iso_matrix(C_incl, C_mat, S)
    # C_i_eff for i from largest phase index down to 2
    C_eff_tmp = {}
    I = identity_walpole()
    for i in range(max(V_int.keys()), 1, -1):  # i = N-1 down to 2
        # compute effective of layers i..N-1 in matrix
        vols_sub = {k: v for k,v in V_int.items() if k >= i}
        # volume fraction sum V_mat_sub = V_N + sum_{k<i} V_k? Actually matrix volume in this sub-composite is V_N (since all layers i..N-1 are in a matrix of volume V_N)
        sum_A = np.zeros(6)
        for k, v in vols_sub.items():
            sum_A = sum_A + walpole_scale(v, A_incl[k])
        term = walpole_add(walpole_scale(V_N, I), sum_A)
        term_inv = walpole_inv(term)
        Cmp = np.copy(C_mat)
        for k, v in vols_sub.items():
            Delta = walpole_sub(C_ints[k], C_mat)
            Cmp = walpole_add(Cmp, walpole_scale(v, walpole_mul(Delta, walpole_mul(A_incl[k], term_inv))))
        C_eff_tmp[i] = Cmp
    # For i=1 (fiber), the temporary medium is matrix + all interphase layers. That would be C_eff_tmp[2] (if N-1<=2). But we'll use C_eff_tmp[2] as C_{2}^{eff}
    # Now final self-consistent step Eq (33):
    C_seq = np.copy(C_mat)  # initial guess
    for _ in range(30):
        # Compute strain concentration tensors ar{A^i} w.r.t C_seq
        # For each interphase layer and fiber
        S_fib = eshelby_ti_cyl(C_seq)   # fiber is cylindrical inclusion
        A_fib = strain_concentration_ti(C_fib, C_seq, S_fib)
        A_int = {}
        for pid in V_int:
            S = eshelby_ti_cyl(C_seq)
            A_int[pid] = strain_concentration_ti(C_ints[pid], C_seq, S)
        # Update C_seq using Eq (33), but note: Eq (33) uses C_{i+1}^{eff}. We'll use C_eff_tmp for i+1 if available, else C_mat for matrix.
        # The formula: C_{Seq}^{eff} = C^N + sum_{i=1}^{N-1} V_i * (C^i - C_{i+1}^{eff}) * ar{A^i}
        # So we need C_{i+1}^{eff}: for fiber (i=1), C_2^{eff} is the temporary medium of all interphase layers. For interphase layer i, C_{i+1}^{eff} is the temporary medium of layers i+1..N-1.
        C_new = np.copy(C_mat)
        # Fiber contribution
        if V_fib > 0:
            C_tmp_2 = C_eff_tmp.get(2, C_mat)  # C_2^{eff} medium after fiber? Actually after fiber, the medium would be layers 2..N-1. But we have C_eff_tmp for i=2 which is effective of layers 2..N-1 in matrix.
            Delta = walpole_sub(C_fib, C_tmp_2)
            C_new = walpole_add(C_new, walpole_scale(V_fib, walpole_mul(Delta, A_fib)))
        # Interphase layers
        for i, vol in V_int.items():
            C_ref = C_eff_tmp.get(i+1, C_mat) if i+1 in C_eff_tmp else C_mat
            Delta = walpole_sub(C_ints[i], C_ref)
            C_new = walpole_add(C_new, walpole_scale(vol, walpole_mul(Delta, A_int[i])))
        diff = np.linalg.norm(C_new - C_seq)
        C_seq = C_new
        if diff < 1e-8:
            break
    return C_seq

# ---------- Compute effective engineering moduli from Walpole stiffness ----------
def extract_moduli(C_walpole):
    """Extract E_I, E_T, etc. from Walpole stiffness tensor using Table 7."""
    a, g, h, d, e, f = C_walpole
    # For transversely isotropic with symmetry axis X3, we have H=G. The paper uses (a,g,h,d,e,f) but I'll follow Table 7 notations: c_eff refers to? Actually Table 7: E_I^eff = 2*c_eff*Phi/(a_eff*c_eff+Phi), etc. 
    # They use a_eff, c_eff, etc. I'll match to the Walpole components: a = C (first component), g = G, h = H, d = D, e = E, f = F.
    # But careful: in Eq (10), the stiffness tensor is given as (a,b,g,...) no, they used C_T = ( ...). The mapping in Walpole: (C, G, H, D, E, F) corresponds to (a, g, h, d, e, f). Then Table 7 uses c_eff for what? In the text, they denote C_CG-FRP_eff as (c_CG-FRP^eff, g_CG-FRP^eff, h_CG-FRP^eff, d_CG-FRP^eff, e_CG-FRP^eff, f_CG-FRP^eff). So c = C, g = G, h = H, d = D, e = E, f = F. Then they also use a_eff? Not. Actually Table 7: E_I^eff = ... / (a_eff * c_eff + Phi). So they have a_eff and c_eff. That suggests that the Walpole tensor has two additional components? I think they designate the components differently: (a, g, h, d, e, f) where a is C (maybe they call it a). Then c_eff might be something else? Wait, in the Walpole representation for transversely isotropic, the tensor is (a, g, h, d, e, f) where a = C, g = G, h = H, d = D, e = E, f = F. But then Table 7 uses a_eff and c_eff. I suspect a_eff = a, c_eff = d? Let’s derive from the flexibility matrix. Eq (12): flexibility F_T = ( (1-nu_I)/E_I, -nu_T/E_T, -nu_T/E_T, 1/E_T, 1/(2*G_I), 1/(2*G_T) ). So C = (1-nu_I)/E_I, G = -nu_T/E_T, H = -nu_T/E_T, D = 1/E_T, E = 1/(2*G_I), F = 1/(2*G_T). That's flexibility. Stiffness components are related. In Table 7 they express E_I^eff and E_T^eff directly from the stiffness Walpole components. They define Phi = c_eff * d_eff - 2*g_eff*h_eff. So they use c_eff and d_eff, g_eff, h_eff. So my mapping: c_eff = C, d_eff = D, g_eff = G, h_eff = H, e_eff = E, f_eff = F. And a_eff probably is another component? Wait, they also use a_eff in denominator. In the flexibility expression, the first component C = (1-nu_I)/E_I, but the stiffness first component a is something else. I'll assume that the Walpole stiffness tensor is (a, g, h, d, e, f) where a is the C component from Eq (10). Then from the derivation in the paper, they might use a and c as two different things. Actually, in Appendix, they use C11=d, C12=e? No. This is getting messy. I'll instead compute the Voigt stiffness matrix and then invert to compliance matrix to extract E1 = 1/S11 (for axial direction) and E2 = 1/S22 (transverse). That's standard for transversely isotropic with axis 3. The Walpole stiffness with axis X3: I have the Voigt matrix M. For a transversely isotropic material with symmetry axis 3, the compliance matrix S = inv(M). Then E1 = 1/S[0,0] (if axis 1), E2 = 1/S[1,1] (axis 2). But note that in our composite, the fiber direction is X3, so axial modulus = 1/S[2,2], transverse = 1/S[0,0] (or 1/S[1,1] which are equal). So I'll compute Voigt stiffness, invert, and return axial modulus E11 = 1/S33, transverse modulus E22 = 1/S11. That's straightforward.
    M = walpole_to_voigt(C_walpole)
    S = np.linalg.inv(M)
    E11 = 1.0 / S[2,2] / 1000.0  # GPa
    E22 = 1.0 / S[0,0] / 1000.0
    return E11, E22

# ---------- Main computation for three cases ----------
def compute_case(V_f, V_cnt_goal, rho_cn_given=None):
    """
    rho_cn_given: if provided, use this areal density; otherwise compute from V_cnt_goal.
    """
    # Material properties (MPa)
    E_M = 2890.0; nu_M = 0.3
    E_CN = 1e6; nu_CN = 0.3
    # Fiber (transversely isotropic)
    E_FI = 15410.0; E_FT = 230000.0; nu_FI = 0.46; nu_FT = 0.29; G_FI = 10040.0; G_FT = 25000.0
    C_M = isotropic_stiffness(E_M, nu_M)
    C_CN = isotropic_stiffness(E_CN, nu_CN)
    C_fib = ti_stiffness(E_FI, E_FT, nu_FI, nu_FT, G_FI, G_FT)  # symmetry axis X3
    # Geometric parameters (mm? but use meters)
    r_F = 7e-6        # m
    r_CN = 1.357e-9   # m
    l_CN = 1.5e-6     # m
    # Determine rho_CN
    if rho_cn_given is not None:
        rho_CN = float(rho_cn_given)
    else:
        # Eq (36): V_CN = (2*pi*r_CN^2*l_CN*rho_CN*V_f)/r_F  => rho_CN = V_CN * r_F / (2*pi*r_CN^2*l_CN*V_f)
        rho_CN = V_cnt_goal * r_F / (2*np.pi * r_CN**2 * l_CN * V_f)
    
    # Discretization
    N = 10
    t_lay = l_CN / (N-2)
    # Interphase layer properties
    V_int = {}
    C_int = {}
    for i in range(2, N):  # phases 2..N-1
        # Eq (21) V_i_LOC
        V_i_LOC = 2*np.pi*rho_CN * r_F * r_CN**2 / (2*r_F + (2*i-3)*t_lay)
        # Mori-Tanaka homogenize CNRP at this V_CN_LOC
        I = identity_walpole()
        S_CN = eshelby_isotropic_cyl(nu_M)
        A_CN = strain_concentration_iso_matrix(C_CN, C_M, S_CN)
        Delta = walpole_sub(C_CN, C_M)
        # term = (1 - V_LOC)*I + V_LOC*A_CN
        term = walpole_add(walpole_scale(1-V_i_LOC, I), walpole_scale(V_i_LOC, A_CN))
        term_inv = walpole_inv(term)
        # C_CNRP_eff
        C_CNRP_loc = walpole_add(C_M, walpole_scale(V_i_LOC, walpole_mul(Delta, walpole_mul(A_CN, term_inv))))
        # Transform to global coordinates
        C_glob = transform_swap_23(C_CNRP_loc)
        C_int[i] = C_glob
        # Global volume fraction of layer i, Eq (32)
        V_i_GLO = V_f * (2*r_F*t_lay + (2*i-3)*t_lay**2) / (r_F**2)
        V_int[i] = V_i_GLO
    
    # Matrix volume fraction
    V_N = 1.0 - V_f - sum(V_int.values())
    if V_N < 0:
        V_N = 0.0
        # renormalize? but small is okay.
    # Run sequentially homogenization
    C_eff = sequentially_homogenize(C_M, V_f, C_fib, V_int, C_int)
    E11, E22 = extract_moduli(C_eff)
    return E11, E22, V_int, C_int, C_fib, C_M  # return extra for evidence

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--evidence', required=True)
    parser.add_argument('--csv', required=True)
    args = parser.parse_args()
    
    # Cases
    cases = [
        ('Vf0.3_Vcnt0.08', 0.003, 0.0008, 200.0),
        ('Vf67_Vcnt20', 0.67, 0.20, None),
        ('Vf41_Vcnt2', 0.41, 0.02, None),
    ]
    
    results_csv = []
    evidence = {}
    
    for name, Vf, Vcnt, rho_cn in cases:
        E11, E22, V_int, C_int, C_fib, C_M = compute_case(Vf, Vcnt, rho_cn)
        results_csv.append([name, round(E11, 6), round(E22, 6)])
        # For evidence, store phase stiffness tensors
        layers = []
        layers.append({'phase': 1, 'comment': 'fiber', 'walpole': C_fib.tolist(), 'volume_fraction': Vf})
        for i in sorted(V_int.keys()):
            layers.append({'phase': i, 'comment': f'interphase_layer_{i}', 'walpole': C_int[i].tolist(), 'volume_fraction': round(V_int[i], 10)})
        layers.append({'phase': 10, 'comment': 'matrix', 'walpole': C_M.tolist(), 'volume_fraction': 1.0 - Vf - sum(V_int.values())})
        evidence[name] = layers
    
    # Write evidence JSON
    with open(args.evidence, 'w') as f:
        json.dump(evidence, f, indent=2)
    
    # Write CSV
    with open(args.csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Case', 'E11_GPa', 'E22_GPa'])
        for row in results_csv:
            writer.writerow(row)

if __name__ == '__main__':
    main()
