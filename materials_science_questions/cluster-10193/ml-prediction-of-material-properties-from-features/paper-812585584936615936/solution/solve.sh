#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_counts.csv ===
python3 << 'PYEOF'
import csv

with open('/app/outputs/step_01_counts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['prototype', 'total_generated', 'after_symmetry', 'after_neutrality', 'after_stability'])
    data = [
        ('BN', 420, 420, 319, 20),
        ('GeSe', 420, 420, 319, 79),
        ('BiTeI', 4200, 4200, 3735, 1249),
        ('CdI₂', 4200, 2310, 2048, 409),
        ('GeS₂', 4200, 2310, 2048, 70),
        ('MoS₂', 4200, 2310, 2048, 214),
        ('MoSSe', 4200, 4200, 3735, 1211),
        ('AuSe', 176400, 97020, 69576, 3871),
        ('CH', 176400, 49665, 35607, 3020),
        ('FeSe', 176400, 49665, 35607, 551),
        ('GaS', 176400, 49665, 35607, 29),
        ('GaSe', 176400, 49665, 35607, 136),
        ('ISb', 176400, 49665, 35607, 4923),
        ('NiSe', 176400, 49665, 35607, 203),
        ('PbS', 176400, 49665, 35607, 3852),
        ('PbSe', 176400, 49665, 35607, 0),
        ('RhO', 176400, 176400, 127651, 0),
        ('SnS', 176400, 49665, 35607, 0),
        ('FeOCl', 17640000, 2731575, 2621992, 16932),
        ('MnS₂', 17640000, 2731575, 2621992, 0),
        ('PdS₂', 17640000, 2731575, 2621992, 19411),
        ('WTe₂', 17640000, 1390620, 1334218, 260325),
    ]
    for row in data:
        writer.writerow(row)
    # Total row
    totals = (
        'Total',
        sum(r[1] for r in data),
        sum(r[2] for r in data),
        sum(r[3] for r in data),
        sum(r[4] for r in data),
    )
    writer.writerow(totals)
PYEOF
