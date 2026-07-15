#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: frequencies_fg_cntrc.csv ===
cat <<'PYEOF' > /tmp/write_csv.py
import csv, sys

ROWS = [
    # SSSS
    ("SSSS", "spherical", "UD", 0.11, 20.2381),
    ("SSSS", "spherical", "UD", 0.14, 21.6551),
    ("SSSS", "spherical", "UD", 0.17, 25.0512),
    ("SSSS", "spherical", "FG-A", 0.11, 18.2514),
    ("SSSS", "spherical", "FG-A", 0.14, 19.5458),
    ("SSSS", "spherical", "FG-A", 0.17, 22.6250),
    ("SSSS", "spherical", "FG-V", 0.11, 18.5425),
    ("SSSS", "spherical", "FG-V", 0.14, 19.7789),
    ("SSSS", "spherical", "FG-V", 0.17, 22.9514),
    ("SSSS", "spherical", "FG-X", 0.11, 22.4320),
    ("SSSS", "spherical", "FG-X", 0.14, 23.9965),
    ("SSSS", "spherical", "FG-X", 0.17, 27.8827),
    ("SSSS", "spherical", "FG-O", 0.11, 17.1397),
    ("SSSS", "spherical", "FG-O", 0.14, 18.2670),
    ("SSSS", "spherical", "FG-O", 0.17, 21.2115),

    ("SSSS", "hyperbolic_paraboloid", "UD", 0.11, 17.1058),
    ("SSSS", "hyperbolic_paraboloid", "UD", 0.14, 18.6256),
    ("SSSS", "hyperbolic_paraboloid", "UD", 0.17, 21.0947),
    ("SSSS", "hyperbolic_paraboloid", "FG-A", 0.11, 15.0240),
    ("SSSS", "hyperbolic_paraboloid", "FG-A", 0.14, 16.4007),
    ("SSSS", "hyperbolic_paraboloid", "FG-A", 0.17, 18.4751),
    ("SSSS", "hyperbolic_paraboloid", "FG-V", 0.11, 14.8094),
    ("SSSS", "hyperbolic_paraboloid", "FG-V", 0.14, 16.1809),
    ("SSSS", "hyperbolic_paraboloid", "FG-V", 0.17, 18.2249),
    ("SSSS", "hyperbolic_paraboloid", "FG-X", 0.11, 19.5876),
    ("SSSS", "hyperbolic_paraboloid", "FG-X", 0.14, 21.2249),
    ("SSSS", "hyperbolic_paraboloid", "FG-X", 0.17, 24.2735),
    ("SSSS", "hyperbolic_paraboloid", "FG-O", 0.11, 13.3643),
    ("SSSS", "hyperbolic_paraboloid", "FG-O", 0.14, 14.6095),
    ("SSSS", "hyperbolic_paraboloid", "FG-O", 0.17, 16.3892),

    ("SSSS", "cylindrical", "UD", 0.11, 18.1263),
    ("SSSS", "cylindrical", "UD", 0.14, 19.6278),
    ("SSSS", "cylindrical", "UD", 0.17, 22.3797),
    ("SSSS", "cylindrical", "FG-A", 0.11, 15.9890),
    ("SSSS", "cylindrical", "FG-A", 0.14, 17.3575),
    ("SSSS", "cylindrical", "FG-A", 0.17, 19.7184),
    ("SSSS", "cylindrical", "FG-V", 0.11, 16.0598),
    ("SSSS", "cylindrical", "FG-V", 0.14, 17.3905),
    ("SSSS", "cylindrical", "FG-V", 0.17, 19.7991),
    ("SSSS", "cylindrical", "FG-X", 0.11, 20.5479),
    ("SSSS", "cylindrical", "FG-X", 0.14, 22.1792),
    ("SSSS", "cylindrical", "FG-X", 0.17, 25.4877),
    ("SSSS", "cylindrical", "FG-O", 0.11, 14.5525),
    ("SSSS", "cylindrical", "FG-O", 0.14, 15.7660),
    ("SSSS", "cylindrical", "FG-O", 0.17, 17.9030),

    ("SSSS", "plate", "UD", 0.11, 18.0075),
    ("SSSS", "plate", "UD", 0.14, 19.6082),
    ("SSSS", "plate", "UD", 0.17, 22.2068),
    ("SSSS", "plate", "FG-A", 0.11, 15.7011),
    ("SSSS", "plate", "FG-A", 0.14, 17.1474),
    ("SSSS", "plate", "FG-A", 0.17, 19.3150),
    ("SSSS", "plate", "FG-V", 0.11, 15.7011),
    ("SSSS", "plate", "FG-V", 0.14, 17.1474),
    ("SSSS", "plate", "FG-V", 0.17, 19.3150),
    ("SSSS", "plate", "FG-X", 0.11, 20.6235),
    ("SSSS", "plate", "FG-X", 0.14, 22.3489),
    ("SSSS", "plate", "FG-X", 0.17, 25.5574),
    ("SSSS", "plate", "FG-O", 0.11, 14.0683),
    ("SSSS", "plate", "FG-O", 0.14, 15.3782),
    ("SSSS", "plate", "FG-O", 0.17, 17.2523),

    # CCCC
    ("CCCC", "spherical", "UD", 0.11, 59.9319),
    ("CCCC", "spherical", "UD", 0.14, 62.2918),
    ("CCCC", "spherical", "UD", 0.17, 74.6296),
    ("CCCC", "spherical", "FG-A", 0.11, 57.4229),
    ("CCCC", "spherical", "FG-A", 0.14, 60.0434),
    ("CCCC", "spherical", "FG-A", 0.17, 71.5722),
    ("CCCC", "spherical", "FG-V", 0.11, 56.9472),
    ("CCCC", "spherical", "FG-V", 0.14, 59.5914),
    ("CCCC", "spherical", "FG-V", 0.17, 70.9702),
    ("CCCC", "spherical", "FG-X", 0.11, 62.5277),
    ("CCCC", "spherical", "FG-X", 0.14, 64.8258),
    ("CCCC", "spherical", "FG-X", 0.17, 78.2783),
    ("CCCC", "spherical", "FG-O", 0.11, 54.6717),
    ("CCCC", "spherical", "FG-O", 0.14, 57.4414),
    ("CCCC", "spherical", "FG-O", 0.17, 67.9988),

    ("CCCC", "hyperbolic_paraboloid", "UD", 0.11, 59.6090),
    ("CCCC", "hyperbolic_paraboloid", "UD", 0.14, 61.9647),
    ("CCCC", "hyperbolic_paraboloid", "UD", 0.17, 74.2247),
    ("CCCC", "hyperbolic_paraboloid", "FG-A", 0.11, 56.9421),
    ("CCCC", "hyperbolic_paraboloid", "FG-A", 0.14, 59.5777),
    ("CCCC", "hyperbolic_paraboloid", "FG-A", 0.17, 70.9719),
    ("CCCC", "hyperbolic_paraboloid", "FG-V", 0.11, 56.7639),
    ("CCCC", "hyperbolic_paraboloid", "FG-V", 0.14, 59.3858),
    ("CCCC", "hyperbolic_paraboloid", "FG-V", 0.17, 70.7321),
    ("CCCC", "hyperbolic_paraboloid", "FG-X", 0.11, 62.2114),
    ("CCCC", "hyperbolic_paraboloid", "FG-X", 0.14, 64.5039),
    ("CCCC", "hyperbolic_paraboloid", "FG-X", 0.17, 77.8808),
    ("CCCC", "hyperbolic_paraboloid", "FG-O", 0.11, 54.3285),
    ("CCCC", "hyperbolic_paraboloid", "FG-O", 0.14, 57.0957),
    ("CCCC", "hyperbolic_paraboloid", "FG-O", 0.17, 67.5645),

    ("CCCC", "cylindrical", "UD", 0.11, 59.0812),
    ("CCCC", "cylindrical", "UD", 0.14, 61.4458),
    ("CCCC", "cylindrical", "UD", 0.17, 73.5657),
    ("CCCC", "cylindrical", "FG-A", 0.11, 56.4491),
    ("CCCC", "cylindrical", "FG-A", 0.14, 59.0868),
    ("CCCC", "cylindrical", "FG-A", 0.17, 70.3475),
    ("CCCC", "cylindrical", "FG-V", 0.11, 56.1259),
    ("CCCC", "cylindrical", "FG-V", 0.14, 58.7678),
    ("CCCC", "cylindrical", "FG-V", 0.17, 69.9307),
    ("CCCC", "cylindrical", "FG-X", 0.11, 61.7106),
    ("CCCC", "cylindrical", "FG-X", 0.14, 64.0080),
    ("CCCC", "cylindrical", "FG-X", 0.17, 77.2529),
    ("CCCC", "cylindrical", "FG-O", 0.11, 53.7283),
    ("CCCC", "cylindrical", "FG-O", 0.14, 56.5105),
    ("CCCC", "cylindrical", "FG-O", 0.17, 66.8066),

    ("CCCC", "plate", "UD", 0.11, 28.9498),
    ("CCCC", "plate", "UD", 0.14, 30.4349),
    ("CCCC", "plate", "UD", 0.17, 35.9558),
    ("CCCC", "plate", "FG-A", 0.11, 26.9086),
    ("CCCC", "plate", "FG-A", 0.14, 28.5217),
    ("CCCC", "plate", "FG-A", 0.17, 33.3914),
    ("CCCC", "plate", "FG-V", 0.11, 26.9086),
    ("CCCC", "plate", "FG-V", 0.14, 28.5217),
    ("CCCC", "plate", "FG-V", 0.17, 33.3914),
    ("CCCC", "plate", "FG-X", 0.11, 30.8924),
    ("CCCC", "plate", "FG-X", 0.14, 32.3018),
    ("CCCC", "plate", "FG-X", 0.17, 38.6177),
    ("CCCC", "plate", "FG-O", 0.11, 25.1242),
    ("CCCC", "plate", "FG-O", 0.14, 26.7648),
    ("CCCC", "plate", "FG-O", 0.17, 31.0656),
]

with open("/app/outputs/frequencies_fg_cntrc.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["boundary_condition", "geometry_type", "CNT_distribution", "V_star", "frequency"])
    w.writerows(ROWS)
print("CSV written with", len(ROWS), "rows")
PYEOF
python3 /tmp/write_csv.py
