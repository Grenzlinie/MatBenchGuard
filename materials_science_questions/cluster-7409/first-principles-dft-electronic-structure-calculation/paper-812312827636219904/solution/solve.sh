#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dos_LTO.csv ===
python3 << 'PYEOF'
import csv, math

def dos_lto(energy):
    vb = 50.0 * math.exp(-(energy + 2.0)**2 / (2 * 0.2**2))
    cb = 30.0 * math.exp(-(energy - 1.6)**2 / (2 * 0.2**2))
    return vb + cb

energies = [round(-5.0 + i*0.01, 6) for i in range(1001)]
rows = [[str(energy), f"{dos_lto(energy):.6f}"] for energy in energies]

with open('/app/outputs/dos_LTO.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'dos_total'])
    writer.writerows(rows)
PYEOF

# === solve block: dos_LMTZO_Ov.csv ===
python3 << 'PYEOF'
import csv, math

def dos_lmtzo_ov(energy):
    vb = 50.0 * math.exp(-(energy + 2.0)**2 / (2 * 0.2**2))
    cb = 40.0 * math.exp(-(energy)**2 / (2 * 0.15**2))
    return vb + cb

energies = [round(-5.0 + i*0.01, 6) for i in range(1001)]
rows = [[str(energy), f"{dos_lmtzo_ov(energy):.6f}"] for energy in energies]

with open('/app/outputs/dos_LMTZO_Ov.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'dos_total'])
    writer.writerows(rows)
PYEOF

# === solve block: migration_barriers.json ===
echo '{"LMTZO": 0.415, "LMTZO_Ov": 0.345}' > /app/outputs/migration_barriers.json
