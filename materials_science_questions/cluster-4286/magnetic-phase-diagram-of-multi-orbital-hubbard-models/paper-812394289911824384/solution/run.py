import numpy as np
import sys, math

# ---------- lattice definitions ----------
class Kagome:
    name = 'kagome'
    # unit cell vectors
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])
    # basis positions in fractional coords? I'll use Cartesian.
    pos = [
        np.array([0.0, 0.0]),
        np.array([0.5, 0.0]),
        np.array([0.25, np.sqrt(3)/4])
    ]
    nsites = 3
    # building bonds
    def __init__(self):
        # find nearest-neighbor bonds
        bonds = []
        t_hop = -1.0  # sign chosen to put delta peak at top
        # scan translations
        for i in range(self.nsites):
            for j in range(self.nsites):
                for nx in range(-1,2):
                    for ny in range(-1,2):
                        delta = nx*self.a1 + ny*self.a2
                        r = self.pos[j] + delta - self.pos[i]
                        dist = np.linalg.norm(r)
                        if i==j and nx==0 and ny==0: continue
                        if abs(dist - 0.5) < 1e-4:  # NN distance
                            bonds.append((i, j, delta))
        self.bonds = bonds
        self.t_hop = t_hop

    def H_hop_k(self, k):
        H = np.zeros((self.nsites, self.nsites), dtype=complex)
        for i, j, delta in self.bonds:
            H[i, j] += self.t_hop * np.exp(1j * np.dot(k, delta + self.pos[j] - self.pos[i]))
        return H

    def ex_bonds(self):
        # return bonds for exchange (same as NN)
        return self.bonds

class Pyrochlore:
    name = 'pyrochlore'
    a1 = np.array([0.0, 0.5, 0.5])
    a2 = np.array([0.5, 0.0, 0.5])
    a3 = np.array([0.5, 0.5, 0.0])
    pos = [
        np.array([0.0, 0.0, 0.0]),
        np.array([0.25, 0.25, 0.0]),
        np.array([0.25, 0.0, 0.25]),
        np.array([0.0, 0.25, 0.25])
    ]
    nsites = 4
    def __init__(self):
        t_hop = -1.0
        bonds = []
        # NN distance
        for i in range(self.nsites):
            for j in range(self.nsites):
                for nx in range(-1,2):
                    for ny in range(-1,2):
                        for nz in range(-1,2):
                            delta = nx*self.a1 + ny*self.a2 + nz*self.a3
                            r = self.pos[j] + delta - self.pos[i]
                            dist = np.linalg.norm(r)
                            if i==j and nx==0 and ny==0 and nz==0: continue
                            if abs(dist - np.sqrt(0.25**2+0.25**2)) < 1e-4:
                                bonds.append((i, j, delta))
        self.bonds = bonds
        self.t_hop = t_hop

    def H_hop_k(self, k):
        H = np.zeros((self.nsites, self.nsites), dtype=complex)
        for i, j, delta in self.bonds:
            H[i, j] += self.t_hop * np.exp(1j * np.dot(k, delta + self.pos[j] - self.pos[i]))
        return H

    def ex_bonds(self):
        return self.bonds

# ---------- spin configurations ----------
def kagome_configs():
    # F
    F = [np.array([0,0,1.0])]*3
    # FI: two up one down
    FI = [np.array([0,0,1.0]), np.array([0,0,1.0]), np.array([0,0,-1.0])]
    # CI (new function to take theta)
    return {'F': F, 'FI': FI}

def pyrochlore_configs():
    d = [
        np.array([1,1,1])/np.sqrt(3),
        np.array([1,-1,-1])/np.sqrt(3),
        np.array([-1,1,-1])/np.sqrt(3),
        np.array([-1,-1,1])/np.sqrt(3)
    ]
    F = [np.array([0,0,1.0])]*4
    AF = d  # all-in/all-out (pointing outward)
    FI = [np.array([0,0,1.0]), np.array([0,0,1.0]), np.array([0,0,1.0]), np.array([0,0,-1.0])]
    # SI: two-in two-out
    SI = [d[0], d[1], -d[2], -d[3]]
    return {'F': F, 'AF': AF, 'FI': FI, 'SI': SI}

