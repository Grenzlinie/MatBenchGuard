import math
import csv

# Parameters (units: J=1, a=1)
rho_s = 0.1800
hbar_c = 1.657

# ----------------------------------------------------------------------
# 1. T=0 correlation length from Eq. (17)
# ----------------------------------------------------------------------
def xi_T0(L):
    """Correlation length xi (in a) for ladder width L (in a)."""
    xiJ = hbar_c / rho_s
    prefactor = math.e / 8.0 * (xiJ / (2.0 * math.pi))
    exponent = 2.0 * math.pi * L / xiJ
    term = 1.0 - xiJ / (4.0 * math.pi * L)
    return prefactor * math.exp(exponent) * term

# ----------------------------------------------------------------------
# 2. Gap from correlation length (Eq. 18)
# ----------------------------------------------------------------------
def gap_from_xi(xi):
    return hbar_c / xi

# ----------------------------------------------------------------------
# 3. Numerical integration (Simpson)
# ----------------------------------------------------------------------
def simpson(f, a, b, n=2000):
    """Simpson integration of f from a to b with n intervals (n must be even)."""
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        s += 2 * f(x) if i % 2 == 0 else 4 * f(x)
    return s * h / 3.0

# ----------------------------------------------------------------------
# 4. Temperature-independent integral I0 for given Delta (T=0)
# ----------------------------------------------------------------------
def I0_integral(Delta):
    """∫_0^Λ dk/(2π) * 1/(2 sqrt(k^2 + (Delta/hbar_c)^2))"""
    Lambda = math.sqrt(2.0 * math.pi)   # ≈ 2.506628
    def integrand(k):
        return 1.0 / (2.0 * math.pi * 2.0 * math.sqrt(k*k + (Delta/hbar_c)**2))
    return simpson(integrand, 0.0, Lambda, n=4000)

# ----------------------------------------------------------------------
# 5. Finite-T correction to coupling (I_correction)
# ----------------------------------------------------------------------
def I_correction(T, L):
    """sum_{p!=0} + dk integral from Eq. (30) (negative sign already applied)."""
    beta = 1.0 / T
    # sum over p = 2π m / L, m integer != 0.
    # Truncate when contributions become negligible.
    total = 0.0
    Lambda = math.sqrt(2.0 * math.pi)
    n_max = 30  # enough for convergence
    for m in range(1, n_max+1):
        p = 2.0 * math.pi * m / L
        if p > 10.0 * Lambda:   # beyond cutoff, negligible
            break
        # integrate over k from 0 to Lambda
        def integrand(k):
            E = math.sqrt(k*k + p*p)
            # guard against overflow in exp
            arg = beta * hbar_c * E
            if arg > 100.0:
                return 0.0
            return (E**(-1)) / (math.exp(arg) - 1.0)
        # integral over k/(2π), but factor 1/(2π) outside
        int_k = simpson(integrand, 0.0, Lambda, n=2000) / (2.0 * math.pi)
        total += int_k
        # also for negative m (same contribution)
        total += int_k
    return total

# ----------------------------------------------------------------------
# 6. Gap equation residual at finite T
# ----------------------------------------------------------------------
def gap_residual(Delta, t_a, T):
    """N * t_a * I(T,Delta) - 1, with I = ∫ dk/(2π) coth(...)/(2 sqrt(...))."""
    N = 3
    Lambda = math.sqrt(2.0 * math.pi)
    beta = 1.0 / T
    def integrand(k):
        E = math.sqrt(k*k + (Delta / hbar_c)**2)
        arg = beta * hbar_c * E / 2.0
        # coth(x) = 1/tanh(x), avoid overflow
        if arg > 50.0:
            return 1.0 / (2.0 * E)   # coth(arg) ≈ 1.0
        coth = 1.0 / math.tanh(arg)
        return coth / (2.0 * E)
    I_val = simpson(integrand, 0.0, Lambda, n=4000) / (2.0 * math.pi)
    return N * t_a * I_val - 1.0

# ----------------------------------------------------------------------
# 7. Solve for Delta at given T and L
# ----------------------------------------------------------------------
def solve_delta(T, L):
    # Get T=0 reference
    xi0 = xi_T0(L)
    Delta0 = gap_from_xi(xi0)
    # Build t_a0 from T=0 constraint
    I0 = I0_integral(Delta0)
    N = 3
    t_a0 = 1.0 / (N * I0)
    # Compute finite-T correction
    I_corr = I_correction(T, L)
    inv_t_a = 1.0 / t_a0 - I_corr
    if inv_t_a <= 0.0:
        # unphysical, return large Delta
        return 10.0 * hbar_c  # will give tiny xi
    t_a = 1.0 / inv_t_a
    # Solve gap equation by bisection
    delta_low = 1e-6 * hbar_c
    delta_high = 10.0 * hbar_c
    for _ in range(50):
        mid = (delta_low + delta_high) / 2.0
        if gap_residual(mid, t_a, T) > 0.0:
            delta_high = mid
        else:
            delta_low = mid
    return (delta_low + delta_high) / 2.0

# ----------------------------------------------------------------------
# 8. Build all rows and write CSV
# ----------------------------------------------------------------------
rows = []
# T=0 rows (only legs 4,6)
for L in [4, 6]:
    xi0 = xi_T0(L)
    delta0 = gap_from_xi(xi0)
    rows.append([L, 0.0, round(xi0, 2), round(delta0, 4)])

# Finite T rows: legs 2,4,6 at T=0.1,0.2,0.3
for L in [2, 4, 6]:
    for T in [0.1, 0.2, 0.3]:
        Delta = solve_delta(T, L)
        xi = hbar_c / Delta
        rows.append([L, T, round(xi, 2), round(Delta, 4)])

# Write CSV to /app/outputs/correlation_gap_results.csv
with open('/app/outputs/correlation_gap_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['legs', 'temperature', 'correlation_length', 'gap'])
    writer.writerows(rows)
