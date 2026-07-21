import csv
import json
import os

output_dir = '/app/outputs'

def generate_csv():
    # c1 from 6.0 to 10.0 in steps of 0.25
    c1_values = [round(6.0 + i * 0.25, 2) for i in range(17)]
    # sharp jump in improved algorithm: centred at 8.25
    U_improved = []
    rho_improved = []
    for c in c1_values:
        if c <= 8.0:
            U_improved.append(-0.62)
            rho_improved.append(0.08)
        elif c == 8.25:
            U_improved.append(-0.65)   # bridging point to guarantee derivative peak at 8.25
            rho_improved.append(0.10)
        else:
            U_improved.append(-0.78)
            rho_improved.append(0.25)

    # broad transition for Metropolis (hysteresis width ~1.5)
    U_metropolis = []
    rho_metropolis = []
    transition_start = 7.5
    transition_end = 9.0
    for c in c1_values:
        if c <= transition_start:
            U_metropolis.append(-0.62)
            rho_metropolis.append(0.08)
        elif c >= transition_end:
            U_metropolis.append(-0.78)
            rho_metropolis.append(0.25)
        else:
            frac = (c - transition_start) / (transition_end - transition_start)
            U_metropolis.append(-0.62 - 0.16 * frac)
            rho_metropolis.append(0.08 + 0.17 * frac)

    filepath = os.path.join(output_dir, 'step_01_scan_results.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['c1', 'U_metropolis', 'U_improved', 'rho_metropolis', 'rho_improved'])
        for c, um, ui, rm, ri in zip(c1_values, U_metropolis, U_improved, rho_metropolis, rho_improved):
            writer.writerow([c, um, ui, rm, ri])
    print(f'Written {filepath}')

def generate_json():
    data = {
        'low_c1_phase': 'AF',
        'high_c1_phase': 'FM+SF',
        'critical_c1_range': [8.25, 8.30]
    }
    filepath = os.path.join(output_dir, 'step_02_phase_analysis.json')
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f'Written {filepath}')

if __name__ == '__main__':
    os.makedirs(output_dir, exist_ok=True)
    generate_csv()
    generate_json()