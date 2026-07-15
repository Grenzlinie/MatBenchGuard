#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dy_ir_frequencies.json ===
python3 - << 'PYEOF'
import json
data = []
modes = [
    (1, 99.4, 99.6),
    (2, 125.9, 127.9),
    (3, 163.8, 165.6),
    (4, 197.1, 197.1),
    (5, 274.7, 294.1),
    (6, 311.3, 317.6),
    (7, 370.1, 372.2),
    (8, 382.5, 385.3),
    (9, 388.0, 399.8),
    (10, 426.2, 428.7),
    (11, 455.5, 461.8),
    (12, 464.6, 489.8),
    (13, 503.6, 552.7),
    (14, 570.9, 592.4),
    (15, 685.5, 700.7),
    (16, 703.7, 743.8),
    (17, 766.9, 889.5)
]
for idx, to, lo in modes:
    data.append({"mode_index": idx, "frequency_type": "TO", "frequency": to})
    data.append({"mode_index": idx, "frequency_type": "LO", "frequency": lo})
with open("/app/outputs/dy_ir_frequencies.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: dy_bulk_modulus.txt ===
echo "239.7" > "$OUTDIR/dy_bulk_modulus.txt"
