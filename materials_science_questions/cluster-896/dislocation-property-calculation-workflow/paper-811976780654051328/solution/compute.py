import sys
import numpy as np
import math

def generate_f(out_csv):
    Nmax = 500
    n1 = np.arange(-Nmax, Nmax+1)
    n2 = np.arange(-Nmax, Nmax+1)
    N1, N2 = np.meshgrid(n1, n2, indexing='ij')
    mask = (N1 != 0) | (N2 != 0)
    denom1 = 2*N1 - N2
    denom2 = N1 - N2
    denom3 = N1 + N2
    safe = (denom1 != 0) & (denom2 != 0) & (denom3 != 0)
    mask = mask & safe
    N1s = N1[mask]
    N2s = N2[mask]
    Nvals = N1s**2 + N2s**2 - N1s*N2s
    N_sqrt = np.sqrt(np.abs(Nvals))
    sin_term = np.sin(np.pi * (N1s + N2s) / 3) ** 2
    denom1v = denom1[mask]
    denom2v = denom2[mask]
    denom3v = denom3[mask]
    term_factor = (Nvals**(1.5) * sin_term) / (denom1v**2 * denom2v**2 * denom3v**2)
    x_vals = np.logspace(-4, 1, 100)
    f_vals = np.zeros_like(x_vals)
    for i, x in enumerate(x_vals):
        f = np.sum(term_factor * np.exp(-4/3 * np.pi * N_sqrt * x))
        f_vals[i] = f
    with open(out_csv, 'w') as fh:
        fh.write('x,f_x\n')
        for x, f in zip(x_vals, f_vals):
            fh.write(f'{x:.12e},{f:.12e}\n')

def compute_critical(out_txt):
    nu = 1.0/3.0
    A_honey = 0.14
    A_two = (4 - 3*nu) / (4 * math.sqrt(3) * math.pi * (1 - nu))
    C1 = math.log(4.5 / math.e)
    C2 = math.log(4*math.pi / (math.sqrt(3)*math.e)) + 1.0/(4 - 3*nu)
    log_theta = (A_two * C2 - A_honey * C1) / (A_honey - A_two)
    theta = math.exp(log_theta)
    with open(out_txt, 'w') as fh:
        fh.write(f'{theta:.6f}\n')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: compute.py --csv out.csv | --txt out.txt')
        sys.exit(1)
    if sys.argv[1] == '--csv':
        generate_f(sys.argv[2])
    elif sys.argv[1] == '--txt':
        compute_critical(sys.argv[2])
    else:
        print('Unknown option')
        sys.exit(1)
