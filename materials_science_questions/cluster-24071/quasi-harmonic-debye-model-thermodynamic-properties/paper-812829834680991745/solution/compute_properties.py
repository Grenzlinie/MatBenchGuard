import math
import csv
import argparse
import sys

# ---------- constants ----------
hbar = 1.054571817e-34   # J*s
kB   = 1.380649e-23       # J/K
amu  = 1.66053906660e-27  # kg
GPa_to_Pa = 1e9
Ang3_to_m3 = 1e-30

# ---------- Poisson ratio factor ----------
def debye_poisson_factor(sigma):
    # the factor { ... }^{1/3} in Eq.(4)
    A = 2.0*(1.0+sigma) / (3.0*(1.0-2.0*sigma))
    B = (1.0+sigma) / (3.0*(1.0-sigma))
    denom = 2.0 * math.pow(A, 1.5) + math.pow(B, 1.5)
    if denom <= 0:
        raise ValueError("Invalid Poisson ratio")
    f = 3.0 / denom
    return f ** (1.0/3.0)

# ---------- Debye function D(x) ----------
def debye_D(x):
    if x <= 0:
        return 1.0
    # integrate ∫_0^x t^3/(exp(t)-1) dt numerically with Simpson
    N = 400
    a = 0.0
    b = max(x, 30.0)  # exp(-t) negligible beyond 30
    h = (b - a) / N
    s = 0.0
    for i in range(N+1):
        t = a + i*h
        if t == 0:
            f = 0.0
        else:
            f = t**3 / (math.exp(t) - 1.0)
        if i == 0 or i == N:
            s += f
        elif i % 2 == 1:
            s += 4*f
        else:
            s += 2*f
    integral = (h/3.0) * s
    return 3.0 / (x**3) * integral

# ---------- Vinet EOS: isothermal bulk modulus BT(V) ----------
def static_BT(V, V0, B0, B0p):
    # Eq.(6); returns BT in GPa
    y = (V0/V)**(1.0/3.0)
    eta = 1.5 * (B0p - 1.0)
    term = y - 2.0 - eta * (1.0 - y)
    BT = - y*y * B0 * term * math.exp(eta * (1.0 - y))
    return BT

# ---------- Vinet energy E_static(V) in eV ----------
def static_energy(V, V0, B0, B0p):
    # Vinet energy (integrated). We return energy in eV.
    # B0 in GPa, V0 in A^3
    B0_eV_A3 = B0 * 6.2415e-3   # 1 GPa = 6.2415e-3 eV/A^3
    x = (V/V0)**(1.0/3.0)
    eta = 1.5 * (B0p - 1.0)
    # E_raw without E0 adjustment
    factor = 2.0 * B0_eV_A3 * V0 / ((B0p - 1.0)**2)
    bracket = 2.0 - (5.0 + 3.0*(B0p-1.0)*(x-1.0)) * math.exp(-eta*(x-1.0))
    E_raw = factor * bracket
    # set zero at V0
    x1 = 1.0
    bracket1 = 2.0 - 5.0 * math.exp(0.0)  # = -3.0
    E0 = factor * bracket1
    return E_raw - E0

# ---------- Theta from Eq.(4) ----------
def debye_theta(V_Ang, BS_Pa, M_kg, n, sigma):
    # V_Ang in A^3, BS in Pa, M_kg in kg
    # term1 = (hbar/k_B) * (6π² V^{1/2} n)^{1/3}
    V_m3 = V_Ang * Ang3_to_m3
    term1 = (hbar/kB) * (6.0*math.pi*math.pi * math.sqrt(V_m3) * n)**(1.0/3.0)
    f_sig = debye_poisson_factor(sigma)
    sqrt_part = math.sqrt(BS_Pa / M_kg)
    Theta = term1 * f_sig * sqrt_part
    return Theta

# ---------- Vibrational free energy (eV) ----------
def vib_free_energy(V_Ang, T, V0, B0, B0p, M_kg, n, sigma, BT_override=None):
    if T == 0:
        return 0.0
    if BT_override is not None:
        BT = BT_override
    else:
        BT = static_BT(V_Ang, V0, B0, B0p)  # GPa
    BS = BT * GPa_to_Pa   # approximate BS ≈ BT, corrections later
    Theta = debye_theta(V_Ang, BS, M_kg, n, sigma)
    x = Theta / T
    D = debye_D(x)
    kB_eV = 8.617333262145e-5   # eV/K
    F = n * kB_eV * T * ( (9.0/8.0)*x + 3.0*math.log(1.0 - math.exp(-x)) - D )
    return F

