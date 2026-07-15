import csv, math, sys

def gaussian(x, x0, amp, sigma):
    return amp * math.exp(-(x-x0)**2 / (2*sigma**2))

def main(atom_type, outpath):
    wavenums = list(range(1, 4001))
    intensity = [0.01] * len(wavenums)   # small baseline

    if atom_type == "oxygen":
        peaks = [
            (87,  1.0, 15),
            (152, 0.5, 20),
            (277, 0.8, 25),
            (334, 0.7, 25),
            (392, 1.2, 20),
            (495, 0.9, 30),
        ]
    else:   # hydrogen
        peaks = [
            (778,  0.6, 25),
            (1014, 1.0, 20),
            (2932, 1.5, 50),
            (3464, 1.2, 50),
        ]

    for x0, amp, sigma in peaks:
        for i, w in enumerate(wavenums):
            intensity[i] += gaussian(w, x0, amp, sigma)

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["wavenumber_cm1", "intensity"])
        for w, intens in zip(wavenums, intensity):
            writer.writerow([w, round(intens, 6)])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])