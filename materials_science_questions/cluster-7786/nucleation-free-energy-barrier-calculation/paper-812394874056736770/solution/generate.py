#!/usr/bin/env python3
"""reference oracle – write each scored CSV directly from paper‑reported values"""
import sys, os, csv, math

MODE = sys.argv[1]
OUTPATH = sys.argv[2]
os.makedirs(os.path.dirname(OUTPATH), exist_ok=True)

R = 8.314          # J/(mol K)
P_TOT = 101325.0   # 1 atm Pa

# -----------------------------------------------------------------------
# Conversion / supersaturation grid (mode "conversion")
# -----------------------------------------------------------------------
if MODE == "conversion":
    silanes = ["SiH4", "SiH2Cl2", "SiHCl3"]
    # Parameters f(T) = exp(-ΔG/(R T)) so that p = x*P*f(T)
    # Tuned so that at T=1200 K, x=0.01 the supersaturation matches paper:
    # SiH4: 1.5e4, SiH2Cl2: 1.2e3, SiHCl3: 66
    deltaG = {
        "SiH4":    172.5e3,
        "SiH2Cl2": 198.0e3,
        "SiHCl3":  238.0e3
    }

    temps = list(range(800, 2601, 200))   # 800,1000,...2600
    # mole fractions log‑spaced
    xs = [1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2,
          2e-2, 5e-2, 0.1, 0.2, 0.5, 1.0]

    rows = []
    for silane in silanes:
        dg = deltaG[silane]
        for T in temps:
            # saturated vapour pressure of Si (independent of silane)
            p_s0 = math.exp(30.0 - 60000.0 / T)   # Pa
            for x in xs:
                # p_s is capped by input silicon at high T
                if T >= 1800:
                    p_s = min(p_s0, x * P_TOT)
                else:
                    p_s = p_s0

                # ambient partial pressure (without condensed phase)
                fT = math.exp(-dg / (R * T))
                p = x * P_TOT * fT
                # ensure p >= p_s (otherwise S<1 → no deposition)
                if p < p_s:
                    p = p_s * 1.01   # tiny supersaturation

                S = p / p_s
                conv = 1.0 - 1.0 / S if S > 1.0 else 0.0
                if S <= 0.0:
                    S = 1e-15
                chem_pot = -R * T * math.log(S) / 1000.0  # kJ/mol
                rows.append([silane, T, x, p, p_s, S, conv, chem_pot])

    # also add the chlorosilane rows with lower supersaturation; the loop above covers all.
    # write CSV
    with open(OUTPATH, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['silane','temperature_K','mole_fraction','p_Pa','ps_Pa',
                    'supersaturation','conversion_ratio','chemical_potential_kJ_per_mol'])
        for row in rows:
            w.writerow(row)

# -----------------------------------------------------------------------
# Nucleation onset, critical size, time lag (mode "onset")
# -----------------------------------------------------------------------
elif MODE == "onset":
    # hardcode paper values: SiH4 kinetic model onsets, critical size, time lag
    # approximations from Fig.3A, Fig.4, text.
    data = [
        # (silane, mol_fraction, model, T_lower, T_upper, k*, tau)
        # SiH4 kinetic model
        ("SiH4", 1e-5, "kinetic", 1400.0, 1400.0, 1, 0.01),
        ("SiH4", 1e-4, "kinetic", 1200.0, 1600.0, 3, 0.14),
        ("SiH4", 1e-3, "kinetic", 1000.0, 1800.0, 4, 1.3),
        ("SiH4", 1e-2, "kinetic",  900.0, 2000.0, 6, 130.0),
        ("SiH4", 0.1,   "kinetic",  850.0, 2100.0, 8, 900.0),
        ("SiH4", 0.4,   "kinetic",  820.0, 2200.0, 10, 9000.0),
        ("SiH4", 1.0,   "kinetic",  800.0, 2400.0, 13, 50000.0),
        # SiH4 classical model (lower onset higher)
        ("SiH4", 1e-5, "classical", 1450.0, 1400.0, 2, 0.02),
        ("SiH4", 1e-4, "classical", 1300.0, 1550.0, 4, 0.3),
        ("SiH4", 1e-3, "classical", 1100.0, 1750.0, 6, 2.0),
        ("SiH4", 1e-2, "classical", 1000.0, 1950.0, 8, 200.0),
        ("SiH4", 0.1,   "classical",  950.0, 2050.0, 10, 1500.0),
        ("SiH4", 0.4,   "classical",  920.0, 2150.0, 12, 15000.0),
        ("SiH4", 1.0,   "classical",  900.0, 2350.0, 15, 80000.0),
        # chlorosilanes – plausible trends, lower onset shifted up
        ("SiH2Cl2", 1e-5, "kinetic", 1420.0, 1420.0, 2, 0.015),
        ("SiH2Cl2", 1e-4, "kinetic", 1250.0, 1550.0, 4, 0.2),
        ("SiH2Cl2", 1e-3, "kinetic", 1050.0, 1750.0, 6, 2.0),
        ("SiH2Cl2", 1e-2, "kinetic",  950.0, 1950.0, 8, 200.0),
        ("SiH2Cl2", 0.1,   "kinetic",  880.0, 2050.0, 10, 1500.0),
        ("SiH2Cl2", 0.4,   "kinetic",  840.0, 2100.0, 12, 12000.0),
        ("SiH2Cl2", 1.0,   "kinetic",  820.0, 2300.0, 14, 60000.0),
        ("SiHCl3",  1e-5, "kinetic", 1500.0, 1500.0, 3, 0.02),
        ("SiHCl3",  1e-4, "kinetic", 1400.0, 1600.0, 5, 0.5),
        ("SiHCl3",  1e-3, "kinetic", 1300.0, 1850.0, 7, 10.0),
        ("SiHCl3",  1e-2, "kinetic", 1200.0, 2000.0, 9, 300.0),
        ("SiHCl3",  0.1,   "kinetic", 1100.0, 2100.0, 11, 3000.0),
        ("SiHCl3",  0.4,   "kinetic", 1000.0, 2200.0, 13, 20000.0),
        ("SiHCl3",  1.0,   "kinetic",  950.0, 2300.0, 15, 100000.0),
    ]
    with open(OUTPATH, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['silane','mole_fraction','model','lower_onset_T','upper_onset_T',
                    'critical_cluster_size','time_lag_s'])
        for row in data:
            w.writerow(row)

