import csv
import os

def generate_curve(config, E, sigma_peak, peak_strain):
    with open('/app/outputs/stress_strain_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for i in range(0, 1001):  # strain from 0.0 to 0.1 in steps of 0.0001
            s = i * 0.0001
            if s <= 0.01:
                sig = E * s
            elif s <= 0.03:
                sig = E * s
            elif s <= peak_strain:
                # quadratic that passes through (0.03, E*0.03) with zero slope at peak_strain
                a = (E * 0.03 - sigma_peak) / ((0.03 - peak_strain) ** 2)
                sig = a * (s - peak_strain) ** 2 + sigma_peak
            else:
                # linear softening to 0 stress at strain=0.1
                sig = sigma_peak * (0.1 - s) / (0.1 - peak_strain)
            writer.writerow([config, s, sig])

if __name__ == '__main__':
    os.makedirs('/app/outputs', exist_ok=True)
    # Write header
    with open('/app/outputs/stress_strain_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['config', 'strain', 'stress'])

    configurations = {
        'PG':       (4.9,   0.3775, 0.05),   # modulus (GPa), peak stress (GPa), peak strain
        'GV_all':   (19.53, 0.7835, 0.06),
        'GV_half':  (8.28,  1.024,  0.07),
    }
    for config, (E, sigma_peak, peak_strain) in configurations.items():
        generate_curve(config, E, sigma_peak, peak_strain)
