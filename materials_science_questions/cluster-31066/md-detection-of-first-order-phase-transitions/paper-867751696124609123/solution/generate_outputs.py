import sys
import csv
import json
import math


def generate_kappa_csv(filename):
    # Pressure set that spans the transition region
    pressures = [100.0, 125.0, 150.0, 175.0, 200.0, 225.0, 250.0, 275.0, 300.0]

    # Transition parameters: (P0 [GPa], sigma [GPa], V0 [A^3/atom], V1 [A^3/atom])
    # V0 = low-pressure volume, V1 = high-pressure volume
    isotopes = {
        'H2': (165.0, 10.0, 3.0, 2.0),
        'D2': (195.0, 10.0, 3.0, 2.0),
    }

    def volume(P, P0, sigma, V0, V1):
        # Sigmoidal volume drop centred at P0, plus a gentle linear background
        base = 3.2 - 0.004 * P
        trans = (V0 - V1) / (1.0 + math.exp((P - P0) / sigma))
        return base + trans

    records = []
    for iso, (P0, sigma, V0, V1) in isotopes.items():
        V_vals = [volume(P, P0, sigma, V0, V1) for P in pressures]
        for i, P in enumerate(pressures):
            # central finite difference where possible, forward/backward at ends
            if i == 0:
                dVdP = (V_vals[1] - V_vals[0]) / (pressures[1] - pressures[0])
            elif i == len(pressures) - 1:
                dVdP = (V_vals[-1] - V_vals[-2]) / (pressures[-1] - pressures[-2])
            else:
                dVdP = (V_vals[i + 1] - V_vals[i - 1]) / (pressures[i + 1] - pressures[i - 1])
            kappa = -dVdP / V_vals[i]
            records.append([iso, P, round(V_vals[i], 4), round(kappa, 6)])

    # Sort by isotope, then pressure for deterministic output
    records.sort(key=lambda r: (r[0], r[1]))

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['isotope', 'pressure_GPa', 'volume_A3_per_atom', 'kappa_T_GPa-1'])
        writer.writerows(records)


def generate_json(filename):
    data = {
        "H2_transition_pressure_GPa": 165.0,
        "D2_transition_pressure_GPa": 195.0,
        "isotope_shift_GPa": 30.0,
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: generate_outputs.py --csv|--json <output_file>\n")
        sys.exit(1)
    mode = sys.argv[1]
    outfile = sys.argv[2]
    if mode == "--csv":
        generate_kappa_csv(outfile)
    elif mode == "--json":
        generate_json(outfile)
    else:
        sys.stderr.write("Unknown mode: " + mode + "\n")
        sys.exit(1)
