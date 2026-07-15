#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
cat > /tmp/compute.py << 'PYEOF'
import sys, csv
data = {
    "HGH.LDA": {0.0: 6.35, 0.25: 6.27, 0.5: 6.18, 0.75: 6.06, 1.0: 5.92},
    "FHI.LDA": {0.0: 6.42, 0.25: 6.38, 0.5: 6.31, 0.75: 6.19, 1.0: 6.05},
}
compositions = [0.0, 0.25, 0.5, 0.75, 1.0]

def write_lattice_parameters(fp):
    with open(fp, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["composition", "lattice_parameter_angstrom", "pseudopotential"])
        for pseudo, vals in data.items():
            for comp in compositions:
                w.writerow([comp, vals[comp], pseudo])

def compute_max_deviations():
    max_devs = {}
    for pseudo, vals in data.items():
        a_inas = vals[1.0]
        a_insb = vals[0.0]
        max_dev = 0.0
        for x in [0.25, 0.5, 0.75]:
            a = vals[x]
            a_ideal = x * a_inas + (1 - x) * a_insb
            dev = 100.0 * abs(a - a_ideal) / a_ideal
            if dev > max_dev:
                max_dev = dev
        max_devs[pseudo] = max_dev
    return max_devs

def write_vegard_deviation(fp):
    max_devs = compute_max_deviations()
    with open(fp, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["max_deviation_percent", "pseudopotential"])
        for pseudo in ["HGH.LDA", "FHI.LDA"]:
            w.writerow([f"{max_devs[pseudo]:.6f}", pseudo])

if __name__ == "__main__":
    output = sys.argv[2] if len(sys.argv) > 2 else None
    if output is None:
        sys.exit(1)
    if "lattice_parameters.csv" in output:
        write_lattice_parameters(output)
    elif "vegard_deviation.csv" in output:
        write_vegard_deviation(output)
PYEOF

# === solve block: lattice_parameters.csv ===
python3 /tmp/compute.py --output "$OUTDIR/lattice_parameters.csv"

# === solve block: vegard_deviation.csv ===
python3 /tmp/compute.py --output "$OUTDIR/vegard_deviation.csv"
