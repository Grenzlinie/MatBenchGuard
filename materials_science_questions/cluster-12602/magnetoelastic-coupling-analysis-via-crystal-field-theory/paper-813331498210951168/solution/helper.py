#!/usr/bin/env python3
"""Helper to compute quadrupole susceptibilities and elastic constants."""
import sys
import numpy as np

# --- angular momentum matrices for J=4 ---
J = 4
m = np.arange(-J, J+1)
Jz = np.diag(m.astype(complex))
Jplus = np.diag([np.sqrt((J - m[i]) * (J + m[i] + 1)) for i in range(1, 2*J+1)], k=1).astype(complex)
Jminus = Jplus.conj().T
Jx = (Jplus + Jminus) / 2
Jy = (Jplus - Jminus) / 2j

# --- Stevens operators (hard‑coded diagonal of O40 and O60 for J=4) ---
# O_4^0 diagonal in |J,m> basis
O40_diag = np.array([840, 30, -480, -690, -720, -690, -480, 30, 840], dtype=complex)
O40 = np.diag(O40_diag)

# O_4^4 = 1/2 (J_+^4 + J_-^4)
Jplus4 = np.linalg.matrix_power(Jplus, 4)
Jminus4 = np.linalg.matrix_power(Jminus, 4)
O44 = (Jplus4 + Jminus4) / 2

# O_6^0 diagonal in |J,m> basis
O60_diag = np.array([80640, -21120, -37440, -2400, 14400, -2400, -37440, -21120, 80640], dtype=complex)
O60 = np.diag(O60_diag)

# O_6^4 = 1/4 { (J_+^4+J_-^4), (11 J_z^2 - J(J+1) - 38) }
B_poly = 11 * (Jz @ Jz) - J*(J+1)*np.eye(2*J+1) - 38*np.eye(2*J+1)
A_poly = Jplus4 + Jminus4
O64 = 0.25 * (A_poly @ B_poly + B_poly @ A_poly)

# --- quadrupole operators ---
# O_v = J_x^2 - J_y^2 = (J_+^2 + J_-^2)/2
O_v = (np.linalg.matrix_power(Jplus, 2) + np.linalg.matrix_power(Jminus, 2)) / 2
# O_zx = J_z J_x + J_x J_z
O_zx = Jz @ Jx + Jx @ Jz

# --- site parameters ---
# 4a site
B4_4a = 2.570e-2
B6_4a = -3.860e-4
# 8c site
B4_8c = 2.243e-2
B6_8c = -4.363e-4

# total Pr3+ number density N (m^-3)
N = 6.225e27
N_4a = N / 3.0
N_8c = 2.0 * N / 3.0

# background and coupling constants for Gamma3 ( (C11-C12)/2 )
bg_Gamma3 = {'a': 3.717e10, 'b': -1e7, 'c': -9e3}
g_Gamma3 = {'4a': 30, '8c': 90}
gp_Gamma3 = {'4a': 0.0, '8c': -0.036}

# background and coupling constants for Gamma5 ( C44 )
bg_Gamma5 = {'a': 3.585e10, 'b': -1e3, 'c': -3.5e4}
g_Gamma5 = {'4a': 31, '8c': 13}
gp_Gamma5 = {'4a': 0.013, '8c': -0.030}

def build_cef(B4, B6):
    return B4 * (O40 + 5*O44) + B6 * (O60 - 21*O64)

def group_degenerate(energies, tol=1e-6):
    order = np.argsort(energies)
    groups = []
    current_E = None
    for idx in order:
        e = energies[idx]
        if current_E is None or abs(e - current_E) > tol:
            if current_E is not None:
                groups.append(current_group)
            current_group = [idx]
            current_E = e
        else:
            current_group.append(idx)
    if current_group:
        groups.append(current_group)
    return groups

