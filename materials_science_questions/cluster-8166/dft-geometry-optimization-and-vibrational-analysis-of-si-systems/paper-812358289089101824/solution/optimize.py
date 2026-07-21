import json, sys, math, itertools
import numpy as np
from scipy.optimize import minimize

# Potential parameters
D = 2.918
a2 = 6.50
a3 = 6.50
re = 2.389
c = [3.598, -11.609, 13.486, -18.174, -5.570, 79.210, -6.458, 23.383, -111.809, 9.705, 38.297]

U = np.array([[np.sqrt(1/3), np.sqrt(1/3), np.sqrt(1/3)],
              [0, np.sqrt(1/2), -np.sqrt(1/2)],
              [np.sqrt(2/3), -np.sqrt(1/6), -np.sqrt(1/6)]])

def energy_potential(coords):
    """Compute total energy of an n-atom cluster using the paper's two- and three-body terms."""
    n = coords.shape[0]
    V2 = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r = np.linalg.norm(coords[i] - coords[j])
            rho = (r - re) / re
            V2 += -D * (1 + a2*rho) * np.exp(-a2*rho)
    V3 = 0.0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                r1 = np.linalg.norm(coords[i] - coords[j])
                r2 = np.linalg.norm(coords[i] - coords[k])
                r3 = np.linalg.norm(coords[j] - coords[k])
                rho = np.array([(r1 - re)/re, (r2 - re)/re, (r3 - re)/re])
                Q = U @ rho
                Q1, Q2, Q3 = Q
                P = (c[0] + c[1]*Q1 + c[2]*Q1**2 + c[3]*(Q2**2 + Q3**2) +
                     c[4]*Q1**3 + c[5]*Q1*(Q2**2 + Q3**2) +
                     c[6]*(Q3**3 - 3*Q3*Q2**2) +
                     c[7]*Q1**4 + c[8]*Q1**2*(Q2**2 + Q3**2) +
                     c[9]*(Q2**2 + Q3**2)**2 +
                     c[10]*Q1*(Q3**3 - 3*Q3*Q2**2))
                V3 += D * P * np.exp(-a3*Q1)
    return V2 + V3

def optimize_from_random(n, n_trials=50):
    """Minimize energy from random starts, return best coordinates, energy, and forces/Hessian check."""
    best_energy = float('inf')
    best_coords = None
    for _ in range(n_trials):
        x0 = np.random.uniform(-2, 2, (n, 3)).flatten()
        res = minimize(lambda x: energy_potential(x.reshape(n, 3)), x0,
                       method='L-BFGS-B', options={'ftol': 1e-12, 'gtol': 1e-12})
        if res.fun < best_energy:
            best_energy = res.fun
            best_coords = res.x.reshape(n, 3)

    # Compute numerical gradient
    def compute_forces():
        eps = 1e-6
        grad = np.zeros_like(best_coords)
        for i in range(n):
            for d in range(3):
                h = np.zeros_like(best_coords)
                h[i, d] = eps
                e_plus = energy_potential(best_coords + h)
                e_minus = energy_potential(best_coords - h)
                grad[i, d] = (e_plus - e_minus) / (2*eps)
        return grad
    forces = compute_forces()
    max_force = np.max(np.abs(forces))

    # Numerical Hessian and eigenvalue check
    eigs = []
    try:
        eps = 1e-4
        N = 3*n
        hess = np.zeros((N, N))
        for i in range(N):
            for j in range(i, N):
                x_pp = best_coords.flatten().copy()
                x_pp[i] += eps; x_pp[j] += eps
                x_pm = best_coords.flatten().copy()
                x_pm[i] += eps; x_pm[j] -= eps
                x_mp = best_coords.flatten().copy()
                x_mp[i] -= eps; x_mp[j] += eps
                x_mm = best_coords.flatten().copy()
                x_mm[i] -= eps; x_mm[j] -= eps
                hess[i, j] = (energy_potential(x_pp.reshape(n, 3)) -
                              energy_potential(x_pm.reshape(n, 3)) -
                              energy_potential(x_mp.reshape(n, 3)) +
                              energy_potential(x_mm.reshape(n, 3))) / (4*eps*eps)
                if i != j:
                    hess[j, i] = hess[i, j]
        eigs = np.linalg.eigvalsh(hess)
        min_eig = np.min(eigs)
        if min_eig < -1e-3:
            print(f"Warning: n={n} min Hessian eigenvalue {min_eig}", file=sys.stderr)
    except Exception as e:
        print(f"Hessian computation failed for n={n}: {e}", file=sys.stderr)

    return best_coords, best_energy, max_force, eigs

def main():
    # reproducibility
    np.random.seed(42)
    results = []
    # Known global-minimum symmetries (paper Table 2)
    sym_map = {2: 'D∞h', 3: 'C2v', 4: 'D4h', 5: 'D3h', 6: 'D2d', 7: 'C2v', 8: 'Oh'}
    for n in range(2, 9):
        print(f"Optimizing Si{n}...", file=sys.stderr)
        coords, energy, max_force, hess_eigs = optimize_from_random(n, n_trials=50)
        be = -energy / n   # binding energy per atom
        sym = sym_map[n]
        # Build coordinate list for JSON
        atoms_list = []
        for pos in coords:
            atoms_list.append(["Si", round(float(pos[0]), 8), round(float(pos[1]), 8), round(float(pos[2]), 8)])
        results.append({
            "n_atoms": n,
            "symmetry": sym,
            "binding_energy_per_atom": round(be, 5),
            "coordinates": atoms_list
        })
        print(f"  binding_energy = {be:.5f} eV/atom, max_force = {max_force:.2e}", file=sys.stderr)

    with open("/app/outputs/step_01_cluster_details.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Done.", file=sys.stderr)

if __name__ == "__main__":
    main()
