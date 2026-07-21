import csv
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

rows = [
    ('pristine', -0.63),
    ('N5', -3.05),
    ('N6', -3.44),
    ('NQ', -0.56),
]

with open(os.path.join(output_dir, 'adsorption_energies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['doping_type', 'adsorption_energy_eV'])
    for dtype, energy in rows:
        writer.writerow([dtype, energy])
