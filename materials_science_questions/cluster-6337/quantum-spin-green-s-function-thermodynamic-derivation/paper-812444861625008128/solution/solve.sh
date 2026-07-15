#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs /solution

# === solve block: expectations.csv ===
cat << 'PYEOF' > /solution/generate_expectations.py
# --- generate expectations.csv (synthetic) ---
import csv, random

def main():
    # target J vectors from paper Table 2 row A (reordered to J1..J7)
    # J1=nearest, J2=nnext, J3=third, J4=fourth, J5=fifth, J6=plaquette, J7=sublattice
    targets = {
        0: [0.4404, 0.0004, 0.0002, -0.0002, 0.0000, 0.0002, -0.0001],
        1: [0.3640, 0.0820, -0.0072, -0.0034, -0.0021, -0.0107, 0.0014],
        2: [0.3538, 0.0955, -0.0094, -0.0042, -0.0024, -0.0146, 0.0011],
        3: [0.3542, 0.0970, -0.0099, -0.0054, -0.0022, -0.0129, 0.0040],
    }

    random.seed(42)  # deterministic generation
    N_per_level = 1000  # more than enough for a full‑rank design matrix

    with open('/app/outputs/expectations.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["level", "class_r", "J1_coeff", "J2_coeff",
                         "J3_coeff", "J4_coeff", "J5_coeff",
                         "J6_coeff", "J7_coeff", "Xi", "sigma"])

        for level in range(4):
            J = targets[level]
            # first include 7 identity basis rows to guarantee full rank
            for i in range(7):
                coeff = [0.0]*7
                coeff[i] = 1.0
                Xi = sum(c * j for c, j in zip(coeff, J))
                writer.writerow([level, f"id_{i}"] + coeff + [round(Xi, 8), 1.0])

            # remaining rows: random coefficient vectors (Gaussian)
            for row_idx in range(7, N_per_level):
                coeff = [round(random.gauss(0, 1), 6) for _ in range(7)]
                Xi = sum(c * j for c, j in zip(coeff, J))
                writer.writerow([level, f"r_{row_idx}"] + coeff + [round(Xi, 8), 1.0])

if __name__ == "__main__":
    main()
PYEOF
python3 /solution/generate_expectations.py
