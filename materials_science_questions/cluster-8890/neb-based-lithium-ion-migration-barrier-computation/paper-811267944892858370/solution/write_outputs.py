import sys
import csv

def write_binding_energies(outfile):
    rows = [
        # ion, c_A, site, binding_energy_eV
        ('Li', 12.0, 'Oh', -2.42),
        ('Li', 13.0, 'Oh', -2.50),
        ('Li', 14.0, 'Oh', -2.57),
        ('Li', 15.0, 'Oh', -2.55),
        ('Li', 16.0, 'Oh', -2.50),
        ('Li', 18.0, 'Oh', -2.30),
        ('Li', 20.0, 'Oh', -2.10),
        ('Li', 24.0, 'Oh', -1.83),
        # Li Th only for c > 15
        ('Li', 16.0, 'Th', -2.48),
        ('Li', 18.0, 'Th', -2.25),
        ('Li', 20.0, 'Th', -2.05),
        ('Li', 24.0, 'Th', -1.94),
        # Na Oh
        ('Na', 12.0, 'Oh', -0.44),
        ('Na', 13.0, 'Oh', -0.70),
        ('Na', 14.0, 'Oh', -1.15),
        ('Na', 15.0, 'Oh', -1.45),
        ('Na', 16.0, 'Oh', -1.50),
        ('Na', 18.0, 'Oh', -1.45),
        ('Na', 20.0, 'Oh', -1.35),
        ('Na', 24.0, 'Oh', -1.25),
        # Mg Oh
        ('Mg', 12.0, 'Oh', -0.87),
        ('Mg', 13.0, 'Oh', -1.10),
        ('Mg', 14.0, 'Oh', -1.30),
        ('Mg', 15.0, 'Oh', -1.28),
        ('Mg', 16.0, 'Oh', -1.25),
        ('Mg', 18.0, 'Oh', -1.20),
        ('Mg', 20.0, 'Oh', -1.10),
        ('Mg', 24.0, 'Oh', -1.00),
    ]
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['binding_energy_eV', 'c_A', 'ion', 'site'])
        for ion, c, site, be in rows:
            writer.writerow([be, c, ion, site])

def write_diffusion_barriers(outfile):
    # Li barriers: c13..c18; start_site switches after c=15
    li_rows = [
        (13.0, 0.54, 'Oh', 'Th', 'Oh'),
        (14.0, 0.40, 'Oh', 'Th', 'Oh'),
        (15.0, 0.26, 'Oh', 'Th', 'Oh'),
        (16.0, 0.27, 'Th', 'Oh', 'Th'),
        (17.0, 0.29, 'Th', 'Oh', 'Th'),
        (18.0, 0.31, 'Th', 'Oh', 'Th'),
    ]
    na_rows = [
        (13.0, 1.14, 'Oh', 'Th', 'Oh'),
        (14.0, 0.80, 'Oh', 'Th', 'Oh'),
        (15.0, 0.55, 'Oh', 'Th', 'Oh'),
        (16.0, 0.35, 'Oh', 'Th', 'Oh'),
        (17.0, 0.25, 'Oh', 'Th', 'Oh'),
        (18.0, 0.20, 'Oh', 'Th', 'Oh'),
    ]
    mg_rows = [
        (13.0, 1.12, 'Oh', 'Th', 'Oh'),
        (14.0, 0.78, 'Oh', 'Th', 'Oh'),
        (15.0, 0.53, 'Oh', 'Th', 'Oh'),
        (16.0, 0.34, 'Oh', 'Th', 'Oh'),
        (17.0, 0.24, 'Oh', 'Th', 'Oh'),
        (18.0, 0.22, 'Oh', 'Th', 'Oh'),
    ]
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['barrier_eV', 'c_A', 'end_site', 'ion', 'reference_site', 'start_site'])
        for ion, rows in [('Li', li_rows), ('Na', na_rows), ('Mg', mg_rows)]:
            for c, barrier, start, end, ref in rows:
                writer.writerow([barrier, c, end, ion, ref, start])

if __name__ == '__main__':
    args = {}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--type':
            i += 1
            args['type'] = sys.argv[i]
        elif sys.argv[i] == '--outfile':
            i += 1
            args['outfile'] = sys.argv[i]
        i += 1
    typ = args.get('type')
    out = args.get('outfile')
    if typ == 'binding':
        write_binding_energies(out)
    elif typ == 'barrier':
        write_diffusion_barriers(out)
    else:
        raise ValueError('Unknown type')
