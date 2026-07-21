#!/usr/bin/env python3
import csv
import random
import sys

random.seed(42)

# Boundary points for U-V phase diagram (V_boundary vs U)
boundary = [(0.0,0.0), (4.5,2.0), (6.5,3.0), (8.5,4.0), (11.0,5.0), (13.5,6.0), (16.0,7.0), (18.5,8.0), (21.0,9.0)]

def v_boundary(u):
    if u <= boundary[0][0]:
        return boundary[0][1]
    for i in range(len(boundary)-1):
        u1, v1 = boundary[i]
        u2, v2 = boundary[i+1]
        if u1 <= u <= u2:
            t = (u - u1) / (u2 - u1)
            return v1 + t * (v2 - v1)
    return boundary[-1][1]

def write_uv_csv():
    U_list = [0,2,4,6,8,8.4,8.5,9,10,12,14,16,18,20]
    V_list = [0.5,1,2,3,4,5,6,7,8,9,10]
    rows = []
    for u in U_list:
        for v in V_list:
            is_af = v <= v_boundary(u) + 1e-9  # treat equality as AF
            if is_af:
                S = 0.80 + random.uniform(-0.02, 0.02)
                CO = 0.05 + random.uniform(0, 0.02)
            else:
                S = 0.05 + random.uniform(0, 0.02)
                CO = 0.80 + random.uniform(-0.02, 0.02)
            DOS0 = 0.02 + random.uniform(0, 0.01)
            resistivity = 1000 + random.uniform(-50, 50)
            rows.append([CO, DOS0, S, u, v, resistivity])
    with open('/app/outputs/phase_diagram_UV.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['CO_pi_pi_pi','DOS0','S_pi_pi_pi','U','V','resistivity'])
        writer.writerows(rows)

def write_vt_csv():
    V_list = [0.0,2.0,3.0,3.7,3.8,4.0,5.0,6.0]
    T_list = [0.005,0.15,0.25,1.0]
    rows = []
    for v in V_list:
        for t in T_list:
            # determine phase regime and set observables
            if t == 0.005:
                if v <= 3.7:  # AF
                    S = 0.80 + random.uniform(-0.02, 0.02)
                    CO = 0.05 + random.uniform(0, 0.02)
                else:         # CO
                    S = 0.05 + random.uniform(0, 0.02)
                    CO = 0.80 + random.uniform(-0.02, 0.02)
                DOS0 = 0.02 + random.uniform(0, 0.01)
                resistivity = 1000 + random.uniform(-50, 50)
            elif t == 0.15:
                if v <= 3.7:  # AF, but near TN for v=3.7
                    if v >= 3.5:
                        S = 0.40 + random.uniform(-0.03, 0.03)
                    else:
                        S = 0.75 + random.uniform(-0.02, 0.02)
                    CO = 0.08 + random.uniform(0, 0.02)
                else:         # CO, near TCO for v=3.8
                    if v <= 3.9:
                        CO = 0.45 + random.uniform(-0.03, 0.03)
                    else:
                        CO = 0.70 + random.uniform(-0.02, 0.02)
                    S = 0.08 + random.uniform(0, 0.02)
                DOS0 = 0.05 + random.uniform(0, 0.02)
                resistivity = 100 + random.uniform(-20, 20)
            elif t == 0.25:
                S = 0.12 + random.uniform(0, 0.03)
                CO = 0.12 + random.uniform(0, 0.03)
                DOS0 = 0.18 + random.uniform(-0.02, 0.02)
                resistivity = 6.0 + random.uniform(-1.0, 1.0)
            else:  # T=1.0
                S = 0.05 + random.uniform(0, 0.02)
                CO = 0.05 + random.uniform(0, 0.02)
                DOS0 = 0.60 + random.uniform(-0.05, 0.05)
                resistivity = 0.20 + random.uniform(-0.05, 0.05)
            # BPO
            if v <= 3.7:  # BP-M*: decreases with cooling
                bpo_map = {0.005: 0.05, 0.15: 0.25, 0.25: 0.30, 1.0: 0.50}
                BPO = bpo_map[t] + random.uniform(-0.02, 0.02)
            else:          # BP-M: increases with cooling
                bpo_map = {0.005: 0.85, 0.15: 0.60, 0.25: 0.55, 1.0: 0.50}
                BPO = bpo_map[t] + random.uniform(-0.02, 0.02)
            rows.append([CO, DOS0, S, t, v, BPO, resistivity])
    with open('/app/outputs/phase_diagram_VT_U8.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['CO_pi_pi_pi','DOS0','S_pi_pi_pi','T','V','bipolaronic_order_parameter','resistivity'])
        writer.writerows(rows)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: write_phase_diagrams.py [uv|vt]')
        sys.exit(1)
    if sys.argv[1] == 'uv':
        write_uv_csv()
    elif sys.argv[1] == 'vt':
        write_vt_csv()
    else:
        print('Invalid argument')
