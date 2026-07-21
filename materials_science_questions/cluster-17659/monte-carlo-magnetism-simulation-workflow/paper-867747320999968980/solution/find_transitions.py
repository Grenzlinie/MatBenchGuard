import csv
import sys

input_csv = sys.argv[1]
output_csv = sys.argv[2]

rows = []
with open(input_csv, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

groups = {}
for row in rows:
    n = row['n']
    if n not in groups:
        groups[n] = []
    groups[n].append(row)

transitions = []
for n, group in groups.items():
    group_sorted = sorted(group, key=lambda r: float(r['T']), reverse=True)
    T_P_SG1 = ''
    T_SG1_SG2 = ''
    for r in group_sorted:
        if float(r['q1']) > 1e-3:
            T_P_SG1 = r['T']
            break
    for r in group_sorted:
        if float(r['q0']) > 1e-3:
            T_SG1_SG2 = r['T']
            break
    transitions.append([n, T_P_SG1, T_SG1_SG2])

with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['n', 'T_P_SG1', 'T_SG1_SG2'])
    writer.writerows(transitions)
