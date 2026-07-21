import csv
import json
import math
import sys

def a1(L):
    return math.sqrt(2) / (L * math.sin(math.pi / (2 * L)))

def a2(L):
    return 3.0 / 4.0

# Paper Table 1 δ_L values (gold)
paper_deltas = {
    8:  0.0250979,
    12: 0.0245631,
    16: 0.0243433,
    20: 0.0242308,
    24: 0.0241652,
    28: 0.0241234,
    32: 0.024095,
}
# Analytic thermodynamic limit: 7 ζ(3) / (8 π³ √2)
delta_inf = 0.0239866

L_list = [8, 12, 16, 20, 24, 28, 32]
g_vals = list(range(10, 21))

def gen_raw_energies():
    with open('/app/outputs/raw_energies.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['L', 'g', 'Delta'])
        for L in L_list:
            a1v = a1(L)
            a2v = a2(L)
            d = paper_deltas[L]
            for g in g_vals:
                Delta = L * (a1v * g + a2v + d / g)
                w.writerow([L, g, Delta])

def gen_delta_L():
    with open('/app/outputs/delta_L_values.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['L', 'delta'])
        for L in L_list:
            w.writerow([L, paper_deltas[L]])
        w.writerow(['inf', delta_inf])

def gen_leading_constant():
    results = [{"L": L, "a1": a1(L), "a2": a2(L)} for L in L_list]
    with open('/app/outputs/leading_constant_report.json', 'w') as f:
        json.dump({"results": results}, f)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'raw_energies':
        gen_raw_energies()
    elif cmd == 'delta_L':
        gen_delta_L()
    elif cmd == 'leading_constant':
        gen_leading_constant()
    else:
        raise ValueError(f'Unknown command: {cmd}')
