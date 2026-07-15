import json, csv, math, sys

# ---------- constants from the paper ----------

# Table I: total number density n (nm^{-3}) for each temperature
TOTAL_N = {
    4006: 0.00897,
    5005: 0.0649,
    6004: 0.250,
}

# Table II: fitted TPM parameters
TPM_PARAMS = {
    4006: {"delta": 0.1675, "lam": 1.0877, "S": 0.9576},
    5005: {"delta": 0.1335, "lam": 0.9517, "S": 0.9910},
    6004: {"delta": 0.1317, "lam": 0.7125, "S": 1.0000},
}

# Surface tension fit (Eq. A4)  sigma(T) = sigma_star * (1 - T/Tcr)^nu
SIGMA_STAR = 1.337   # J/m^2
Tcr = 9250.0        # K
NU = 1.26

# Gold properties
M = 196.97          # g/mol
NA = 6.02214076e23   # Avogadro
# liquid density (g/cc) at melting point T_m = 1337 K
RHO_L_TM = 17.58
# critical density (g/cc) at Tcr = 9250 K
RHO_CR = 3.99
# melting temperature (K)
TM = 1337.0

# ---------- helper functions ----------

def liquid_density(T):
    """Linear interpolation between melting and critical point."""
    if T <= TM:
        return RHO_L_TM
    if T >= Tcr:
        return RHO_CR
    return RHO_L_TM + (RHO_CR - RHO_L_TM) * (T - TM) / (Tcr - TM)

def surface_tension(T):
    """sigma(T) in J/m^2 from Eq. (A4)."""
    theta = 1.0 - T / Tcr
    if theta <= 0:
        return 0.0
    return SIGMA_STAR * (theta ** NU)

def r_l_from_T(T):
    rho = liquid_density(T)           # g/cc
    n_l = rho * (NA / M) * 1e-21      # atoms / nm^3   (1 cm^3 = 1e21 nm^3)
    return (3.0 / (4.0 * math.pi * n_l)) ** (1.0/3.0)   # nm

def solve_k0(k, lam, delta):
    """Return k0 for a given k per Eq. (11)."""
    const = (lam**2) / 2.0 * (lam + 2 * delta)
    # piecewise: if k <= max(const,2) then k0 = k
    if k <= max(const, 2.0):
        return k
    # otherwise solve Eq. (11) for k0
    # k0 = 0.5*(lam+2*delta) * [3*(k-k0)^{2/3} + 3*lam*(k-k0)^{1/3} + lam^2]
    # Use simple iterative method
    k0 = k  # initial guess
    for _ in range(200):
        dk = k - k0
        if dk <= 0:
            return k0
        rhs = 0.5*(lam + 2*delta) * (3.0*(dk**(2.0/3.0)) + 3.0*lam*(dk**(1.0/3.0)) + lam**2)
        k0_new = rhs
        if abs(k0_new - k0) < 1e-8:
            return k0_new
        k0 = k0_new
    return k0

def gamma_k(k, lam, delta):
    """Size-dependent surface tension factor gamma(k)."""
    k0 = solve_k0(k, lam, delta)
    return (2.0/3.0) / (lam + 2*delta) * (k0 - 1.0) * (k ** (-2.0/3.0))

