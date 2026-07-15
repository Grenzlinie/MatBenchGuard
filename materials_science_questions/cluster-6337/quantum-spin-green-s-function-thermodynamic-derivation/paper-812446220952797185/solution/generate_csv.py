import csv
import math
import sys

# ------------------------------------------------------------
# Spin‑1 TIM effective‑field theory (EFT) for honeycomb (Z=3)
# Equations from paper: (26) with decoupling, (35)‑(45).
# All quantities are dimensionless (J=1).
# ------------------------------------------------------------

Z = 3

def safe_exp(x):
    if x > 500: return 1e300
    if x < -500: return 0.0
    return math.exp(x)

def f(x, beta, Omega):
    """f(x) from eq. (10)"""
    E = math.sqrt(Omega**2 + x**2)
    be = beta * E
    if be > 500:
        # sinh/cosh ~ 0.5*exp(be)
        return x / E * (1.0)   # limit -> x/E
    sh = math.sinh(be)
    ch = math.cosh(be)
    denom = 1.0 + 2.0 * ch
    if denom == 0:
        return 0.0
    return (x / E) * (2.0 * sh / denom)

def g(x, beta, Omega):
    """g(x) from eq. (11)"""
    E = math.sqrt(Omega**2 + x**2)
    be = beta * E
    if be > 500:
        return Omega / E  # limit
    sh = math.sinh(be)
    ch = math.cosh(be)
    denom = 1.0 + 2.0 * ch
    if denom == 0:
        return 0.0
    return (Omega / E) * (2.0 * sh / denom)

def h(x, beta, Omega):
    """h(x) from eq. (18)"""
    E2 = Omega**2 + x**2
    E = math.sqrt(E2)
    be = beta * E
    if be > 500:
        # cosh dominates, numerator -> (Omega^2 + (Omega^2+2x^2)*ch) / (E2 * 2*ch)  ~ (Omega^2+2x^2)/(2*E2)
        # but limit is (Omega^2+2x^2)/(2*E2) / (1+0+...)?  Actually from formula, limit -> (Omega^2+2x^2)/(2*E2)? Check
        # For large be, cosh ~ sinh >> 1, numerator ~ (Omega^2+ (Omega^2+2x^2)*ch) / (E2 * (2*ch)) = (Omega^2+2x^2)/(2*E2) + Omega^2/(E2*2*ch) ~ (Omega^2+2x^2)/(2*E2).
        return (Omega**2 + 2*x**2) / (2.0 * E2)
    ch = math.cosh(be)
    denom = E2 * (1.0 + 2.0 * ch)
    if denom == 0:
        return 0.0
    num = Omega**2 + (Omega**2 + 2*x**2) * ch
    return num / denom

def k(x, beta, Omega):
    """k(x) from eq. (19)"""
    E2 = Omega**2 + x**2
    E = math.sqrt(E2)
    be = beta * E
    if be > 500:
        # limit: (x^2 + (2*Omega^2+x^2)*ch) / (E2 * 2*ch) -> (2*Omega^2+x^2)/(2*E2)
        return (2*Omega**2 + x**2) / (2.0 * E2)
    ch = math.cosh(be)
    denom = E2 * (1.0 + 2.0 * ch)
    if denom == 0:
        return 0.0
    num = x**2 + (2*Omega**2 + x**2) * ch
    return num / denom

# ------------------------------------------------------------
# Operator evaluation: O = 1 + mz*sinh(J D) + qz*(cosh(J D) - 1)
# J=1. Rewrite as c0 + c1 e^D + c2 e^{-D}
# Apply to func: sum over i,j,k with j+k <= Z of coeff * func((j-k))
# ------------------------------------------------------------
def apply_operator(mz, qz, func, beta, Omega):
    """Apply O^Z to func(x)|_{x=0} where O = c0 + c1 e^D + c2 e^{-D}."""
    c0 = 1.0 - qz
    c1 = (mz + qz) / 2.0
    c2 = (-mz + qz) / 2.0
    total = 0.0
    # Enumerate all powers of c0, c1, c2 with sum Z, compute shift d = j - k
    # Loop j from 0..Z, k from 0..Z-j, i = Z - j - k
    for j in range(Z + 1):
        for k in range(Z + 1 - j):
            i = Z - j - k
            coeff = 1.0
            if i > 0:
                coeff *= c0**i
            if j > 0:
                coeff *= c1**j
            if k > 0:
                coeff *= c2**k
            # multinomial coefficient
            coeff *= math.comb(Z, i) * math.comb(Z - i, j)  # correct
            d = j - k
            total += coeff * func(d, beta, Omega)
    return total

