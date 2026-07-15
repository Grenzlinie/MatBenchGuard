import csv
import sys

writer = csv.writer(sys.stdout)
writer.writerow(["strain", "stress"])
peak_strain = 0.200
peak_stress = 35.0

# Linear elastic regime up to peak
for i in range(int(peak_strain * 1000) + 1):  # 0.0 to 0.200 inclusive
    strain = i * 0.001
    stress = peak_stress * (strain / peak_strain)
    writer.writerow([f"{strain:.3f}", f"{stress:.3f}"])

# Rapid drop after failure
for strain in [0.201, 0.202, 0.203, 0.204, 0.205, 0.210, 0.220, 0.230, 0.240, 0.250]:
    writer.writerow([f"{strain:.3f}", "-10.000"])
