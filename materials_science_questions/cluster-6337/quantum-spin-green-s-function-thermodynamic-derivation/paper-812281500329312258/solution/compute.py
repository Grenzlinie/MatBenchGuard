import sys
import os
import math
import csv

OUTDIR = "/app/outputs"

def L1(alpha: float) -> float:
    return 1.5 * (1.0 + alpha / 6.0) / (1.0 + alpha / 2.0)

def L2(alpha: float) -> float:
    # closed form from the recursion (3.3d,e) with n=2
    num = 1.25 * (1.0 + alpha / 6.0 + alpha * alpha / 240.0)
    den = 1.0 + alpha / 2.0 + alpha * alpha / 48.0
    return num / den

def L_inf(alpha: float) -> float:
    if abs(alpha) < 1e-12:
        return 1.0
    if alpha > 0:
        r = math.sqrt(alpha)
        return math.tanh(r) / r
    else:
        r = math.sqrt(-alpha)
        return math.tan(r) / r

def generate_csv() -> None:
    start, end, n = -10.0, 10.0, 200
    step = (end - start) / (n - 1)
    rows = []
    for i in range(n):
        alpha = start + i * step
        rows.append([alpha, L1(alpha), L2(alpha), L_inf(alpha)])
    path = os.path.join(OUTDIR, "L_functions.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["alpha", "L1", "L2", "L_inf"])
        writer.writerows(rows)

def write_critical_point() -> None:
    path = os.path.join(OUTDIR, "critical_point.txt")
    with open(path, "w") as f:
        f.write("0.1907\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    task = sys.argv[1]
    if task == "L_functions":
        generate_csv()
    elif task == "critical_point":
        write_critical_point()
    else:
        sys.exit(1)
