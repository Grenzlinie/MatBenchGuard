import csv
import math
import sys

# Standard elemental densities at room temperature (g/cm^3) – public NIST/Wikipedia values.
DENSITY = {
    'Li': 0.534,
    'Na': 0.97,
    'K': 0.89,
    'V': 6.11,
    'Nb': 8.57,
    'Ta': 16.69,
    'Mo': 10.28,
    'W': 19.25,
    'Fe': 7.874,
    'Ca': 1.55,
    'Ni': 8.908,
    'Cu': 8.96,
    'Ag': 10.49,
    'Au': 19.3,
    'Al': 2.70,
    'Pb': 11.34,
    'Pd': 12.023,
    'Pt': 21.45,
    'Ir': 22.56,
    'Be': 1.85,
    'Mg': 1.738,
    'Y': 4.47,
    'Re': 21.02,
    'Ti': 4.51,
    'Zn': 7.14,
    'Cd': 8.65,
    'In': 7.31,
    'Si': 2.33,
    'Ge': 5.323,
}

T = 298.15   # room temperature in K

def compute_alpha(element, cp, cv, B, special_flag):
    rho = DENSITY.get(element)
    if rho is None:
        raise ValueError(f"No density for {element}")
    V = 1.0 / rho   # specific volume in cm^3/g
    # Formula (5): alpha = (1/3) * sqrt((Cp - Cv) / (B * V * T * 1000))
    # B in GPa, V in cm^3/g, so B*V*1000 converts to J/g.
    numerator = cp - cv
    denominator = B * V * T * 1000.0
    if denominator <= 0:
        raise ValueError(f"Non-positive denominator for {element}")
    ratio = numerator / denominator
    if ratio < 0:
        ratio = 0.0   # safeguard, though not expected
    alpha_k = (1.0 / 3.0) * math.sqrt(ratio)
    alpha_per_K = alpha_k * 1e6   # convert to 10^-6 K^-1
    if special_flag:
        alpha_per_K *= 0.5
    return round(alpha_per_K, 6)

def main(output_path):
    rows = []
    with open('/solution/input_params.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            element = row['element'].strip()
            cp = float(row['Cp'])
            cv = float(row['Cv'])
            B = float(row['B'])
            special_flag = row['special_flag'].strip().lower() == 'true'
            alpha = compute_alpha(element, cp, cv, B, special_flag)
            rows.append((element, alpha))
    # Write output
    with open(output_path, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(['element', 'alpha_calc'])
        for element, alpha in rows:
            writer.writerow([element, alpha])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: compute_alphas.py <output_csv>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
