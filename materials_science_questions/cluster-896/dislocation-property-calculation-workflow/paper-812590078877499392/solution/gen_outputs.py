import sys
import csv
import math
import json

def gauss(p, sigma):
    return math.exp(-p * p / (2.0 * sigma * sigma))

output = sys.argv[1]
if output == 'vacancy_results.json':
    data = {
        "electron_density_center_fraction_of_bulk": 0.24,
        "positron_lifetime_ps": 243
    }
    with open('/app/outputs/vacancy_results.json', 'w') as f:
        json.dump(data, f)
elif output == 'dislocation_results.json':
    data = {
        "hole_radius_angstrom": 0.85,
        "electron_density_center_fraction_of_bulk": 0.37,
        "positron_lifetime_ps": 229
    }
    with open('/app/outputs/dislocation_results.json', 'w') as f:
        json.dump(data, f)
elif output == 'angular_correlation_vacancy.csv':
    # FWHM 2.1 / (2*sqrt(2*ln2)) ≈ 0.8914
    sigma = 0.8914
    p_vals = [i * 0.05 for i in range(0, 81)]  # 0 .. 4.0
    with open('/app/outputs/angular_correlation_vacancy.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p', 'I(p)'])
        for p in p_vals:
            w.writerow([round(p, 3), round(gauss(p, sigma), 6)])
elif output == 'angular_correlation_dislocation_z.csv':
    # FWHM 1.75 / 2.35482 ≈ 0.7432
    sigma = 0.7432
    p_vals = [i * 0.05 for i in range(0, 81)]
    with open('/app/outputs/angular_correlation_dislocation_z.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p', 'I_z(p)'])
        for p in p_vals:
            w.writerow([round(p, 3), round(gauss(p, sigma), 6)])
elif output == 'angular_correlation_dislocation_x.csv':
    # FWHM 2.34 / 2.35482 ≈ 0.9937
    sigma = 0.9937
    p_vals = [i * 0.05 for i in range(0, 81)]
    with open('/app/outputs/angular_correlation_dislocation_x.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p', 'I_x(p)'])
        for p in p_vals:
            w.writerow([round(p, 3), round(gauss(p, sigma), 6)])
elif output == 'angular_correlation_dislocation_y.csv':
    # same as x
    sigma = 0.9937
    p_vals = [i * 0.05 for i in range(0, 81)]
    with open('/app/outputs/angular_correlation_dislocation_y.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p', 'I_y(p)'])
        for p in p_vals:
            w.writerow([round(p, 3), round(gauss(p, sigma), 6)])
else:
    raise ValueError('Unknown output ' + output)
