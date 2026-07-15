import sys, math, csv

# Constants
kB = 1.380649e-23       # J/K
h  = 6.62607015e-34     # J s
me = 9.10938356e-31     # kg
e  = 1.602176634e-19    # C
P  = 101325.0           # Pa (1 atm)
L  = 2.687e19           # cm^-3 (Loschmidt)

# Argon ionization energies (eV)
E1 = 15.759 * e
E2 = 27.629 * e

# Partition functions (approximate)
Z0 = 1.0
Z1 = 2.5
Z2 = 1.0

# Constant factor for Saha
C_factor = (2 * math.pi * me * kB / h**2) ** 1.5   # (m^-3 K^-1.5)

def K_eq(T, dZ, Eion):
    """eq (A3)/(A4): K = 2 * (Zup/Zlow) * C_factor * T^{1.5} * exp(-Eion/(kB*T))"""
    return 2.0 * dZ * C_factor * (T ** 1.5) * math.exp(-Eion / (kB * T))

def solve_cubic_N_e(T, Nt, K1, K2):
    """Solve cubic: Ne^3 + 2*K1*Ne^2 + (3*K1*K2 - K1*Nt)*Ne - 2*K1*K2*Nt = 0
    Returns positive real root."""
    # Newton iteration with a safe initial guess (Nt/2)
    Ne = Nt / 2.0
    for _ in range(50):
        f = Ne**3 + 2*K1*Ne**2 + (3*K1*K2 - K1*Nt)*Ne - 2*K1*K2*Nt
        df = 3*Ne**2 + 4*K1*Ne + (3*K1*K2 - K1*Nt)
        if df == 0.0:
            break
        Ne_new = Ne - f/df
        if Ne_new <= 0.0:
            Ne_new = Ne / 2.0
        if abs(Ne_new - Ne) < 1e-10 * Ne:
            return Ne_new
        Ne = Ne_new
    return Ne

def compute_arrays():
    # Temperatures from 5000 to 20000 K step 500
    T_list = [i for i in range(5000, 20500, 500)]
    N = len(T_list)
    N_t = [P / (kB * T) for T in T_list]  # m^-3
    K1 = [K_eq(T, Z1/Z0, E1) for T in T_list]
    K2 = [K_eq(T, Z2/Z1, E2) for T in T_list]
    
    N_e = [0.0]*N
    N_a = [0.0]*N
    N_1 = [0.0]*N
    N_2 = [0.0]*N
    for i in range(N):
        Ne = solve_cubic_N_e(T_list[i], N_t[i], K1[i], K2[i])
        N_e[i] = Ne
        N_1[i] = Ne**2 / (Ne + 2*K2[i])
        N_2[i] = K2[i] * N_1[i] / Ne
        N_a[i] = N_1[i] * Ne / K1[i]
    N_i = [a + b for a, b in zip(N_1, N_2)]
    
    # Convert to cm^-3
    conv = 1e-6
    N_e_cm = [v * conv for v in N_e]
    N_a_cm = [v * conv for v in N_a]
    N_i_cm = [v * conv for v in N_i]
    
    # Numerical derivatives (central diff)
    dNe_dT_cm = [0.0]*N
    dNa_dT_cm = [0.0]*N
    dNi_dT_cm = [0.0]*N
    for i in range(N):
        if i == 0:
            dT = T_list[1] - T_list[0]
            dNe_dT_cm[i] = (N_e_cm[1] - N_e_cm[0]) / dT
            dNa_dT_cm[i] = (N_a_cm[1] - N_a_cm[0]) / dT
            dNi_dT_cm[i] = (N_i_cm[1] - N_i_cm[0]) / dT
        elif i == N-1:
            dT = T_list[-1] - T_list[-2]
            dNe_dT_cm[i] = (N_e_cm[-1] - N_e_cm[-2]) / dT
            dNa_dT_cm[i] = (N_a_cm[-1] - N_a_cm[-2]) / dT
            dNi_dT_cm[i] = (N_i_cm[-1] - N_i_cm[-2]) / dT
        else:
            dT = T_list[i+1] - T_list[i-1]
            dNe_dT_cm[i] = (N_e_cm[i+1] - N_e_cm[i-1]) / dT
            dNa_dT_cm[i] = (N_a_cm[i+1] - N_a_cm[i-1]) / dT
            dNi_dT_cm[i] = (N_i_cm[i+1] - N_i_cm[i-1]) / dT
    
    return T_list, N_e_cm, N_a_cm, N_i_cm, dNe_dT_cm, dNa_dT_cm, dNi_dT_cm, N