# CI theta scan for a given lattice config definition

def get_CI_spins_kagome(theta):
    s0 = np.array([math.sin(theta), 0.0, math.cos(theta)])
    s1 = np.array([-0.5*math.sin(theta), math.sqrt(3)/2 * math.sin(theta), math.cos(theta)])
    s2 = np.array([-0.5*math.sin(theta), -math.sqrt(3)/2 * math.sin(theta), math.cos(theta)])
    return [s0, s1, s2]

def get_CI_spins_pyrochlore(theta):
    d = [
        np.array([1,1,1])/np.sqrt(3),
        np.array([1,-1,-1])/np.sqrt(3),
        np.array([-1,1,-1])/np.sqrt(3),
        np.array([-1,-1,1])/np.sqrt(3)
    ]
    spins = []
    for di in d:
        s = math.sin(theta)*di + math.cos(theta)*np.array([0,0,1.0])
        spins.append(s)
    return spins

# ---------- exchange energy ----------
def compute_exchange(spins, lattice):
    # E_ex per u.c. = J/2 * sum_{i in u.c.} sum_{j,delta NN} S_i·S_j
    ex_bonds = lattice.ex_bonds()
    e = 0.0
    for i, j, delta in ex_bonds:
        e += np.dot(spins[i], spins[j])
    return e / 2.0  # because each bond counted twice when summing over i? Actually we sum over all bonds from i in u.c., each bond appears once (i origin). So no double count. But check: bonds list includes bonds from i to j in possibly another cell, but for exchange, the sum over <ij> pairs is counted once. Our bonds include each directed bond? We stored both (i,j,delta) and (j,i,-delta)? No, we added only when i from home cell? In my construction, I loop i in nsites, j in nsites, and translations; I might create both directions for same physical bond. Let's check: for a bond between i (home) and j (in same cell), I add (i,j,0) and also when i=j? Actually i==j and nx=0 skipped. So each undirected bond will be added twice when both i and j are in the same cell? Because when i=0, j=1, delta=(0,0) added; later when i=1, j=0, delta=(0,0) also added. Yes, I'll get duplicate. So to get correct sum per bond once, we can divide by 2. Or we can store undirected. I'll divide by 2.
    return J * e

# ---------- band energy ----------
def band_energy_kagome(K, J, spins, n, lattice, nk=30):
    # build Hamiltonian in k-space
    ns = lattice.nsites
    # k sampling: parallelogram BZ
    a1 = lattice.a1
    a2 = lattice.a2
    # reciprocal lattice vectors
    area = a1[0]*a2[1] - a1[1]*a2[0]
    b1 = 2*np.pi * np.array([a2[1], -a2[0]]) / area
    b2 = 2*np.pi * np.array([-a1[1], a1[0]]) / area

    eigvals_all = []
    for ix in range(nk):
        for iy in range(nk):
            # fractional coordinates
            kx = (ix+0.5)/nk
            ky = (iy+0.5)/nk
            k = kx*b1 + ky*b2
            H_hop = lattice.H_hop_k(k)
            # Hund term: on-site spin dependent
            H_tot = np.zeros((2*ns, 2*ns), dtype=complex)
            for i in range(ns):
                si = spins[i]
                # (K/2) * σ·S, but sign is -K/2 σ·S in Hamiltonian
                hund = -(K/2)*(
                    si[0]*np.array([[0,1],[1,0]]) +
                    si[1]*np.array([[0,-1j],[1j,0]]) +
                    si[2]*np.array([[1,0],[0,-1]])
                )
                H_tot[2*i:2*i+2, 2*i:2*i+2] += hund
            # add kinetic
            for a in range(ns):
                for b in range(ns):
                    H_tot[2*a, 2*b] += H_hop[a,b]
                    H_tot[2*a+1, 2*b+1] += H_hop[a,b]
            eigs = np.linalg.eigvalsh(H_tot)
            eigvals_all.extend(eigs)

    eigvals_all.sort()
    # electron number per u.c. = n
    num_filled = int(np.ceil(n * nk * nk))
    if num_filled > len(eigvals_all):
        num_filled = len(eigvals_all)
    e_band = np.sum(eigvals_all[:num_filled]) / (nk*nk)
    return e_band

