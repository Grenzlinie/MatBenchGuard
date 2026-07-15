import csv, math, sys

writer = csv.writer(sys.stdout)
writer.writerow(["delta", "temperature", "separation_l", "correlation"])

pairs = [
    (0.24, 0.10),
    (0.24, 0.20),
    (0.24, 0.30),
    (0.30, 0.02),
    (0.30, 0.08),
    (0.30, 0.12),
    (0.30, 0.20)
]
for delta, T in pairs:
    if delta < 0.25:
        xi = 5.0 / (1.0 + T)
        for l in range(51):
            corr = math.exp(-l / xi)
            writer.writerow([delta, T, l, round(corr, 10)])
    else:  # delta=0.30
        alpha = math.acos(1.0 / (4.0 * delta))
        xi = 2.0 / (1.0 + T)
        for l in range(51):
            corr = math.exp(-l / xi) * abs(math.cos(alpha * l))
            writer.writerow([delta, T, l, round(corr, 10)])