def quadrupole_susceptibility(energies, V, O_op, temps):
    """
    Compute -χ_Γ for operator O_op at given temperatures.
    Returns array of length len(temps).
    """
    O_cef = V.conj().T @ O_op @ V
    groups = group_degenerate(energies)
    # Build unitary U that diagonalizes each degenerate block
    U = np.eye(len(energies), dtype=complex)
    for group_inds in groups:
        if len(group_inds) == 1:
            continue
        inds = np.array(group_inds)
        sub = O_cef[np.ix_(inds, inds)]
        _, W = np.linalg.eigh(sub)
        U[np.ix_(inds, inds)] = W
    O_tilde = U.conj().T @ O_cef @ U
    # assign energy for each state after transformation (same as original group energy)
    energies_t = np.zeros(len(energies))
    for group_inds in groups:
        e_val = energies[group_inds[0]]
        for idx in group_inds:
            energies_t[idx] = e_val
    diag_vals = np.real(np.diag(O_tilde))
    negchi = np.zeros_like(temps)
    for iT, T in enumerate(temps):
        Z = np.sum(np.exp(-energies_t / T))
        p = np.exp(-energies_t / T) / Z
        # van Vleck: sum_i p_i sum_{j, E_j != E_i} 2|O_{ij}|^2 / (E_i - E_j)
        vv = 0.0
        for i in range(len(energies_t)):
            e_i = energies_t[i]
            for j in range(len(energies_t)):
                if energies_t[j] != e_i:
                    vv += p[i] * 2.0 * (abs(O_tilde[i,j])**2) / (e_i - energies_t[j])
        curie = np.sum(p * diag_vals**2) - (np.sum(p * diag_vals))**2
        negchi[iT] = vv - (1.0 / T) * curie
    return negchi

def make_temp_array():
    return np.logspace(np.log10(0.1), np.log10(50), 50)

def main():
    if len(sys.argv) < 3:
        print("Usage: helper.py <mode: susceptibilities|elastic> <outdir>", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    outdir = sys.argv[2]
    import os
    os.makedirs(outdir, exist_ok=True)

    # solve CEF for both sites
    H4a = build_cef(B4_4a, B6_4a)
    E4a, V4a = np.linalg.eigh(H4a)
    H8c = build_cef(B4_8c, B6_8c)
    E8c, V8c = np.linalg.eigh(H8c)

    temps = make_temp_array()

    # susceptibilities
    negchi_Gamma3_4a = quadrupole_susceptibility(E4a, V4a, O_v, temps)
    negchi_Gamma3_8c = quadrupole_susceptibility(E8c, V8c, O_v, temps)
    negchi_Gamma5_4a = quadrupole_susceptibility(E4a, V4a, O_zx, temps)
    negchi_Gamma5_8c = quadrupole_susceptibility(E8c, V8c, O_zx, temps)

    if mode == 'susceptibilities':
        with open(os.path.join(outdir, 'quadrupole_susceptibilities.csv'), 'w') as f:
            f.write('temperature,chi_Gamma3_4a,chi_Gamma3_8c,chi_Gamma5_4a,chi_Gamma5_8c\n')
            for i, T in enumerate(temps):
                f.write(f'{T:.6e},{negchi_Gamma3_4a[i]:.12e},{negchi_Gamma3_8c[i]:.12e},{negchi_Gamma5_4a[i]:.12e},{negchi_Gamma5_8c[i]:.12e}\n')
        return

    if mode == 'elastic':
        # positive chi = - negchi
        chi_Gamma3_4a = -negchi_Gamma3_4a
        chi_Gamma3_8c = -negchi_Gamma3_8c
        chi_Gamma5_4a = -negchi_Gamma5_4a
        chi_Gamma5_8c = -negchi_Gamma5_8c

        C_Gamma3 = np.zeros_like(temps)
        C_Gamma5 = np.zeros_like(temps)
        for i, T in enumerate(temps):
            C0_3 = bg_Gamma3['a'] + bg_Gamma3['b']*T + bg_Gamma3['c']*T*T
            C0_5 = bg_Gamma5['a'] + bg_Gamma5['b']*T + bg_Gamma5['c']*T*T
            term_3_4a = (g_Gamma3['4a']**2 * chi_Gamma3_4a[i]) / (1 - gp_Gamma3['4a'] * chi_Gamma3_4a[i])
            term_3_8c = (g_Gamma3['8c']**2 * chi_Gamma3_8c[i]) / (1 - gp_Gamma3['8c'] * chi_Gamma3_8c[i])
            term_5_4a = (g_Gamma5['4a']**2 * chi_Gamma5_4a[i]) / (1 - gp_Gamma5['4a'] * chi_Gamma5_4a[i])
            term_5_8c = (g_Gamma5['8c']**2 * chi_Gamma5_8c[i]) / (1 - gp_Gamma5['8c'] * chi_Gamma5_8c[i])
            C_Gamma3[i] = C0_3 - N_4a * term_3_4a - N_8c * term_3_8c
            C_Gamma5[i] = C0_5 - N_4a * term_5_4a - N_8c * term_5_8c
        with open(os.path.join(outdir, 'elastic_constants.csv'), 'w') as f:
            f.write('temperature,C_Gamma3,C_Gamma5\n')
            for i, T in enumerate(temps):
                f.write(f'{T:.6e},{C_Gamma3[i]:.12e},{C_Gamma5[i]:.12e}\n')
        return

    print(f"Unknown mode: {mode}", file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    main()
