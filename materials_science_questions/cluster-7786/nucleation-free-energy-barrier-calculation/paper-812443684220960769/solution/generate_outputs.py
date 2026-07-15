import csv
import math
import sys
import os

OUTDIR = "/app/outputs"
V0 = 5.8e-7

def compute_albon_dunning(c, d):
    return V0 * (1 + c * (d - 1)) * ((1 - c) ** d)

def compute_squeezing(x, d):
    arg = 1 - d * math.sqrt(x)
    if arg <= 0:
        return 0.0
    return V0 * math.sqrt(arg)

def compute_flux_reduction(x):
    return V0 * (1 - x)

def compute_combined(x, d):
    arg = 1 - d * math.sqrt(x)
    if arg <= 0:
        return 0.0
    return V0 * (1 - x) * math.sqrt(arg)

def write_albon_dunning():
    path = os.path.join(OUTDIR, "step_01_albon_dunning_curve.csv")
    d_vals = [2, 6, 10]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['c', 'V_d2', 'V_d6', 'V_d10'])
        for i in range(101):
            c = i / 100.0
            vs = [compute_albon_dunning(c, d) for d in d_vals]
            writer.writerow([f"{c:.2f}"] + [f"{v:.15e}" for v in vs])
    print(f"Wrote {path}")

def write_cabrera_vermilyea():
    path = os.path.join(OUTDIR, "step_02_cabrera_vermilyea_curve.csv")
    d_vals = [2, 5, 10]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'V_squeezing_d2', 'V_squeezing_d5', 'V_squeezing_d10',
                         'V_flux_d2', 'V_flux_d5', 'V_flux_d10',
                         'V_combined_d2', 'V_combined_d5', 'V_combined_d10'])
        for i in range(1001):
            x = i / 1000.0
            squeezing = [compute_squeezing(x, d) for d in d_vals]
            flux = [compute_flux_reduction(x) for d in d_vals]
            combined = [compute_combined(x, d) for d in d_vals]
            row = [f"{x:.3f}"]
            row += [f"{v:.15e}" for v in squeezing]
            row += [f"{v:.15e}" for v in flux]
            row += [f"{v:.15e}" for v in combined]
            writer.writerow(row)
    print(f"Wrote {path}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("step_01", "step_02"):
        print("Usage: generate_outputs.py step_01|step_02", file=sys.stderr)
        sys.exit(1)
    step = sys.argv[1]
    if step == "step_01":
        write_albon_dunning()
    elif step == "step_02":
        write_cabrera_vermilyea()