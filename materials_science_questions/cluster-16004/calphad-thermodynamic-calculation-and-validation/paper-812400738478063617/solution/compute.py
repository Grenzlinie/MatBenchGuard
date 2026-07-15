import math, csv

R = 8.31448
T_fcc = 1273.0
T_liq = 1823.0

# Graphite Gibbs energy per mole of C
def G_gra(T):
    return (-17369 + 170.73*T - 24.3*T*math.log(T) - 4.723e-4*T**2
            + 2562600/T - 2.643e8/T**2 + 1.2e10/T**3)

# --- FCC phase (two sublattice) ---

def G_FeVa_fcc(T):
    return (-237.57 + 132.416*T - 24.6643*T*math.log(T)
            - 3.75752e-3*T**2 - 5.89269e-8*T**3 + 77358.5/T)

def G_NiVa_fcc(T):
    return (-5179.159 + 117.854*T - 22.096*T*math.log(T) - 4.8407e-3*T**2)

def G_FeC_fcc(T):
    return G_FeVa_fcc(T) + G_gra(T) + 77207 - 15.877*T

def G_NiC_fcc(T):
    return G_NiVa_fcc(T) + G_gra(T) + 45000 + 1.88*T

def safe_log(x):
    return math.log(x) if x > 0 else 0.0

def fcc_magnetic(y_Fe, y_Ni, y_Va, T):
    Tc = (-201*y_Fe + 633*y_Ni
          + y_Fe*y_Ni*y_Va*(2133 - 682*(y_Fe - y_Ni)))
    if Tc <= 0:
        return 0.0
    B = (-2.1*y_Fe + 0.52*y_Ni
         + y_Fe*y_Ni*y_Va*(9.55 + 7.23*(y_Fe - y_Ni)
                           + 5.93*(y_Fe - y_Ni)**2
                           + 6.18*(y_Fe - y_Ni)**3))
    if B + 1.0 <= 0:
        return 0.0
    t = T / Tc
    if t < 1.0:
        f = (-0.86034/t + 1.0 - 0.1745*t**3
             - 7.755e-3*t**9 - 1.745e-3*t**15)
    else:
        f = (-4.269e-2*t**-5 - 1.355e-3*t**-15
             - 2.846e-4*t**-25)
    return R * T * math.log(B + 1.0) * f

def G_m_fcc(y_Fe, y_C, T):
    y_Ni = 1.0 - y_Fe
    y_Va = 1.0 - y_C
    G = (y_Fe*y_Va*G_FeVa_fcc(T) + y_Fe*y_C*G_FeC_fcc(T)
         + y_Ni*y_Va*G_NiVa_fcc(T) + y_Ni*y_C*G_NiC_fcc(T))
    G_ideal = R*T*((y_Fe*safe_log(y_Fe) + y_Ni*safe_log(y_Ni))
                   + (y_C*safe_log(y_C) + y_Va*safe_log(y_Va)))
    # Interaction parameters
    L0 = -12054.355 + 3.27413*T
    L1 = 11082.1315 - 4.45077*T
    L2 = -725.805174
    d = y_Fe - y_Ni
    L_FeNiVa = L0 + d*L1 + d*d*L2
    L0c = 49074 - 7.32*T
    L1c = -25800
    L_FeNiC = L0c + d*L1c
    ex1 = y_Fe*y_Ni*(y_C*L_FeNiC + y_Va*L_FeNiVa)
    ex2 = y_Va*y_C*(y_Fe*(-34671.0))   # L_Ni:Va,C = 0
    G_ex = ex1 + ex2
    G_mo = fcc_magnetic(y_Fe, y_Ni, y_Va, T)
    return G + G_ideal + G_ex + G_mo

def mu_C_fcc(y_Fe, y_C, T):
    eps = 1e-6
    y0 = min(max(y_C, 0.0), 1.0 - eps)
    G1 = G_m_fcc(y_Fe, y0 + eps, T)
    G2 = G_m_fcc(y_Fe, y0 - eps, T)
    return (G1 - G2) / (2*eps)

