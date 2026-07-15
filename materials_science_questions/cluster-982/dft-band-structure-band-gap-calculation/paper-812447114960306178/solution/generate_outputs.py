import csv
import json
import math
import sys

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def generate_dos_curve(output_path):
    # Define peaks: energy_eV, sigma, amplitude
    peaks = [
        (-6.0, 0.5, 1.0),   # D
        (-4.9, 0.5, 1.0),   # C
        (-2.8, 0.4, 1.2),   # B main
        (-3.1, 0.4, 0.6),   # B shoulder
        (-1.0, 0.4, 1.0),   # A
        (6.8, 0.5, 1.0),    # d
        (7.7, 0.5, 1.0),    # e
        (8.6, 0.5, 0.7),    # f shoulder
        (9.6, 0.5, 1.0),    # f main
        (11.0, 0.5, 1.0),   # g
        (13.3, 0.5, 0.7),   # h shoulder
        (14.4, 0.5, 1.0),   # h main
    ]

    energy_range = (-10.0, 20.0)
    step = 0.01
    num_points = int((energy_range[1] - energy_range[0]) / step) + 1

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy_eV', 'dos'])
        for i in range(num_points):
            e = energy_range[0] + i * step
            dos = 0.0
            for mu, sigma, amp in peaks:
                dos += gaussian(e, mu, sigma, amp)
            writer.writerow([f"{e:.4f}", f"{dos:.6f}"])

def generate_peaks_json(output_path):
    peaks = [
        {"peak": "A", "energy_eV": -1.0},
        {"peak": "B", "energy_eV": -2.8},
        {"peak": "C", "energy_eV": -4.9},
        {"peak": "D", "energy_eV": -6.0},
        {"peak": "d", "energy_eV": 6.8},
        {"peak": "e", "energy_eV": 7.7},
        {"peak": "f", "energy_eV": 9.6},
        {"peak": "g", "energy_eV": 11.0},
        {"peak": "h", "energy_eV": 14.4},
    ]
    with open(output_path, 'w') as f:
        json.dump(peaks, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    if sys.argv[1] == '--dos-curve':
        generate_dos_curve(sys.argv[2])
    elif sys.argv[1] == '--peaks':
        generate_peaks_json(sys.argv[2])
    else:
        sys.exit(1)