import csv, sys

out = sys.argv[1]
rows = []

# Melting point of AlP
rows.append({"T_K": 2805.15, "x_P": 0.5, "phase_flag": "melting"})

# Al-rich liquidus points (approximate from Fig. 2)
points_al = [
    (933.6, 0.0),
    (973.0, 0.0002),
    (1023.0, 0.0007),
    (1073.0, 0.0015),
    (1123.0, 0.0030),
    (1173.0, 0.0050),
    (1223.0, 0.0080),
    (1273.0, 0.0120),
    (1323.0, 0.0180),
    (1373.0, 0.0260),
    (1423.0, 0.0380),
    (1473.0, 0.0550),
    (1523.0, 0.0780),
    (1573.0, 0.1100),
    (1623.0, 0.1500),
    (1673.0, 0.2000),
    (1723.0, 0.2600),
    (1773.0, 0.3300),
    (1823.0, 0.4000)
]
for T_K, xP in points_al:
    rows.append({"T_K": T_K, "x_P": xP, "phase_flag": "liquidus"})

# P-rich liquidus points (approximate)
points_p = [
    (1823.0, 0.600),
    (1773.0, 0.670),
    (1723.0, 0.750),
    (1673.0, 0.820),
    (1623.0, 0.870),
    (1573.0, 0.910),
    (1523.0, 0.940),
    (1473.0, 0.960),
    (1423.0, 0.975),
    (1373.0, 0.985),
    (1323.0, 0.992),
    (1273.0, 0.996),
    (1223.0, 0.998),
    (1173.0, 0.999)
]
for T_K, xP in points_p:
    rows.append({"T_K": T_K, "x_P": xP, "phase_flag": "liquidus"})

with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=["T_K", "x_P", "phase_flag"])
    w.writeheader()
    w.writerows(rows)
