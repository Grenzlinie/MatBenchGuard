import numpy as np
import csv
import sys

# ----- Paper Table 1 -----
L = 100e-6
b = 15e-6
hb = 3e-6
hp = 0.5e-6
Eb = 169e9
Ep = 78.6e9
nu_b = 0.06
nu_p = 0.3
e31_p = -9.29               # e31
eps_v = 8.854e-12
d_default = 1e-6
V0 = 1.0                     # unit voltage

# ----- DQM differentiation matrices (Chebyshev-Gauss-Lobatto on [0,1]) -----
def cheb(N):
    j = np.arange(N)
    x = np.cos(np.pi * j / (N-1))           # [-1, 1]
    xi = 0.5 * (1 - x)                      # [0, 1]
    c = np.ones(N)
    c[0] = 2
    c[-1] = 2
    Dx = np.zeros((N, N))
    for i in range(N):
        for k in range(N):
            if i != k:
                Dx[i, k] = (c[i] / c[k]) * ((-1)**(i+k)) / (x[i] - x[k])
    Dx -= np.diag(np.sum(Dx, axis=1))
    D1 = 2 * Dx                              # d/dxi = 2 * d/dx
    D2 = D1 @ D1
    D3 = D2 @ D1
    D4 = D3 @ D1
    return xi, D1, D2, D3, D4

# ----- Compute nondimensional parameters -----
def compute_params(D=0, leq=None, d_gap=d_default):
    # neutral axis zc (Eq. 5)
    num = (1-D)*Eb * hp * hb + 0.5*Ep*hp**2 + 0.5*(1-D)*Eb*hb**2
    den = Ep*hp + (1-D)*Eb*hb
    zc = num / den
    # bending stiffness (EI)_eq   (Eq. 22)
    EI1 = (1/12)*Ep*b*hp**3
    EI2 = (1/12)*(1-D)*Eb*b*hb**3
    EI3 = Ep*b*hp*(zc - 0.5*hp)**2
    EI4 = (1-D)*Eb*b*hb*(hp + 0.5*hb - zc)**2
    EI_eq = EI1 + EI2 + EI3 + EI4
    # axial stiffness (EA)_eq
    EA_eq = Ep*b*hp + (1-D)*Eb*b*hb
    # (mu A l^2)_eq
    mu_p = Ep / (2*(1+nu_p))
    mu_b = (1-D)*Eb / (2*(1+nu_b))
    int_mu_dA = mu_p * (b*hp) + mu_b * (b*hb)
    if leq is not None:
        muAl2_eq = leq**2 * int_mu_dA
    else:
        muAl2_eq = 0.0
    H = EI_eq + muAl2_eq
    # nondimensional coefficients
    alpha = 3 * d_gap**2 * EA_eq / (2 * H)
    e31_bar = b * e31_p * L**2 * V0 / H
    beta = b * eps_v * L**4 * V0**2 / (2 * d_gap**3 * H)
    bc_term = (hp - 2*zc) / d_gap
    return e31_bar, alpha, beta, bc_term

# ----- Newton solver for a single voltage -----
def solve_bvp(Vbar, Vp, e31_bar, alpha, beta, bc_term, W_guess=None, N=25, max_iter=50, tol=1e-10):
    xi, D1, D2, D3, D4 = cheb(N)
    if W_guess is not None:
        W = W_guess.copy()
    else:
        W = np.zeros(N)
    for it in range(max_iter):
        W1 = D1 @ W
        W2 = D2 @ W
        W3 = D3 @ W
        W4 = D4 @ W
        # residual
        R = W4 + e31_bar*Vp * W2 - alpha * (W1**2) * W2 - beta * Vbar**2 / (1 - W)**2
        # boundary conditions
        R[0] = W[0]                                   # W(0)=0
        R[1] = W1[0]                                  # W'(0)=0
        R[-2] = W2[-1] + 0.5 * e31_bar * Vp * bc_term # BC at xi=1 (moment)
        R[-1] = (W3[-1] + e31_bar*Vp * W1[-1]         # BC at xi=1 (shear)
                 - (alpha/3) * (W1[-1])**3)
        # Jacobian
        J = np.zeros((N, N))
        # interior points (and initial for overwrite)
        for i in range(N):
            J[i, :] = (D4[i, :] + e31_bar*Vp*D2[i, :]
                       - 2*alpha*W1[i]*W2[i]*D1[i, :]
                       - alpha*(W1[i]**2)*D2[i, :])
            J[i, i] -= 2 * beta * Vbar**2 / (1 - W[i])**3
        # BC rows
        J[0, :] = 0
        J[0, 0] = 1
        J[1, :] = D1[0, :]
        J[-2, :] = D2[-1, :]
        J[-1, :] = D3[-1, :] + e31_bar*Vp*D1[-1, :] - alpha*(W1[-1]**2)*D1[-1, :]
        try:
            dW = np.linalg.solve(J, -R)
        except np.linalg.LinAlgError:
            return None
        W += dW
        if np.linalg.norm(dW) < tol:
            return W
    return None

