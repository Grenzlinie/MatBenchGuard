import math

# --- physical constants (cgs units) ---
SIGMA = 20.0          # ice-water interfacial free energy (erg/cm^2)
RHO   = 1.0            # density of water (g/cm^3)
L     = 3.34e9         # latent heat of fusion (erg/g)
T_m   = 273.0           # melting temperature (K)
K_B   = 1.380649e-16    # Boltzmann constant (erg/K)
K_COEFF = 1e20          # kinetic prefactor per unit area (cm^-2 s^-1)

# --- substrate parameter ---
M = 0.5

# --- pit distribution parameters ---
A0  = 2e-15             # most probable pit area (cm^2)
GAMMA = 0.8
BETA  = 0.001

# --- target data ---
TARGETS = [
    (100, 0.1),
    (100, 0.5),
    (100, 0.9),
    (316, 0.1),
    (316, 0.5),
    (316, 0.9),
    (1000, 0.1),
    (1000, 0.5),
    (1000, 0.9),
]

def fletcher_f(m, x):
    """
    Spherical cap factor f(m,x) from Fletcher (1963).
    x = R / r*   (R particle radius, r* critical embryo radius)
    """
    if x <= 0:
        return 1.0
    g = math.sqrt(1.0 + x*x - 2.0*m*x)
    # guard for small x to avoid division by zero; when x->0, f->1
    if g < 1e-12:
        return 1.0
    term1 = ((1.0 - m*x) / g) ** 3
    term2 = (x**3 / 2.0) * (2.0 - 3.0*(x - m)/g + ((x - m)/g)**3)
    term3 = 1.5 * m * x**2 * ((x - m)/g - 1.0)
    return 0.5 * (1.0 + term1) + term2 + term3

def delta_G0(dT):
    """Homogeneous nucleation barrier (erg) for supercooling dT (K)."""
    if dT <= 0:
        return float('inf')
    return (16.0 * math.pi / 3.0) * (SIGMA**3) * (T_m**2) / (RHO**2 * L**2 * dT**2)

def r_star(dT):
    """Critical embryo radius (cm) for supercooling dT (K)."""
    if dT <= 0:
        return float('inf')
    return 2.0 * SIGMA * T_m / (RHO * L * dT)

def barrier(m, R_cm, alpha, T):
    """
    ΔG* for a spherical particle with a conical pit of relative area alpha.
    R_cm : particle radius in cm
    alpha : pit area / R^2
    T     : temperature (K)
    """
    dT = T_m - T
    if dT <= 0:
        return float('inf')
    dG0 = delta_G0(dT)
    rstar = r_star(dT)
    x = R_cm / rstar
    f = fletcher_f(m, x)
    # surface term from the active site
    surface_term = alpha * (R_cm**2) * (1.0 - m) * SIGMA
    return dG0 * f - surface_term

def nucleation_rate(R_cm, alpha, T):
    """Total nucleation rate per particle (s^-1)."""
    dGstar = barrier(M, R_cm, alpha, T)
    area = 4.0 * math.pi * (R_cm**2)
    return area * K_COEFF * math.exp(-dGstar / (K_B * T))

def threshold_temperature(R_cm, alpha):
    """
    Return the temperature (K) where nucleation occurs within 1 second
    for given particle radius (cm) and pit area fraction alpha.
    Condition: nucleation_rate = 1 (one nucleus per second).
    Solved by binary search from -60°C to melting temperature.
    """
    T_lo = 213.15   # -60°C
    T_hi = 273.0    # 0°C
    # Ensure that at T_lo, nucleation is impossible (rate ~ 0), at T_hi rate > 1
    if nucleation_rate(R_cm, alpha, T_lo) >= 1.0:
        return T_lo
    for _ in range(60):  # sufficient for convergence to ~1e-6
        T_mid = 0.5 * (T_lo + T_hi)
        if nucleation_rate(R_cm, alpha, T_mid) >= 1.0:
            T_hi = T_mid
        else:
            T_lo = T_mid
    return 0.5 * (T_lo + T_hi)

