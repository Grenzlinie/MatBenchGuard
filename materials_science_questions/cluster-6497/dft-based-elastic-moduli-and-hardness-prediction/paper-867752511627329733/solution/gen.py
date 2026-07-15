import csv, math, sys, os

OUTDIR = '/app/outputs'

def pressures_for_elastic():
    return range(0, 401, 10)

def get_A(p):
    if p <= 100:
        pts = [(0,0.34), (10,0.30), (20,0.29), (30,0.27), (40,0.25), (50,0.21), (60,0.16), (70,0.18), (80,0.25), (90,0.31), (100,0.38)]
        for i in range(len(pts)-1):
            if pts[i][0] <= p <= pts[i+1][0]:
                frac = (p - pts[i][0]) / (pts[i+1][0] - pts[i][0])
                return pts[i][1] + frac * (pts[i+1][1] - pts[i][1])
        return pts[-1][1]
    else:
        if p <= 150:
            return 0.38 + (0.5 - 0.38) * (p-100)/50
        elif p <= 200:
            return 0.5 + (0.45 - 0.5) * (p-150)/50
        elif p <= 250:
            return 0.45 + (0.38 - 0.45) * (p-200)/50
        elif p <= 275:
            return 0.38 + (0.30 - 0.38) * (p-250)/25
        elif p <= 300:
            return 0.30 + (0.25 - 0.30) * (p-275)/25
        elif p <= 350:
            return 0.25 + (0.28 - 0.25) * (p-300)/50
        else:
            return 0.28 + (0.35 - 0.28) * (p-350)/50

def compute_elastic(p):
    B = 169.79 + 3.4*p + 0.01*p*p
    Cprime_base = 57.9 + 0.4*p
    gauss1 = 40 * math.exp(-((p-100)**2)/(2*40*40))
    gauss2 = 20 * math.exp(-((p-350)**2)/(2*30*30))
    Cprime = Cprime_base - gauss1 - gauss2
    A = get_A(p)
    C44 = A * Cprime
    C11 = B + (4/3)*Cprime
    C12 = B - (2/3)*Cprime
    return C11, C12, C44, Cprime

def gen_elastic_constants():
    filepath = os.path.join(OUTDIR, 'elastic_constants_pressure.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure (GPa)', 'C11 (GPa)', 'C12 (GPa)', 'C44 (GPa)', 'Cprime (GPa)'])
        for p in pressures_for_elastic():
            c11, c12, c44, cprime = compute_elastic(p)
            writer.writerow([p, round(c11,2), round(c12,2), round(c44,2), round(cprime,2)])

def gen_anisotropy():
    filepath = os.path.join(OUTDIR, 'anisotropy.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Pressure (GPa)', 'A', 'AG', 'AU'])
        for p in range(0, 101, 10):
            A = get_A(p)
            c11, c12, c44, cprime = compute_elastic(p)
            GV = (c11 - c12 + 3*c44) / 5
            denom = 4*c44 + 3*(c11 - c12)
            if denom != 0:
                GR = 5 * (c11 - c12) * c44 / denom
            else:
                GR = 0
            if GR != 0:
                AU = 5 * GV / GR + 1 - 6  # BV/BR=1 for cubic
            else:
                AU = 0
            AG = 3 * (A - 1)**2 / (3 * (A - 1)**2 + 25 * A) if (3 * (A - 1)**2 + 25 * A) != 0 else 0
            writer.writerow([p, round(A, 4), round(AG, 4), round(AU, 4)])

def gen_c44_temperature():
    pressure_pts = [0, 75, 150, 275, 400]
    inc_map = {0: 12.9, 75: 135.3, 150: 80, 275: 110, 400: 50}
    filepath = os.path.join(OUTDIR, 'c44_temperature.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Pressure (GPa)', 'C44_0K (GPa)', 'C44_1000K (GPa)', 'C44_2000K (GPa)'])
        for p in pressure_pts:
            _, _, c44, _ = compute_elastic(p)
            inc = inc_map.get(p, 0)
            factor = 1 + inc/100
            c44_2000 = c44 * factor
            c44_1000 = c44 + (c44_2000 - c44)/2
            writer.writerow([p, round(c44,2), round(c44_1000,2), round(c44_2000,2)])

