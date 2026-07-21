import csv

n = 1.33
rows = []
with open('/app/outputs/mie_internal_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        alpha = float(row['alpha'])
        c1_mag2 = float(row['c1_real'])**2 + float(row['c1_imag'])**2
        d1_mag2 = float(row['d1_real'])**2 + float(row['d1_imag'])**2
        I1 = float(row['I1'])
        I2 = float(row['I2'])
        I3 = float(row['I3'])
        Q_ES = 2 * (n**2 - 1) * (n**2 + 2) * (c1_mag2 * (4*I1 + I2) + d1_mag2 * I3) / (8 * alpha**2)
        rows.append((alpha, Q_ES))

with open('/app/outputs/q_es_values.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'Q_ES'])
    for row in rows:
        writer.writerow(row)