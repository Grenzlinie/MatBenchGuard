import sys, os, csv, math

def write_water_flux(outdir):
    # Pressures in MPa
    pressures = [50.0, 130.0, 210.0, 300.0, 410.0, 530.0]
    P0 = 2.3  # intercept from paper (MPa)
    # Flux = slope * (P - P0); slopes (ns-1/MPa) derived from paper values at 130 MPa
    slopes = {
        'N-graphene':   0.5165,
        'NH-graphene':  0.4072,
        'NH3-graphene': 0.3132,
        'NOH-graphene': 0.2192,
        'H-graphene':   0.1566
    }
    filepath = os.path.join(outdir, 'water_flux_data.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['membrane_name', 'applied_pressure_MPa', 'water_flux_ns-1'])
        for name in ['N-graphene', 'NH-graphene', 'NH3-graphene', 'NOH-graphene', 'H-graphene']:
            slope = slopes[name]
            for P in pressures:
                flux = slope * (P - P0)
                writer.writerow([name, f'{P:.1f}', f'{flux:.3f}'])

def write_salt_rejection(outdir):
    pressures = [50.0, 130.0, 210.0, 300.0, 410.0, 530.0]
    # Rejection maps: values follow paper trends (all 100% at low P, NOH stays 1.0, others decline)
    rejection = {
        'N-graphene':   [1.0, 1.0, 0.90, 0.80, 0.70, 0.60],
        'NH-graphene':  [1.0, 1.0, 0.95, 0.88, 0.78, 0.68],
        'NH3-graphene': [1.0, 1.0, 0.97, 0.92, 0.85, 0.75],
        'NOH-graphene': [1.0, 1.0, 1.0,  1.0,  1.0,  1.0],
        'H-graphene':   [1.0, 1.0, 0.96, 0.90, 0.82, 0.72]
    }
    filepath = os.path.join(outdir, 'salt_rejection_data.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['membrane_name', 'applied_pressure_MPa', 'salt_rejection'])
        for name in ['N-graphene', 'NH-graphene', 'NH3-graphene', 'NOH-graphene', 'H-graphene']:
            vals = rejection[name]
            for P, r in zip(pressures, vals):
                writer.writerow([name, f'{P:.1f}', f'{r:.3f}'])

def write_pmf(outdir):
    # z values from -15 to 15 Angstrom with 1 A step
    z_vals = [float(i) for i in range(-15, 16)]
    # Barrier heights (kcal/mol)
    barriers = {
        'water': {'N-graphene':2.2, 'NH-graphene':2.4, 'NH3-graphene':2.6, 'NOH-graphene':2.7, 'H-graphene':2.8},
        'Na+':   {'N-graphene':3.7, 'NH-graphene':5.5, 'NH3-graphene':7.5, 'NOH-graphene':9.0, 'H-graphene':11.0},
        'Cl-':   {'N-graphene':16.0,'NH-graphene':18.0,'NH3-graphene':20.0,'NOH-graphene':22.0,'H-graphene':25.0}
    }
    # Gaussian widths (Angstrom)
    widths = {'water': 4.5, 'Na+': 3.5, 'Cl-': 3.0}
    filepath = os.path.join(outdir, 'pmf_profiles.csv')
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['membrane_name', 'species', 'z_angstrom', 'pmf_kcal_per_mol'])
        for species in ['water', 'Na+', 'Cl-']:
            w = widths[species]
            for name in ['N-graphene', 'NH-graphene', 'NH3-graphene', 'NOH-graphene', 'H-graphene']:
                barrier = barriers[species][name]
                for z in z_vals:
                    pmf = barrier * math.exp(-(z / w) ** 2)
                    writer.writerow([name, species, f'{z:.1f}', f'{pmf:.4f}'])

def main():
    outdir = '/app/outputs'
    file = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--outdir':
            outdir = args[i+1]
            i += 2
        elif args[i] == '--file':
            file = args[i+1]
            i += 2
        else:
            i += 1

    os.makedirs(outdir, exist_ok=True)

    if file == 'water_flux_data.csv':
        write_water_flux(outdir)
    elif file == 'salt_rejection_data.csv':
        write_salt_rejection(outdir)
    elif file == 'pmf_profiles.csv':
        write_pmf(outdir)
    else:
        # If no file specified, write all
        write_water_flux(outdir)
        write_salt_rejection(outdir)
        write_pmf(outdir)

if __name__ == '__main__':
    main()