def thermo_data(wavelength):
    T, Ne, Na, Ni, dNe, dNa, dNi, N = compute_arrays()
    # Coefficients for given wavelength
    if wavelength == 532:
        f_atom = 1.05959e-23
        f_e    = -1.2623e-22
    elif wavelength == 808:
        f_atom = 1.05959e-23   # same A,B approx
        lam_cm = 8.08e-5
        f_e    = -4.46e-14 * lam_cm**2
    else:
        raise ValueError("Unknown wavelength")
    
    rows = []
    for i in range(N):
        n_minus_one = f_atom * (Na[i] + 0.67 * Ni[i]) + f_e * Ne[i]
        dn_dT = f_atom * (dNa[i] + 0.67 * dNi[i]) + f_e * dNe[i]
        if abs(dn_dT) < 1e-30:
            e_val = 1e10  # clip
        else:
            e_val = 1e-5 / (abs(dn_dT) * T[i])
        rows.append([T[i], Ne[i], n_minus_one, dn_dT, e_val])
    return rows

def find_intervals(rows, thresholds):
    """Find main contiguous interval where e <= threshold."""
    T = [r[0] for r in rows]
    e = [r[4] for r in rows]
    # find min e index
    min_e_idx = min(range(len(e)), key=lambda i: e[i])
    intervals = []
    for th in thresholds:
        # collect indices where e <= th
        idxs = [i for i in range(len(e)) if e[i] <= th]
        if not idxs:
            intervals.append([th, None, None])
            continue
        # find contiguous stretches
        stretches = []
        start = idxs[0]
        for i in range(1, len(idxs)):
            if idxs[i] != idxs[i-1] + 1:
                stretches.append((start, idxs[i-1]))
                start = idxs[i]
        stretches.append((start, idxs[-1]))
        # select stretch that contains the minimum e point
        chosen = None
        for s, end in stretches:
            if s <= min_e_idx <= end:
                chosen = (T[s], T[end])
                break
        if chosen is None:
            # fallback: largest stretch
            chosen = max([(T[s], T[e]) for s,e in stretches], key=lambda x: x[1]-x[0])
        intervals.append([th, chosen[0], chosen[1]])
    return intervals

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--mode", required=True)
    args = ap.parse_args()
    
    if args.mode == "532_data":
        rows = thermo_data(532)
        with open(args.output, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["T","N_e","n-1","dn/dT","e"])
            w.writerows(rows)
    elif args.mode == "808_data":
        rows = thermo_data(808)
        with open(args.output, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["T","N_e","n-1","dn/dT","e"])
            w.writerows(rows)
    elif args.mode == "532_intervals":
        rows = thermo_data(532)
        thrs = [0.10, 0.12, 0.15, 0.20]
        intervals = find_intervals(rows, thrs)
        with open(args.output, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["error_threshold","T_lower","T_upper"])
            for th, lo, hi in intervals:
                w.writerow([th, lo, hi])
    elif args.mode == "808_intervals":
        rows = thermo_data(808)
        thrs = [0.10, 0.12, 0.15, 0.20]
        intervals = find_intervals(rows, thrs)
        with open(args.output, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["error_threshold","T_lower","T_upper"])
            for th, lo, hi in intervals:
                w.writerow([th, lo, hi])
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)
