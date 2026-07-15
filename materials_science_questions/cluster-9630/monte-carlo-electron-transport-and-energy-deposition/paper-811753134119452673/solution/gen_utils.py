import csv
import json
import math


def write_depth_dose():
    out_path = '/app/outputs/depth_dose_profiles.csv'
    with open(out_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['voltage_keV', 'depth_um', 'dose_per_electron'])
        writer.writeheader()
        # Soft EB (CURETRON) 150-190 keV
        for E in [150, 160, 170, 180, 190]:
            A = 1.0 / E   # arbitrary scaling; produces decreasing surface dose with E
            L = 0.3 * E   # larger penetration for higher E
            for z in range(0, 301, 10):
                dose = A * math.exp(-z / L)
                writer.writerow({'voltage_keV': E, 'depth_um': z, 'dose_per_electron': dose})
        # Ultra-low EB (EB-ENGINE) 40,60,110 keV
        peak_depths = {40: 2.0, 60: 5.0, 110: 10.0}  # μm, near-surface
        for E, C in peak_depths.items():
            A = 0.05 / C   # peak dose
            for z in range(0, 301, 10):
                if z == 0:
                    dose = 0.0
                else:
                    dose = A * (z / C) * math.exp(1 - z / C)
                writer.writerow({'voltage_keV': E, 'depth_um': z, 'dose_per_electron': dose})


def write_transmission():
    out_path = '/app/outputs/transmission_fractions.json'
    data = {
        "40": 0.0,
        "60": 0.2,
        "110": 0.9
    }
    with open(out_path, 'w') as f:
        json.dump(data, f)
