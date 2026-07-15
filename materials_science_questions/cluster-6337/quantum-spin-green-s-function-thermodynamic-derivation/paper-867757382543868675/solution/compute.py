import sys
import csv
import math
import numpy as np
from scipy.integrate import solve_ivp

def xi(alpha):
    return 1.0 / (1.0 + alpha**2)

def compute_A1(alpha, D, tau, mu):
    x = xi(alpha)
    term1 = -D**2 * tau * (6.0 * mu**2 * alpha**2 - 1.0) * x**4
    term2 = 2.0 * mu**2 * alpha * D * tau * x**3
    term3 = -D * (mu**2 * alpha**2 - 2.0) * x**2
    term4 = mu**2 * alpha * x
    return term1 + term2 + term3 + term4

def compute_A2(alpha, D, tau, mu):
    x = xi(alpha)
    term1 = 0.5 * mu * alpha * D**2 * tau * (11.0 - 3.0 * mu**2 * alpha**2) * x**4
    term2 = mu * D * tau * (mu**2 * alpha**2 - 1.0) * x**3
    term3 = 3.0 * mu * D * alpha * x**2
    term4 = -mu * x
    return term1 + term2 + term3 + term4

def compute_A3(alpha, D, tau, mu):
    x = xi(alpha)
    term1 = D**2 * tau * (3.0 * mu**2 * alpha**2 + 1.0) * x**4
    term2 = -4.0 * mu**2 * alpha * D * tau * x**3
    term3 = 2.0 * D * x**2
    return term1 + term2 + term3

def compute_tau_c(alpha, D, mu):
    # Eq. (28)
    x = xi(alpha)
    num = -(mu**2 * (alpha**3 - D * alpha**2 + alpha) + 2.0 * D) * (1.0 + alpha**2)**2
    denom = 2.0 * D * mu**2 * (alpha**3 - 3.0 * D * alpha**2 + alpha) + D**2
    if abs(denom) < 1e-30:
        return float('nan')
    return num / denom

def build_G(A1, A2, A3):
    G = np.array([[-A1,  A2,  0.0],
                  [-A2, -A1,  0.0],
                  [ 0.0, 0.0, -A3]])
    return G

def build_L_coefficients():
    # L[ik][a]  where index i: row of Lambda, k: column of Lambda (summed), a: coordinate of psi
    # We'll store as L[i,k,a] tensor
    L = np.zeros((3,3,3))
    xi_val = 1.0  # we will multiply by xi(alpha) externally, but actually L depends on alpha?
    # Actually L contains xi factor. We'll compute L for given alpha inside the ODE function.
    # Here we define the structure without xi factor; later multiply.
    # But it's easier to compute L as function of alpha inside ODE.
    pass

def stability_mode(output_path):
    mu = 0.9
    tau = 1.0
    alpha_grid = np.linspace(0.0, 2.0, 20)
    D_grid = np.linspace(-2.0, 2.0, 20)
    rows = []
    for alpha in alpha_grid:
        for D in D_grid:
            A1 = compute_A1(alpha, D, tau, mu)
            A2 = compute_A2(alpha, D, tau, mu)
            A3 = compute_A3(alpha, D, tau, mu)
            tau_c = compute_tau_c(alpha, D, mu)
            rows.append([alpha, D, A1, A2, A3, tau_c])
    # also add the specific point alpha=0.005, D=0.1 (it may already be in grid; ensure it is)
    # We'll compute it separately and append if not present
    specific_alpha = 0.005
    specific_D = 0.1
    # check if present
    present = any(abs(r[0]-specific_alpha)<1e-9 and abs(r[1]-specific_D)<1e-9 for r in rows)
    if not present:
        A1 = compute_A1(specific_alpha, specific_D, tau, mu)
        A2 = compute_A2(specific_alpha, specific_D, tau, mu)
        A3 = compute_A3(specific_alpha, specific_D, tau, mu)
        tau_c = compute_tau_c(specific_alpha, specific_D, mu)
        rows.append([specific_alpha, specific_D, A1, A2, A3, tau_c])
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['alpha', 'D', 'A1', 'A2', 'A3', 'tau_c'])
        for row in rows:
            # replace NaN with 'NaN' string
            row[5] = 'NaN' if math.isnan(row[5]) else row[5]
            writer.writerow(row)

