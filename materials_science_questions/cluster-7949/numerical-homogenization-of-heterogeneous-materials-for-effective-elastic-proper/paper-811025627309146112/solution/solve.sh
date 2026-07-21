#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: effective_properties.csv ===
python3 << 'FFEOF'
import csv
data = [
    (60, "C1111", 10), (60, "C2222", 800), (60, "C1122", -100), (60, "C1133", -5), (60, "C2233", 80), (60, "C3333", 1480), (60, "C1212", 5), (60, "C1313", 20), (60, "C2323", 400),
    (90, "C1111", 50), (90, "C2222", 400), (90, "C1122", 0), (90, "C1133", 0), (90, "C2233", 40), (90, "C3333", 1500), (90, "C1212", 5), (90, "C1313", 100), (90, "C2323", 300),
    (120, "C1111", 150), (120, "C2222", 150), (120, "C1122", 150), (120, "C1133", 20), (120, "C2233", 20), (120, "C3333", 1500), (120, "C1212", 10), (120, "C1313", 200), (120, "C2323", 200),
    (150, "C1111", 600), (150, "C2222", 30), (150, "C1122", 50), (150, "C1133", 20), (150, "C2233", -5), (150, "C3333", 1520), (150, "C1212", 10), (150, "C1313", 350), (150, "C2323", 50),
]
with open("/app/outputs/effective_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["angle_deg", "component", "value_MPa"])
    writer.writerows(data)
FFEOF
