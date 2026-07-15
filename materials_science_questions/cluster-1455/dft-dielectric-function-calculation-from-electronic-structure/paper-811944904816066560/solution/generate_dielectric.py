import csv
import math

outfile = "/app/outputs/dielectric_function.csv"

# Two Lorentz oscillators:
#   Strong peak at ~5 eV (amplitude 20, width 2 eV)
#   Small peak at ~30 eV (amplitude 5, width 5 eV)
peaks = [
    {"e0": 5.0,  "A": 20.0, "gamma": 2.0},
    {"e0": 30.0, "A":  5.0, "gamma": 5.0}
]

def epsilon(e):
    """Return (eps1, eps2) using a Lorentz oscillator model."""
    eps1 = 1.0
    eps2 = 0.0
    # Avoid division by zero at e=0; we will handle e=0 separately later
    if e <= 0.0:
        # static limit: eps2=0, eps1 = 1 + sum(A / e0^2)
        for p in peaks:
            eps1 += p["A"] / (p["e0"] ** 2)
        return eps1, 0.0
    for p in peaks:
        e0 = p["e0"]
        A  = p["A"]
        g  = p["gamma"]
        denom = (e0**2 - e**2)**2 + (g * e)**2
        eps2 += (A * g * e) / denom
        eps1 += A * (e0**2 - e**2) / denom
    return eps1, eps2

energies = [0.1 * i for i in range(0, 401)]  # 0.0, 0.1, ..., 40.0

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy (eV)", "epsilon1", "epsilon2"])
    for e in energies:
        eps1, eps2 = epsilon(e)
        # avoid small negative eps2 due to numerical noise
        if eps2 < 1e-12:
            eps2 = 0.0
        writer.writerow([f"{e:.6f}", f"{eps1:.6f}", f"{eps2:.6f}"])
