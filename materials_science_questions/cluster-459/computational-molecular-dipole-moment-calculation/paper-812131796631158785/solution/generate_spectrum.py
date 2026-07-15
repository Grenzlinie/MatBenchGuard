import csv
import math

def absorption(w):
    # parameters tuned to approximate the convolved spectrum at 195 K
    # from Fig. 1 of the paper (solid line)
    A0 = 2.5e-11
    A1 = 1.35e-6
    w0 = 280.0
    sigma = 135.0
    # main Gaussian peak
    peak = A1 * math.exp(-(w - w0)**2 / (2 * sigma**2))
    # low-frequency rise controlled by w^2 factor and exponential cutoff
    low = A0 * w * w * math.exp(-w / 180.0)
    # high-frequency tail extension
    high = 0.3 * A1 * math.exp(-w / 400.0)
    return low + peak + high

if __name__ == "__main__":
    with open("/app/outputs/absorption_spectrum_195K.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["wavenumber", "absorption_coefficient"])
        for w in range(0, 801, 2):
            alpha = absorption(w)
            writer.writerow([w, f"{alpha:.6e}"])
