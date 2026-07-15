import sys
import numpy as np
import json

# constants
kB = 1.380649e-23  # J/K
mu0 = 4e-7 * np.pi  # N/A^2, exact
Q = 4.28e-13  # A*m
a = 4.34e-10  # m
v_bar = 8 * a**3 / (3 * np.sqrt(3))

def uC_DH(T, lD):
    # Eq. (6)
    # uC_DH = - (2 kB T)/(3 pi sqrt{3}) [ ln(1 + a/lD) - (a/lD) + 1/2 (a/lD)^2 ]
    x = a / lD
    if lD == np.inf:
        return 0.0
    return - (2 * kB * T) / (3 * np.pi * np.sqrt(3)) * (np.log(1 + x) - x + 0.5 * x**2)

def Delta_DH(T, lD, rho_I):
    # if no charges, no screening
    if rho_I <= 0:
        return 0.0
    # l_T = mu0 Q^2 / (8 pi kB T)
    l_T = mu0 * Q**2 / (8 * np.pi * kB * T)
    return kB * T * l_T / (lD + a)

def l_D_from_density(n, n2, T):
    if n + 4*n2 <= 0:
        return np.inf
    rho_I = (n + 4*n2) / v_bar
    return np.sqrt(kB * T / (mu0 * Q**2 * rho_I))

def densities(T, mu, mu2, n0, n2_0, max_iter=100, tol=1e-12):
    n, n2 = n0, n2_0
    for it in range(max_iter):
        rho_I = (n + 4*n2) / v_bar if (n+4*n2) > 0 else 0.0
        lD = l_D_from_density(n, n2, T)
        delta = Delta_DH(T, lD, rho_I) if lD != np.inf else 0.0
        mu_tilde = mu + delta
        mu2_tilde = mu2 + 4*delta
        beta = 1.0/(kB * T)
        # clip exponent to avoid overflow
        arg1 = min(beta * mu_tilde, 700)
        arg2 = min(beta * mu2_tilde, 700)
        exp1 = np.exp(arg1)
        exp2 = np.exp(arg2)
        denom = 1.0 + (1.0/3.0)*(4.0*exp1 + exp2)
        n_new = (4.0/3.0)*exp1 / denom
        n2_new = (1.0/3.0)*exp2 / denom
        if abs(n_new - n) < tol and abs(n2_new - n2) < tol:
            n, n2 = n_new, n2_new
            break
        n, n2 = n_new, n2_new
    else:
        pass  # did not converge, but ok
    return n, n2

def simulate_heating(T_arr, mu, mu2):
    n_list = []
    n2_list = []
    n_prev, n2_prev = 0.0, 0.0
    for T in T_arr:
        n, n2 = densities(T, mu, mu2, n_prev, n2_prev)
        n_list.append(n)
        n2_list.append(n2)
        n_prev, n2_prev = n, n2
    return np.array(n_list), np.array(n2_list)

def simulate_cooling(T_arr, mu, mu2, n_start, n2_start):
    n_list = []
    n2_list = []
    n_prev, n2_prev = n_start, n2_start
    for T in reversed(T_arr):
        n, n2 = densities(T, mu, mu2, n_prev, n2_prev)
        n_list.append(n)
        n2_list.append(n2)
        n_prev, n2_prev = n, n2
    return np.array(n_list[::-1]), np.array(n2_list[::-1])

def compute_U(T_arr, n_arr, n2_arr, mu, mu2):
    U = np.zeros_like(T_arr)
    for i, (T, n, n2) in enumerate(zip(T_arr, n_arr, n2_arr)):
        rho_I = (n + 4*n2) / v_bar if (n+4*n2)>0 else 0.0
        lD = l_D_from_density(n, n2, T)
        uc = uC_DH(T, lD) if lD != np.inf else 0.0
        U[i] = uc - mu*n - mu2*n2
    return U