# ------------------------------------------------------------
# Full self-consistent solve for (mz, mx, qz, qx) at given beta, Omega
# Use damped fixed-point iteration.
# ------------------------------------------------------------
def solve_order_parameters(beta, Omega, initial=(1.0,0.0,1.0,0.5), tol=1e-8, max_iter=500):
    mz, mx, qz, qx = initial
    for it in range(max_iter):
        # Compute RHS using current mz,qz
        new_mz = apply_operator(mz, qz, f, beta, Omega)
        new_mx = apply_operator(mz, qz, g, beta, Omega)
        new_qz = apply_operator(mz, qz, h, beta, Omega)
        new_qx = apply_operator(mz, qz, k, beta, Omega)
        # Under-relaxation (important near transitions)
        damping = 0.5
        mz = mz + damping * (new_mz - mz)
        mx = mx + damping * (new_mx - mx)
        qz = qz + damping * (new_qz - qz)
        qx = qx + damping * (new_qx - qx)
        # Check convergence
        if abs(new_mz - mz)/damping < tol and abs(new_mx - mx)/damping < tol and abs(new_qz - qz)/damping < tol and abs(new_qx - qx)/damping < tol:
            break
    return mz, mx, qz, qx

# ------------------------------------------------------------
# Critical line: solve eqs (39)-(40) Z=3. For given Omega, find T_c where 3K=1.
# K from eq (37): K = sinh(D) [q_c*cosh(D) + 1 - q_c]^2 f(x)|_{x=0}
# and q_c is determined by (38): q_c = [q_c*cosh(D) + 1 - q_c]^3 h(x)|_{x=0}
# We'll solve using bisection.
# ------------------------------------------------------------
def aux_K_and_qc(beta, Omega):
    """Return K, qc for given beta, Omega."""
    # Solve qc self-consistently (eq 38) via fixed point
    qc = 2.0/3.0  # high-T guess
    for _ in range(200):
        # apply operator (with mz=0) O = 1 + qc*(cosh(D)-1) = (1-qc) + qc*cosh(D)
        # So O^Z with mz=0: only even terms. We can reuse apply_operator with mz=0.
        new_qc = apply_operator(0.0, qc, h, beta, Omega)
        if abs(new_qc - qc) < 1e-12:
            break
        qc = new_qc
    # Now compute K: K = sinh(D) * [qc*cosh(D) + 1 - qc]^{Z-1} f(x)|_{x=0}
    # For Z=3, Z-1 = 2. So O2 = (1 - qc) + qc*cosh(D) raised to 2, then multiplied by sinh(D) and applied to f.
    # We can compute directly using the operator algebra.
    # We'll expand O2 = (c0 + c1 (e^D+e^{-D})/2)^2 where c0 = 1-qc, c1 = qc.
    c0 = 1.0 - qc
    c1 = qc
    # O2 = A0 + A1 e^D + A2 e^{-D} + A3 e^{2D} + A4 e^{-2D}
    # Compute coefficients by expanding (c0 + c1/2 e^D + c1/2 e^{-D})^2
    # using multinomial formula.
    total = 0.0
    # We'll brute-force over shifts from -4 to 4
    for d in range(-4, 5):
        coeff = 0.0
        # iterate over powers
        for j in range(3):  # power of e^D
            for k in range(3):  # power of e^{-D}
                i = 2 - j - k
                if i < 0 or i > 2:
                    continue
                if j - k != d:
                    continue
                coeff += (c0**i) * ((c1/2.0)**j) * ((c1/2.0)**k) * math.comb(2, i) * math.comb(2-i, j) if i <=2 else 0
        # Now apply sinh(D) to this term: <sinh(D) e^{d D}> f(x)|_{x=0} = 0.5*(f(d+1) - f(d-1))
        if coeff != 0.0:
            total += coeff * 0.5 * (f(d+1, beta, Omega) - f(d-1, beta, Omega))
    return total, qc

