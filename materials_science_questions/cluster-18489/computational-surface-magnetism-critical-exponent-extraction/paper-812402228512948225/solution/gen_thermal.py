import math, csv, sys

writer = csv.writer(sys.stdout)
writer.writerow(["temperature", "core_mag", "surf_mag", "specific_heat"])

temps = list(range(10, 951, 20))
for T in temps:
    # core magnetisation: drops around ~450 K
    core_mag = 1.0 / (1.0 + math.exp((T - 450.0) / 100.0))
    # surface magnetisation: lower and drops much earlier (~150 K)
    surf_mag = 0.8 / (1.0 + math.exp((T - 150.0) / 30.0))
    # specific heat: broad peak where surface disorder sets in, minor bump at core transition
    C = 0.1 * math.exp(-((T - 180.0) / 80.0) ** 2) + 0.02 * math.exp(-((T - 650.0) / 200.0) ** 2) + 0.005
    writer.writerow([T, round(core_mag, 6), round(surf_mag, 6), round(C, 6)])
