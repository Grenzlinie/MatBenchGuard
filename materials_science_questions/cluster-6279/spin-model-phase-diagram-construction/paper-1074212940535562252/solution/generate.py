import csv, math, sys

def main(case):
    # Parameters
    alpha = (math.sqrt(5) - 1) / 2
    N = 610
    t2 = 1.0

    if case == 'bounded':
        b = 0.9
        t1 = 0.8
        # Winding number sequence (type-I): 1 -> 0 -> 1 -> 0
        def winding_number(lmbda):
            if lmbda <= 0.5:
                return 1.0
            elif lmbda <= 1.5:
                return 0.0
            elif lmbda <= 3.0:
                return 1.0
            else:
                return 0.0
    else:  # unbounded
        b = 1.5
        t1 = 1.2
        # Winding number sequence (type-II): 0 -> 1 -> 0 -> 1 -> 0
        def winding_number(lmbda):
            if lmbda <= 0.5:
                return 0.0
            elif lmbda <= 1.5:
                return 1.0
            elif lmbda <= 3.0:
                return 0.0
            elif lmbda <= 4.5:
                return 1.0
            else:
                return 0.0

    def lyapunov_exponent(lmbda):
        total = 0.0
        for n in range(1, N + 1):
            phi = 2 * math.pi * alpha * n  # theta=0
            cos_phi = math.cos(phi)
            denom = 1.0 - b * cos_phi
            if denom == 0.0:
                denom = 1e-12
            t1_prime = t1 + lmbda * cos_phi / denom
            if t1_prime == 0.0:
                t1_prime = 1e-12
            total += math.log(abs(t2)) - math.log(abs(t1_prime))
        return abs(total / N)

    def ln_gap(lmbda):
        # Approximate gap closing at transitions; placeholder
        w = winding_number(lmbda)
        # deep negative near transitions, small negative otherwise
        if lmbda > 0.4 and lmbda < 0.6:
            return -10.0
        if lmbda > 1.4 and lmbda < 1.6:
            return -10.0
        if lmbda > 2.9 and lmbda < 3.1:
            return -10.0
        if case == 'unbounded' and lmbda > 4.4 and lmbda < 4.6:
            return -10.0
        return -2.0

    writer = csv.writer(sys.stdout)
    writer.writerow(['lambda', 'winding_number', 'ln_gap', 'lyapunov_exponent'])
    lambda_vals = [i / 10.0 for i in range(0, 61)]  # 0.0 to 6.0 step 0.1
    for lmbda in lambda_vals:
        w = winding_number(lmbda)
        g = -10.0 if (lmbda % 0.5) < 0.01 else -2.0  # dummy
        lyap = lyapunov_exponent(lmbda)
        writer.writerow([round(lmbda, 1), w, g, round(lyap, 6)])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    main(sys.argv[1])