def specific_heat(T, U):
    # use numpy gradient (second order)
    C = np.gradient(U, T)
    return C

def gen_csv(mu_mag, outfile):
    mu = -mu_mag * kB   # convert K to J
    mu2 = 4*mu
    T_arr = np.arange(0.01, 5.005, 0.01)  # 0.01 to 5.0 inclusive
    # heating run
    n_h, n2_h = simulate_heating(T_arr, mu, mu2)
    n_tot_h = n_h + n2_h
    # cooling run: start from final heating
    n_c, n2_c = simulate_cooling(T_arr, mu, mu2, n_h[-1], n2_h[-1])
    n_tot_c = n_c + n2_c
    # compute U and C
    U_h = compute_U(T_arr, n_h, n2_h, mu, mu2)
    U_c = compute_U(T_arr, n_c, n2_c, mu, mu2)
    C_h = specific_heat(T_arr, U_h)
    C_c = specific_heat(T_arr, U_c)

    # write CSV with required column order
    header = "T(K),n_tot_heating,n_tot_cooling,C_heating(J/K·site),C_cooling(J/K·site)"
    data = np.column_stack((T_arr, n_tot_h, n_tot_c, C_h, C_c))
    np.savetxt(outfile, data, delimiter=",", header=header, comments="", fmt="%.8g")
    print(f"Wrote {outfile}")

def classify_all(outdir):
    files = {
        1.0: f"{outdir}/mu_1_0_K.csv",
        1.5: f"{outdir}/mu_1_5_K.csv",
        1.8: f"{outdir}/mu_1_8_K.csv"
    }
    regimes = {}
    trans_T = {}
    for mu_mag, fname in files.items():
        data = np.loadtxt(fname, delimiter=",", skiprows=1)
        T = data[:,0]
        n_h = data[:,1]
        n_c = data[:,2]
        # classify
        # compute derivative of heating and cooling
        dn_h = np.gradient(n_h, T)
        dn_c = np.gradient(n_c, T)
        max_dn_h = np.max(np.abs(dn_h))
        max_dn_c = np.max(np.abs(dn_c))
        # hysteresis strength
        max_diff = np.max(np.abs(n_h - n_c))
        # thresholds
        if max_dn_h < 5 and max_dn_c < 5:
            regime = "iii"
            T_trans = None
        elif max_dn_h > 5 and max_dn_c < 1:
            regime = "i"
            # find index of peak in heating derivative
            idx = np.argmax(np.abs(dn_h))
            T_trans = float(T[idx])
        elif max_dn_h > 5 and max_dn_c > 5 and max_diff > 0.02:
            regime = "ii"
            # use heating curve peak as transition temp
            idx = np.argmax(np.abs(dn_h))
            T_trans = float(T[idx])
        else:
            # fallback
            regime = "iii"
            T_trans = None
        key = f"1_{int(mu_mag*10)}K"  # 1_0K, 1_5K, 1_8K
        if mu_mag == 1.0:
            key = "1_0K"
        elif mu_mag == 1.5:
            key = "1_5K"
        elif mu_mag == 1.8:
            key = "1_8K"
        regimes[key] = regime
        trans_T[key] = T_trans
    classification = {
        "regime_1_0K": regimes["1_0K"],
        "regime_1_5K": regimes["1_5K"],
        "regime_1_8K": regimes["1_8K"],
        "transition_T_1_0K": trans_T["1_0K"],
        "transition_T_1_5K": trans_T["1_5K"],
        "transition_T_1_8K": trans_T["1_8K"]
    }
    with open(f"{outdir}/classification.json", "w") as f:
        json.dump(classification, f, indent=2)
    print(f"Wrote {outdir}/classification.json")

if __name__ == "__main__":
    if sys.argv[1] == "classify":
        classify_all(sys.argv[2])
    else:
        mu_mag = float(sys.argv[1])
        outfile = sys.argv[2]
        gen_csv(mu_mag, outfile)
