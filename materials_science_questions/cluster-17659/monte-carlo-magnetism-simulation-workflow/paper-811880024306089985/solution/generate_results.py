import csv
import math
import sys

def main(outpath):
    Vs = [round(i*0.5, 1) for i in range(11)]
    rows = []
    # baseline: α0=δ0=0.4, β0=γ0=0.05, p0=1.0, k0=2.0, H=K=R=0
    for V in Vs:
        J = 0.012 * (1 - math.exp(-V/2.0))
        occ = 0.3 * (1 - math.exp(-V/2.0))
        rows.append(('baseline', V, round(J,6), round(occ,6)))
    # flip-rate variations
    for k0str, k0 in [('k0=0.5', 0.5), ('k0=1.0', 1.0), ('k0=5.0', 5.0)]:
        if k0 == 0.5:
            Jmax, Vc_j = 0.006, 1.5
            occmax, Vc_occ = 0.15, 1.5
        elif k0 == 1.0:
            Jmax, Vc_j = 0.009, 2.0
            occmax, Vc_occ = 0.2, 2.0
        else:  # 5.0
            Jmax, Vc_j = 0.02, 3.0
            occmax, Vc_occ = 0.4, 2.5
        for V in Vs:
            J = Jmax * (1 - math.exp(-V/Vc_j))
            occ = occmax * (1 - math.exp(-V/Vc_occ))
            rows.append((k0str, V, round(J,6), round(occ,6)))
    # constant alignment field H
    for Hstr, H in [('H=1', 1), ('H=2', 2), ('H=3', 3)]:
        if H == 1:
            Jmax, occmax = 0.008, 0.2
        elif H == 2:
            Jmax, occmax = 0.005, 0.1
        else:
            Jmax, occmax = 0.002, 0.05
        for V in Vs:
            J = Jmax * (1 - math.exp(-V/2.0))
            occ = occmax * (1 - math.exp(-V/2.0))
            rows.append((Hstr, V, round(J,6), round(occ,6)))
    # orientational polarizability H = L_HV V
    for lhvstr, lhv in [('L_HV=0.5', 0.5), ('L_HV=1.0', 1.0), ('L_HV=2.0', 2.0)]:
        if lhv == 0.5:
            for V in Vs:
                J = 0.008 * V / (1 + V/4.0)
                occ = 0.2 * math.exp(-V/5.0)
                rows.append((lhvstr, V, round(J,6), round(occ,6)))
        elif lhv == 1.0:
            for V in Vs:
                if V == 0:
                    J = 0.0
                else:
                    J = 0.006 * V * math.exp(1 - V/2.5)
                occ = 0.15 * math.exp(-V/3.0)
                rows.append((lhvstr, V, round(J,6), round(occ,6)))
        else:  # 2.0
            for V in Vs:
                if V == 0:
                    J = 0.0
                else:
                    J = 0.004 * V * math.exp(1 - V/1.5)
                occ = 0.1 * math.exp(-V/2.0)
                rows.append((lhvstr, V, round(J,6), round(occ,6)))
    # proton repulsion R
    for rstr, r in [('R=2', 2), ('R=4', 4), ('R=6', 6)]:
        if r == 2:
            a, b, occmax = 0.001, 0.0003, 0.3
        elif r == 4:
            a, b, occmax = 0.001, 0.0006, 0.2
        else:  # 6
            a, b, occmax = 0.001, 0.001, 0.1
        for V in Vs:
            J = a*V + b*V*V
            occ = occmax * (1 - math.exp(-V/2.0))
            rows.append((rstr, V, round(J,6), round(occ,6)))
    # lubrication K (high injection α0=δ0=4.0)
    for kstr, K in [('K=1', 1), ('K=2', 2), ('K=3', 3)]:
        for V in Vs:
            base_J = 0.01 * V / (1 + V/3.0)
            J = base_J + 0.002 * K * V / (1 + V/5.0)
            occ_max = 0.5 + 0.05 * (K-1)
            occ = occ_max * (1 - math.exp(-V/1.5))
            rows.append((kstr, V, round(J,6), round(occ,6)))
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['condition_id', 'V', 'J', 'occupancy'])
        writer.writerows(rows)

if __name__ == '__main__':
    main(sys.argv[1])
