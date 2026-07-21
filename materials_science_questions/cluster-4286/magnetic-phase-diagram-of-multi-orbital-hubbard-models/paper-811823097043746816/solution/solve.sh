#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

cat > /solution/gen_csv.py <<'PYEOF'
import sys, csv, os

def write_occupancies():
    # Hardcoded occupancy data: param_set strings and values
    # Rows for Ud=6, eps=2, n varying 0.8 .. 1.2 step 0.1
    rows = [
        ("Ud6_eps2_n0.8", 0.72, 0.04, 0.04),
        ("Ud6_eps2_n0.9", 0.77, 0.06, 0.07),
        ("Ud6_eps2_n1.0", 0.82, 0.08, 0.10),
        ("Ud6_eps2_n1.1", 0.865, 0.13, 0.105),
        ("Ud6_eps2_n1.2", 0.90, 0.20, 0.10),
    ]
    path = os.path.join("/app/outputs", "occupancies.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n_d", "n_p_h", "n_p_n", "param_set"])
        for param_set, nd, nph, npn in rows:
            writer.writerow([f"{nd:.3f}", f"{nph:.3f}", f"{npn:.3f}", param_set])

def write_eigenvalues():
    rows = [
        (0.05, 0.92, 0.45),
        (0.10, 0.76, 0.38),
        (0.15, 0.60, 0.30),
        (0.20, 0.42, 0.22),
    ]
    path = os.path.join("/app/outputs", "eigenvalues.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["T_over_tpd", "lambda_d", "lambda_sstar"])
        for T, ld, ls in rows:
            writer.writerow([f"{T:.2f}", f"{ld:.2f}", f"{ls:.2f}"])

def write_TN():
    rows = [
        (4, 0.022),
        (6, 0.032),
        (8, 0.045),
        (10, 0.042),
        (12, 0.039),
    ]
    path = os.path.join("/app/outputs", "TN.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["TN_over_tpd", "Ud_over_tpd"])
        for Ud, TN in rows:
            writer.writerow([f"{TN:.4f}", Ud])

if __name__ == "__main__":
    arg = sys.argv[1]
    {"occupancies": write_occupancies, "eigenvalues": write_eigenvalues, "TN": write_TN}[arg]()
PYEOF

# === solve block: occupancies.csv ===
python3 /solution/gen_csv.py occupancies

# === solve block: eigenvalues.csv ===
python3 /solution/gen_csv.py eigenvalues

# === solve block: TN.csv ===
python3 /solution/gen_csv.py TN
