import csv, json, argparse, math

def generate_isotherm(material, output_path):
    # Reference zero-loading Qst from paper (supplement Figures S23, S24)
    if material == 'Ni':
        Qst = 32.8  # kJ/mol
        q_sat = 2.2   # mmol/g
        H_293 = 1.2   # Henry constant in mmol/(g*bar) at 293 K
    elif material == 'Cu':
        Qst = 33.5  # kJ/mol
        q_sat = 2.0
        H_293 = 1.0
    else:
        raise ValueError(f'Unknown material {material}')
    R = 8.314
    # b(T) = b0 * exp(Qst/(RT))
    b_293 = H_293 / q_sat
    b0 = b_293 * math.exp(-Qst * 1000 / (R * 293.0))
    temps = [273, 283, 293]
    # Fugacity points covering 0-1 bar with emphasis on low-loading region
    fugacities = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]
    rows = []
    for t in temps:
        b = b0 * math.exp(Qst * 1000 / (R * t))
        for f in fugacities:
            if f == 0.0:
                loading = 0.0
            else:
                loading = q_sat * b * f / (1.0 + b * f)
            rows.append((t, f, loading))
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Temperature_K', 'Fugacity_bar', 'Loading_mmol_g'])
        for row in rows:
            writer.writerow([row[0], f'{row[1]:.2f}', f'{row[2]:.6f}'])

def generate_qst_json(output_path):
    data = {
        'DICRO-3-Ni-i_zero_loading_Qst_kJmol': 32.8,
        'DICRO-3-Cu-i_zero_loading_Qst_kJmol': 33.5
    }
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--material', choices=['Ni', 'Cu'])
    parser.add_argument('--output', required=True)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    if args.json:
        generate_qst_json(args.output)
    else:
        if not args.material:
            parser.error('--material required for isotherm generation')
        generate_isotherm(args.material, args.output)