# --- fcc isoactivity CSV ---
y_Fe_vals = [i/10.0 for i in range(11)]           # 0..1 step 0.1
y_C_vals  = [i/100.0 for i in range(1, 13)]      # 0.01..0.12 step 0.01
with open("/app/outputs/fcc_isoactivity_1273K.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T", "x_Ni", "x_Fe", "x_C", "a_C"])
    for y_Fe in y_Fe_vals:
        y_Ni = 1.0 - y_Fe
        for y_C in y_C_vals:
            mu = mu_C_fcc(y_Fe, y_C, T_fcc)
            aC = math.exp((mu - G_gra(T_fcc)) / (R*T_fcc))
            w.writerow([T_fcc, y_Ni/2.0, y_Fe/2.0, y_C/2.0, aC])

# --- Liquid phase (single sublattice) ---

def G_C_liq(T):
    return (100000 + 146.1*T - 24.3*T*math.log(T) - 4.723e-4*T**2
            + 2562600/T - 2.643e8/T**2 + 1.2e10/T**3)

def G_Fe_liq(T):
    # only T>1811 branch (1823 K)
    return -10839.7 + 291.302*T - 46*T*math.log(T)

def G_Ni_liq(T):
    # only T>1728 branch
    return -9549.775 + 268.598*T - 43.1*T*math.log(T)

def G_m_liq(x_Fe, x_Ni, x_C, T):
    G = x_C*G_C_liq(T) + x_Fe*G_Fe_liq(T) + x_Ni*G_Ni_liq(T)
    G += R*T*(x_C*safe_log(x_C) + x_Fe*safe_log(x_Fe) + x_Ni*safe_log(x_Ni))
    # excess
    d_FeC = x_Fe - x_C
    L_FeC0 = -124320 + 28.5*T
    L_FeC1 = 19300
    L_FeC2 = 49260 - 19*T
    L_FeC = L_FeC0 + d_FeC*L_FeC1 + d_FeC*d_FeC*L_FeC2
    L_NiC = -110160 + 34.6*T
    d_FeNi = x_Fe - x_Ni
    L_FeNi0 = -18378.86 + 6.03912*T
    L_FeNi1 = 9228.1 - 3.54642*T
    L_FeNi = L_FeNi0 + d_FeNi*L_FeNi1
    tern_L = 122200 - 58.8*T - 30000*(x_Fe - x_Ni)
    G_ex = (x_Fe*x_C*L_FeC + x_Ni*x_C*L_NiC
            + x_Fe*x_Ni*L_FeNi + x_Fe*x_Ni*x_C*tern_L)
    return G + G_ex

def mu_C_liq(x_Ni_ref, x_C, T):
    eps = 1e-7
    n_Fe0 = 1.0 - x_Ni_ref - x_C
    n_Ni0 = x_Ni_ref
    n_C0  = x_C
    def total_G(n_Fe, n_Ni, n_C):
        n = n_Fe + n_Ni + n_C
        return n * G_m_liq(n_Fe/n, n_Ni/n, n_C/n, T)
    Gp = total_G(n_Fe0, n_Ni0, n_C0 + eps)
    Gm = total_G(n_Fe0, n_Ni0, n_C0 - eps)
    return (Gp - Gm) / (2*eps)

# --- liquid solubility CSV ---
x_Ni_vals = [i/50.0 for i in range(51)]   # 0..1 step 0.02
with open("/app/outputs/liquid_solubility_1823K.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T", "x_Ni_liquid", "x_C_saturated"])
    g_gra = G_gra(T_liq)
    for x_Ni in x_Ni_vals:
        lo, hi = 0.0, 0.5
        f_lo = mu_C_liq(x_Ni, lo, T_liq) - g_gra
        f_hi = mu_C_liq(x_Ni, hi, T_liq) - g_gra
        # Expand search if needed
        if f_lo * f_hi > 0:
            hi = 0.8
            f_hi = mu_C_liq(x_Ni, hi, T_liq) - g_gra
        if f_lo * f_hi > 0:
            # fallback: choose mid of range
            xC = 0.25
        else:
            for _ in range(50):
                mid = (lo + hi) / 2
                f_mid = mu_C_liq(x_Ni, mid, T_liq) - g_gra
                if f_mid == 0:
                    break
                if f_lo * f_mid < 0:
                    hi = mid
                else:
                    lo = mid
                    f_lo = f_mid
            xC = mid
        w.writerow([T_liq, x_Ni, xC])
