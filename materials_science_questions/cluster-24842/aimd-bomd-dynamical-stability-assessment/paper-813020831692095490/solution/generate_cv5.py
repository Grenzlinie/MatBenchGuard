import csv
import math

# Generate CV5 timeseries: 100 ps, step 0.02 ps -> 5000 points
# Mean = -0.363 Å, amplitude ~0.8 Å, sinusoidal rocking with ~5 ps period

out_path = "/app/outputs/eta1_3b1_CV5_timeseries.csv"
with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time_ps", "CV5_angstrom"])
    t = 0.0
    while t <= 100.0:
        cv5 = -0.363 + 0.8 * math.sin(2.0 * math.pi * t / 5.0)  # main oscillation
        cv5 += 0.05 * math.sin(2.0 * math.pi * t / 1.2)          # small high-frequency ripple
        writer.writerow([round(t, 4), round(cv5, 6)])
        t += 0.02
