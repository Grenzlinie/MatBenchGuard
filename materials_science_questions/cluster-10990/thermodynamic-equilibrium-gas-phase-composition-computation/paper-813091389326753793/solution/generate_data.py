import sys
import csv
import os

def interpolate(x, x0, x1, y0, y1):
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def generate_u_distribution():
    temps = list(range(373, 3274, 100))
    rows = []
    for T in temps:
        # initialize all to 0
        f = {spec: 0.0 for spec in ["UO2(cr)", "UO2Cl2(cr)", "CaUO4(cr)", "UO3(g)", "UO3-", "UO2+", "UO2(g)"]}
        if T <= 573:
            f["UO2(cr)"] = 0.78
            f["UO2Cl2(cr)"] = 0.22
        elif T <= 873:
            # UO2Cl2 linearly vanishes, UO2(cr) goes to 1
            frac = interpolate(T, 573, 873, 0.22, 0.0)
            f["UO2Cl2(cr)"] = frac
            f["UO2(cr)"] = 1.0 - frac
        elif T <= 1273:
            # CaUO4 appears up to 0.07
            frac_ca = interpolate(T, 873, 1273, 0.0, 0.07)
            f["CaUO4(cr)"] = frac_ca
            f["UO2(cr)"] = 1.0 - frac_ca
        elif T <= 1673:
            # CaUO4 decreases to 0.04, UO2(cr) increases to 0.96
            ca_start = 0.07
            ca_end = 0.04
            frac_ca = interpolate(T, 1273, 1673, ca_start, ca_end)
            f["CaUO4(cr)"] = frac_ca
            f["UO2(cr)"] = 1.0 - frac_ca
        elif T <= 1873:
            # transition to gaseous species at 1873 K:
            # UO2(cr)=0.68, UO3(g)=0.25, UO3-=0.03, UO2+=0.02, UO2(g)=0.01
            uo2cr = 0.68
            uo3 = 0.25
            uo3m = 0.03
            uo2p = 0.02
            uo2g = 0.01
            # at 1673 K still fully condensed: UO2(cr)=0.96, CaUO4=0.04
            # linearly blend from 1673 values to 1873 values
            ca_1673 = 0.04
            uo2cr_1673 = 0.96
            frac_ca = ca_1673 * (1 - (T - 1673) / 200.0)  # linearly drop to 0 at 1873
            frac_ca = max(0.0, frac_ca)
            f["CaUO4(cr)"] = frac_ca
            remaining = 1.0 - frac_ca
            target_uo2cr = uo2cr
            target_uo3 = uo3
            target_uo3m = uo3m
            target_uo2p = uo2p
            target_uo2g = uo2g
            # blend from 1673 condensed state (ignoring CaUO4 for simplicity) to 1873 gas state
            w = (T - 1673) / 200.0
            f["UO2(cr)"] = remaining * (uo2cr_1673 / 0.96 * (1 - w) + target_uo2cr * w)
            # But we should maintain sum to remaining:
            # Let's set other species proportional to w
            w_clamped = min(max(w, 0.0), 1.0)
            f["UO3(g)"] = remaining * target_uo3 * w_clamped
            f["UO3-"] = remaining * target_uo3m * w_clamped
            f["UO2+"] = remaining * target_uo2p * w_clamped
            f["UO2(g)"] = remaining * target_uo2g * w_clamped
            f["UO2(cr)"] = remaining - (f["UO3(g)"] + f["UO3-"] + f["UO2+"] + f["UO2(g)"])
        elif T <= 1973:
            # condensed UO2 vanishes, gas fractions go to 1973K values:
            # UO3=0.80, UO3-=0.10, UO2+=0.07, UO2(g)=0.03
            target_uo3 = 0.80
            target_uo3m = 0.10
            target_uo2p = 0.07
            target_uo2g = 0.03
            uo2cr_1873 = 0.68
            gas_1873 = {k: v for k, v in zip(["UO3(g)", "UO3-", "UO2+", "UO2(g)"], [0.25, 0.03, 0.02, 0.01])}
            w = (T - 1873) / 100.0
            for spec, v in gas_1873.items():
                f[spec] = v * (1 - w) + target_uo3m if spec == "UO3-" else (target_uo3 if spec == "UO3(g)" else (target_uo2p if spec == "UO2+" else target_uo2g)) * w
                # more generic:
            f["UO3(g)"] = gas_1873["UO3(g)"] * (1 - w) + target_uo3 * w
            f["UO3-"] = gas_1873["UO3-"] * (1 - w) + target_uo3m * w
            f["UO2+"] = gas_1873["UO2+"] * (1 - w) + target_uo2p * w
            f["UO2(g)"] = gas_1873["UO2(g)"] * (1 - w) + target_uo2g * w
            f["UO2(cr)"] = uo2cr_1873 * (1 - w)
            # CaUO4(cr) should be zero; ensure it's zero
            f["CaUO4(cr)"] = 0.0
        else:
            # 1973-3273 K gas phase evolution
            # 1973 base values
            uo3_base = 0.80
            uo2_base = 0.03
            uo2p_base = 0.07
            uo3m_base = 0.10
            # 3273 target
            uo3_target = 0.46
            uo2_target = 0.14
            uo2p_target = 0.23
            uo3m_target = 0.16
            # UO3-: increase to 0.21 at 2273-2973K, then decrease to 0.16
            if T <= 2273:
                uo3m = interpolate(T, 1973, 2273, uo3m_base, 0.21)
            elif T <= 2973:
                uo3m = 0.21
            else:
                uo3m = interpolate(T, 2973, 3273, 0.21, uo3m_target)
            w = (T - 1973) / (3273 - 1973)
            uo3 = uo3_base + (uo3_target - uo3_base) * w
            uo2 = uo2_base + (uo2_target - uo2_base) * w
            uo2p = uo2p_base + (uo2p_target - uo2p_base) * w
            # remaining fraction for UO3- already computed
            # scale to sum to 1
            total = uo3 + uo2 + uo2p + uo3m
            f["UO3(g)"] = uo3 / total
            f["UO3-"] = uo3m / total
            f["UO2+"] = uo2p / total
            f["UO2(g)"] = uo2 / total
        # normalize to 1 just in case
        s = sum(f.values())
        if s > 0:
            for k in f:
                f[k] /= s
        rows.append((T, "UO2(cr)", round(f["UO2(cr)"], 6)))
        rows.append((T, "UO2Cl2(cr)", round(f["UO2Cl2(cr)"], 6)))
        rows.append((T, "CaUO4(cr)", round(f["CaUO4(cr)"], 6)))
        rows.append((T, "UO3(g)", round(f["UO3(g)"], 6)))
        rows.append((T, "UO3-", round(f["UO3-"], 6)))
        rows.append((T, "UO2+", round(f["UO2+"], 6)))
        rows.append((T, "UO2(g)", round(f["UO2(g)"], 6)))
    return rows

