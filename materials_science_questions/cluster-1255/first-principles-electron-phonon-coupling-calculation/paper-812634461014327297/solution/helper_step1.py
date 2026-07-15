import math
import csv
import sys

def f(p, alpha):
    return p**4 * (1.0 - 2.0*alpha/(3.0*p)) - 1.0

def fp(p, alpha):
    return 4.0 * p**3 - 2.0 * alpha * p**2

def newton(alpha):
    # initial guess: for small alpha p~1, for large p ~ 2*alpha/3 + 0.1
    if alpha < 1e-6:
        return 1.0
    p0 = max(1.0, 2.0*alpha/3.0 + 0.1)
    p = p0
    for i in range(100):
        fv = f(p, alpha)
        if abs(fv) < 1e-12:
            break
        fpp = fp(p, alpha)
        if fpp == 0:
            raise RuntimeError("zero derivative")
        p -= fv / fpp
        if p <= 0:
            p = 1e-6
    return p

def compute(alpha):
    p = newton(alpha)
    p2 = p * p
    E0 = -3.0 * (p2 - 1.0) * (p2 + 3.0) / (4.0 * p2)
    # effective mass ratio
    m_star = ( (p2 - 1.0) * (p2*p2 + 2.0*p2 - 2.0) / (p2 + 1.0) ) + 1.0
    return p, E0, m_star

def main():
    alphas = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]
    outfile = '/app/outputs/step_01_results.csv'
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['alpha', 'p', 'E0', 'm_star_over_m'])
        for a in alphas:
            p, E0_val, ms = compute(a)
            writer.writerow([a, p, E0_val, ms])

if __name__ == '__main__':
    main()
