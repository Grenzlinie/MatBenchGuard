import sys, csv, json

def load_curve(path):
    N, S = [], []
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            N.append(int(row[0]))
            S.append(float(row[1]))
    return N, S

def find_critical(N, S, C):
    for n, s in zip(N, S):
        if s <= C:
            return n
    return None

# Material constants from PhiP Table I (ΔE_bs / E_coh,b)
materials = {
    "V":  5.37e-2,
    "Cr": 9.25e-2,
    "Nb": 3.82e-2,
    "Mo": 5.58e-2,
    "Ta": 3.53e-2,
    "W":  4.32e-2
}

curve_path = sys.argv[1]
out_path = sys.argv[2]

N, S = load_curve(curve_path)
results = {}
for metal, C in materials.items():
    ncrit = find_critical(N, S, C)
    results[metal] = ncrit

with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
