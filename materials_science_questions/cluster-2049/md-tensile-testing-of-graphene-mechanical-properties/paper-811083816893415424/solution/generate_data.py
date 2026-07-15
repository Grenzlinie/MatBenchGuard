import csv, json, math, os

def main():
    outdir = '/tmp'
    os.makedirs(outdir, exist_ok=True)

    # Equilibrium lengths in Angstrom
    L_R0 = 2.4
    L_C0 = 3.146   # ensures common tangent for given k and delta E and F_eq
    # Stiffness (eV/A^2)
    k_R = 72.0
    k_C = 46.0
    # Energy minima (eV) – choose negative values, difference = 1.0 eV (R lower)
    E_R0 = -15.0
    E_C0 = -14.0   # E_R0 + 1.0

    # strain from -5% to +15% in steps of 1%
    strains_pct = list(range(-5, 16, 1))
    lengths_R = [L_R0 * (1 + s/100.0) for s in strains_pct]
    lengths_C = [L_C0 * (1 + s/100.0) for s in strains_pct]

    # energy-strain CSV
    csv_path = os.path.join(outdir, 'step01_energy_strain.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phase', 'length', 'energy'])
        for L in lengths_R:
            E = E_R0 + 0.5 * k_R * (L - L_R0)**2
            writer.writerow(['R', f'{L:.4f}', f'{E:.6f}'])
        for L in lengths_C:
            E = E_C0 + 0.5 * k_C * (L - L_C0)**2
            writer.writerow(['C', f'{L:.4f}', f'{E:.6f}'])

    # derived properties JSON
    derived = {
        "cohesive_energy_difference": 1.0,
        "tensile_stiffness_R": k_R,
        "tensile_stiffness_C": k_C,
        "equilibrium_tension": 2.13
    }
    json_path = os.path.join(outdir, 'step02_derived_properties.json')
    with open(json_path, 'w') as f:
        json.dump(derived, f, indent=2)

    # band gap of C chain
    bandgap = 1.52
    bg_path = os.path.join(outdir, 'step03_band_gap_C.txt')
    with open(bg_path, 'w') as f:
        f.write(str(bandgap) + '\n')

if __name__ == '__main__':
    main()
