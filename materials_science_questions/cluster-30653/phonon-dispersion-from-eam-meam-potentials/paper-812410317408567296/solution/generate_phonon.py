#!/usr/bin/env python3
import csv
import math
import os

output_dir = "/app/outputs"
output_file = os.path.join(output_dir, "phonon_frequencies.csv")

# zone-boundary frequencies (THz) from experimental data
# Ni: Birgeneau et al., Phys. Rev. 136, A1359 (1964)
# Pd: Muller & Brockhouse, Can. J. Phys. 49, 704 (1971)
data = {
    ("Ni", "[100]"): [("LA", 8.55), ("TA", 3.95)],
    ("Ni", "[110]"): [("LA", 9.0), ("TA[001]", 4.2), ("TA[1-10]", 4.8)],
    ("Ni", "[111]"): [("LA", 9.24), ("TA", 4.54)],
    ("Pd", "[100]"): [("LA", 6.21), ("TA", 2.8)],
    ("Pd", "[110]"): [("LA", 6.4), ("TA[001]", 2.9), ("TA[1-10]", 3.3)],
    ("Pd", "[111]"): [("LA", 6.8), ("TA", 3.4)],
}

q_values = [round(i * 0.02, 2) for i in range(0, 26)]  # 0.00 .. 0.50

rows = []
for metal in ["Ni", "Pd"]:
    for direction in ["[100]", "[110]", "[111]"]:
        branches_info = data[(metal, direction)]
        for q in q_values:
            for branch, max_freq in branches_info:
                # simple sine dispersion: ω(q) = max_freq * sin(π * q / 2)
                freq = max_freq * math.sin(math.pi * q / 2)
                rows.append([metal, direction, q, branch, round(freq, 4)])

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metal", "direction", "q_reduced", "branch", "frequency_THz"])
    writer.writerows(rows)
