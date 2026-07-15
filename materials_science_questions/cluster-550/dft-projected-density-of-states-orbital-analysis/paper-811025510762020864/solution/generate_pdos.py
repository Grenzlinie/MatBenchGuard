import sys, csv, math

def gaussian(x, center, sigma, amplitude):
    return amplitude * math.exp(-((x - center) ** 2) / (2.0 * sigma * sigma))

compositions = [0, 25, 50, 75]
energy_min = -8.0
energy_max = 5.0
step = 0.02

if sys.argv[1] == "co3d":
    # Co 3d PDOS: peak at EF (0 eV) for x=25, smaller elsewhere
    def co3d_0(x):
        return 0.0
    def co3d_25(x):
        return gaussian(x, 0.0, 0.4, 6.0) + gaussian(x, -2.0, 0.5, 2.0)
    def co3d_50(x):
        return gaussian(x, 0.1, 0.5, 3.0)
    def co3d_75(x):
        return gaussian(x, 0.2, 0.5, 2.0)
    funcs = {0: co3d_0, 25: co3d_25, 50: co3d_50, 75: co3d_75}
    outfile = "/app/outputs/pdos_co3d.csv"
elif sys.argv[1] == "pd4d":
    # Pd 4d PDOS: single Gaussian with FWHM increasing with x
    def pd4d_0(x):
        return gaussian(x, -2.5, 1.5, 10.0)
    def pd4d_25(x):
        return gaussian(x, -2.5, 1.8, 10.0)
    def pd4d_50(x):
        return gaussian(x, -2.5, 2.1, 10.0)
    def pd4d_75(x):
        return gaussian(x, -2.5, 2.4, 10.0)
    funcs = {0: pd4d_0, 25: pd4d_25, 50: pd4d_50, 75: pd4d_75}
    outfile = "/app/outputs/pdos_pd4d.csv"
else:
    raise ValueError("Invalid argument, expected co3d or pd4d")

with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["composition", "energy_ev", "dos"])
    for comp in compositions:
        func = funcs[comp]
        x = energy_min
        while x <= energy_max + step/2:  # ensure last point included
            dos = func(x)
            writer.writerow([comp, f"{x:.8f}", f"{dos:.8f}"])
            x += step
            x = round(x, 10)  # avoid floating point drift