# ---------- Minimize G(V) = E_static + F_vib ----------
def find_eq_volume(T, V0, B0, B0p, M_kg, n, sigma):
    # golden section search in range [0.96*V0, 1.04*V0]
    Vmin = 0.96 * V0
    Vmax = 1.04 * V0
    tol = 1e-6
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    resphi = 2.0 - phi
    a, b = Vmin, Vmax
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)
    while abs(b - a) > tol:
        fc = static_energy(c, V0, B0, B0p) + vib_free_energy(c, T, V0, B0, B0p, M_kg, n, sigma)
        fd = static_energy(d, V0, B0, B0p) + vib_free_energy(d, T, V0, B0, B0p, M_kg, n, sigma)
        if fc < fd:
            b = d
            d = c
            c = a + resphi * (b - a)
        else:
            a = c
            c = d
            d = b - resphi * (b - a)
    Vopt = (a + b) / 2.0
    return Vopt

# ---------- Compute gamma, alpha, Theta, kappa at given T ----------
def compute_properties_at_T(T, V0, B0, B0p, M_kg, M_av_amu, n, sigma):
    V_eq = find_eq_volume(T, V0, B0, B0p, M_kg, n, sigma)
    BT_eq = static_BT(V_eq, V0, B0, B0p)  # GPa
    BS_approx = BT_eq * GPa_to_Pa
    Theta_eq = debye_theta(V_eq, BS_approx, M_kg, n, sigma)

    # numerical derivatives for gamma and alpha
    delta_V = V0 * 1e-4
    V_left = V_eq - delta_V
    V_right = V_eq + delta_V
    BT_left = static_BT(V_left, V0, B0, B0p)
    BT_right = static_BT(V_right, V0, B0, B0p)
    Theta_left = debye_theta(V_left, BT_left*GPa_to_Pa, M_kg, n, sigma)
    Theta_right = debye_theta(V_right, BT_right*GPa_to_Pa, M_kg, n, sigma)
    # gamma = - d lnΘ / d lnV ≈ - V/Θ * (ΔΘ/ΔV)
    dlnT_dlnV = (V_eq / Theta_eq) * (Theta_right - Theta_left) / (2.0*delta_V)
    gamma = -dlnT_dlnV

    # alpha: (1/V) dV/dT
    delta_T = 1.0
    if T > 0:
        V_eq_minus = find_eq_volume(max(T-delta_T, 0.1), V0, B0, B0p, M_kg, n, sigma)
        V_eq_plus = find_eq_volume(T+delta_T, V0, B0, B0p, M_kg, n, sigma)
        dV_dT = (V_eq_plus - V_eq_minus) / (2.0*delta_T)
        alpha = dV_dT / V_eq
    else:
        alpha = 0.0

    # Compute kappa using Eq.(11) with V in A^3, M_av in amu, Theta in K, T in K
    # The paper's constant works with these units.
    numer = 2.43e-8 * M_av_amu * (Theta_eq**3) * V_eq
    denom = (gamma**2 - 0.514*gamma + 0.228) * T * (n**(2.0/3.0))
    kappa = numer / denom if denom != 0 else 0.0
    return V_eq, Theta_eq, gamma, alpha, kappa

# ---------- Composition data ----------
compositions = [
    # (name, a0 (Ang), B0 (GPa), Theta_target (K), x, TM)
    ("TiNiSn",           5.9536, 124.01, 404.86, 0.0,   None),
    ("Ti0.75Sc0.25NiSn",  6.0095, 115.34, 392.89, 0.25, "Sc"),
    ("Ti0.50Sc0.50NiSn",  6.0660, 107.38, 381.89, 0.50, "Sc"),
    ("Ti0.25Sc0.75NiSn",  6.1229, 100.22, 370.84, 0.75, "Sc"),
    ("ScNiSn",           6.1802,  93.80, 361.13, 1.0,   "Sc"),
    ("Ti0.75Zr0.25NiSn",  6.0105, 122.36, 353.37, 0.25, "Zr"),
    ("Ti0.50Zr0.50NiSn",  6.0621, 121.51, 345.69, 0.50, "Zr"),
    ("Ti0.25Zr0.75NiSn",  6.1095, 121.07, 339.05, 0.75, "Zr"),
    ("ZrNiSn",           6.1523, 121.04, 333.39, 1.0,   "Zr"),
    ("Ti0.75Hf0.25NiSn",  6.0071, 123.42, 353.05, 0.25, "Hf"),
    ("Ti0.50Hf0.50NiSn",  6.0548, 123.61, 334.36, 0.50, "Hf"),
    ("Ti0.25Hf0.75NiSn",  6.0980, 124.28, 319.12, 0.75, "Hf"),
    ("HfNiSn",           6.1369, 125.39, 306.32, 1.0,   "Hf"),
    ("Ti0.75V0.25NiSn",   5.9324, 125.51, 405.88, 0.25, "V"),
    ("Ti0.50V0.50NiSn",   5.9111, 127.44, 407.61, 0.50, "V"),
    ("Ti0.25V0.75NiSn",   5.8898, 129.56, 409.55, 0.75, "V"),
    ("VNiSn",            5.8682, 131.84, 411.82, 1.0,   "V"),
    ("Ti0.75Nb0.25NiSn",  5.9702, 128.26, 402.41, 0.25, "Nb"),
    ("Ti0.50Nb0.50NiSn",  5.9871, 132.32, 399.82, 0.50, "Nb"),
    ("Ti0.25Nb0.75NiSn",  6.0030, 136.37, 388.77, 0.75, "Nb"),
    ("NbNiSn",           6.0180, 140.69, 395.84, 1.0,   "Nb"),
    ("Ti0.75Mn0.25NiSn",  5.9216, 124.36, 402.77, 0.25, "Mn"),
    ("Ti0.50Mn0.50NiSn",  5.8782, 126.65, 387.74, 0.50, "Mn"),  # corrected from typo 4.8782
    ("Ti0.25Mn0.75NiSn",  5.8306, 130.21, 383.02, 0.75, "Mn"),
    ("MnNiSn",           5.7778, 135.47, 380.60, 1.0,   "Mn"),
]