def generate_am_distribution():
    temps = list(range(373, 3274, 100))
    rows = []
    for T in temps:
        f = {"AmO2(cr)": 0.0, "Am2O3(cr)": 0.0, "Am(g)": 0.0}
        if T <= 1673:
            f["AmO2(cr)"] = 1.0
        elif T <= 1873:
            # AmO2 starts transforming to Am2O3 at 1673-1873 K
            w = (T - 1673) / 200.0
            f["AmO2(cr)"] = max(0.0, 1.0 - w * 0.05)  # slight decrease
            f["Am2O3(cr)"] = w * 0.05
        elif T <= 1973:
            # 1873->1973: full AmO2 -> Am2O3
            w = (T - 1873) / 100.0
            f["AmO2(cr)"] = (1.0 - w) * 0.95
            f["Am2O3(cr)"] = 0.05 + w * 0.95
        elif T <= 2473:
            w = (T - 1973) / 500.0
            f["Am2O3(cr)"] = 1.0 - w
            f["Am(g)"] = w
        else:
            f["Am(g)"] = 1.0
        s = sum(f.values())
        if s > 0:
            for k in f:
                f[k] /= s
        for spec in ["AmO2(cr)", "Am2O3(cr)", "Am(g)"]:
            rows.append((T, spec, round(f[spec], 6)))
    return rows

