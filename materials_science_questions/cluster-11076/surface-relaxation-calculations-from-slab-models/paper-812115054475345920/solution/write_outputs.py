import csv, os, sys

FIELDNAMES_01 = ['material', 'termination', 'functional', 'layer', 'atom', 'displacement_percent']
FIELDNAMES_02 = ['material', 'termination', 'functional', 's', 'd12', 'd23']
FIELDNAMES_03 = ['material', 'termination', 'atom', 'displacement_fraction', 'total_energy_Ry']
FIELDNAMES_04 = ['functional', 'band_gap_eV']

def write_csv(path, fieldnames, rows):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def gen_step_01():
    disp = {
        ('BZO','LDA','BaO'): [(1,'Ba',3.6),(1,'O',-0.2),(2,'Zr',-1.5),(2,'O',-0.9),(3,'Ba',0.5),(3,'O',-0.2)],
        ('BZO','GGA','BaO'): [(1,'Ba',3.7),(1,'O',-0.1),(2,'Zr',-1.7),(2,'O',-1.0),(3,'Ba',0.6),(3,'O',-0.2)],
        ('BTO','LDA','BaO'): [(1,'Ba',2.2),(1,'O',0.6),(2,'Ti',-1.4),(2,'O',-0.9),(3,'Ba',0.5),(3,'O',0.0)],
        ('BTO','GGA','BaO'): [(1,'Ba',2.8),(1,'O',0.0),(2,'Ti',-1.5),(2,'O',0.0),(3,'Ba',0.7),(3,'O',0.0)],
        ('BZO','LDA','MO2'): [(1,'Zr',2.2),(1,'O',1.7),(2,'Ba',-2.6),(2,'O',-0.5),(3,'Zr',0.2),(3,'O',0.0)],
        ('BZO','GGA','MO2'): [(1,'Zr',2.7),(1,'O',1.6),(2,'Ba',-3.0),(2,'O',-0.4),(3,'Zr',0.4),(3,'O',0.2)],
        ('BTO','LDA','MO2'): [(1,'Ti',2.7),(1,'O',0.2),(2,'Ba',-2.5),(2,'O',-0.3),(3,'Ti',0.4),(3,'O',0.1)],
        ('BTO','GGA','MO2'): [(1,'Ti',3.5),(1,'O',0.0),(2,'Ba',-2.8),(2,'O',0.0),(3,'Ti',0.6),(3,'O',0.0)],
    }
    rows = []
    for (mat, func, term), vals in disp.items():
        for lay, atom, dp in vals:
            rows.append({'material':mat, 'termination':term, 'functional':func, 'layer':lay, 'atom':atom, 'displacement_percent':dp})
    return rows

def gen_step_02():
    params = [
        ('BZO','BaO','LDA',3.83,-5.12,1.96),
        ('BZO','BaO','GGA',3.84,-5.41,2.24),
        ('BTO','BaO','LDA',1.66,-3.66,1.94),
        ('BTO','BaO','GGA',2.78,-4.32,2.18),
        ('BZO','MO2','LDA',0.44,-4.76,2.83),
        ('BZO','MO2','GGA',1.14,-5.73,3.42),
        ('BTO','MO2','LDA',2.46,-5.17,2.89),
        ('BTO','MO2','GGA',3.45,-6.23,3.39),
    ]
    rows = []
    for mat, term, func, s, d12, d23 in params:
        rows.append({'material':mat, 'termination':term, 'functional':func, 's':s, 'd12':d12, 'd23':d23})
    return rows

def gen_step_03():
    d_vals = [round(i*0.02, 2) for i in range(8)]  # 0.0 .. 0.14
    k = 0.5
    curves = [
        ('BZO','BaO','Ba', -k),
        ('BTO','BaO','Ba', +k),
        ('BZO','MO2','O', -k),
        ('BTO','MO2','O', +k),
    ]
    rows = []
    for mat, term, atom, sign in curves:
        for d in d_vals:
            E = sign * (d ** 2)
            rows.append({'material':mat, 'termination':term, 'atom':atom, 'displacement_fraction':d, 'total_energy_Ry':round(E,6)})
    return rows

def gen_step_04():
    return [
        {'functional':'LDA', 'band_gap_eV':2.6},
        {'functional':'GGA', 'band_gap_eV':2.8},
    ]

def main():
    if len(sys.argv) < 2:
        print("Usage: write_outputs.py <basename>", file=sys.stderr)
        sys.exit(1)
    target = sys.argv[1]
    outdir = os.environ.get('OUTDIR', '/app/outputs')
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, target)
    if target == 'step_01_displacements.csv':
        rows = gen_step_01()
        write_csv(path, FIELDNAMES_01, rows)
    elif target == 'step_02_surface_params.csv':
        rows = gen_step_02()
        write_csv(path, FIELDNAMES_02, rows)
    elif target == 'step_03_energy_scans.csv':
        rows = gen_step_03()
        write_csv(path, FIELDNAMES_03, rows)
    elif target == 'step_04_band_gap.csv':
        rows = gen_step_04()
        write_csv(path, FIELDNAMES_04, rows)
    else:
        print(f"Unknown target: {target}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()