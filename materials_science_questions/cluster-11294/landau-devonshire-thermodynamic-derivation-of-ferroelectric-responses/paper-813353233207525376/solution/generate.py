import sys
import numpy as np

def solve_polarization(N, lam, e_over_K, beta=1.0, Omega=1.0, max_iter=1000, tol=1e-10):
    # Build coupling matrix J (N x N)
    J = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            dist = abs(i - j)
            J[i,j] = np.exp(-lam * dist)
    s = np.zeros(N)
    for it in range(max_iter):
        h_eff = np.dot(J, s) + 2.0 * e_over_K
        # compute new s
        r = np.sqrt(Omega**2 + h_eff**2)
        new_s = 0.5 * np.tanh(beta * r / 2.0) * (h_eff / r)
        diff = np.max(np.abs(new_s - s))
        s = new_s
        if diff < tol:
            break
    P = np.mean(s)
    return P, s

def compute_susceptibility(N, lam, e_over_K, delta=0.001):
    P_plus, _ = solve_polarization(N, lam, e_over_K + delta)
    P_minus, _ = solve_polarization(N, lam, e_over_K - delta)
    return (P_plus - P_minus) / (2*delta)

def main(outfile):
    configs = [
        (5, 0.0),
        (5, 0.261),
        (50, 0.0),
        (50, 0.01)
    ]
    fields = np.arange(0.0, 2.01, 0.1)
    results = []
    for N, lam in configs:
        chi0 = compute_susceptibility(N, lam, 0.0)
        for e in fields:
            P, _ = solve_polarization(N, lam, e)
            chi = compute_susceptibility(N, lam, e)
            eta = (chi0 - chi) / chi0 * 100.0 if chi0 != 0 else 0.0
            results.append((N, lam, 1.0, e, P, chi, eta))
    with open(outfile, 'w') as f:
        f.write("N,lambda,kBT_K,e_z_over_K,mean_polarization,dielectric_susceptibility,tunability_percentage\n")
        for row in results:
            f.write(f"{row[0]},{row[1]},{row[2]},{row[3]:.6f},{row[4]:.12f},{row[5]:.12f},{row[6]:.8f}\n")

if __name__ == "__main__":
    main(sys.argv[1])