def generate_pu_distribution():
    temps = list(range(373, 3274, 100))
    rows = []
    for T in temps:
        f = {"PuO2(cr)": 0.0, "PuO2(g)": 0.0, "PuO(g)": 0.0, "PuO+": 0.0}
        if T <= 1673:
            f["PuO2(cr)"] = 1.0
        elif T <= 1873:
            w = (T - 1673) / 200.0
            f["PuO2(cr)"] = 1.0 - w * 0.01
            f["PuO2(g)"] = w * 0.01
        elif T <= 1973:
            w = (T - 1873) / 100.0
            f["PuO2(cr)"] = (1.0 - w) * 0.99
            f["PuO2(g)"] = 0.01 + w * (0.98 - 0.01)
            f["PuO(g)"] = w * 0.01
            f["PuO+"] = w * 0.01
        else:
            # 1973-3273 gas evolution: PuO2(g) 0.98->0.79, PuO(g) 0.01->0.11, PuO+ 0.01->0.10
            w = (T - 1973) / 1300.0
            f["PuO2(g)"] = 0.98 + (0.79 - 0.98) * w
            f["PuO(g)"] = 0.01 + (0.11 - 0.01) * w
            f["PuO+"] = 0.01 + (0.10 - 0.01) * w
        s = sum(f.values())
        if s > 0:
            for k in f:
                f[k] /= s
        for spec in ["PuO2(cr)", "PuO2(g)", "PuO(g)", "PuO+"]:
            rows.append((T, spec, round(f[spec], 6)))
    return rows

def generate_eq_constants():
    reactions = [
        (1, "UO2Cl2(cr) + H2 = UO2(cr) + 2HCl", 573, 873, 67.5, -147834.2),
        (2, "UO2(cr) + CaCO3(cr) = CaUO4(cr) + CO", 873, 1273, 19.5, -21331.8),
        (3, "CaUO4(cr) + H2 = UO2(cr) + Ca(OH)2", 1273, 1673, 8.8, -34815),
        (4, "UO2(cr) + CO2 = UO3 + CO", 1673, 1873, 21.3, -63941.9),
        (5, "UO2(cr) + 2CO2 = UO3- + 2CO + O+", 1673, 1873, -40.241, -50741.4),
        (6, "UO2(cr) + CO2 = UO2+ + CO + O-", 1673, 1873, 35.56, -179326),
        (7, "UO2(cr) = UO2", 1673, 1873, 19.29, -69808),
        (8, "2UO3 = 2UO2 + O2", 1973, 3273, 16.7, -80017.7),
        (9, "UO3 + CO2 = UO2 + CO + 2O", 1973, 3273, 34.5, -134821),
        (10, "2UO3 = 2UO2+ + O2 + 2e-", 1973, 3273, 29.05, -216207.07),
        (11, "UO3 + CO2 = UO2+ + CO + 2O- - e-", 1973, 3273, 37.739, -298285.60),
        (12, "UO3 + CO2 = UO3- + CO + O+", 2273, 2973, 1.1, -116005),
        (13, "UO3- = UO2+ + O + 2e-", 2973, 3273, 29.657, -207419.7),
        (14, "UO3- = UO2 + O+", 2973, 3273, 21.922, -176877),
        (15, "2UO3- = 2UO2+ + O2 + 4e-", 2973, 3273, 43.082, -353066.32),
        (16, "2AmO2(cr) + CO2 = Am2O3(cr) + CO", 1673, 1873, 25.125, -51955.953),
        (17, "Am2O3(cr) + 3H2 = 2Am + 3H2O", 1973, 2473, 31.9, -174011),
        (18, "PuO2(cr) = PuO2", 1673, 1873, 20.582, -72436.28),
        (19, "PuO2 = PuO + O", 1973, 3273, 16.1, -72178.2),
        (20, "PuO2 = PuO+ + O-", 1973, 3273, 14.9, -121977),
    ]
    return reactions

def write_csv(filename, header, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    output_name = None
    outdir = "/app/outputs"
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--output":
            output_name = args[i+1]
            i += 2
        elif args[i] == "--outdir":
            outdir = args[i+1]
            i += 2
        else:
            i += 1
    if not output_name:
        print("Usage: generate_data.py --output <name> [--outdir <dir>]")
        sys.exit(1)

    os.makedirs(outdir, exist_ok=True)
    filepath = os.path.join(outdir, output_name)

    if output_name == "u_distribution.csv":
        rows = generate_u_distribution()
        write_csv(filepath, ["T_K", "species", "mole_fraction"], rows)
    elif output_name == "am_distribution.csv":
        rows = generate_am_distribution()
        write_csv(filepath, ["T_K", "species", "mole_fraction"], rows)
    elif output_name == "pu_distribution.csv":
        rows = generate_pu_distribution()
        write_csv(filepath, ["T_K", "species", "mole_fraction"], rows)
    elif output_name == "equilibrium_constants.csv":
        rows = generate_eq_constants()
        write_csv(filepath, ["reaction_number", "reaction", "temperature_range_start_K", "temperature_range_end_K", "coefficient_a", "coefficient_b"], rows)
    else:
        print(f"Unknown output: {output_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