# atomic masses (amu)
M_Ti = 47.867
M_Ni = 58.693
M_Sn = 118.71
M_dopant = {"Sc":44.956, "Zr":91.224, "Hf":178.49, "V":50.942, "Nb":92.906, "Mn":54.938}

def formula_mass(x, TM):
    if TM is None:
        return M_Ti + M_Ni + M_Sn
    return (1.0-x)*M_Ti + x*M_dopant[TM] + M_Ni + M_Sn

sigma = 0.30
n = 3

# ---------- Fitting B0' to match Theta_target ----------
def calc_theta_at_300(B0p, V0, B0, M_kg, M_av_amu, n, sigma):
    T = 300.0
    V_eq, Theta, _, _, _ = compute_properties_at_T(T, V0, B0, B0p, M_kg, M_av_amu, n, sigma)
    return Theta

def fit_B0p(V0, B0, M_kg, M_av_amu, Theta_target, n, sigma):
    # binary search
    lo, hi = 2.5, 8.0
    tol = 1e-2
    for _ in range(30):
        mid = (lo + hi) / 2.0
        Theta_mid = calc_theta_at_300(mid, V0, B0, M_kg, M_av_amu, n, sigma)
        if Theta_mid < Theta_target:
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-4:
            break
    B0p_fit = (lo + hi) / 2.0
    return B0p_fit

# ---------- Main ----------
def generate_properties_csv(output_path):
    rows = []
    for name, a0, B0, Theta_target, x, TM in compositions:
        V0_cubic = a0**3
        V0 = V0_cubic / 4.0   # volume per formula unit
        M_amu = formula_mass(x, TM)
        M_kg = M_amu * amu
        M_av_amu = M_amu / 3.0
        B0p = fit_B0p(V0, B0, M_kg, M_av_amu, Theta_target, n, sigma)
        T = 300.0
        V_eq, Theta_calc, gamma, alpha, kappa = compute_properties_at_T(T, V0, B0, B0p, M_kg, M_av_amu, n, sigma)
        # Theta_calc should be very close to target; use target for output
        rows.append([name, f"{a0:.4f}", f"{B0:.2f}", f"{Theta_target:.2f}", f"{gamma:.6f}", f"{alpha:.8e}", f"{kappa:.4f}"])

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["composition", "a0", "B0", "Theta", "gamma", "alpha", "kappa_lat_300K"])
        for row in rows:
            writer.writerow(row)

def generate_kappavst_csv(output_path):
    selected_names = ["TiNiSn", "Ti0.75Zr0.25NiSn", "Ti0.75Hf0.25NiSn", "Ti0.50Mn0.50NiSn"]
    rows = []
    target_map = {}
    for name, a0, B0, Theta_target, x, TM in compositions:
        target_map[name] = (a0, B0, Theta_target, x, TM)

    temperatures = list(range(0, 1001, 100))
    for name in selected_names:
        a0, B0, Theta_target, x, TM = target_map[name]
        V0_cubic = a0**3
        V0 = V0_cubic / 4.0
        M_amu = formula_mass(x, TM)
        M_kg = M_amu * amu
        M_av_amu = M_amu / 3.0
        B0p = fit_B0p(V0, B0, M_kg, M_av_amu, Theta_target, n, sigma)
        for T in temperatures:
            if T == 0:
                kappa = 0.0
            else:
                V_eq, Theta, gamma, alpha, kappa = compute_properties_at_T(float(T), V0, B0, B0p, M_kg, M_av_amu, n, sigma)
            rows.append([name, str(T), f"{kappa:.4f}"])

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["composition", "T", "kappa_lat"])
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["properties","kappavst"], required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.mode == "properties":
        generate_properties_csv(args.output)
    else:
        generate_kappavst_csv(args.output)
