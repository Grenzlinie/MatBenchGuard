#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: TBC_vs_temperature.csv ===
python3 <<'PYEOF'
import csv

# Approximate experimental TBC values (MW/m²K) from paper Fig. 3(a)
# at temperatures 80,100,150,200,250,300,350,400,450,500 K for each interface.
rows = [
    # Al_sapphire
    (80, 'Al_sapphire', 250),
    (100, 'Al_sapphire', 270),
    (150, 'Al_sapphire', 300),
    (200, 'Al_sapphire', 320),
    (250, 'Al_sapphire', 340),
    (300, 'Al_sapphire', 350),
    (350, 'Al_sapphire', 360),
    (400, 'Al_sapphire', 370),
    (450, 'Al_sapphire', 380),
    (500, 'Al_sapphire', 390),
    # Co_sapphire
    (80, 'Co_sapphire', 230),
    (100, 'Co_sapphire', 260),
    (150, 'Co_sapphire', 290),
    (200, 'Co_sapphire', 320),
    (250, 'Co_sapphire', 350),
    (300, 'Co_sapphire', 370),
    (350, 'Co_sapphire', 400),
    (400, 'Co_sapphire', 430),
    (450, 'Co_sapphire', 460),
    (500, 'Co_sapphire', 500),
    # Ru_sapphire
    (80, 'Ru_sapphire', 200),
    (100, 'Ru_sapphire', 230),
    (150, 'Ru_sapphire', 270),
    (200, 'Ru_sapphire', 290),
    (250, 'Ru_sapphire', 310),
    (300, 'Ru_sapphire', 330),
    (350, 'Ru_sapphire', 350),
    (400, 'Ru_sapphire', 370),
    (450, 'Ru_sapphire', 390),
    (500, 'Ru_sapphire', 410),
]

with open('/app/outputs/TBC_vs_temperature.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'interface', 'TBC'])
    writer.writerows(rows)
PYEOF