def find_Tc(Omega):
    """Return kBTc/J for given Omega (J=1)."""
    # If Omega >= Omega_c, Tc = 0
    Omega_c = 2.241  # approximate from paper for Z=3; we can compute by solving K(infty)=1/Z? Actually at T=0, beta infinite. We'll handle by setting Tc=0 if Tc < 1e-6.
    if Omega >= Omega_c:
        return 0.0
    # Use bisection in temperature T (kBT/J = 1/beta)
    low_T = 1e-6
    high_T = 2.0
    # Ensure K at low_T > 1/Z, K at high_T < 1/Z
    beta_low = 1.0 / low_T
    K_low, _ = aux_K_and_qc(beta_low, Omega)
    beta_high = 1.0 / high_T
    K_high, _ = aux_K_and_qc(beta_high, Omega)
    if K_low <= 1/Z:
        return 0.0
    if K_high >= 1/Z:
        high_T = 5.0
        beta_high = 1.0 / high_T
        K_high, _ = aux_K_and_qc(beta_high, Omega)
        if K_high >= 1/Z:
            return high_T
    for _ in range(60):
        mid = (low_T + high_T) / 2.0
        beta_mid = 1.0 / mid
        K_mid, _ = aux_K_and_qc(beta_mid, Omega)
        if K_mid > 1/Z:
            low_T = mid
        else:
            high_T = mid
        if high_T - low_T < 1e-8:
            break
    Tc = (low_T + high_T) / 2.0
    return Tc

# ------------------------------------------------------------
# CSV writers
# ------------------------------------------------------------
def write_critical():
    Omega_c = 2.241
    points = []
    # Omega from 0 to Omega_c plus a bit beyond
    for om in [i*0.05 for i in range(0, 51)]:  # 0..2.5
        if om > Omega_c + 0.1:
            Tc = 0.0
        else:
            Tc = find_Tc(om)
            if Tc < 5e-5:
                Tc = 0.0
        points.append((om, Tc))
    writer = csv.writer(sys.stdout)
    writer.writerow(['omega_over_J', 'kBTc_over_J'])
    for om, tc in points:
        writer.writerow([f'{om:.6f}', f'{tc:.8f}'])

def write_temperature_dependence():
    Omega = 1.5
    # Determine Tc at this Omega
    Tc = find_Tc(Omega)
    print(f"# Tc at Omega={Omega} = {Tc:.6f}", file=sys.stderr)
    T_range = []
    if Tc > 0.02:
        T_range = [i * 0.01 for i in range(0, 100)]  # up to 1.0
    else:
        T_range = [i * 0.005 for i in range(0, 20)]
    # Ensure we include temperatures above Tc
    T_range += [Tc + 0.01, Tc + 0.05]  # add above Tc
    T_range = sorted(set(T_range))
    writer = csv.writer(sys.stdout)
    writer.writerow(['kBT_over_J', 'mz', 'mx', 'qz', 'qx'])
    for T in T_range:
        if T < 0.0001:
            T = 0.0001
        beta = 1.0 / T
        if T < Tc:
            init = (1.0, 0.0, 1.0, 0.5)
        else:
            init = (0.0, 0.0, 2.0/3.0, 2.0/3.0)  # paramagnetic
        mz, mx, qz, qx = solve_order_parameters(beta, Omega, initial=init, tol=1e-8, max_iter=500)
        # enforce mz=0 if T>Tc
        if T >= Tc:
            mz = 0.0
        writer.writerow([f'{T:.8f}', f'{mz:.8f}', f'{mx:.8f}', f'{qz:.8f}', f'{qx:.8f}'])

def write_field_dependence():
    T = 0.05
    beta = 1.0 / T
    Omega_max = 2.5
    points = [i*0.05 for i in range(0, 51)]
    writer = csv.writer(sys.stdout)
    writer.writerow(['omega_over_J', 'mz', 'mx'])
    for om in points:
        # For T=0.05, mz may be zero above Omega_c
        init = (1.0, 0.0, 1.0, 0.5)
        mz, mx, _, _ = solve_order_parameters(beta, om, initial=init, tol=1e-8, max_iter=500)
        if mz < 1e-8:
            mz = 0.0
        writer.writerow([f'{om:.6f}', f'{mz:.8f}', f'{mx:.8f}'])

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'critical':
        write_critical()
    elif mode == 'temperature':
        write_temperature_dependence()
    elif mode == 'field':
        write_field_dependence()
    else:
        print('Usage: generate_csv.py critical|temperature|field')
        sys.exit(1)