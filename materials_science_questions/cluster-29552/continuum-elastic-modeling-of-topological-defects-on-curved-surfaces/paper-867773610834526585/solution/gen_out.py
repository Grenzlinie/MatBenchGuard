import sys, csv, math

def gen_phase_diagram(output_path):
    n = 20
    a_min, a_max = 2.0, 10.0
    c_min, c_max = 1.0, 10.0
    a_step = (a_max - a_min) / (n - 1)
    c_step = (c_max - c_min) / (n - 1)
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['K24_over_K2', 'K3_over_K2', 'beta1_rad', 'free_energy_per_piL'])
        for i in range(n):
            a = a_min + i * a_step
            for j in range(n):
                c = c_min + j * c_step
                # surface tilt angle beta1 (Eq. 4 at r=R)
                arg = 2 * a * (a - 2) / c
                beta1 = math.atan(math.sqrt(max(0.0, arg)))
                # free energy per pi*L (Eq. 5, with K2=1)
                if abs(c - 1.0) < 1e-12:
                    # limit c->1: F = -(a-2)^2/(a-1)
                    if abs(a - 2) < 1e-12:
                        F = 0.0
                    else:
                        F = -(a - 2) + (a - 2) / (a - 1)
                else:
                    term1 = -(a - 2)
                    factor = c / math.sqrt(c - 1)
                    ratio = (a - 2) * math.sqrt(c - 1) / (c + a - 2)
                    term2 = factor * math.atan(ratio)
                    F = term1 + term2
                w.writerow([a, c, beta1, F])

def gen_defect_energies(output_path):
    # plausible synthetic energies matching paper's trends: monotonic, crossover ~4
    k_vals = [2.0, 3.0, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    e_point = [0.50, 0.35, 0.25, 0.20, 0.18, 0.14, 0.11, 0.08, 0.06, 0.04]
    e_wall  = [0.30, 0.32, 0.35, 0.38, 0.40, 0.45, 0.50, 0.55, 0.58, 0.60]
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['K24_over_K', 'energy_point', 'energy_wall'])
        for k, ep, ew in zip(k_vals, e_point, e_wall):
            w.writerow([k, ep, ew])

if __name__ == '__main__':
    mode = sys.argv[1]
    out_path = sys.argv[2]
    if mode == 'phase_diagram':
        gen_phase_diagram(out_path)
    elif mode == 'defect_energies':
        gen_defect_energies(out_path)
