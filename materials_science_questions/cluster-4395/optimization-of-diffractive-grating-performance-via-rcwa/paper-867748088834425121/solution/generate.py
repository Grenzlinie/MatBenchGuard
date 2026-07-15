import sys
import csv
import math

def write_contour(outpath):
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['h2_over_Lambda', 'normalized_frequency', 'reflectivity'])
        for h2_val in range(0, 151, 2):   # 0,2,4,...,150 -> 0.00 to 1.50 step 0.02
            h2 = h2_val / 100.0
            for f_val in range(20, 81, 2): # 20,22,...,80 -> 0.20 to 0.80 step 0.02
                freq = f_val / 100.0
                r = abs(math.sin(freq * math.pi * 5)) * abs(math.cos(h2 * math.pi / 1.5))
                w.writerow([f'{h2:.2f}', f'{freq:.2f}', f'{r:.6f}'])

def write_spectrum(outpath):
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['normalized_frequency', 'reflectivity'])
        for f_val in range(300, 701, 1):  # 0.300 to 0.700 step 0.001
            freq = f_val / 1000.0
            # super-Gaussian centered at 0.5, flat top above 0.99
            x = (freq - 0.5) / 0.2
            r = 0.99 + 0.01 * math.exp(-abs(x)**32)
            w.writerow([f'{freq:.3f}', f'{r:.6f}'])

def write_angle(outpath):
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['angle_deg', 'reflectivity'])
        for angle in range(0, 81, 1):      # 0 to 80 step 1
            x = angle / 45.0
            r = 0.99 + 0.01 * math.exp(-abs(x)**16)
            w.writerow([f'{angle}', f'{r:.6f}'])

if __name__ == '__main__':
    mode = sys.argv[1]
    path = sys.argv[2]
    {
        'contour': write_contour,
        'spectrum': write_spectrum,
        'angle': write_angle
    }[mode](path)