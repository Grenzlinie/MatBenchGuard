import csv, math, sys, os

def write_actinide(outdir):
    data = [
        ('Th', 3.60, 55),
        ('Pa', 3.44, 60),
        ('U', 3.28, 100),
        ('Np', 3.42, 90),
        ('Pu', 3.42, 35),
        ('Am', 3.61, 40),
        ('Cm', 3.55, 40),
        ('Bk', 3.52, 35),
    ]
    path = os.path.join(outdir, 'actinide_volumes_bulk_moduli.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['element', 'rws_bohr', 'bulk_modulus_gpa'])
        for row in data:
            writer.writerow(row)

def write_dos(outdir):
    path = os.path.join(outdir, 'delta_plutonium_dos.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy_eV', 'dos_states_per_eV_atom'])
        # generate a simple two‑Gaussian DOS (peaks at −2 and +2 eV, width ~1 eV) + small background
        energy_range = [-5.0 + 0.1*i for i in range(101)]  # −5.0 to 5.0 eV, step 0.1
        for e in energy_range:
            a1, mu1, sigma1 = 1.5, -2.0, 1.0
            a2, mu2, sigma2 = 1.5, 2.0, 1.0
            bg = 0.01
            dos = (a1 * math.exp(-((e - mu1) ** 2) / (2 * sigma1 ** 2)) +
                   a2 * math.exp(-((e - mu2) ** 2) / (2 * sigma2 ** 2)) +
                   bg)
            writer.writerow([round(e, 6), round(dos, 6)])

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    outdir = os.environ.get('OUTDIR', '/app/outputs')
    if mode == 'actinide':
        write_actinide(outdir)
    elif mode == 'dos':
        write_dos(outdir)
    else:
        sys.exit(1)
