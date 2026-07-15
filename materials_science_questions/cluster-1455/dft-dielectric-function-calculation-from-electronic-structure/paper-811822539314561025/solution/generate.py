import sys
import csv
import math

def generate(output_file, eps2_peak, peak_eV, eps1_0):
    epsilon_inf = 1.0
    omega0 = peak_eV
    A = (eps1_0 - epsilon_inf) * (omega0 ** 2)
    gamma = A / (eps2_peak * omega0)

    def eps1(w):
        return epsilon_inf + A * (omega0**2 - w**2) / ((omega0**2 - w**2)**2 + (gamma * w)**2)

    def eps2(w):
        return A * gamma * w / ((omega0**2 - w**2)**2 + (gamma * w)**2)

    energies = [0.0]
    step = 0.02
    current = step
    while current <= 15.0:
        energies.append(current)
        current = round(current + step, 5)
    if peak_eV not in energies:
        energies.append(peak_eV)
    energies.sort()

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy_eV', 'epsilon1', 'epsilon2'])
        for e in energies:
            writer.writerow([e, eps1(e), eps2(e)])

if __name__ == '__main__':
    generate(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
