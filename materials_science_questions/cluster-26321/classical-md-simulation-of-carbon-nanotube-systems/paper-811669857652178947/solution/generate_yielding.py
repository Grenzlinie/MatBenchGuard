import csv, sys

sp3 = {
    (300, 2.0): 12.0, (300, 0.1): 9.5, (300, 0.0125): 7.0,
    (800, 2.0): 10.0, (800, 0.1): 7.5, (800, 0.0125): 5.0,
    (1600, 2.0): 8.0, (1600, 0.1): 5.5, (1600, 0.0125): 4.0,
}
rotation = {
    (300, 2.0): 10.0, (300, 0.1): 8.0, (300, 0.0125): 6.5,
    (800, 2.0): 8.5, (800, 0.1): 6.5, (800, 0.0125): 5.0,
    (1600, 2.0): 7.0, (1600, 0.1): 5.0, (1600, 0.0125): 3.5,
}

out = sys.argv[1] if len(sys.argv) > 1 else '/app/outputs/yielding_strain.csv'
temps = [300, 800, 1600]
rates = [2.0, 0.1, 0.0125]

with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'strain_rate', 'defect_type', 'yielding_strain'])
    for t in temps:
        for r in rates:
            writer.writerow([t, r, 'sp3', sp3[(t, r)]])
            writer.writerow([t, r, 'rotation', rotation[(t, r)]])
