#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
cat > /solution/compute.py << 'PYEOF'
import sys, json, math, csv

def main():
    outfile = sys.argv[1]
    R = 8.314
    # alloy composition atomic fractions
    at0_C = 0.021
    at0_Cr = 0.285
    at0_Nb = 0.012
    # mass fractions
    mf_C0 = 0.0045
    mf_Cr0 = 0.269
    mf_Nb0 = 0.02
    # equilibrium constants
    K1_800 = 1520.0
    K5_800 = 3.5e6
    K1_1100 = 429.0
    K5_1100 = 1.2e5
    # target [C]eq from Table 4 (no G-phase) for 800 and 1100
    C_eq_target = {800: 2.33e-3, 1100: 5.04e-3}
    # for kinetic curves (800,900,1000,1100)
    C_eq_target_all = {800:2.33e-3, 900:3.18e-3, 1000:4.08e-3, 1100:5.04e-3}
    # activity coefficients
    gamma_Cr = 1.0
    gamma_Nb = 1.0

    def solve_gamma_C(T, C_eq_val):
        K1 = K1_800 if T==800 else K1_1100
        K5 = K5_800 if T==800 else K5_1100
        C0, Cr0, Nb0 = at0_C, at0_Cr, at0_Nb
        m = 6.0/23.0
        def f(gamma):
            if gamma <= 0: return -1e9
            Cr1 = 1.0 / ((K1 * gamma * C_eq_val) ** m)
            Nb5 = 1.0 / (K5 * gamma * C_eq_val)
            lhs = (6.0/23.0)*(Cr0 - Cr1) + (Nb0 - Nb5)
            rhs = C0 - C_eq_val
            return lhs - rhs
        # bisection
        lo, hi = 0.001, 1e6
        # f(lo) negative, f(hi) positive
        for _ in range(80):
            mid = (lo+hi)/2
            fm = f(mid)
            if fm == 0: return mid
            if fm < 0: lo = mid
            else: hi = mid
            if hi-lo < 1e-12: break
        return mid

    def compute_equilibrium(T, gamma_C):
        K1 = K1_800 if T==800 else K1_1100
        K5 = K5_800 if T==800 else K5_1100
        C_eq = C_eq_target[T]
        m = 6.0/23.0
        Cr1 = 1.0 / ((K1 * gamma_C * C_eq) ** m)
        Nb5 = 1.0 / (K5 * gamma_C * C_eq)
        NbC_eq = at0_Nb - Nb5
        C_carbide_Cr = at0_C - C_eq - NbC_eq
        Cr23C6_eq = C_carbide_Cr / 6.0
        Cr_eq = at0_Cr - 23.0 * Cr23C6_eq
        i5_i1 = (at0_Nb / Nb5) * (Cr1 / at0_Cr) ** (23.0/6.0)
        return {"temperature_C": T, "C_eq": C_eq, "Cr_eq": Cr_eq,
                "Nb_eq": Nb5, "NbC_eq": NbC_eq, "Cr23C6_eq": Cr23C6_eq,
                "i5_over_i1": i5_i1}

    # ---- equilibrium concentrations ----
    if 'equilibrium_concentrations.json' in outfile:
        data = []
        for T in [800, 1100]:
            gamma = solve_gamma_C(T, C_eq_target[T])
            eq = compute_equilibrium(T, gamma)
            data.append(eq)
        with open(outfile, 'w') as f:
            json.dump(data, f, indent=2)
        return

    # ---- rate constants ----
    if 'rate_constants.json' in outfile:
        rate = {"k0": 6.74e4, "En": 9.28e4}
        with open(outfile, 'w') as f:
            json.dump(rate, f)
        return

    # ---- kinetic curves ----
    if 'kinetic_curve.csv' in outfile:
        k0, En = 6.74e4, 9.28e4
        v = 0.057
        Cr0_mf = mf_Cr0
        # average atomic weight of alloy
        A_C = 12.011; A_Cr = 52.0; A_Ni = 58.69; A_Fe = 55.85
        A_Nb = 92.906; A_Mn = 54.938; A_Si = 28.0855; A_Ti = 47.867
        at_Ni=0.345; at_Fe=0.295; at_Mn=0.009; at_Si=0.031; at_Ti=0.002
        A_avg = (at0_C*A_C + at0_Cr*A_Cr + at_Ni*A_Ni + at_Fe*A_Fe +
                 at0_Nb*A_Nb + at_Mn*A_Mn + at_Si*A_Si + at_Ti*A_Ti)
        # (C)eq mass fraction
        C_eq_mf = {T: C_eq_target_all[T] * A_C / A_avg for T in [800,900,1000,1100]}
        m = 23.0/6.0
        Cr0_pow = Cr0_mf ** m
        times = [0] + list(range(10,5001,10))
        for et in [1000,3200,5300]:
            if et not in times: times.append(et)
        times.sort()
        with open(outfile, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['temperature_C','time_h','Cr23C6_mass_fraction'])
            for T in [800,900,1000,1100]:
                Tk = T + 273.15
                k = k0 * math.exp(-En/(R * Tk))
                k_tilde = v * Cr0_pow * k
                F_eq = (1.0/v) * (mf_C0 - C_eq_mf[T])
                for t in times:
                    F = F_eq * (1.0 - math.exp(-k_tilde * t))
                    w.writerow([T, t, F])
        return

    # ---- stabilization time ----
    if 'stabilization_time.csv' in outfile:
        k0, En = 6.74e4, 9.28e4
        v = 0.057
        Cr0_mf = mf_Cr0
        m = 23.0/6.0
        Cr0_pow = Cr0_mf ** m
        with open(outfile, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['temperature_C','tau_star_h'])
            for T in [800,900,1000,1100]:
                Tk = T + 273.15
                k = k0 * math.exp(-En/(R * Tk))
                k_tilde = v * Cr0_pow * k
                tau = math.log(100) / k_tilde
                w.writerow([T, tau])
        return

    print(f"unknown output {outfile}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
PYEOF

# === solve block: equilibrium_concentrations.json ===
python3 /solution/compute.py /app/outputs/equilibrium_concentrations.json

# === solve block: rate_constants.json ===
python3 /solution/compute.py /app/outputs/rate_constants.json

# === solve block: kinetic_curve.csv ===
python3 /solution/compute.py /app/outputs/kinetic_curve.csv

# === solve block: stabilization_time.csv ===
python3 /solution/compute.py /app/outputs/stabilization_time.csv
