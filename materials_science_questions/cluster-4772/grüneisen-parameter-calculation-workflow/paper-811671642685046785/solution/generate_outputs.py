import csv
import sys

if len(sys.argv) != 3:
    print("Usage: generate_outputs.py <curve_type> <output_csv>")
    sys.exit(1)

curve_type = sys.argv[1]
outpath = sys.argv[2]

def gen_isotherm():
    # compression from 1.02 down to 0.70, step 0.005
    comps = [round(1.02 - 0.005 * i, 4) for i in range(65)]
    rows = []
    K0 = 444.0
    K0p = 3.5
    for comp in comps:
        pressure = (K0 / K0p) * ((1.0 / comp) ** K0p - 1.0)
        rows.append((comp, round(pressure, 4)))
    return rows

def gen_hugoniot():
    # compression from 1.00 down to 0.50, step 0.005
    comps = [round(1.00 - 0.005 * i, 4) for i in range(101)]
    rows = []
    K0 = 444.0
    K0p = 3.5
    for comp in comps:
        pc = (K0 / K0p) * ((1.0 / comp) ** K0p - 1.0)
        # shock-heating factor
        multi = 1.0 + 0.2 * ((1.0 / comp) - 1.0)
        pressure = pc * multi
        rows.append((comp, round(pressure, 4)))
    return rows

def gen_gruneisen():
    comps = [round(1.02 - 0.005 * i, 4) for i in range(65)]
    rows = []
    for comp in comps:
        gamma = 1.02 - 0.02 * comp   # nearly constant, ~1.0
        rows.append((comp, round(gamma, 4)))
    return rows

if curve_type == 'isotherm':
    data = gen_isotherm()
    header = ['compression', 'pressure']
elif curve_type == 'hugoniot':
    data = gen_hugoniot()
    header = ['compression', 'pressure']
elif curve_type == 'gruneisen':
    data = gen_gruneisen()
    header = ['compression', 'gamma']
else:
    print(f"Unknown curve type: {curve_type}")
    sys.exit(1)

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
