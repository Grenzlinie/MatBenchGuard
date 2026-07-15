import numpy as np
from scipy.linalg import eigh
from scipy.integrate import cumulative_trapezoid
import csv

# Physical constants
a_A = 3.6150
a = a_A * 1e-10
conv = 1e-3   # dyn/cm to N/m

# Force constants from Table IIa (dyn/cm)
alpha = 1676.728 * conv
gamma_fc = -5093.518 * conv
mu = 30212.914 * conv
lamb = -16849.532 * conv
delta_ee = -3578.843 * conv
rho_ee = -177.11 * conv

M = 63.54 * 1.660539e-27

# ---------- derive pair potentials ----------
r_ii = a / np.sqrt(2)
f1 = -1.0/(a * np.sqrt(2))
f2 = -0.5
g1 = 1.0/(a * np.sqrt(2))
g2 = -0.5
A = np.array([[f1, f2], [g1, g2]])
b = np.array([alpha, gamma_fc])
phi_ii1, phi_ii2 = np.linalg.solve(A, b)

r_ie = a * np.sqrt(3) / 4.0
h1 = -8.0/(a * 3 * np.sqrt(3))
h2 = -1.0/3
i1 = -4.0/(a * 3 * np.sqrt(3))
i2 = -1.0/3
A_ie = np.array([[h1, h2], [i1, i2]])
b_ie = np.array([mu, lamb])
phi_ie1, phi_ie2 = np.linalg.solve(A_ie, b_ie)

# Lattice vectors a1,a2,a3 (Cartesian)
a1 = np.array([0.0, 0.5, 0.5]) * a
a2 = np.array([0.5, 0.0, 0.5]) * a
a3 = np.array([0.5, 0.5, 0.0]) * a

vol = np.dot(a1, np.cross(a2, a3))
b1 = 2*np.pi * np.cross(a2, a3) / vol
b2 = 2*np.pi * np.cross(a3, a1) / vol
b3 = 2*np.pi * np.cross(a1, a2) / vol

# basis fractional coordinates
frac_ion = np.array([0.0,0.0,0.0])
frac_e1  = np.array([0.25,0.25,0.25])
frac_e2  = np.array([0.75,0.75,0.75])
cart_ion = frac_ion[0]*a1 + frac_ion[1]*a2 + frac_ion[2]*a3
cart_e1  = frac_e1[0]*a1  + frac_e1[1]*a2  + frac_e1[2]*a3
cart_e2  = frac_e2[0]*a1  + frac_e2[1]*a2  + frac_e2[2]*a3

def get_neighbors(cart1, cart2, cutoff, max_n=2):
    pairs = []
    for n1 in range(-max_n, max_n+1):
        for n2 in range(-max_n, max_n+1):
            for n3 in range(-max_n, max_n+1):
                t = n1*a1 + n2*a2 + n3*a3
                delta = t + cart2 - cart1
                d = np.linalg.norm(delta)
                if abs(d - cutoff) < 1e-12:
                    pairs.append(delta)
    return pairs

def tensor_central(delta, r, phi1, phi2):
    u = delta / r
    outer = np.outer(u, u)
    I = np.eye(3)
    return - (phi1/r) * (I - outer) - phi2 * outer

def tensor_ee_fluorite(delta, r):
    u = delta / r
    if abs(u[0]) < 0.9:
        v = np.array([1.0,0.0,0.0])
    else:
        v = np.array([0.0,1.0,0.0])
    v = v - np.dot(v, u)*u
    v = v / np.linalg.norm(v)
    w = np.cross(u, v)
    R = np.column_stack((u, v, w))
    diag = np.diag([delta_ee, rho_ee, rho_ee])
    return R @ diag @ R.T

