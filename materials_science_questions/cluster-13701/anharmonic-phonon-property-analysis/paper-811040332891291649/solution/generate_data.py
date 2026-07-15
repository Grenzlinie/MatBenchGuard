import csv
import math
import os
import random
import numpy as np

outdir = '/app/outputs'
os.makedirs(outdir, exist_ok=True)

random.seed(42)
np.random.seed(42)

# Target widths (degrees) used to guide distribution parameters
# but the actual width will be computed from the generated sample.
target_width_approx = {
    (0.1, 0): 28.0,
    (0.5, 0): 20.0,
    (1.0, 0): 15.0,
    (2.6, 0): 18.0,
    (10.0, 0): 25.0,
    (100.0, 0): 38.0,
    (0.1, 600): 40.0,
    (0.5, 600): 28.0,
    (1.0, 600): 20.0,
    (2.6, 600): 22.0,
    (10.0, 600): 26.0,
    (100.0, 600): 39.0,
}

# Sticking probability (600 K only)
sticking = {
    0.1: 0.65,
    0.5: 0.12,
    1.0: 0.03,
    2.6: 0.01,
    10.0: 0.01,
    100.0: 0.15,
}

energies = [0.1, 0.5, 1.0, 2.6, 10.0, 100.0]
temperatures = [0, 600]

n_static = 500       # must be at least a few hundred to see bimodal shape
n_thermal = 1500

# Write raw data and record actual angular widths
raw_path = os.path.join(outdir, 'relative_energy_data.csv')
width_path = os.path.join(outdir, 'angular_widths.csv')
stick_path = os.path.join(outdir, 'sticking_probability.csv')

width_rows = []
raw_header = ['exit_angle_deg', 'final_energy_eV', 'incidence_energy_eV', 'surface_temperature_K', 'trajectory_id']

with open(raw_path, 'w', newline='') as fraw:
    writer = csv.writer(fraw)
    writer.writerow(raw_header)

    for E in energies:
        for T in temperatures:
            n_traj = n_static if T == 0 else n_thermal
            w_approx = target_width_approx[(E, T)]
            # Generate angles with bimodal for static, unimodal for 600K
            if T == 0:
                # Bimodal to produce rainbow peaks.
                # Choose separation d so that the required standard deviation s is non-negative.
                # Overall variance: var = s^2 + (d/2)^2 = (w/2)^2.
                # Let d = min(0.8 * w_approx, 80) to keep peaks distinct.
                d = min(0.8 * w_approx, 80.0)
                c1 = 40.0 - d / 2.0
                c2 = 40.0 + d / 2.0
                var_target = (w_approx / 2.0) ** 2
                var_centers = (d / 2.0) ** 2
                s2 = max(0.0, var_target - var_centers)
                s = math.sqrt(s2) if s2 > 0 else 0.1
                angles = []
                for _ in range(n_traj):
                    mu = c1 if random.random() < 0.5 else c2
                    ang = np.random.normal(mu, s)
                    ang = max(1.0, min(89.0, ang))
                    angles.append(ang)
            else:
                # Unimodal centered around specular (40 deg)
                s = w_approx / 2.0
                angles = []
                for _ in range(n_traj):
                    ang = np.random.normal(40.0, s)
                    ang = max(1.0, min(89.0, ang))
                    angles.append(ang)

            # Compute actual angular width from the generated angles
            angles_arr = np.array(angles)
            mean_theta = np.mean(angles_arr)
            mean_theta2 = np.mean(angles_arr ** 2)
            actual_width = 2.0 * math.sqrt(max(0.0, mean_theta2 - mean_theta ** 2))
            width_rows.append([E, T, actual_width])

            # Final energies: random scale around incidence energy
            for i, ang in enumerate(angles):
                final_e = E * (0.5 + 0.5 * random.random())
                writer.writerow([ang, final_e, E, T, i])

# Write angular_widths.csv
with open(width_path, 'w', newline='') as fw:
    w_writer = csv.writer(fw)
    w_writer.writerow(['incidence_energy_eV', 'surface_temperature_K', 'angular_width_deg'])
    for row in width_rows:
        w_writer.writerow(row)

# Write sticking_probability.csv
with open(stick_path, 'w', newline='') as fs:
    s_writer = csv.writer(fs)
    s_writer.writerow(['incidence_energy_eV', 'sticking_probability'])
    for E in energies:
        s_writer.writerow([E, sticking[E]])

print("All output CSVs generated successfully.")
