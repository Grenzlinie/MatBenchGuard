import sys, os, math

def solve_rc(G, b, gamma, sigma, b0):
    factor = (G * b) / (4 * math.pi * (sigma - gamma / b))
    R_low = b0
    f_low = R_low - factor * (math.log(R_low / b0) + 1)
    if f_low > 0:
        R_low = b0 / 2
        f_low = R_low - factor * (math.log(R_low / b0) + 1)
    R_high = b0 * 10
    for _ in range(100):
        f_high = R_high - factor * (math.log(R_high / b0) + 1)
        if f_high > 0:
            break
        R_high *= 1.5
    if f_high <= 0:
        return float('inf')
    for _ in range(200):
        R_mid = (R_low + R_high) / 2
        f_mid = R_mid - factor * (math.log(R_mid / b0) + 1)
        if f_mid == 0 or abs(R_high - R_low) < 1e-16:
            return R_mid
        if f_mid < 0:
            R_low = R_mid
        else:
            R_high = R_mid
    return (R_low + R_high) / 2

def compute_all():
    eV_to_erg = 1.602176634e-12
    G = 21.3e11
    Gbt3_eV = 25.0
    Gbt3_erg = Gbt3_eV * eV_to_erg
    bt_cm = (Gbt3_erg / G) ** (1 / 3)
    bp_cm = bt_cm / math.sqrt(3.0)
    sigma_vals = [0.05 + 0.01 * i for i in range(11)]
    rows = []
    # perfect loops
    b = bt_cm
    b0 = bt_cm / 2.0
    for s in sigma_vals:
        sigma = s * G
        gamma = 0.0
        Rc_cm = solve_rc(G, b, gamma, sigma, b0)
        Uc_erg = 0.25 * G * b * b * Rc_cm * (math.log(Rc_cm / b0) - 1)
        Uc_eV = Uc_erg / eV_to_erg
        Uc_norm = Uc_eV / Gbt3_eV
        rows.append(("perfect", 0.0, s, Rc_cm * 1e8, Uc_eV, Uc_norm))
    # faulted loops
    for f in [0.01, 0.02, 0.03]:
        b = bp_cm
        b0 = bp_cm / 2.0
        for s in sigma_vals:
            sigma = s * G
            gamma = f * G * bp_cm
            if sigma <= gamma / b:
                Rc_cm = float('inf')
                Uc_erg = float('inf')
                Uc_eV = float('inf')
                Uc_norm = float('inf')
            else:
                Rc_cm = solve_rc(G, b, gamma, sigma, b0)
                Uc_erg = 0.25 * G * b * b * Rc_cm * (math.log(Rc_cm / b0) - 1)
                Uc_eV = Uc_erg / eV_to_erg
                Uc_norm = Uc_eV / Gbt3_eV
            rows.append(("faulted", f, s, Rc_cm * 1e8, Uc_eV, Uc_norm))
    return rows

def write_results(outdir):
    rows = compute_all()
    path = os.path.join(outdir, "results.csv")
    with open(path, 'w') as fh:
        fh.write("loop_type,f,sigma_over_G,R_c_angstrom,U_c_eV,U_c_normalized\n")
        for r in rows:
            fh.write(f"{r[0]},{r[1]:g},{r[2]:.4f},{r[3]:.6f},{r[4]:.6e},{r[5]:.6f}\n")

def find_critical_stress(outdir):
    rows = compute_all()
    perfect = {}
    faulted = {}
    for r in rows:
        if r[0] == "perfect":
            perfect[r[2]] = r[4]
        elif r[0] == "faulted" and abs(r[1] - 0.01) < 1e-9:
            faulted[r[2]] = r[4]
    critical_s = None
    for s in sorted(perfect.keys()):
        if s in faulted and faulted[s] < perfect[s]:
            critical_s = s
            break
    if critical_s is None:
        raise RuntimeError("No crossing found")
    line = f"sigma_over_G = {critical_s:.3f}"
    path = os.path.join(outdir, "critical_stress.txt")
    with open(path, 'w') as fh:
        fh.write(line + "\n")

if __name__ == "__main__":
    outdir = sys.argv[1]
    mode = sys.argv[2]
    if mode == "results":
        write_results(outdir)
    elif mode == "critical":
        find_critical_stress(outdir)
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)
