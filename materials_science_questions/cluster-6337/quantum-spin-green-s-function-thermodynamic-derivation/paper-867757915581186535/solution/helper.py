import numpy as np
import json, sys
from itertools import product

# lattice parameters
L = 18  # 18x18
N = L * L
open_bc = True

# build tight-binding matrix (t=1)
T = np.zeros((N, N))
# map 2D index to 1D index
def idx(i, j):
    return i * L + j
for i, j in product(range(L), range(L)):
    p = idx(i, j)
    # nearest neighbours: up, down, left, right (if inside)
    if i > 0:
        T[p, idx(i-1, j)] = -1.0
    if i < L-1:
        T[p, idx(i+1, j)] = -1.0
    if j > 0:
        T[p, idx(i, j-1)] = -1.0
    if j < L-1:
        T[p, idx(i, j+1)] = -1.0

# energy grid
emin, emax = -10.0, 10.0
nbins = 200
edges = np.linspace(emin, emax, nbins+1)
centers = (edges[:-1] + edges[1:]) / 2.0
bin_width = edges[1] - edges[0]

# factor for DOS: D(E) = (1/(N*pi)) * counts/bin_width
dos_factor = 1.0 / (N * np.pi * bin_width)

def compute_dos_from_configs(configs, U):
    """configs: array of shape (n_conf, N) with values +1/-1.
    Returns dos array (averaged over configs)."""
    n_conf = configs.shape[0]
    dos_acc = np.zeros(nbins)
    for idx_c in range(n_conf):
        S = configs[idx_c]
        h = T + np.diag(-0.5 * U * S)
        eigvals = np.linalg.eigvalsh(h)
        # histogram counts
        counts, _ = np.histogram(eigvals, bins=edges)
        dos = counts * dos_factor
        dos_acc += dos
    return dos_acc / n_conf

# Monte Carlo for effective Ising model (antiferromagnetic coupling J)
def generate_ising_configs(J, beta, n_configs, n_thermal=1000, n_interval=50):
    """Metropolis simulation of 2D Ising model with Hamiltonian H = -J sum_{<rr'>} S(r)S(r').
    Returns n_configs configurations."""
    S = np.ones((L, L), dtype=int)  # initial state
    def energy_delta(i, j, new_s):
        old_s = S[i,j]
        delta = 0.0
        if i > 0: delta += S[i-1,j] * (old_s - new_s)
        if i < L-1: delta += S[i+1,j] * (old_s - new_s)
        if j > 0: delta += S[i, j-1] * (old_s - new_s)
        if j < L-1: delta += S[i, j+1] * (old_s - new_s)
        return -J * delta  # because H sum -J product
    # thermalization
    for sweep in range(n_thermal):
        for i in range(L):
            for j in range(L):
                new_s = -S[i,j]
                dE = energy_delta(i, j, new_s)
                if dE <= 0 or np.random.random() < np.exp(-beta * dE):
                    S[i,j] = new_s
    configs = np.zeros((n_configs, N), dtype=np.float64)
    for c in range(n_configs):
        # run n_interval sweeps between configs
        for sweep in range(n_interval):
            for i in range(L):
                for j in range(L):
                    new_s = -S[i,j]
                    dE = energy_delta(i, j, new_s)
                    if dE <= 0 or np.random.random() < np.exp(-beta * dE):
                        S[i,j] = new_s
        configs[c] = S.flatten()
    return configs

# random configurations for high T (paramagnetic)
def random_configs(n_configs):
    return np.random.choice([-1, 1], size=(n_configs, N))

# Conditions
conditions = []

# U=3, half-filling mu=U/2
U1 = 3.0
mu1 = U1/2.0
t_bar = 1.0
J1 = t_bar**2 / (2.0 * U1)  # ≈ 0.1667

for beta in [3, 7, 10, 14]:
    if beta == 3:
        # high T, random configs
        configs = random_configs(100)
    else:
        # use effective Ising model with J1
        configs = generate_ising_configs(J1, beta, 100, n_thermal=500, n_interval=50)
    dos = compute_dos_from_configs(configs, U1)
    conditions.append({
        "U": U1,
        "mu": mu1,
        "beta": beta,
        "energy": centers.tolist(),
        "dos": dos.tolist()
    })

# U=8, half-filling mu=4, beta=3
U2 = 8.0
mu2 = U2/2.0
configs = random_configs(100)  # beta=3, random
dos = compute_dos_from_configs(configs, U2)
conditions.append({
    "U": U2,
    "mu": mu2,
    "beta": 3,
    "energy": centers.tolist(),
    "dos": dos.tolist()
})

output = {"conditions": conditions}
with open("/app/outputs/dos_results.json", "w") as f:
    json.dump(output, f)
