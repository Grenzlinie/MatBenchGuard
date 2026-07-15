import csv
import math
import sys

def gauss(energy, mu, sigma):
    return math.exp(-0.5 * ((energy - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))

def integrate_trapezoid(energies, values):
    area = 0.0
    n = len(energies)
    for i in range(n - 1):
        de = energies[i + 1] - energies[i]
        area += de * (values[i] + values[i + 1]) / 2.0
    return area

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    dos_type = sys.argv[1]
    outfile = sys.argv[2]

    # uniform energy grid from 0.3 to 0.9 Ryd
    e_start = 0.3
    e_end = 0.9
    npts = 1001
    energies = [e_start + i * (e_end - e_start) / (npts - 1) for i in range(npts)]

    # raw Ti DOS as a sum of Gaussians
    peaks_ti = [(0.42, 0.06), (0.58, 0.08), (0.74, 0.07)]
    weights_ti = [1.2, 1.5, 1.0]
    raw_ti = [sum(w * gauss(e, mu, sig) for (mu, sig), w in zip(peaks_ti, weights_ti)) for e in energies]

    # raw Ru DOS
    peaks_ru = [(0.45, 0.07), (0.60, 0.06), (0.76, 0.05)]
    weights_ru = [1.0, 1.8, 1.2]
    raw_ru = [sum(w * gauss(e, mu, sig) for (mu, sig), w in zip(peaks_ru, weights_ru)) for e in energies]

    # integrate and normalise each to 5 d‑electrons per atom
    area_ti = integrate_trapezoid(energies, raw_ti)
    area_ru = integrate_trapezoid(energies, raw_ru)
    scaled_ti = [v * 5.0 / area_ti for v in raw_ti]
    scaled_ru = [v * 5.0 / area_ru for v in raw_ru]

    if dos_type == 'total':
        dos = [ti + ru for ti, ru in zip(scaled_ti, scaled_ru)]
        headers = ['energy', 'total_DOS']
    elif dos_type == 'ti':
        dos = scaled_ti
        headers = ['energy', 'ldos_Ti']
    elif dos_type == 'ru':
        dos = scaled_ru
        headers = ['energy', 'ldos_Ru']
    else:
        sys.exit(1)

    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for e, d in zip(energies, dos):
            writer.writerow([f"{e:.6f}", f"{d:.6f}"])

if __name__ == "__main__":
    main()