def pit_probability(R_cm, alpha):
    """
    Probability that a particle of radius R_cm has at least one surface pit
    of area >= alpha * R^2, given the log-normal distribution parameters.
    """
    A = alpha * R_cm**2          # absolute pit area in cm^2
    if A <= 0:
        return 0.0
    # Eq. (15): x = gamma * ln(A/A0) - 1/(2*gamma)
    x_val = GAMMA * math.log(A / A0) - 0.5 / GAMMA
    # Eq. (16) – approximate number per cm^2
    sq = math.sqrt(x_val**2 + 1.5)
    N = (BETA / (GAMMA * A0)) * math.exp(0.25 / (GAMMA**2) - x_val**2) / (x_val + sq)
    # Total expected number of pits larger than A on the particle surface
    lam = 4.0 * math.pi * R_cm**2 * N
    # Poisson probability of at least one such pit
    return 1.0 - math.exp(-lam)

def main():
    # R values in Å, convert to cm
    R_list = [100, 316, 1000]
    R_cm_dict = {r: r * 1e-8 for r in R_list}

    # Precompute (alpha, T_threshold) pairs for each R
    # We need alpha values covering the transition range
    # Map from R -> list of (alpha, T_K)
    alpha_map = {}
    for R_ang, R_cm in R_cm_dict.items():
        # generate alpha values logarithmically spaced from 1e-7 to 1e-0
        n = 2000
        alphas = [10.0 ** (val) for val in [math.log10(1e-7) + i * (math.log10(1e-0) - math.log10(1e-7)) / (n-1) for i in range(n)]]
        Ts = []
        for a in alphas:
            T = threshold_temperature(R_cm, a)
            Ts.append(T)
        alpha_map[R_ang] = list(zip(alphas, Ts))

    # Build interpolation: given R, T -> alpha_crit (the smallest alpha for which T_threshold >= T)
    # We invert: for a target fraction F, we solve alpha such that pit_probability(alpha) = F,
    # then find the temperature corresponding to that alpha.
    # Instead, we can produce curve T vs F by scanning temperatures.
    results = []
    for R_ang, F_target in TARGETS:
        R_cm = R_cm_dict[R_ang]
        # bisect temperature between -40°C and 0°C
        T_lo = 233.15
        T_hi = 273.0
        # ensure F at low T is >0, at high T is <target
        # For low T, almost any pit size is active -> high probability
        # We'll compute F as function of T and invert.
        def F_vs_T(T):
            # find alpha that gives threshold exactly T; use interpolation of alpha-T pairs
            # but we need the minimum alpha to be active at or above T.
            # Since threshold increases with alpha (larger pits activate at warmer temperatures),
            # for a given T, the condition is alpha >= alpha_crit(T).
            # We invert the monotonic relation threshold_temperature(R_cm, alpha) >= T.
            # Find alpha_crit such that threshold_temperature(R_cm, alpha_crit) == T.
            # Use binary search on alpha.
            alpha_lo, alpha_hi = 1e-10, 1.0
            for _ in range(60):
                mid = 0.5 * (alpha_lo + alpha_hi)
                if threshold_temperature(R_cm, mid) >= T:
                    alpha_hi = mid
                else:
                    alpha_lo = mid
            alpha_crit = 0.5 * (alpha_lo + alpha_hi)
            return pit_probability(R_cm, alpha_crit)
        # ensure F at T_lo >= 0.9 and at T_hi < 0.1
        # adjust bounds if necessary
        if F_vs_T(T_lo) < F_target:
            # lower T_lo
            T_lo = 213.15
        if F_vs_T(T_hi) > F_target:
            # impossible (no particle active at Tm)
            T_hi = T_m
        for _ in range(60):
            T_mid = 0.5 * (T_lo + T_hi)
            if F_vs_T(T_mid) >= F_target:
                T_lo = T_mid
            else:
                T_hi = T_mid
        T_K = 0.5 * (T_lo + T_hi)
        T_C = T_K - 273.15
        results.append((R_ang, F_target, round(T_C, 3)))

    # output CSV
    print("R_Angstrom,F_fraction,T_Celsius")
    for R_ang, F_frac, T_c in results:
        print(f"{R_ang},{F_frac},{T_c}")

if __name__ == "__main__":
    main()
