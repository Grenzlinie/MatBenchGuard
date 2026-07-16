import math, sys

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))

energies = [i * 0.001 - 0.5 for i in range(1001)]  # -0.5 to 0.5 Ryd
baseline = 1.0
amp = 3.0
width = 0.05
center1 = -0.1
center2 = 0.1

with open(sys.argv[1], 'w') as f:
    for e in energies:
        dos = baseline + amp * math.exp(-((e - center1) / width)**2) + amp * math.exp(-((e - center2) / width)**2)
        f.write(f"{e:.7f} {dos:.7f}\n")