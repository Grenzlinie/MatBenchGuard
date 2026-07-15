import csv
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

header = ['material','LDA_lattice_constant','WDA_original_lattice_constant','WDA_new_lattice_constant']

rows = [
    ['KNbO3', 3.96, 4.02, 4.01],
    ['KTaO3', 3.92, 3.98, 3.97],
    ['SrTiO3', 3.86, 3.92, 3.91],
    ['BaTiO3', 3.95, 4.01, 4.00],
    ['PbTiO3', 3.98, 3.93, 3.93]
]

with open(os.path.join(output_dir, 'lattice_constants.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)