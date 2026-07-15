import sys
import numpy as np
from scipy.integrate import nquad
from scipy.special import i0e, i1e, ive
import csv, io, warnings


def compute_gc(lam, d):
    if lam == 0.0:
        return 4.0 * d   # exact result
    s_c = d * (1.0 + lam) / 2.0

    def integrand(u, theta):
        if u == 0.0:
            return 0.0
        sin2 = np.sin(theta) ** 2
        cos2 = np.cos(theta) ** 2
        rho = u * ((1.0 + lam) / 2.0 * sin2 + (1.0 - lam) / 2.0 * cos2)
        i0 = i0e(rho)
        i1 = i1e(rho)
        i2 = ive(2, rho)
        ratio1 = i1 / i0
        ratio2 = i2 / i0
        fac = i0 ** d
        exp_factor = np.exp(-u * d * lam * cos2)
        term1 = s_c ** 2
        term2 = d * (d - 1.0) * (1.0 - lam ** 2) / 4.0 * ratio1 ** 2
        term3 = d * (1.0 - lam ** 2) / 8.0 * (1.0 + ratio2)
        bracket = term1 - term2 - term3
        return 2.0 * fac * exp_factor * bracket

    # integrate over u (0, inf) then theta (0, pi/2) (nquad: last range innermost)
    ranges = [[0.0, np.inf], [0.0, np.pi / 2.0]]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        D, _ = nquad(integrand, ranges, opts=[{'limit': 200, 'epsabs': 1e-8, 'epsrel': 1e-8},
                                               {'limit': 200, 'epsabs': 1e-8, 'epsrel': 1e-8}])
    gc = np.pi ** 2 * d ** 3 * (1.0 + lam) ** 3 / (D ** 2)
    return gc


def main():
    tasks = []
    # d = 2, lambda = 0.0 .. 1.0 step 0.1
    for lam in [x/10.0 for x in range(0, 11)]:
        tasks.append((lam, 2.0))
    # d = 1.5
    for lam in [0.0, 0.1]:
        tasks.append((lam, 1.5))
    # d = 2.1
    for lam in [0.0, 0.1]:
        tasks.append((lam, 2.1))

    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(['lambda', 'd', 'g_c'])
    for lam, d in tasks:
        gc = compute_gc(lam, d)
        writer.writerow([lam, d, gc])
    sys.stdout.write(out.getvalue())

if __name__ == '__main__':
    main()
