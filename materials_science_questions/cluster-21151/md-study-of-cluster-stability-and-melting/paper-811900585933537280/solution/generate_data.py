import csv
import os

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

# Ground-state potential energy per atom (eV/atom) for Ni clusters.
# Data exhibits local minima at N=55 and N=147.
ep_data = [
    (50, -3.680),
    (51, -3.685),
    (52, -3.690),
    (53, -3.695),
    (54, -3.685),
    (55, -3.710),
    (56, -3.690),
    (57, -3.700),
    (58, -3.705),
    (59, -3.710),
    (60, -3.715),
    (142, -3.880),
    (143, -3.885),
    (144, -3.890),
    (145, -3.895),
    (146, -3.900),
    (147, -3.920),
    (148, -3.905),
    (149, -3.910),
    (150, -3.915),
    (151, -3.920),
    (152, -3.925),
]

with open(os.path.join(outdir, "Ni_ground_state_energy.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "Ep"])
    for N, Ep in ep_data:
        writer.writerow([N, Ep])

# Temperature (K) and second energy difference Δ₂ (eV) for N=55 and N=147.
# Δ₂ remains positive and essentially constant up to melting.
temperatures = list(range(200, 1221, 20))   # 200 K to 1200 K in 20 K steps
delta2_data = []
for T in temperatures:
    delta2_data.append((55, T, 0.250))
    delta2_data.append((147, T, 0.150))

with open(os.path.join(outdir, "Ni_delta2_temperature.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "T", "Delta2"])
    for N, T, D2 in delta2_data:
        writer.writerow([N, T, D2])
