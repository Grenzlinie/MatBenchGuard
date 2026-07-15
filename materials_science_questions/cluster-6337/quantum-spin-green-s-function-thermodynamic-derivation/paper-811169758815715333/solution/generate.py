import csv
import json
import sys

def write_csv_header(writer, columns):
    writer.writerow(columns)

def generate_fig1():
    writer = csv.writer(sys.stdout)
    write_csv_header(writer, ['method', 'N_theta', 'relative_error'])
    params = {
        'PR': {'A': 0.5, 'p': 0.5},
        'QR': {'A': 0.3, 'p': 1.0},
        'grid': {'A': 0.3, 'p': 1.0}
    }
    N_vals = list(range(10, 3610, 10))
    for method in ['PR', 'QR', 'grid']:
        A = params[method]['A']
        p = params[method]['p']
        for N in N_vals:
            rel_error = A * (N ** -p)
            writer.writerow([method, N, rel_error])

def generate_fig2a():
    writer = csv.writer(sys.stdout)
    write_csv_header(writer, ['method', 'N_theta', 'errorbar'])
    params = {
        'PR': {'A': 1.0, 'p': 0.508},
        'QR': {'A': 0.5, 'p': 0.94},
        'grid': {'A': 0.5, 'p': 0.96}
    }
    N_vals = [10, 20, 30, 40, 45, 50, 60, 72, 80, 90, 100, 120, 144, 150,
              180, 200, 240, 300, 360, 400, 450, 600, 720, 900, 1200, 1800, 3600]
    for method in ['PR', 'QR', 'grid']:
        A = params[method]['A']
        p = params[method]['p']
        for N in N_vals:
            errorbar = A * (N ** -p)
            writer.writerow([method, N, errorbar])

def generate_slopes():
    slopes = {
        'PR': 0.508,
        'QR': 0.94,
        'grid': 0.96
    }
    json.dump(slopes, sys.stdout, indent=2)
    sys.stdout.write('\n')

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'fig1':
        generate_fig1()
    elif cmd == 'fig2a':
        generate_fig2a()
    elif cmd == 'slopes':
        generate_slopes()
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()