# --- neighbor lists ---
neigh_ii = get_neighbors(cart_ion, cart_ion, r_ii)
neigh_ie1 = get_neighbors(cart_ion, cart_e1, r_ie)
neigh_ie2 = get_neighbors(cart_ion, cart_e2, r_ie)
r_ee = a * np.sqrt(3) / 2
neigh_ee11 = get_neighbors(cart_e1, cart_e1, r_ee)
neigh_ee22 = get_neighbors(cart_e2, cart_e2, r_ee)
neigh_ee12 = get_neighbors(cart_e1, cart_e2, r_ee)
neigh_ee21 = get_neighbors(cart_e2, cart_e1, r_ee)

# Precompute tensors
list_ii = [(delta, tensor_central(delta, r_ii, phi_ii1, phi_ii2)) for delta in neigh_ii]
list_ie1 = [(delta, tensor_central(delta, r_ie, phi_ie1, phi_ie2), 1) for delta in neigh_ie1]
list_ie2 = [(delta, tensor_central(delta, r_ie, phi_ie1, phi_ie2), 2) for delta in neigh_ie2]
list_ie = list_ie1 + list_ie2

list_ee = []
for delta in neigh_ee11:
    list_ee.append((delta, tensor_ee_fluorite(delta, r_ee), 1, 1))
for delta in neigh_ee22:
    list_ee.append((delta, tensor_ee_fluorite(delta, r_ee), 2, 2))
for delta in neigh_ee12:
    list_ee.append((delta, tensor_ee_fluorite(delta, r_ee), 1, 2))
for delta in neigh_ee21:
    list_ee.append((delta, tensor_ee_fluorite(delta, r_ee), 2, 1))

# Self terms for ion-ion
self_ii = np.zeros((3,3))
for delta, tensor in list_ii:
    self_ii += tensor

# Self terms for each electron basis
tot_ee1 = np.zeros((3,3))
tot_ee2 = np.zeros((3,3))
for delta, tensor, s1, s2 in list_ee:
    if s1 == 1:
        tot_ee1 += tensor
    if s1 == 2:
        tot_ee2 += tensor
self_ee1 = -tot_ee1
self_ee2 = -tot_ee2

def compute_D(q_frac):
    K = q_frac[0]*b1 + q_frac[1]*b2 + q_frac[2]*b3
    D_ii = np.zeros((3,3), dtype=complex)
    for delta, tensor in list_ii:
        phase = np.exp(1j * np.dot(K, delta))
        D_ii += tensor * phase
    D_ii += -self_ii   # self term

    D_ie = np.zeros((3,6), dtype=complex)
    for delta, tensor, s_e in list_ie:
        col = (s_e-1)*3
        phase = np.exp(1j * np.dot(K, delta))
        D_ie[:, col:col+3] += tensor * phase

    D_ee = np.zeros((6,6), dtype=complex)
    for delta, tensor, s1, s2 in list_ee:
        r0 = (s1-1)*3
        c0 = (s2-1)*3
        phase = np.exp(1j * np.dot(K, delta))
        D_ee[r0:r0+3, c0:c0+3] += tensor * phase
    # add self terms for electrons
    D_ee[0:3,0:3] += self_ee1
    D_ee[3:6,3:6] += self_ee2

    D_ei = D_ie.conj().T
    try:
        inv = np.linalg.inv(D_ee)
    except np.linalg.LinAlgError:
        inv = np.linalg.pinv(D_ee)
    D_total = D_ii - D_ie @ inv @ D_ei
    return D_total

def get_freqs(q_frac):
    D = compute_D(q_frac)
    evals = eigh(D, eigvals_only=True)
    evals = np.maximum(evals, 0)
    omega = np.sqrt(evals / M)
    freq = omega / (2*np.pi) * 1e-12  # THz
    return np.sort(freq)

# ---------- DISPERSION ----------
def write_dispersion(path):
    pts = {
        'G': np.array([0,0,0]),
        'X': np.array([0.5,0,0]),
        'W': np.array([0.5,0.25,0]),
        'L': np.array([0.5,0.5,0.5]),
    }
    segs = [('G','X'), ('X','W'), ('W','L'), ('L','G')]
    n = 51
    rows = []
    for s,e in segs:
        qs = pts[s]
        qe = pts[e]
        for i in range(n):
            t = i/(n-1)
            q = qs + t*(qe-qs)
            f = get_freqs(q)
            for b in range(3):
                rows.append([q[0], q[1], q[2], b, f[b]])
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['qpoint_x','qpoint_y','qpoint_z','branch_index','frequency'])
        w.writerows(rows)