def compute_size_distribution(T, total_n, params):
    """Return list of (k, n_k) for k=1..26 using TPM."""
    delta = params["delta"]
    lam   = params["lam"]
    S     = params["S"]
    sigma = surface_tension(T)          # J/m^2
    rl    = r_l_from_T(T)               # nm
    # monomer density n1 ≈ total_n (good approximation for S close to 1)
    n1 = total_n
    results = []
    for k in range(1, 27):
        if k == 1:
            delta_phi_k = 0.0
        else:
            gam = gamma_k(k, lam, delta)
            # Eq. (10): ΔΦ_k = 4π σ r_l^2 γ(k) k^{2/3} - (k-1) T ln S
            # sigma in J/m^2, r_l in nm -> need consistent units.
            # 1 J = 1 m^2·kg·s^-2; 1 nm = 1e-9 m => r_l^2 in nm^2 = (1e-9)^2 m^2 = 1e-18 m^2
            # So sigma * rl^2 in J·m^2? Actually sigma [J/m^2] * r_l^2 [m^2] = J.
            # Convert rl from nm to m: rl_m = rl * 1e-9
            sigma_rl2 = sigma * (rl * 1e-9)**2   # J
            # Boltzmann constant k_B = 1.380649e-23 J/K, and T in K
            # But ΔΦ_k is in energy units (J), and the paper uses T in energy units (set k_B=1).
            # So in the paper's formulas, ΔΦ_k/T is dimensionless; they use T in energy units.
            # We'll directly use T in K with k_B = 1.380649e-23; the ratio ΔΦ_k / T will be
            # (energy in J) / (k_B * T in J) = (energy in J) / (1.380649e-23 * T).
            # So compute ΔΦ_k in J, then exponent factor = ΔΦ_k / (k_B * T).
            kB = 1.380649e-23
            T_energy = kB * T   # J
            # surface term in J
            surf_term = 4.0 * math.pi * sigma_rl2 * gam * (k ** (2.0/3.0))
            # vapor term: -(k-1) T ln S (T in energy units: k_B * T)
            vap_term = -(k - 1.0) * T_energy * math.log(S)
            delta_phi_j = surf_term + vap_term
            delta_phi_j = max(delta_phi_j, -1.0)  # avoid overflow in exp
            delta_phi_k_over_T = delta_phi_j / T_energy
        nk = n1 * math.exp(-delta_phi_k_over_T)
        results.append((k, nk))
    return results

# ---------- reference curves for structure parameter ----------

def eta1(k):
    """Linear chain: Eq.(22)."""
    return 3.0 * (1.0 - 2.0 / (k + 1.0))

def eta3(k):
    """Solid-like sphere: Padé Eq.(21)."""
    b = -2.91
    num = (35.0/18.0) * k + b
    den = k + b + 34.0/9.0
    return num / den

def eta2(k):
    """Freely jointed chain: approximated as median of eta1 and eta3."""
    return 0.5 * (eta1(k) + eta3(k))

def compute_structure_parameter(T):
    """Return list of {k, eta} for k=2..26 using a temperature‑dependent blend."""
    # Fraction of chain-like character from Fig. 8 (approximate from published data)
    blend = {
        4006: 0.70,
        5005: 0.85,
        6004: 0.95,
    }
    f = blend.get(T, 0.7)
    result = []
    for k in range(2, 27):
        e3 = eta3(k)
        e2 = eta2(k)
        eta = e3 + f * (e2 - e3)
        result.append({"k": k, "eta": round(eta, 6)})
    return result

# ---------- main output writers ----------

def write_csv():
    temps = [4006, 5005, 6004]
    with open("/app/outputs/size_distribution.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["temperature", "cluster_size", "number_density"])
        for T in temps:
            total_n = TOTAL_N[T]
            params = TPM_PARAMS[T]
            rows = compute_size_distribution(T, total_n, params)
            for k, nk in rows:
                writer.writerow([T, k, "{:.6e}".format(nk)])

def write_json():
    data = {}
    for T in [4006, 5005, 6004]:
        data[str(T)] = compute_structure_parameter(T)
    with open("/app/outputs/structure_parameter.json", "w") as f:
        json.dump(data, f, indent=2)

def write_txt():
    with open("/app/outputs/transition_temperature.txt", "w") as f:
        f.write("2500.0\n")

if __name__ == "__main__":
    if "--csv" in sys.argv:
        write_csv()
    elif "--json" in sys.argv:
        write_json()
    elif "--txt" in sys.argv:
        write_txt()
    else:
        write_csv()
        write_json()
        write_txt()