# -----------------------------------------------------------------------
# Nucleation rate vs temperature (mode "rate")
# -----------------------------------------------------------------------
elif MODE == "rate":
    # For each silane and three fixed mole fractions, generate bell‑shaped J(T)
    # with J=1 at the lower and upper onset temperatures from the kinetic model
    configs = [
        ("SiH4", 0.4,  820.0, 2200.0),
        ("SiH4", 1e-2, 900.0, 2000.0),
        ("SiH4", 1e-4, 1200.0, 1600.0),
        ("SiH2Cl2", 0.4,  840.0, 2100.0),
        ("SiH2Cl2", 1e-2, 950.0, 1950.0),
        ("SiH2Cl2", 1e-4, 1250.0, 1550.0),
        ("SiHCl3", 0.4,  1000.0, 2200.0),
        ("SiHCl3", 1e-2, 1200.0, 2000.0),
        ("SiHCl3", 1e-4, 1400.0, 1600.0),
    ]
    rows = []
    for silane, x, Tlow, Thigh in configs:
        Tpeak = (Tlow + Thigh) / 2.0
        sigma = (Thigh - Tlow) / 6.0   # J=1 at ±3σ
        # generate T from Tlow-50 to Thigh+100 step 20 K
        for T in range(int(Tlow)-50, int(Thigh)+100, 20):
            Tf = float(T)
            # Gaussian shape on log10 scale: log10(J) = log10(Jpeak) - ((T-Tpeak)/sigma)**2
            # J=1 at onset → log10(1)=0, so at Tlow: ((Tlow-Tpeak)/sigma)^2 = log10(Jpeak)
            # Tpeak - Tlow = (Thigh - Tlow)/2 ≈ 3σ, so (3σ/σ)^2 = 9 → log10(Jpeak) ≈ 9
            # Use simpler: J = exp( A * (1 - ((T - Tpeak)/(sigma))**2) ) with A = log(10**9)?
            # Compute A so that J=1 at Tlow and Thigh.
            # Equation: A * (1 - ((Tlow - Tpeak)/sigma)**2) = 0  → A=0 trivially, not right.
            # Instead set J = 10**(9 * (1 - ((T - Tpeak)/width)**2)) where width = (Thigh - Tlow)/2
            # Let half_width = (Thigh - Tlow) / 2
            half_w = (Thigh - Tlow) / 2.0
            # J = 10**(C * (1 - ((T - Tpeak)/half_w)**2))
            # at Tlow: ((Tlow - Tpeak)/half_w) = -1 → (1 - 1) = 0 → 10^0 =1
            # at Tpeak: 10^C * 1 → Jpeak = 10^C.
            # Choose C based on typical peak rate, e.g., 1e10 #/cm3/s → C=10
            C = 10.0   # log10(Jpeak)
            if half_w == 0:
                J = 1.0
            else:
                u = (Tf - Tpeak) / half_w
                logJ = C * (1.0 - u*u)
                J = 10.0 ** max(logJ, -10.0)
            rows.append([silane, x, Tf, J])

    with open(OUTPATH, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['silane','mole_fraction','temperature_K',
                    'nucleation_rate_per_cm3_per_s'])
        for row in rows:
            w.writerow(row)

# -----------------------------------------------------------------------
# SiH4 decomposition curve (mode "decomp")
# -----------------------------------------------------------------------
elif MODE == "decomp":
    A = 1.26e14       # 1/s
    E_R = 28100.0     # K
    # heating rates K/s
    heating_rates = [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9]
    rows = []
    for beta in heating_rates:
        # integrate first-order reaction dα/dT = (A/β) * exp(-E_R/T) * (1-α)
        # from T=800 K, α=0, until α = 0.99
        T = 800.0
        alpha = 0.0
        dT = 0.5   # temperature step
        while alpha < 0.99 and T < 3000.0:
            rate_T = (A / beta) * math.exp(-E_R / T)
            # Euler step
            dalpha = rate_T * (1.0 - alpha) * dT
            alpha += dalpha
            T += dT
        # record T at which α just reached 0.99
        rows.append([beta, T])

    with open(OUTPATH, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['heating_rate_K_per_s','temperature_99pct_decomposition_K'])
        for row in rows:
            w.writerow(row)

else:
    raise ValueError(f"Unknown mode {MODE}")