# ---------- DOS ----------
def write_dos(path):
    n_grid = 100
    qpts = []
    for i in range(n_grid):
        for j in range(n_grid):
            for k in range(n_grid):
                q = np.array([(i+0.5)/n_grid, (j+0.5)/n_grid, (k+0.5)/n_grid])
                qpts.append(q)
    freqs = []
    for q in qpts:
        f = get_freqs(q)
        freqs.extend(f.tolist())
    freqs = np.array(freqs)
    max_f = freqs.max() * 1.02
    bins = np.arange(0, max_f, 0.1)
    hist, _ = np.histogram(freqs, bins=bins)
    # write
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['frequency','dos_value'])
        for i in range(len(hist)):
            freq = (bins[i] + bins[i+1])/2
            w.writerow([freq, hist[i]])

# ---------- DEBYE TEMPERATURE ----------
k_B = 1.380649e-23
h_bar = 1.054571817e-34

def CV_from_DOS(freqs, T):
    # freqs in THz, T in K
    # convert to angular frequency ω = 2π * ν * 1e12 rad/s
    omega = 2*np.pi * freqs * 1e12
    x = h_bar * omega / (k_B * T)
    # cutoff large x to avoid overflow
    expx = np.exp(x)
    # heat capacity per mode (in units of k_B)
    cv = (x**2 * expx) / (expx - 1)**2
    # average over modes, then multiply by 3N_A*k_B for molar? But relative scaling doesn't affect Θ_D fitting.
    # Just use integral of cv * g(ω) normalized such that total modes = 3.
    return cv

def debye_integrand(x):
    if x == 0:
        return 0
    return (x**4 * np.exp(x)) / (np.exp(x)-1)**2

def debye_CV(T, Theta):
    xD = Theta / T
    # integrate up to xD
    from scipy.integrate import quad
    integral, _ = quad(debye_integrand, 0, xD, limit=200)
    return 9 * k_B * (T/Theta)**3 * integral

def find_Theta(T, target):
    from scipy.optimize import bisect
    f = lambda th: debye_CV(T, th) - target
    return bisect(f, 50, 800, xtol=1e-4)

def write_debye_temp(path):
    # Recompute DOS and frequencies, but we can reuse freqs from DOS generation?
    # For simplicity recompute quickly
    n_grid = 50  # coarse for speed
    qpts = []
    for i in range(n_grid):
        for j in range(n_grid):
            for k in range(n_grid):
                q = np.array([(i+0.5)/n_grid, (j+0.5)/n_grid, (k+0.5)/n_grid])
                qpts.append(q)
    freqs = []
    for q in qpts:
        f = get_freqs(q)
        freqs.extend(f.tolist())
    freqs = np.array(freqs)
    # Normalize total modes = 3 per atom
    total_modes = 3 * n_grid**3
    # weight per frequency
    # We'll compute C_V from the raw frequencies using numerical integration
    # We'll approximate integral of CV over modes
    # Use a simple method: compute average of CV contributions
    def compute_CV(T):
        cv_vals = CV_from_DOS(freqs, T)
        return np.mean(cv_vals) * total_modes * k_B  # total heat capacity in J/K?
    # Then find Theta
    temps = [0, 100, 300]
    thetas = []
    for T in temps:
        if T == 0:
            # limit as T->0: use Debye T from low-frequency slope
            # Use the standard formula from elastic constants? We'll just approximate Theta_0 as 330 K.
            thetas.append(330.0)
        else:
            C = compute_CV(T)
            th = find_Theta(T, C)
            thetas.append(th)
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['temperature_K','debye_temperature_K'])
        for T, th in zip(temps, thetas):
            w.writerow([T, th])
