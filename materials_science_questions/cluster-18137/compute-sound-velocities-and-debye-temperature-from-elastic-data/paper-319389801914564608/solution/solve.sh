#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: computed_table.csv ===
cat > /tmp/gen_csv.py << 'PYEOF'
import csv
crystals = [
    ("Au", 19.234, 16.314, 4.195),
    ("Ag", 12.399, 9.367, 4.612),
    ("V", 22.8, 11.9, 4.26),
    ("Nb", 24.6, 13.4, 2.87),
    ("Ta", 26.7, 16.1, 8.25),
    ("Pb", 4.953, 4.229, 1.490),
]
with open("/app/outputs/computed_table.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["crystal", "G0", "K"])
    for name, c11, c12, c44 in crystals:
        a = (c11 - c12) / (2 * c44)
        G0 = c44 * (a ** (0.4))
        K = (c11 + 2 * c12) / 3.0
        writer.writerow([name, G0, K])
PYEOF
python3 /tmp/gen_csv.py
