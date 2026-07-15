#!/usr/bin/env python3
import csv, math, os

# ---------- constants ----------
T = 279.15          # K
g = 9.81
Rd = 287.0
Rv = 461.5
cp = 1005.0
Lw = 2.5e6
rho_w = 1000.0
rho_a = 1.265        # kg/m3 at T=6C, P=101325 Pa
A1 = 4.7e-4          # m^-1   (Pinsky et al. 2012 for T=6C)
A2 = 390
F_const = 2.7e6      # s/m^2  (Pinsky et al. 2012 for T=6C)
A_kohler = 1.2e-9    # m
B_kohler = 0.72
pi = math.pi

# ---------- Table 1: S_max*(Q0) ----------
Sstar_tab = [
    (0.0, 1.0540), (0.1, 0.9589), (0.2, 0.9147), (0.3, 0.8821),
    (0.4, 0.8557), (0.5, 0.8333), (0.6, 0.8139), (0.7, 0.7967),
    (0.8, 0.7812), (0.9, 0.7672), (1.0, 0.7543), (1.1, 0.7425),
    (1.2, 0.7315), (1.3, 0.7214), (1.4, 0.7120), (1.5, 0.7032),
    (1.6, 0.6931), (1.7, 0.6850), (1.8, 0.6772), (1.9, 0.6698),
    (2.0, 0.6628), (2.1, 0.6561), (2.2, 0.6497)
]

# ---------- Table 2: aerosol modes (R_um, sigma, N_cm3) ----------
aerosol_modes = {
    "marine": [
        (0.005, 1.6, 340),
        (0.035, 2.0, 60),
        (0.31,  2.7, 3.1),
    ],
    "clean_continental": [
        (0.008, 1.6, 1000),
        (0.034, 2.1, 800),
        (0.46,  2.2, 0.72),
    ],
    "background": [
        (0.008, 1.7, 6400),
        (0.038, 2.0, 2300),
        (0.51,  2.16, 3.2),
    ],
    "urban": [
        (0.007, 1.8, 106000),
        (0.027, 2.16, 32000),
        (0.43,  2.21, 5.4),
    ],
}

# ---------- helpers ----------
def lookup_Sstar(Q):
    if Q <= Sstar_tab[0][0]:
        return Sstar_tab[0][1]
    if Q >= Sstar_tab[-1][0]:
        return Sstar_tab[-1][1]
    for i in range(len(Sstar_tab)-1):
        q0, s0 = Sstar_tab[i]
        q1, s1 = Sstar_tab[i+1]
        if q0 <= Q <= q1:
            frac = (Q - q0) / (q1 - q0)
            return s0 + frac * (s1 - s0)
    return Sstar_tab[-1][1]   # fallback


def compute_one(aerosol_type, w, q2):
    modes_um = aerosol_modes[aerosol_type]  # (R_um, sig, N_cm3)
    # convert to SI
    modes = []
    for R_um, sig, N_cm3 in modes_um:
        R_m = R_um * 1e-6
        N_m3 = N_cm3 * 1e6   # 1/cm3 -> 1/m3
        modes.append((R_m, sig, N_m3))

    S_max = 0.005   # initial guess
    converged = False
    max_iter = 200
    for _ in range(max_iter):
        # step b
        rn_cr = (A_kohler/3.0) * (4.0 / max(B_kohler * S_max**2, 1e-30))**(1.0/3.0)

        # step c: N via Eq.18
        N_tot = 0.0
        for R_m, sig, N_m3 in modes:
            if rn_cr <= 0 or R_m <= 0:
                continue
            arg = math.log(rn_cr / R_m) / (math.sqrt(2) * math.log(sig))
            frac = 0.5 * (1.0 - math.erf(arg))
            N_tot += N_m3 * frac
        N_tot = max(N_tot, 1e-20)   # avoid zero

        # step d: R
        bracket = (4.0 * pi * rho_w * A2 * N_tot) / (3.0 * rho_a)
        if bracket <= 0 or w <= 0 or F_const <= 0 or A1 <= 0:
            break
        R_val = (3.0 / (F_const * A1 * w)) * bracket**(2.0/3.0)

        # step e: r_0
        r_star = math.sqrt(B_kohler / A_kohler) * (rn_cr ** 1.5)
        sum_r0 = 0.0
        for R_m, sig, N_m3 in modes:
            alpha = 1.5 * math.log(sig)
            R_star_i = math.sqrt(B_kohler * (R_m**3) / A_kohler)
            if r_star <= 0 or R_star_i <= 0:
                continue
            ln_arg = math.log(R_star_i) + alpha**2 - math.log(r_star)
            erf_arg = ln_arg / (math.sqrt(2) * alpha)
            contrib = (N_m3 / 2.0) * R_star_i * math.exp(alpha**2 / 2.0) * (1.0 + math.erf(erf_arg))
            sum_r0 += contrib
        r0 = sum_r0 / N_tot if N_tot > 0 else 0.0

        # step f: Q0
        if R_val <= 0:
            break
        R_34 = R_val ** (3.0/4.0)
        haze_term = (4.0 * pi * rho_w * A2 * N_tot / (3.0 * rho_a)) * (r0 ** 3)
        Q0 = R_34 * (A2 * q2 + haze_term)

        # step g
        S_star = lookup_Sstar(Q0)

        # step h
        S_new = S_star / R_34 if R_34 > 0 else 0.0

        if abs(S_new - S_max) / max(abs(S_max), 1e-12) < 1e-6:
            converged = True
            S_max = S_new
            break
        S_max = S_new

    return S_max, N_tot


# ---------- main: produce CSV ----------
conditions = []
# specific velocities
velocities = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

for atype in ["marine", "clean_continental", "background", "urban"]:
    for w in velocities:
        conditions.append((atype, w, 0.0))
    if atype in ("marine", "clean_continental"):
        for w in velocities:
            conditions.append((atype, w, 1e-5))
            conditions.append((atype, w, 1e-4))

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)
out_path = os.path.join(output_dir, "results.csv")

with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["aerosol_type", "w", "q2", "S_max", "N"])
    for atype, w, q2 in conditions:
        Smax, N = compute_one(atype, w, q2)
        writer.writerow([atype, w, q2, Smax, N])
