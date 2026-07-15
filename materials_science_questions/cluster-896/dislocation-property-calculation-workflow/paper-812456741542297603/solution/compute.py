import sys
import csv
import numpy as np


def alpha(eps, delta):
    r = np.sqrt(eps**2 + delta**2)
    a = np.sqrt(r + delta)
    b = np.sqrt(r - delta)
    return 0.5 * (a * (1 + 1j) - b * (1 - 1j))


def compute_W(z, eps, delta):
    al = alpha(eps, delta)
    denom = 1j * delta + eps
    C1 = (1 - np.exp(-al)) / (2 * np.sinh(al) * denom)
    C2 = (np.exp(al) - 1) / (2 * np.sinh(al) * denom)
    return C1 * np.exp(al * np.array(z, dtype=complex)) + C2 * np.exp(-al * np.array(z, dtype=complex)) - 1 / denom


def compute_amplitude(eps, delta, z):
    W = compute_W(z, eps, delta)
    U = np.real(W)
    V = np.imag(W)
    amp = np.abs(W)
    return U, V, amp


def write_shape_csv(eps, delta, outfile):
    z = np.linspace(0, 1, 1000)
    U, V, amp = compute_amplitude(eps, delta, z)
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z', 'U', 'V', 'amplitude'])
        for i in range(len(z)):
            writer.writerow([z[i], U[i], V[i], amp[i]])


delta_values = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100]


def write_delta_sweep(eps, outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['delta', 'max_amplitude'])
        for delta in delta_values:
            _, _, amp = compute_amplitude(eps, delta, 0.5)
            writer.writerow([delta, amp])


epsilon_values = [0.1, 1, 5, 10, 20, 50, 100]


def write_epsilon_sweep(delta, outfile):
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['epsilon', 'max_amplitude'])
        for eps in epsilon_values:
            _, _, amp = compute_amplitude(eps, delta, 0.5)
            writer.writerow([eps, amp])


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'shape':
        eps = float(sys.argv[2])
        delta = float(sys.argv[3])
        out = sys.argv[4]
        write_shape_csv(eps, delta, out)
    elif mode == 'delta_sweep':
        eps = float(sys.argv[2])
        out = sys.argv[3]
        write_delta_sweep(eps, out)
    elif mode == 'epsilon_sweep':
        delta = float(sys.argv[2])
        out = sys.argv[3]
        write_epsilon_sweep(delta, out)
    else:
        raise ValueError("unknown mode")
