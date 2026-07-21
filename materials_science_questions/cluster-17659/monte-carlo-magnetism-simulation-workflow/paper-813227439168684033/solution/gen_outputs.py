import math
import csv

# --- parameters matching the paper's simulation for N=9171 ---
Delta2 = 2.0
E_dm = 100.0            # 50 * Delta2
W = 5.0                 # 2.5 * Delta2
tau = E_dm / Delta2**2  # 25

# constants
pi = math.pi
alpha = 16 * pi / (9 * math.sqrt(3))        # Eq. (4.16)
Gamma0 = Delta2**2 / (4 * W)                # 0.2
coeff = 4 * alpha * Gamma0 * E_dm / W      # = 16*alpha ≈ 51.58
kappa2 = 50.0                              # finite‑sample value from paper

# --- TGA parameters as functions of m (Eqs. (5.31)–(5.34)) ---
def tga_params(m):
    one_minus_m2 = 1.0 - m * m
    a0   = 1.0 - 1.5 * m * one_minus_m2
    a_plus = 0.5 * m * one_minus_m2
    a_minus = m * one_minus_m2
    sigma2 = (kappa2 - 48.0 * m) * one_minus_m2 * E_dm**2
    sigma  = math.sqrt(max(sigma2, 0.0))
    return a0, a_plus, a_minus, sigma

# --- pre‑compute ℱ on a uniform grid of m to speed ODE integration ---
def gauss_integral_contrib(center, sigma, n_grid=200):
    """
    Numerically evaluate  W² ∫_{|E|>W} g(E) / E² dE  for a single Gaussian
    g(E) = (1/√(2πσ²)) exp(–(E–center)²/(2σ²)).
    Integration uses trapezoidal rule on a uniform grid.
    """
    E_max = 15.0 * E_dm          # cut‑off far enough
    h = (E_max - W) / n_grid
    s = 0.0
    # positive side
    for i in range(n_grid + 1):
        E = W + i * h
        w = 0.5 if (i == 0 or i == n_grid) else 1.0
        val = math.exp(-(E - center)**2 / (2 * sigma**2)) / (math.sqrt(2.0 * pi) * sigma)
        s += w * val / E**2
    s *= h
    # negative side (symmetric loop)
    for i in range(n_grid + 1):
        E = -W - i * h
        w = 0.5 if (i == 0 or i == n_grid) else 1.0
        val = math.exp(-(E - center)**2 / (2 * sigma**2)) / (math.sqrt(2.0 * pi) * sigma)
        s += w * val / E**2
    s *= h
    return s * W**2

def compute_F(m, sigma, a0, a_plus, a_minus):
    """return ℱ = W²∫_{|E|>W} ρ(E)/E² dE  for given TGA parameters"""
    if sigma == 0.0:
        return 0.0
    F = a0 * gauss_integral_contrib(0.0, sigma) \
        + a_plus * gauss_integral_contrib(8.0 * E_dm, sigma) \
        + a_minus * gauss_integral_contrib(-4.0 * E_dm, sigma)
    return F

# Build a lookup table for m ∈ [-1, 1] with step 0.001
m_grid = []
F_grid = []
for t in range(2001):
    m_val = -1.0 + 0.001 * t
    a0, a_plus, a_minus, sigma = tga_params(m_val)
    F_val = compute_F(m_val, sigma, a0, a_plus, a_minus)
    m_grid.append(m_val)
    F_grid.append(F_val)

def F_from_m(m):
    """linear interpolation of precomputed ℱ"""
    import bisect
    idx = bisect.bisect_left(m_grid, m)
    if idx == 0:
        return F_grid[0]
    if idx == len(m_grid):
        return F_grid[-1]
    low, high = m_grid[idx-1], m_grid[idx]
    f_low, f_high = F_grid[idx-1], F_grid[idx]
    t = (m - low) / (high - low)
    return f_low + t * (f_high - f_low)

# --- ODE integration ---
t_max = 5.0 * tau
dt_ode = 0.001                   # small step
target_t_norm = [0.1, 0.3, 0.5, 1.0, 3.0, 5.0]
target_t = [tn * tau for tn in target_t_norm]

m = 1.0
nr = 1.0
mr = 1.0
t = 0.0
target_idx = 0
m_series = []

while t < t_max and target_idx < len(target_t):
    F_val = F_from_m(m)
    dnr = -coeff * nr * (nr - F_val)
    dmr = -2.0 * Gamma0 * mr - coeff * nr * (mr - m * F_val)
    dm  = -2.0 * Gamma0 * mr

    nr += dnr * dt_ode
    mr += dmr * dt_ode
    m  += dm  * dt_ode
    t  += dt_ode

    # physical clamps
    if nr < 0.0: nr = 0.0
    if m < -1.0: m = -1.0
    if mr < 0.0: mr = 0.0

    while target_idx < len(target_t) and t >= target_t[target_idx]:
        m_series.append((target_t_norm[target_idx], m))
        target_idx += 1

# fill any remaining times with last m
while target_idx < len(target_t):
    m_series.append((target_t_norm[target_idx], m))
    target_idx += 1

# 1. Write magnetization_curve.csv
with open('/app/outputs/magnetization_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'magnetization'])
    for tn, m_val in m_series:
        writer.writerow([f'{tn}', f'{m_val:.6f}'])

# 2. Write sqrt_coefficient.txt = theoretical Γ₁/₂ (Eq. (6.20))
G_theory = (1.0 / (pi * alpha)) * (Delta2**2 / E_dm)
with open('/app/outputs/sqrt_coefficient.txt', 'w') as f:
    f.write(f'{G_theory:.10f}\n')
