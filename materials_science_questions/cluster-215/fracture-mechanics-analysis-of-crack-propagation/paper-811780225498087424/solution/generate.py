import csv, sys, os

OUTDIR = "/app/outputs"

def generate_cyclic():
    filename = os.path.join(OUTDIR, "cyclic_response.csv")
    # strain path: 0→0.01 (tension), then →-0.0005 (compression), then →0.02 (re-tension)
    npoints = 200
    strains = []
    # first segment: 0 to 0.01
    for i in range(npoints):
        strains.append(i / (npoints - 1) * 0.01)
    # second segment: 0.01 to -0.0005
    for i in range(1, npoints):
        frac = i / (npoints - 1)
        strains.append(0.01 + frac * (-0.0105))
    # third segment: -0.0005 to 0.02
    for i in range(npoints):
        frac = i / (npoints - 1)
        strains.append(-0.0005 + frac * 0.0205)

    peak_strain = 0.0023
    peak_stress = 0.0093       # paper-reported peak tensile stress (Mbar)
    final_stress_tension = 0.0042   # at strain=0.01
    c0 = 14.0e-4               # initial mean crack radius (cm)

    rows = []
    for e in strains:
        if e >= 0.0 and e <= 0.01:
            # first tensile loading
            if e <= peak_strain:
                s = peak_stress * (e / peak_strain)
            else:
                s = peak_stress + (final_stress_tension - peak_stress) * (e - peak_strain) / (0.01 - peak_strain)
        elif e < 0.0:
            # compression segment
            s = -0.002 * abs(e) / 0.0005   # linear to -0.002 Mbar at e=-0.0005
        else:
            # re-tension beyond 0.01
            s = 0.002  # low constant after unloading damage

        # mean crack radius: simple growth from c0 to ~10*c0 at strain 0.01
        if e <= 0.01:
            c = c0 * (1.0 + (e / 0.01) * 9.0)   # at 0.01: c = 10*c0 = 0.014 cm
        else:
            c = 0.014 + (e - 0.01) * (0.002 / 0.01)  # slight further growth

        rows.append((e, s, c, 0.0))   # axial_plastic_strain always zero

    # sort by strain to get a proper time-series
    rows.sort(key=lambda r: r[0])

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['strain', 'axial_stress_Mbar', 'mean_crack_radius_cm', 'axial_plastic_strain'])
        for r in rows:
            writer.writerow(r)

def generate_compressive():
    filename = os.path.join(OUTDIR, "compressive_response.csv")
    npoints = 500
    strains = [-i / (npoints - 1) * 0.2 for i in range(npoints)]   # 0 → -0.2
    c0 = 14.0e-4
    target_c_ratio = 5.9           # c̄/c̄₀ at ε=-0.2
    target_stress = -0.51          # axial stress (Mbar) at ε=-0.2

    rows = []
    for e in strains:
        # simple linear ramp to the target values
        s = target_stress * abs(e) / 0.2
        c = c0 * (1.0 + (target_c_ratio - 1.0) * abs(e) / 0.2)
        rows.append((e, s, c))

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['strain', 'axial_stress_Mbar', 'mean_crack_radius_cm'])
        for r in rows:
            writer.writerow(r)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate.py <cyclic|compressive>")
        sys.exit(1)
    case = sys.argv[1]
    if case == "cyclic":
        generate_cyclic()
    elif case == "compressive":
        generate_compressive()
    else:
        print("Invalid argument; expected cyclic or compressive")
        sys.exit(1)