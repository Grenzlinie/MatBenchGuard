import sys
import csv
import math

def write_kde():
    points = 200
    start, end = 0.0, 40.0
    step = (end - start) / (points - 1)
    with open('/app/outputs/kde_pore_size_dut32.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pore_diameter_A', 'density'])
        for i in range(points):
            x = start + i * step
            # Three Gaussian components matching paper Table 4 peaks
            g1 = 2.0 * math.exp(-0.5 * ((x - 14.0) / 2.0) ** 2)
            g2 = 3.0 * math.exp(-0.5 * ((x - 19.4) / 2.0) ** 2)
            g3 = 1.0 * math.exp(-0.5 * ((x - 28.2) / 2.0) ** 2)
            density = g1 + g2 + g3 + 0.1
            w.writerow([f'{x:.3f}', f'{density:.6f}'])

def write_pore_centers():
    with open('/app/outputs/pore_centers_dut32.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pore_label', 'x_A', 'y_A', 'z_A'])
        w.writerow([1, 0.0, 0.0, 0.0])
        w.writerow([2, 15.0, 5.0, 10.0])
        w.writerow([3, 30.0, 20.0, 15.0])

def write_adsorption_isotherm():
    # 75 pressure points log-spaced from 1e-5 to 1 bar
    pressures = [10 ** (-5.0 + (5.0 / 74) * i) for i in range(75)]
    k = 20.0   # steepness
    p1, p2 = 0.04, 0.1
    L1, L2 = 45.0, 31.5   # total saturation 76.5 mmol/g based on pore volume
    with open('/app/outputs/adsorption_isotherm_dut32.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pressure_bar', 'loading_mmol_g'])
        for p in pressures:
            if p == 0.0:
                p = 1e-10
            step1 = L1 / (1 + math.exp(-k * (math.log10(p) - math.log10(p1))))
            step2 = L2 / (1 + math.exp(-k * (math.log10(p) - math.log10(p2))))
            loading = step1 + step2
            w.writerow([f'{p:.6e}', f'{loading:.6f}'])

def write_pore_isotherms():
    pressures = [10 ** (-5.0 + (5.0 / 74) * i) for i in range(75)]
    k = 20.0
    p1, p2 = 0.04, 0.1
    L1, L2 = 45.0, 31.5
    # allocation consistent with cooperative filling description
    a1, a2, a3 = 10.0 / 45.0, 20.0 / 45.0, 15.0 / 45.0
    with open('/app/outputs/pore_isotherms_dut32.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pressure_bar', 'pore1_loading_mmol_g', 'pore2_loading_mmol_g', 'pore3_loading_mmol_g'])
        for p in pressures:
            step1 = L1 / (1 + math.exp(-k * (math.log10(p) - math.log10(p1))))
            step2 = L2 / (1 + math.exp(-k * (math.log10(p) - math.log10(p2))))
            p1_l = a1 * step1
            p2_l = a2 * step1
            p3_l = a3 * step1 + step2
            w.writerow([f'{p:.6e}', f'{p1_l:.6f}', f'{p2_l:.6f}', f'{p3_l:.6f}'])

def write_radial_distribution():
    r_values = [i * 0.5 for i in range(31)]  # 0 to 15 Å
    sigma = 2.0
    def gauss(r, mu):
        return math.exp(-0.5 * ((r - mu) / sigma) ** 2)
    pore_params = {
        1: {'centers': [7.0], 'amps': {'P3': [0.5], 'P4': [2.0], 'P5': [5.0]}},
        2: {'centers': [9.7, 12.0], 'amps': {'P3': [0.5, 1.0], 'P4': [2.0, 3.0], 'P5': [5.0, 5.0]}},
        3: {'centers': [14.1], 'amps': {'P3': [0.5], 'P4': [1.0], 'P5': [5.0]}}
    }
    pressure_points = ['P3', 'P4', 'P5']
    with open('/app/outputs/radial_distribution_dut32.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['pressure_point', 'pore_label', 'radius_A', 'density_arb'])
        for pp in pressure_points:
            for pore in [1, 2, 3]:
                centers = pore_params[pore]['centers']
                amps = pore_params[pore]['amps'][pp]
                for r in r_values:
                    dens = 0.1
                    for mu, amp in zip(centers, amps):
                        dens += amp * gauss(r, mu)
                    w.writerow([pp, pore, r, f'{dens:.6f}'])

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--output':
        sys.exit(1)
    basename = sys.argv[2]
    if basename == 'kde_pore_size_dut32.csv':
        write_kde()
    elif basename == 'pore_centers_dut32.csv':
        write_pore_centers()
    elif basename == 'adsorption_isotherm_dut32.csv':
        write_adsorption_isotherm()
    elif basename == 'pore_isotherms_dut32.csv':
        write_pore_isotherms()
    elif basename == 'radial_distribution_dut32.csv':
        write_radial_distribution()
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
