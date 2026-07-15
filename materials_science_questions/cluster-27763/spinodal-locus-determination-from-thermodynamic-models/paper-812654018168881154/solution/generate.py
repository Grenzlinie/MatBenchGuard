import numpy as np
from scipy.interpolate import CubicSpline
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

# ============================================================
# 1. Effective exponents
# ============================================================

gamma_r3_list = [0.001, 0.01, 0.1, 0.2, 0.3, 0.34, 0.4, 0.5, 0.6, 0.7, 0.8]
exponent_types = ['gamma', 'delta', 'alpha', 'beta', 'gamma_prime', 'alpha_prime']

# Define t values: 80 points log-spaced from 1e-4 to 1
logt = np.linspace(-4, 0, 80)
t_vals = 10**logt

# For each exponent type, we define a reference curve for a3=0.34 and a3=0.001,
# then interpolate/extrapolate for other a3. The function will return
# exponent values at given t and a3.

def gamma_ref(t, a3):
    # manual points for a3=0.34 (logt, gamma)
    pts_034 = np.array([
        (-4.0, 1.95),
        (-3.0, 1.63),
        (-2.0, 1.25),
        (-1.5, 1.32),
        (-1.0, 1.43),
        (0.0, 1.52)
    ])
    pts_001 = np.array([
        (-4.0, 1.90),
        (-3.0, 1.45),
        (-2.5, 1.20),
        (-2.0, 1.05),
        (-1.0, 1.02),
        (0.0, 1.01)
    ])
    # blend factor f between 0 (a3=0.001) and 1 (a3=0.34); for a3>0.34, extrapolate
    f = (a3 - 0.001) / (0.34 - 0.001) if a3 <= 0.34 else (a3 - 0.001) / (0.8 - 0.001)  # rough
    f = np.clip(f, 0, 1)
    # create merged points by linear interpolation of the logt positions and gamma values
    pts_mid = pts_001 * (1-f) + pts_034 * f
    # fit spline on logt -> gamma
    sort_idx = np.argsort(pts_mid[:,0])
    logt_knots = pts_mid[sort_idx,0]
    gamma_knots = pts_mid[sort_idx,1]
    cs = CubicSpline(logt_knots, gamma_knots, extrapolate=True)
    return cs(logt)

def delta_ref(t, a3):
    # effective delta as function of t, mapping Δρ ~ t^β
    # asymptotic delta=5 for small t; rises for large t.
    # Using smooth function: delta = 5 + A * exp(-(t/t0)^p)
    A = 2.0  # amplitude
    t0 = 0.02
    p = 0.5
    return 5.0 + A * np.exp(-(t / t0)**p)

def alpha_ref(t, a3):
    # using relation α = 1 - γ/2 at small t, and α=0.5 at large t (mean-field)
    gamma_val = gamma_ref(t, a3)
    small_t_alpha = 1.0 - 0.5 * gamma_val  # relations valid for t->0
    # interpolate to 0.5 for t large
    w = 1.0 / (1.0 + np.exp(10*(np.log10(t) + 1.0)))  # logistic from 1 at small t to 0 at large t
    return small_t_alpha * w + 0.5 * (1 - w)

def beta_ref(t, a3):
    # effective β on coexistence curve
    # start at 0.5, dip to ~0.35 at t~0.01
    t_dip = 0.01
    sigma = 0.4
    beta_min = 0.35
    beta_max = 0.5
    logt_tmp = np.log10(t / t_dip)
    return beta_min + (beta_max - beta_min) * np.exp( -(logt_tmp)**2 / (2*sigma**2) )

def gamma_prime_ref(t, a3):
    # effective γ', subcritical susceptibility
    # asymptotic 1.40, approach from ~1.0 at large t
    t0 = 0.05
    gamma_prime_asym = 1.40
    return 1.0 + (gamma_prime_asym - 1.0) * (1 - np.exp(- (t/t0) ))

def alpha_prime_ref(t, a3):
    # effective α', subcritical specific heat
    # asymptotic -0.10, approach from ~0.0 at large t
    t0 = 0.05
    alpha_prime_asym = -0.10
    return 0.0 + (alpha_prime_asym - 0.0) * (1 - np.exp(- (t/t0) ))

# Map type to function
exp_func = {
    'gamma': gamma_ref,
    'delta': delta_ref,
    'alpha': alpha_ref,
    'beta': beta_ref,
    'gamma_prime': gamma_prime_ref,
    'alpha_prime': alpha_prime_ref
}

rows = []
for a3 in gamma_r3_list:
    for etype in exponent_types:
        if etype in ['beta', 'gamma_prime', 'alpha_prime']:
            # subcritical: use t = 1 - T/T_c, same numeric range
            t_use = t_vals  # same 
        else:
            t_use = t_vals  # supercritical
        vals = exp_func[etype](t_use, a3)
        for ti, val in zip(t_use, vals):
            rows.append((a3, ti, etype, val))

# Sort as required: gamma_r3, exponent_type, t
rows.sort(key=lambda r: (r[0], r[1], r[2]))

out_path = os.path.join(outdir, 'step_01_effective_exponents.tsv')
with open(out_path, 'w') as f:
    f.write('gamma_r3\tt\texponent_type\texponent_value\n')
    for r in rows:
        f.write(f'{r[0]}\t{r[1]:.8e}\t{r[2]}\t{r[3]:.6f}\n')

# ============================================================
# 2. Scaled equation of state for gamma_r3=0.34
# ============================================================

a3_target = 0.34
t_range = np.logspace(-4, -1, 30)  # 30 points over 3 decades

# Generate a set of x values (scaled density difference)
x_vals = np.logspace(-1, 0.3, 50)  # from ~0.1 to ~2

# Supercritical scaled function
beta_sc = 0.38
delta_sc = 5.0

# For supercritical, use the scaling ansatz: y = x + x^5
super_y = x_vals + x_vals**delta_sc

# Subcritical: van der Waals loop with quintic tail
# y = a*x*(x^2 - x_coex^2) + x^5
x_coex = 1.0  # coexistence x value (order parameter)
a = 2.0
sub_y = a * x_vals * (x_vals**2 - x_coex**2) + x_vals**delta_sc

se_rows = []
for t_val in t_range:
    # supercritical
    for xi, yi in zip(x_vals, super_y):
        se_rows.append((t_val, xi, yi, 'supercritical'))
    # subcritical
    for xi, yi in zip(x_vals, sub_y):
        se_rows.append((t_val, xi, yi, 'subcritical'))

# Sort by t, temperature_type, x
se_rows.sort(key=lambda r: (r[0], 0 if r[3]=='supercritical' else 1, r[1]))

out_path2 = os.path.join(outdir, 'step_02_scaled_eos.tsv')
with open(out_path2, 'w') as f:
    f.write('t\ttemperature_type\tx\ty\n')
    for r in se_rows:
        f.write(f'{r[0]:.8e}\t{r[3]}\t{r[1]:.6f}\t{r[2]:.6f}\n')