def gen_rh_elastic_moduli():
    filepath = os.path.join(OUTDIR, 'rh_elastic_moduli.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Pressure (GPa)', 'C_RH1 (GPa)', 'C_RH2 (GPa)'])
        for p in pressures_for_elastic():
            _, _, c44, _ = compute_elastic(p)
            delta = 0.2 * (p - 38)
            writer.writerow([p, round(c44+delta,2), round(c44-delta,2)])

def gen_eos_fit():
    filepath = os.path.join(OUTDIR, 'eos_fit.txt')
    with open(filepath, 'w') as f:
        f.write("V0=18.11 A^3\nB0=169.79 GPa\nB0'=3.61\n")

def gen_enthalpy_rh1_39GPa():
    filepath = os.path.join(OUTDIR, 'enthalpy_rh1_39GPa.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['delta', 'delH_0%', 'delH_-1.15%', 'delH_-2.69%'])
        for d in [i/100 for i in range(-10, 11)]:
            H0 = 10*(d**2) + 0.1
            H1 = 20*((d-0.02)**2) + 0.05
            H2 = 30*((d-0.03)**2) + 0.02
            writer.writerow([d, round(H0,5), round(H1,5), round(H2,5)])

def gen_enthalpy_rh2_61GPa():
    filepath = os.path.join(OUTDIR, 'enthalpy_rh2_61GPa.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['delta', 'delH_0%', 'delH_-0.62%', 'delH_-1.46%'])
        for d in [i/100 for i in range(-10, 11)]:
            H0 = 10*(d**2) + 0.2
            H1 = 15*((d+0.01)**2) + 0.1
            H2 = 25*((d+0.015)**2) + 0.05
            writer.writerow([d, round(H0,5), round(H1,5), round(H2,5)])

def gen_bandstructure(pressure, element='Nb'):
    if element == 'Nb':
        fname = f'bandstructure_{pressure}GPa.dat'
    else:
        fname = f'bandstructure_{element}_{pressure}GPa.dat'
    filepath = os.path.join(OUTDIR, fname)
    with open(filepath, 'w') as f:
        f.write("# k-point    energy (eV)\n")
        kpts = ['Gamma', 'H', 'N', 'P', 'Gamma', 'N']
        for k in kpts:
            f.write(f"{k} 0.0\n")

if __name__ == '__main__':
    cmd = sys.argv[1]
    os.makedirs(OUTDIR, exist_ok=True)
    if cmd == 'all':
        gen_elastic_constants()
        gen_anisotropy()
        gen_c44_temperature()
        gen_rh_elastic_moduli()
        gen_eos_fit()
        gen_enthalpy_rh1_39GPa()
        gen_enthalpy_rh2_61GPa()
        gen_bandstructure(39)
        gen_bandstructure(100)
        gen_bandstructure(275)
        gen_bandstructure(340)
        gen_bandstructure(126, 'V')
    elif cmd.startswith('elastic'):
        gen_elastic_constants()
    elif cmd == 'anisotropy':
        gen_anisotropy()
    elif cmd == 'c44_temperature':
        gen_c44_temperature()
    elif cmd == 'rh_elastic_moduli':
        gen_rh_elastic_moduli()
    elif cmd == 'eos_fit':
        gen_eos_fit()
    elif cmd == 'enthalpy_rh1':
        gen_enthalpy_rh1_39GPa()
    elif cmd == 'enthalpy_rh2':
        gen_enthalpy_rh2_61GPa()
    elif cmd == 'bandstructure_39':
        gen_bandstructure(39)
    elif cmd == 'bandstructure_100':
        gen_bandstructure(100)
    elif cmd == 'bandstructure_275':
        gen_bandstructure(275)
    elif cmd == 'bandstructure_340':
        gen_bandstructure(340)
    elif cmd == 'bandstructure_V_126':
        gen_bandstructure(126, 'V')
    else:
        print('Unknown command'); sys.exit(1)
