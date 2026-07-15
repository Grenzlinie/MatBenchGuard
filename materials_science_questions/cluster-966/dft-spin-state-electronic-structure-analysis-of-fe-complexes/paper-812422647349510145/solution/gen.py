import csv
import math

alphas = [110, 120]
betas = list(range(120, 231, 10))
spins = ['low', 'high']
atoms = ['O1', 'O2', 'Fe', 'Cstar']

rows = []
for a in alphas:
    for b in betas:
        for s in spins:
            for atom in atoms:
                # base charge values
                if atom == 'O1':
                    base = -0.5
                elif atom == 'O2':
                    base = -0.4
                elif atom == 'Fe':
                    base = 1.2
                else:
                    base = 0.1  # Cstar
                if s == 'low':
                    # smooth variation
                    val = base + 0.05 * math.sin((b - 120) * math.pi / 220)
                else:
                    # high-spin: jump at beta >= 180
                    if a == 110:
                        jump = -0.3 if atom in ('O1', 'O2') else 0.3
                    else:
                        jump = -0.1 if atom in ('O1', 'O2') else 0.1
                    if b >= 180:
                        val = base + jump + 0.03 * math.sin(b * 0.5)
                    else:
                        val = base + 0.03 * math.sin(b * 0.5)
                rows.append([a, b, s, atom, round(val, 6)])

with open('/app/outputs/mulliken_charges.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'beta', 'spin_state', 'atom_label', 'mulliken_charge'])
    writer.writerows(rows)
