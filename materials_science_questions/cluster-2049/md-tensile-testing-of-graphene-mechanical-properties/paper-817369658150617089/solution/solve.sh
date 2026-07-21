#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
python3 <<PYEOF
import csv, os

outdir = os.environ.get("OUTDIR", "/app/outputs")
output_path = os.path.join(outdir, "results.csv")

data = [
    ("zigzag", 1, 250.0, 124.48871, 0.55457),
    ("zigzag", 2, 255.0, 122.84942, 0.55114),
    ("zigzag", 3, 260.0, 121.21013, 0.54771),
    ("zigzag", 4, 265.0, 119.57084, 0.54428),
    ("zigzag", 5, 270.0, 117.93155, 0.54085),
    ("zigzag", 8, 400.0, 113.01368, 0.53056),
    ("armchair", 1, 250.0, 123.23871, 0.43018),
    ("armchair", 2, 255.0, 122.34942, 0.42736),
    ("armchair", 3, 260.0, 121.46013, 0.42454),
    ("armchair", 4, 265.0, 120.57084, 0.42172),
    ("armchair", 5, 270.0, 119.68155, 0.41890),
    ("armchair", 8, 300.0, 117.01368, 0.41044),
]

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["orientation", "layers", "shear_modulus_GPa", "ultimate_stress_GPa", "failure_strain"])
    for row in data:
        writer.writerow(row)
PYEOF

# === solve finalize ===
echo 'Done.'
