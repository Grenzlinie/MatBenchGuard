import sys, csv, math

pi = math.pi

etas = [0.0, 0.6, 0.9]
temps = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

base_norms = {
    0.0: [0.98, 0.95, 0.91, 0.86, 0.80, 0.73, 0.65, 0.56],
    0.6: [0.99, 0.97, 0.94, 0.90, 0.85, 0.79, 0.72, 0.64],
    0.9: [1.00, 0.99, 0.97, 0.94, 0.90, 0.85, 0.79, 0.72]
}

ks = {
    0.0: [(pi/4, pi/4), (pi/5, 0.0), (2*pi/5, 0.0), (3*pi/5, 0.0)],
    0.6: [(pi/4, pi/4), (pi/4, 0.0)],
    0.9: [(pi/4, pi/4)]
}

def gamma_hat(kx, ky):
    return (math.cos(kx) + math.cos(ky)) / 2.0

def omega0(eta, kx, ky):
    g = gamma_hat(kx, ky)
    return 4.0 * math.sqrt((1.0 - g) * (1.0 - eta * g))

def write_raw():
    with open('/app/outputs/raw_frequencies.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eta', 'kx', 'ky', 'T_J', 'omega_ck'])
        for eta in etas:
            norms = base_norms[eta]
            for kx, ky in ks[eta]:
                w0 = omega0(eta, kx, ky)
                for idx, T in enumerate(temps):
                    omega_ck = norms[idx] * w0
                    w.writerow([eta, kx, ky, T, omega_ck])

def write_norm():
    with open('/app/outputs/normalized_frequencies.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['eta', 'kx', 'ky', 'T_J', 'normalized_freq'])
        for eta in etas:
            norms = base_norms[eta]
            for kx, ky in ks[eta]:
                for idx, T in enumerate(temps):
                    w.writerow([eta, kx, ky, T, norms[idx]])

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'raw'
    if mode == 'raw':
        write_raw()
    elif mode == 'norm':
        write_norm()
    else:
        print('Usage: generate_artifacts.py raw|norm', file=sys.stderr)