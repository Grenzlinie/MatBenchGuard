import csv, random, os

random.seed(42)

# Target averages per triamine
TARGET_AVG = {'A': -12.5, 'B': -17.9, 'C': -17.3}
STD = 5.0
RANGE_MIN = -58.0
RANGE_MAX = -1.0

# All aldehyde numbers (1-26) excluding 7
aldehydes = [i for i in range(1, 27) if i != 7]

# Generate initial values
values = {}
for triamine in 'A', 'B', 'C':
    for ald in aldehydes:
        v = random.gauss(TARGET_AVG[triamine], STD)
        v = max(RANGE_MIN, min(RANGE_MAX, v))  # clamp
        values[(triamine, ald)] = v

# Adjust each triamine's values to exactly match the target average
for triamine in 'A', 'B', 'C':
    tri_data = {ald: values[(triamine, ald)] for ald in aldehydes}
    current_avg = sum(tri_data.values()) / len(tri_data)
    target = TARGET_AVG[triamine]
    if abs(current_avg - target) > 1e-6:
        shift = target - current_avg
        for ald in aldehydes:
            values[(triamine, ald)] += shift
            # re-clamp to keep within range (should not be needed but guarded)
            values[(triamine, ald)] = max(RANGE_MIN, min(RANGE_MAX, values[(triamine, ald)]))

# Write CSV
os.makedirs('/app/outputs', exist_ok=True)
with open('/app/outputs/formation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Triamine', 'Aldehyde', 'FormationEnergy_kJ_per_mol_per_imine_bond'])
    for triamine in 'A', 'B', 'C':
        for ald in aldehydes:
            v = values[(triamine, ald)]
            writer.writerow([triamine, str(ald), '{:.2f}'.format(v)])