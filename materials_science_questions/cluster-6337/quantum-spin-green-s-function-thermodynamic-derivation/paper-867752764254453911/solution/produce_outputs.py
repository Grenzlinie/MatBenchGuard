#!/usr/bin/env python3
"""Produce the analytic BBGKY closure time series.
Usage: produce_outputs.py finite|thermo output_filename
"""
import sys
import csv
import math
import numpy as np

def betas(N, lam):
    """Return beta_n = n*(1 - n*lam) for n=1..N-1."""
    return [n * (1.0 - n*lam) for n in range(1, N)]

def jacobi_matrix(betas, degree):
    """Build symmetric tridiagonal Jacobi matrix of size degree.
    Diagonals zero, off-diagonals sqrt(beta_n)."""
    diag = np.zeros(degree)
    off_diag = np.sqrt(betas[:degree-1])   # beta_1 .. beta_{ell-1}
    J = np.diag(diag)
    for i in range(degree-1):
        J[i, i+1] = off_diag[i]
        J[i+1, i] = off_diag[i]
    return J

def eval_polys(x, betas, max_n):
    """Evaluate both families of orthogonal polynomials at x up to order max_n.
    Returns arrays p_n^{(0)}, dp_n^{(0)}, q_n^{(1)} for n=0..max_n.
    p_n^{(0)} recurrence: p_{n+1} = x p_n - beta_n p_{n-1}, p_0=1, p_1=x.
    q_n^{(1)} recurrence: q_{n+1} = x q_n - beta_{n+1} q_{n-1}, q_0=1, q_1=x.
    Derivative dp_n same as p but with p_n'.
    """
    p = np.zeros(max_n+1)
    dp = np.zeros(max_n+1)
    q = np.zeros(max_n+1)
    p[0] = 1.0; dp[0] = 0.0
    if max_n >= 1:
        p[1] = x; dp[1] = 1.0
    for n in range(1, max_n):
        p[n+1] = x * p[n] - betas[n-1] * p[n-1]  # beta_n index n-1 because list starts at n=1
        dp[n+1] = p[n] + x * dp[n] - betas[n-1] * dp[n-1]
    q[0] = 1.0
    if max_n >= 1:
        q[1] = x
    for n in range(1, max_n):
        # beta_{n+1} is betas[n] because betas list index 0 corresponds to beta_1
        q[n+1] = x * q[n] - betas[n] * q[n-1]
    return p, dp, q

def compute_finite_series(lam, N, l, s, tau_vals):
    """Compute u1(tau) for given closure order l.
    Returns array of complex values."""
    beta_list = betas(N, lam)
    if l == 1:
        # trivial case, not used
        return np.ones(len(tau_vals)) * s
    # Jacobi matrix size l
    J = jacobi_matrix(beta_list, l)
    zeros = np.linalg.eigvalsh(J)   # sorted real eigenvalues
    # Take positive zeros only for even l
    pos_zeros = zeros[zeros > 0]
    npos = len(pos_zeros)
    if npos == 0:
        return np.zeros(len(tau_vals), dtype=complex)
    # Precompute residues for positive zeros
    residues = np.zeros(npos, dtype=float)
    for i, xk in enumerate(pos_zeros):
        # evaluate p_l^{(0)} derivative and p_{l-1}^{(1)}
        p, dp, q = eval_polys(xk, beta_list, l)
        p_l_prime = dp[l]   # p_l'(xk)
        q_lm1 = q[l-1]      # p_{l-1}^{(1)}(xk)
        residues[i] = q_lm1 / p_l_prime
    # u1(tau) = 2 * s * sum_j residues[j] * cos(x_j * tau)
    u1 = np.zeros(len(tau_vals), dtype=complex)
    for i, xk in enumerate(pos_zeros):
        u1 += residues[i] * np.cos(xk * tau_vals)
    u1 *= 2.0 * s
    return u1

def write_finite_csv(filename):
    """Generate finite_N_timeseries.csv."""
    lam = 0.1
    N = 10
    s = complex(1.0, 0.0)   # s^x + i s^y
    tau_vals = np.arange(0.0, 20.0 + 1e-12, 0.01)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['tau', 'u1_real', 'u1_imag', 'closure_order', 'N'])
        for l in [2, 4]:
            u1 = compute_finite_series(lam, N, l, s, tau_vals)
            for i, tau in enumerate(tau_vals):
                row = [tau, u1[i].real, u1[i].imag, l, N]
                writer.writerow(row)

def write_thermo_csv(filename):
    """Generate thermodynamic_limit_timeseries.csv."""
    tau_vals = np.arange(0.0, 5.0 + 1e-12, 0.01)
    u1 = np.exp(-tau_vals**2 / 2.0)   # s^x = 1, s^y = 0 -> u1 = e^{-tau^2/2}
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['tau', 'u1_real', 'u1_imag'])
        for i, tau in enumerate(tau_vals):
            writer.writerow([tau, u1[i].real, 0.0])  # imag = 0

def main():
    if len(sys.argv) != 3:
        print('Usage: produce_outputs.py finite|thermo output_file', file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == 'finite':
        write_finite_csv(outpath)
    elif mode == 'thermo':
        write_thermo_csv(outpath)
    else:
        print(f'Unknown mode {mode}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