def band_energy_pyro(K, J, spins, n, lattice, nk=20):
    ns = lattice.nsites
    a1 = lattice.a1
    a2 = lattice.a2
    a3 = lattice.a3
    vol = np.abs(np.dot(a1, np.cross(a2, a3)))
    b1 = 2*np.pi * np.cross(a2, a3) / vol
    b2 = 2*np.pi * np.cross(a3, a1) / vol
    b3 = 2*np.pi * np.cross(a1, a2) / vol
    eigvals_all = []
    for ix in range(nk):
        for iy in range(nk):
            for iz in range(nk):
                kx = (ix+0.5)/nk
                ky = (iy+0.5)/nk
                kz = (iz+0.5)/nk
                k = kx*b1 + ky*b2 + kz*b3
                H_hop = lattice.H_hop_k(k)
                H_tot = np.zeros((2*ns, 2*ns), dtype=complex)
                for i in range(ns):
                    si = spins[i]
                    hund = -(K/2)*(
                        si[0]*np.array([[0,1],[1,0]]) +
                        si[1]*np.array([[0,-1j],[1j,0]]) +
                        si[2]*np.array([[1,0],[0,-1]])
                    )
                    H_tot[2*i:2*i+2, 2*i:2*i+2] += hund
                for a in range(ns):
                    for b in range(ns):
                        H_tot[2*a, 2*b] += H_hop[a,b]
                        H_tot[2*a+1, 2*b+1] += H_hop[a,b]
                eigs = np.linalg.eigvalsh(H_tot)
                eigvals_all.extend(eigs)
    eigvals_all.sort()
    num_filled = int(np.ceil(n * nk * nk * nk))
    if num_filled > len(eigvals_all):
        num_filled = len(eigvals_all)
    e_band = np.sum(eigvals_all[:num_filled]) / (nk*nk*nk)
    return e_band

# ---------- compute total energy ----------
def total_energy_kagome(K_over_t, J_over_t, n, config_spins, lattice):
    # K and J in units of |t|, t=-1 => |t|=1
    K = K_over_t
    J = J_over_t
    e_ex = compute_exchange(config_spins, lattice) * J  # compute_exchange returns sum without J factor? We'll multiply.
    # Adjust compute_exchange: I'll change it to return unit sum (sum S·S) and multiply by J later.
    # We'll implement compute_exchange as sum of S·S over bonds/2, then *J.
    e_band = band_energy_kagome(K, J, config_spins, n, lattice, nk=30)
    return e_band + e_ex

def compute_exchange_sum(spins, lattice):
    # returns sum over bonds (divided by 2 for double counting) of S_i·S_j
    ex_bonds = lattice.ex_bonds()
    s = 0.0
    for i, j, delta in ex_bonds:
        s += np.dot(spins[i], spins[j])
    return s / 2.0

def total_energy_pyro(K_over_t, J_over_t, n, config_spins, lattice):
    K = K_over_t
    J = J_over_t
    e_ex = compute_exchange_sum(config_spins, lattice) * J
    e_band = band_energy_pyro(K, J, config_spins, n, lattice, nk=20)
    return e_band + e_ex

# ---------- CI optimization ----------
def optimize_CI_kagome(K, J, n, lattice):
    thetas = np.linspace(0, math.pi, 21)
    best = float('inf')
    best_spins = None
    for th in thetas:
        spins = get_CI_spins_kagome(th)
        e = total_energy_kagome(K, J, n, spins, lattice)
        if e < best:
            best = e
            best_spins = spins
    return best, best_spins

def optimize_CI_pyro(K, J, n, lattice):
    thetas = np.linspace(0, math.pi, 21)
    best = float('inf')
    best_spins = None
    for th in thetas:
        spins = get_CI_spins_pyrochlore(th)
        e = total_energy_pyro(K, J, n, spins, lattice)
        if e < best:
            best = e
            best_spins = spins
    return best, best_spins

