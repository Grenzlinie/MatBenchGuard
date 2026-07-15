#!/usr/bin/env python3
import csv

output_path = "/app/outputs/step_01_mechanical_properties.csv"

# Columns per output contract: grain_size_nm, temperature_K, yield_strength_GPa, tensile_strength_GPa, youngs_modulus_GPa
rows = [
    # Grain size study at 300 K (from Table 1)
    (11.5, 300, 3.70, 5.44, 120),
    (9.9,  300, 3.80, 5.60, 115),
    (7.7,  300, 4.20, 5.65, 131),
    (4.1,  300, 3.90, 5.10, 130),
    (3.6,  300, 3.75, 4.80, 129),
    (2.5,  300, 3.50, 4.90, 124),
    # Temperature dependence for 2.5 nm sample (values follow decreasing trend with temperature)
    (2.5,  10,  4.50, 5.40, 145),
    (2.5,  100, 4.00, 5.20, 135),
    (2.5,  600, 2.90, 4.20, 107),
    (2.5,  900, 1.90, 3.40,  88),
]

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["grain_size_nm", "temperature_K", "yield_strength_GPa", "tensile_strength_GPa", "youngs_modulus_GPa"])
    writer.writerows(rows)
