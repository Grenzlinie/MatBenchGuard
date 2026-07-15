#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bandstructure_results.json ===
cat > "$OUTDIR/bandstructure_results.json" << 'EOF'
{
    "pbe_bandgap": 2.06,
    "hse_bandgap": 3.04,
    "bandgap_type": "indirect",
    "quasi_direct_gap": 3.07,
    "cbm_location": "Gamma",
    "vbm_location": "along Gamma-X"
}
EOF

# === solve block: strain_bandgap.csv ===
python3 -c '
import csv
with open("/app/outputs/strain_bandgap.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["strain_x", "hse_bandgap"])
    writer.writerow([-0.04, 2.80])
    writer.writerow([0.0, 3.04])
    writer.writerow([0.04, 3.12])
'

# === solve block: layer_bandgap.csv ===
python3 -c '
import csv
with open("/app/outputs/layer_bandgap.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n_layers", "hse_bandgap"])
    writer.writerow([1, 3.04])
    writer.writerow([2, 2.858])
    writer.writerow([3, 2.795])
'

# === solve block: piezoelectric_coefficients.csv ===
python3 -c '
import csv
with open("/app/outputs/piezoelectric_coefficients.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n_layers", "e11_2D", "e12_2D", "e11_3D", "e12_3D"])
    writer.writerow([1, 2.23e-10, 0.38e-10, 0.23, 0.0392])
    writer.writerow([2, 4.46e-10, 0.76e-10, 0.23, 0.0392])
    writer.writerow([3, 6.69e-10, 1.14e-10, 0.23, 0.0392])
'
