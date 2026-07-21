import math, csv, sys

writer = csv.writer(sys.stdout)
writer.writerow(["radial_bin", "local_mag"])

# 21 radial bins from 0.0 to 2.0 nm
for i in range(21):
    r = i * 0.1
    # monotonic decrease: cos profile from centre (1.0) to surface (~0.7)
    mag = 0.85 + 0.15 * math.cos(math.pi * r / 2.0)
    writer.writerow([round(r, 1), round(mag, 6)])
