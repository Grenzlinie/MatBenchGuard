import csv, math, sys

writer = csv.writer(sys.stdout)
writer.writerow(["delta", "temperature", "q", "chi_T"])

# delta = 0.10
delta = 0.10
for T in [0.10, 0.20, 0.30]:
    sigma = 0.3 + 0.5 * T
    q = 0.0
    while q <= math.pi + 1e-9:
        chi = math.exp(-(q - math.pi) ** 2 / (2.0 * sigma ** 2))
        writer.writerow([delta, T, round(q, 10), round(chi, 10)])
        q = round(q + 0.02, 10)

# delta = 0.30
delta = 0.30
q_max_map = {0.10: 2.5, 0.20: 2.8, 0.30: 3.0}
for T in [0.10, 0.20, 0.30]:
    q_max = q_max_map[T]
    sigma = 0.3 + 0.3 * T
    q = 0.0
    while q <= math.pi + 1e-9:
        chi = math.exp(-(q - q_max) ** 2 / (2.0 * sigma ** 2))
        writer.writerow([delta, T, round(q, 10), round(chi, 10)])
        q = round(q + 0.02, 10)
