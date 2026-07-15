import sys
import math

def generate(model):
    e_min, e_max, de = -10.0, 10.0, 0.05
    n = int((e_max - e_min) / de) + 1

    if model == "slab":
        vbm = -3.0
        cbm = 2.5
        gap_peaks = []
    elif model == "isolated":
        vbm = -3.0
        cbm = 2.5
        gap_peaks = [(0.0, 0.15, 3.0)]  # center, sigma, amplitude
    elif model == "two":
        vbm = -3.0
        cbm = 2.5
        gap_peaks = []
    elif model == "three":
        vbm = -3.0
        cbm = 2.5
        gap_peaks = [(-0.8, 0.15, 2.0), (0.3, 0.15, 2.0)]
    else:
        raise ValueError("Unknown model")

    band_sigma = 2.0
    valence_center = vbm - 2.0
    conduction_center = cbm + 2.0
    background = 0.01

    for i in range(n):
        e = e_min + i * de
        if e < vbm or e > cbm:
            band = 5.0 * (math.exp(-0.5 * ((e - valence_center) / band_sigma) ** 2) +
                          math.exp(-0.5 * ((e - conduction_center) / band_sigma) ** 2))
        else:
            band = 0.0
        gp = 0.0
        for cen, sig, amp in gap_peaks:
            gp += amp * math.exp(-0.5 * ((e - cen) / sig) ** 2)
        dos = band + gp + background
        print(f"{e:.6f},{dos:.6f}")

if __name__ == "__main__":
    model = sys.argv[1]
    generate(model)
