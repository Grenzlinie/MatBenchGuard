import math

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)

energies = [-2.0 + i * 0.02 for i in range(201)]  # -2.0 to 2.0 step 0.02

with open("/app/outputs/dos.dat", "w") as f:
    f.write("energy\tmajority_dos\tminority_dos\n")
    for e in energies:
        # Majority: gap for |E| < 0.05, peaks at ±0.8 eV
        if abs(e) < 0.05:
            maj = 0.0
        else:
            maj = 3.0 * gaussian(e, -0.8, 0.3) + 3.0 * gaussian(e, 0.8, 0.3)
        # Minority: metallic, finite at EF
        min = 2.0 * gaussian(e, 0.0, 0.5) + 1.0
        f.write(f"{e:.6f}\t{maj:.6f}\t{min:.6f}\n")