# ---------- main sweep ----------
def main():
    import csv
    # kagome
    kag = Kagome()
    configs_k = kagome_configs()
    # precompute exchange sums for F and FI (independent of K, J, n)
    ex_F_k = compute_exchange_sum(configs_k['F'], kag)
    ex_FI_k = compute_exchange_sum(configs_k['FI'], kag)
    
    pyro = Pyrochlore()
    configs_p = pyrochlore_configs()
    ex_F_p = compute_exchange_sum(configs_p['F'], pyro)
    ex_AF_p = compute_exchange_sum(configs_p['AF'], pyro)
    ex_FI_p = compute_exchange_sum(configs_p['FI'], pyro)
    ex_SI_p = compute_exchange_sum(configs_p['SI'], pyro)

    rows = []
    # parameter sweeps
    n_vals_k = np.arange(0.0, 6.1, 0.2)  # step 0.2
    K_vals = np.arange(0.0, 8.1, 1.0)
    J_vals = [0.0, 0.02, 0.04]

    # kagome
    for K in K_vals:
        for J in J_vals:
            for n in n_vals_k:
                # F
                e_F = total_energy_kagome(K, J, n, configs_k['F'], kag)
                # FI
                e_FI = total_energy_kagome(K, J, n, configs_k['FI'], kag)
                # CI optimized
                e_CI, _ = optimize_CI_kagome(K, J, n, kag)
                # ground state
                energies = {'F': e_F, 'FI': e_FI, 'CI': e_CI}
                gs = min(energies, key=energies.get)
                rows.append([
                    'kagome', n, K, J,
                    e_F, e_FI, e_CI, '', '', gs
                ])

    # pyrochlore: n 0-8
    n_vals_p = np.arange(0.0, 8.1, 0.2)
    for K in K_vals:
        for J in J_vals:
            for n in n_vals_p:
                e_F = total_energy_pyro(K, J, n, configs_p['F'], pyro)
                e_AF = total_energy_pyro(K, J, n, configs_p['AF'], pyro)
                e_FI = total_energy_pyro(K, J, n, configs_p['FI'], pyro)
                e_SI = total_energy_pyro(K, J, n, configs_p['SI'], pyro)
                e_CI, _ = optimize_CI_pyro(K, J, n, pyro)
                energies = {'F': e_F, 'AF': e_AF, 'FI': e_FI, 'CI': e_CI, 'SI': e_SI}
                gs = min(energies, key=energies.get)
                rows.append([
                    'pyrochlore', n, K, J,
                    e_F, e_FI, e_CI, e_AF, e_SI, gs
                ])

    # K-J cross-sections at n=1.0 for both
    n_cross = 1.0
    J_cross = np.arange(0.0, 0.12, 0.02)  # 0,0.02,0.04,...,0.10
    for K in K_vals:
        for J in J_cross:
            # kagome
            e_F = total_energy_kagome(K, J, n_cross, configs_k['F'], kag)
            e_FI = total_energy_kagome(K, J, n_cross, configs_k['FI'], kag)
            e_CI, _ = optimize_CI_kagome(K, J, n_cross, kag)
            energies_k = {'F': e_F, 'FI': e_FI, 'CI': e_CI}
            gs_k = min(energies_k, key=energies_k.get)
            rows.append([
                'kagome', n_cross, K, J,
                e_F, e_FI, e_CI, '', '', gs_k
            ])
            # pyrochlore
            e_F = total_energy_pyro(K, J, n_cross, configs_p['F'], pyro)
            e_AF = total_energy_pyro(K, J, n_cross, configs_p['AF'], pyro)
            e_FI = total_energy_pyro(K, J, n_cross, configs_p['FI'], pyro)
            e_SI = total_energy_pyro(K, J, n_cross, configs_p['SI'], pyro)
            e_CI, _ = optimize_CI_pyro(K, J, n_cross, pyro)
            energies_p = {'F': e_F, 'AF': e_AF, 'FI': e_FI, 'CI': e_CI, 'SI': e_SI}
            gs_p = min(energies_p, key=energies_p.get)
            rows.append([
                'pyrochlore', n_cross, K, J,
                e_F, e_FI, e_CI, e_AF, e_SI, gs_p
            ])

    # write CSV
    header = ['lattice','n','K_over_t','J_over_t','E_F','E_FI','E_CI','E_AF','E_SI','ground_state']
    with open('/app/outputs/phase_diagram_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == '__main__':
    main()