def correlation_mode(output_path):
    mu = 0.9
    alpha = 0.005
    D = 0.1
    tau = 1.0
    x = xi(alpha)
    A1 = compute_A1(alpha, D, tau, mu)
    A2 = compute_A2(alpha, D, tau, mu)
    A3 = compute_A3(alpha, D, tau, mu)
    G = build_G(A1, A2, A3)
    # Build L_ik^a matrix (i: row of Lambda, k: column of Lambda, a: index of psi)
    # Lambda from Eq. (13): Lambda_ik = xi * M_ik, where M is given without xi.
    # So L_ik^a = xi * M_ik^a
    # We'll define M_ik^a as a 3x3x3 array.
    M = np.zeros((3,3,3))
    # lambda_{1,1} = alpha*mu*psi3  -> M[0,0,2] = alpha*mu
    M[0,0,2] = alpha * mu
    # lambda_{1,2} = psi3           -> M[0,1,2] = 1.0
    M[0,1,2] = 1.0
    # lambda_{1,3} = -(psi2 + alpha*mu*psi1) -> M[0,2,0] = -alpha*mu, M[0,2,1] = -1.0
    M[0,2,0] = -alpha * mu
    M[0,2,1] = -1.0
    # lambda_{2,1} = -psi3          -> M[1,0,2] = -1.0
    M[1,0,2] = -1.0
    # lambda_{2,2} = alpha*mu*psi3 -> M[1,1,2] = alpha*mu
    M[1,1,2] = alpha * mu
    # lambda_{2,3} = psi1 - alpha*mu*psi2 -> M[1,2,0] = 1.0, M[1,2,1] = -alpha*mu
    M[1,2,0] = 1.0
    M[1,2,1] = -alpha * mu
    # lambda_{3,1} = psi2           -> M[2,0,1] = 1.0
    M[2,0,1] = 1.0
    # lambda_{3,2} = -psi1          -> M[2,1,0] = -1.0
    M[2,1,0] = -1.0
    # lambda_{3,3} = 0              -> all zero already.
    L = x * M  # L_ik^a

    # Compute tensor T_{ijab} = sum_{k} L_{ik}^{a} * L_{jk}^{b}
    T = np.zeros((3,3,3,3))
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    s = 0.0
                    for k in range(3):
                        s += L[i,k,a] * L[j,k,b]
                    T[i,j,a,b] = s

    # ODE function y is (9,) flattened C row-major
    def ode_func(s, y):
        C = y.reshape((3,3))
        # term1 = G @ C
        term1 = G @ C
        # term2 = D * exp(-s/tau) * sum_{a,b} T_{ijab} C_ab
        exp_fac = D * math.exp(-s / tau)
        term2 = np.zeros((3,3))
        for a in range(3):
            for b in range(3):
                term2 += T[:,:,a,b] * C[a,b]
        dCdt = term1 + exp_fac * term2
        return dCdt.flatten()

    # initial condition C(0) = C0 for all components
    C0 = 1.0
    y0 = np.full((3,3), C0).flatten()

    # time points
    s_span = (0.0, 10.0)
    t_eval = np.arange(0.0, 10.05, 0.1)  # step 0.1, including endpoint 10.0
    sol = solve_ivp(ode_func, s_span, y0, t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)
    if not sol.success:
        raise RuntimeError("ODE integration failed: " + sol.message)

    C12_vals = []
    for t, y in zip(sol.t, sol.y.T):
        Cmat = y.reshape((3,3))
        C12_vals.append(Cmat[0,1])  # C_{12}

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['s', 'C12'])
        for s_val, c12 in zip(sol.t, C12_vals):
            writer.writerow([s_val, c12])

def main():
    if len(sys.argv) < 4 or sys.argv[1] != '--mode' or sys.argv[3] != '--output':
        print("Usage: python3 compute.py --mode <stability|correlation> --output <filepath>")
        sys.exit(1)
    mode = sys.argv[2]
    output_path = sys.argv[4]
    if mode == 'stability':
        stability_mode(output_path)
    elif mode == 'correlation':
        correlation_mode(output_path)
    else:
        print("Unknown mode:", mode)
        sys.exit(1)

if __name__ == '__main__':
    main()
