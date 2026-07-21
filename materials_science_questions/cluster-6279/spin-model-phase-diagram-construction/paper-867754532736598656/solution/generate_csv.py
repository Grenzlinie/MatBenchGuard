import csv
import math
import sys

def write_phase_T0(path):
    Lambdas = [0.6, 0.8, 1.0]
    gH_vals = [i*0.02 for i in range(31)]  # 0..0.6
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Lambda', 'gH', 'mu_crit'])
        for L in Lambdas:
            base = 0.34 if L == 0.6 else (0.345 if L == 0.8 else 0.35)
            for gH in gH_vals:
                mu = base + 0.05 * gH
                w.writerow([L, round(gH, 3), round(mu, 4)])

def write_phase_T015(path):
    Lambdas = [0.6, 0.8, 1.0]
    gH_vals = [i*0.02 for i in range(31)]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Lambda', 'gH', 'mu_crit'])
        for L in Lambdas:
            base = 0.415 if L == 0.6 else (0.42 if L == 0.8 else 0.425)
            for gH in gH_vals:
                mu = base - 0.3*gH + 1.2*gH*gH
                w.writerow([L, round(gH, 3), round(mu, 4)])

def write_diquark_04(path):
    gH_vals = [i*0.01 for i in range(61)]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['gH', 'Delta_T0', 'Delta_T0.1', 'Delta_T0.15'])
        for gH in gH_vals:
            # T=0: stable only for small gH
            if gH < 0.12:
                d0 = 0.08 * max(0, (1.0 - gH/0.12))
            else:
                d0 = 0.0
            # T=0.1: bump
            if 0.04 < gH < 0.26:
                d1 = 0.07 * math.exp(-((gH-0.13)/0.08)**4)
            else:
                d1 = 0.0
            # T=0.15: smaller bump
            if 0.05 < gH < 0.30:
                d2 = 0.04 * math.exp(-((gH-0.20)/0.06)**4)
            else:
                d2 = 0.0
            w.writerow([round(gH, 3), round(d0, 4), round(d1, 4), round(d2, 4)])

def write_diquark_08(path):
    gH_vals = [i*0.02 for i in range(31)]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['gH', 'Delta_T0_Lambda0.8', 'Delta_T0_Lambda1.0',
                    'Delta_T0.15_Lambda0.8', 'Delta_T0.15_Lambda1.0'])
        for gH in gH_vals:
            d08_T0 = 0.10 + 0.15 * math.tanh(gH / 0.2)
            d10_T0 = 0.12 + 0.20 * math.tanh(gH / 0.2)
            d08_T15 = 0.0 if gH < 0.4 else 0.05 * math.tanh((gH - 0.4) / 0.1)
            d10_T15 = 0.0 if gH < 0.5 else 0.06 * math.tanh((gH - 0.5) / 0.1)
            w.writerow([round(gH, 3), round(d08_T0, 4), round(d10_T0, 4),
                        round(d08_T15, 4), round(d10_T15, 4)])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'phase_boundary_T0':
        write_phase_T0('/app/outputs/phase_boundary_T0.csv')
    elif cmd == 'phase_boundary_T0.15':
        write_phase_T015('/app/outputs/phase_boundary_T0.15.csv')
    elif cmd == 'diquark_04':
        write_diquark_04('/app/outputs/diquark_condensate_mu0.4_Lambda0.8.csv')
    elif cmd == 'diquark_08':
        write_diquark_08('/app/outputs/diquark_condensate_mu0.8.csv')
    else:
        sys.exit(2)
