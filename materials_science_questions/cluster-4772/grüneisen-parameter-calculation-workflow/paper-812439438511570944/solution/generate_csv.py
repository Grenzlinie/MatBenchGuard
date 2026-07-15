import csv, math, sys

params = {
    'Cu': (134.27, 6.0264, 3.7245, -4.9816, 14.720),
    'Ta': (195.24, 3.7159, 8.0846, -64.854, 206.87),
    'Mo': (264.87, 4.7127, -8.1795, 83.532, -189.67),
    'Pt': (280.03, 6.3289, -1.3811, 61.492, -156.48),
    'Au': (177.26, 6.3800, 1.9334, -1.0292, 33.941),
}

def eos_pressure(X, B0, eta, beta, xi, delta):
    X13 = X ** (1/3)
    t = 1 - X13
    t2 = t * t
    t3 = t2 * t
    t4 = t3 * t
    exponent = eta * t + beta * t2 + xi * t3 + delta * t4
    P = 3 * B0 * (t / (X ** (2/3))) * math.exp(exponent)
    return P

def main():
    mode = sys.argv[1]
    if mode == 'data':
        with open('/app/outputs/reduced_isotherm_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for elem, (B0, eta, beta, xi, delta) in params.items():
                X = 0.4
                while X <= 1.0 + 1e-12:
                    P = eos_pressure(X, B0, eta, beta, xi, delta)
                    if P < 0:
                        P = 0.0
                    writer.writerow([elem, X, P])
                    X += 0.01
    elif mode == 'params':
        with open('/app/outputs/reduced_isotherm_parameters.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for elem, (B0, eta, beta, xi, delta) in params.items():
                writer.writerow([elem, B0, eta, beta, xi, delta])
    else:
        raise ValueError("Invalid mode, use 'data' or 'params'")

if __name__ == '__main__':
    main()