# ----- Voltage sweep for tip displacement -----
def voltage_sweep(Vp, e31_bar, alpha, beta, bc_term, Vmax=100, dV=0.5):
    results = []
    Vbar = 0.0
    W_guess = None
    while Vbar <= Vmax:
        W = solve_bvp(Vbar, Vp, e31_bar, alpha, beta, bc_term, W_guess=W_guess)
        if W is None:
            break
        W_tip = W[-1]
        if W_tip >= 0.95:  # near contact, stop
            results.append((Vbar, W_tip))
            break
        results.append((Vbar, W_tip))
        W_guess = W
        Vbar += dV
    return results

# ----- Pull‑in voltage by bisection -----
def find_pull_in(Vp, e31_bar, alpha, beta, bc_term, Vstart=0.0, Vmax_guess=100.0, tol=1e-2):
    if solve_bvp(Vstart, Vp, e31_bar, alpha, beta, bc_term) is None:
        return None
    Vlow = Vstart
    Vhigh = Vmax_guess
    while True:
        sol = solve_bvp(Vhigh, Vp, e31_bar, alpha, beta, bc_term)
        if sol is None:
            break
        Vlow = Vhigh
        Vhigh *= 2
        if Vhigh > 2000:  # prevent runaway
            return Vhigh
    while Vhigh - Vlow > tol:
        Vmid = (Vlow + Vhigh) / 2
        if solve_bvp(Vmid, Vp, e31_bar, alpha, beta, bc_term) is not None:
            Vlow = Vmid
        else:
            Vhigh = Vmid
    return Vlow

# =========================================================
def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'

    # tip displacement cases
    tip_cases = [
        ('CM_Vp=-1', 0, None, -1),
        ('CM_Vp=0',  0, None,  0),
        ('CM_Vp=1',  0, None,  1),
        ('PM_Vp=-1', 0, 0.7e-6, -1),
        ('PM_Vp=0',  0, 0.7e-6,  0),
        ('PM_Vp=1',  0, 0.7e-6,  1),
    ]

    if target in ('tip_displacement', 'all'):
        out = '/app/outputs/tip_displacement.csv'
        with open(out, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['case', 'V_bar', 'W_tip'])
            for case, D, leq, Vp in tip_cases:
                e31_bar, alpha, beta, bc_term = compute_params(D=D, leq=leq)
                pts = voltage_sweep(Vp, e31_bar, alpha, beta, bc_term)
                for Vbar, Wtip in pts:
                    w.writerow([case, Vbar, Wtip])

    if target in ('pull_in_voltage', 'all'):
        out = '/app/outputs/pull_in_voltage.csv'
        pull_cases = []

        # Vp sweep (Fig. 3)
        for Vp in np.arange(-1.5, 1.51, 0.5):
            for leq_val, model in [(0.7e-6, 'PM'), (None, 'CM')]:
                case = f"{model}_Vp={Vp:.1f}"
                e31_bar, alpha, beta, bc_term = compute_params(D=0, leq=leq_val)
                Vpl = find_pull_in(Vp, e31_bar, alpha, beta, bc_term)
                if Vpl is not None:
                    pull_cases.append((case, Vpl))
        # damage (Fig. 6)  Vp=1
        for leq_val, model in [(0.7e-6, 'PM'), (None, 'CM')]:
            case = f"{model}_D=0.2_Vp=1"
            e31_bar, alpha, beta, bc_term = compute_params(D=0.2, leq=leq_val)
            Vpl = find_pull_in(1.0, e31_bar, alpha, beta, bc_term)
            if Vpl is not None:
                pull_cases.append((case, Vpl))
        # different gaps (Fig. 7)  PM, Vp=1
        for d_gap in [1e-6, 2e-6, 3e-6, 4e-6]:
            case = f"PM_d={d_gap*1e6:.1f}um"
            e31_bar, alpha, beta, bc_term = compute_params(D=0, leq=0.7e-6, d_gap=d_gap)
            Vpl = find_pull_in(1.0, e31_bar, alpha, beta, bc_term)
            if Vpl is not None:
                pull_cases.append((case, Vpl))
        # geometric linear vs. nonlinear (Fig. 9)  PM, Vp=1
        for nl_flag, nl_name in [(True, 'nonlinear'), (False, 'linear')]:
            case = f"{nl_name}_L=100"
            e31_bar, alpha, beta, bc_term = compute_params(D=0, leq=0.7e-6)
            if not nl_flag:
                alpha_use = 0.0
            else:
                alpha_use = alpha
            Vpl = find_pull_in(1.0, e31_bar, alpha_use, beta, bc_term)
            if Vpl is not None:
                pull_cases.append((case, Vpl))

        with open(out, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['case', 'V_pl'])
            for case, Vpl in pull_cases:
                w.writerow([case, Vpl])

if __name__ == '__main__':
    main()
