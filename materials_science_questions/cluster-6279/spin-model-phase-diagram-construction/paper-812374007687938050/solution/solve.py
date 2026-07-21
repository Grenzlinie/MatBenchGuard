#!/usr/bin/env python3
import sys, csv, argparse
import numpy as np

# ---------- 1-ACA self-consistency solver ----------
def solve_system(N, c_v, y, J_AB, D, max_iter=5000, tol=1e-7):
    J_AA = 1.0
    J_BB = 0.1
    N = len(c_v)
    m_A = 0.5 * np.ones(N)
    m_B = 0.25 * np.ones(N)
    for it in range(max_iter):
        h_A = np.zeros(N)
        h_B = np.zeros(N)
        for v in range(N):
            # in-plane 4 neighbours
            in_A = 4.0 * (c_v[v] * J_AA * m_A[v] + (1.0 - c_v[v]) * J_AB * m_B[v])
            in_B = 4.0 * (c_v[v] * J_AB * m_A[v] + (1.0 - c_v[v]) * J_BB * m_B[v])
            # out-of-plane v-1
            if v > 0:
                cm = c_v[v-1]
                out_A_p = cm * J_AA * m_A[v-1] + (1.0 - cm) * J_AB * m_B[v-1]
                out_B_p = cm * J_AB * m_A[v-1] + (1.0 - cm) * J_BB * m_B[v-1]
            else:
                out_A_p = 0.0
                out_B_p = 0.0
            # out-of-plane v+1
            if v < N-1:
                cp = c_v[v+1]
                out_A_n = cp * J_AA * m_A[v+1] + (1.0 - cp) * J_AB * m_B[v+1]
                out_B_n = cp * J_AB * m_A[v+1] + (1.0 - cp) * J_BB * m_B[v+1]
            else:
                out_A_n = 0.0
                out_B_n = 0.0
            h_A[v] = in_A + out_A_p + out_A_n
            h_B[v] = in_B + out_B_p + out_B_n
        # thermal functions
        expD = np.exp(D / y)
        hA_div = np.clip(h_A / y, -100.0, 100.0)
        hB_div = np.clip(h_B / y, -100.0, 100.0)
        # spin-1
        sinh_A = np.sinh(hA_div)
        cosh_A = np.cosh(hA_div)
        denom_A = 1.0 + 2.0 * expD * cosh_A
        new_m_A = 2.0 * expD * sinh_A / denom_A
        # spin-1/2
        new_m_B = 0.5 * np.tanh(0.5 * hB_div)

        if it > 0:
            diff = max(
                np.max(np.abs(new_m_A - old_m_A)),
                np.max(np.abs(new_m_B - old_m_B))
            )
            if diff < tol:
                break
        old_m_A = m_A.copy()
        old_m_B = m_B.copy()
        m_A = 0.5 * old_m_A + 0.5 * new_m_A
        m_B = 0.5 * old_m_B + 0.5 * new_m_B
    return m_A, m_B

# ---------- MDP CSV generation ----------
def generate_mdp():
    # layers: 6 layers (c=0.75), 2 DLI (c=0.8), 3 B (c=0.0), 2 DLI (c=0.8), 6 layers (c=0.75)
    N = 6 + 2 + 3 + 2 + 6  # =19
    c_v = np.concatenate([
        np.full(6, 0.75),
        np.full(2, 0.80),
        np.full(3, 0.00),
        np.full(2, 0.80),
        np.full(6, 0.75),
    ])
    y_list = [0.5, 1.5, 2.5, 3.5, 4.5]
    D_scalar = 1.0
    J_AB_scalar = 4.0
    with open(f"{OUTDIR}/magnetisation_depth_profile.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['layer_index', 'reduced_temperature', 'concentration_c', 'm_v'])
        for y in y_list:
            m_A, m_B = solve_system(N, c_v, y, J_AB_scalar, D_scalar)
            m = c_v * m_A + (1.0 - c_v) * m_B
            concentration_c = 0.8   # fixed interface concentration for this run
            for v in range(N):
                writer.writerow([v, y, concentration_c, m[v]])

# ---------- Phase diagram boundary CSV ----------
def find_boundary(c_interface, y, c_v_template, D=1.0):
    N = len(c_v_template)
    J_scan = np.linspace(0.0, 10.0, 501)
    f_vals = []
    for J_AB in J_scan:
        c_v = c_v_template.copy()
        c_v[5] = c_v[6] = c_v[10] = c_v[11] = c_interface
        m_A, m_B = solve_system(N, c_v, y, J_AB, D)
        m = c_v * m_A + (1.0 - c_v) * m_B
        diff = (m[5] + m[6]) / 2.0 - m[2]
        f_vals.append(diff)
    f_array = np.array(f_vals)
    sign_changes = np.where(np.diff(np.sign(f_array)))[0]
    roots = []
    for i in sign_changes:
        J1, J2 = J_scan[i], J_scan[i+1]
        f1, f2 = f_array[i], f_array[i+1]
        if abs(f1 - f2) < 1e-15:
            continue
        J_root = J1 - f1 * (J2 - J1) / (f2 - f1)
        roots.append(J_root)
    return roots

def generate_phase_boundary():
    # structure: A(5) 0-4 (c=0.9), DLI 5,6 (c variable), B 7-9 (c=0), DLI 10,11 (c variable), A'(5) 12-16 (c=0.9)
    N = 5 + 2 + 3 + 2 + 5  # =17
    c_v_template = np.concatenate([
        np.full(5, 0.9),
        np.full(2, np.nan),   # to be filled per c
        np.full(3, 0.0),
        np.full(2, np.nan),
        np.full(5, 0.9),
    ])
    y_list = [1.5, 2.0, 2.2, 2.5]
    c_grid = np.arange(0.0, 1.01, 0.01)
    with open(f"{OUTDIR}/phase_diagram_boundary.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['reduced_temperature', 'concentration_c', 'J_AB_over_J'])
        for y in y_list:
            for c_iface in c_grid:
                roots = find_boundary(c_iface, y, c_v_template)
                if roots:
                    J_root = roots[0]   # take first root
                    writer.writerow([y, c_iface, J_root])

# ---------- main ----------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True,
                        choices=['magnetisation_depth_profile.csv', 'phase_diagram_boundary.csv'])
    args = parser.parse_args()
    OUTDIR = '/app/outputs'
    if args.output == 'magnetisation_depth_profile.csv':
        generate_mdp()
    elif args.output == 'phase_diagram_boundary.csv':
        generate_phase_boundary()
