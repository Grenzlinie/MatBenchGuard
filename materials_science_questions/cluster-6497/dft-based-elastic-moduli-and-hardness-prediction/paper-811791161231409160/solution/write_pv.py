import math
import csv

# Reference paper DFT 2nd-order BM values
B0 = 348.0      # GPa
V0 = 206.36     # Å³
a0 = 8.2492     # Å
b0 = 8.3067     # Å
c0 = 3.0119     # Å

def p_from_v(v):
    # 2nd-order BM (B' fixed to 4)
    if v <= 0:
        return 1e10
    x = (V0 / v) ** (1.0 / 3.0)
    return 1.5 * B0 * (x ** 7 - x ** 5)

def v_from_p(p_target):
    lo, hi = V0 * 0.6, V0 * 1.2
    for _ in range(40):
        mid = (lo + hi) / 2.0
        p_mid = p_from_v(mid)
        if p_mid < p_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

pressures = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
outfile = "/app/outputs/eta_Ta2N3_PV.csv"

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["pressure_GPa", "volume_A3", "a_A", "b_A", "c_A"])
    for P in pressures:
        if P == 0.0:
            V = V0
        else:
            V = v_from_p(P)
        factor = (V / V0) ** (1.0 / 3.0)
        a = a0 * factor
        b = b0 * factor
        c = c0 * factor
        writer.writerow([f"{P:.4f}", f"{V:.6f}", f"{a:.6f}", f"{b:.6f}", f"{c:.6f}"])
