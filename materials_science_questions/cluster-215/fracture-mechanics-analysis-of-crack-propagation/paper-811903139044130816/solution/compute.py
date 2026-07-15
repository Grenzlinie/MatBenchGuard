import sys
import csv
import math

EPSILON = 1e6

def gen_mode2():
    ps = [0.5, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
    # n from 0.2 to 4.0 inclusive, step 0.2 -> 20 points
    ns = [0.2 + i*0.2 for i in range(20)]
    writer = csv.writer(sys.stdout)
    writer.writerow(['n', 'parameter_R_over_epsilon_d', 'sigma_Pa'])
    for p in ps:
        for n in ns:
            # σ/ε = ((n+1)*p / n)**(n/(n+1))
            factor = ((n+1)*p / n) ** (n/(n+1))
            sigma = EPSILON * factor
            writer.writerow([n, p, sigma])

def f_lambda(lmbda, n):
    """Return (λ-1)^(n+1)/√λ"""
    if lmbda <= 1:
        return 0.0
    return (lmbda - 1)**(n+1) / math.sqrt(lmbda)

def solve_lambda(p2, n):
    target = (n+1) * p2
    lo = 1.000000001
    up = 1.1
    # expand upper bound until f(up) >= target
    while f_lambda(up, n) < target:
        up *= 2.0
        if up > 1e9:
            break
    # bisection
    for _ in range(200):
        mid = (lo + up) / 2.0
        if f_lambda(mid, n) < target:
            lo = mid
        else:
            up = mid
    return (lo + up) / 2.0

def gen_tension():
    k = 3.0
    epsilon = EPSILON
    # two parameter sets
    p2_set1 = 5000.0 / (2.0 * k * 0.001 * epsilon)   # c=1 mm
    p2_set2 = 500.0  / (2.0 * k * 0.01  * epsilon)   # c=10 mm
    ns = [0.2, 0.5, 1, 2, 4]
    writer = csv.writer(sys.stdout)
    writer.writerow(['n', 'parameter_R_over_2kc_epsilon', 'sigma_Pa'])
    for p2 in (p2_set1, p2_set2):
        for n in ns:
            lam = solve_lambda(p2, n)
            sigma = epsilon * (lam - 1)**n
            writer.writerow([n, p2, sigma])

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'mode2':
        gen_mode2()
    elif mode == 'tension':
        gen_tension()
    else:
        raise SystemExit('unknown mode')
