#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: teg_performance.csv ===
python3 << 'PYEOF'
import csv
import math

output_dir = "/app/outputs"
filename = f"{output_dir}/teg_performance.csv"

# Cold source temperature (K)
Tc = 353.15

# Factor = 1 - Tc/Th
factor = {500.0: 1.0 - Tc/500.0, 800.0: 1.0 - Tc/800.0}

rows = []

# single_bi2te3 at 500 K – paper reports P=2.87 W, η=4.15%
p = 2.87
eta = 4.15
eta_e = eta / factor[500.0]
rows.append(["single_bi2te3", 500.0, p, eta, round(eta_e, 2)])

# single_skutterudite at 500 K – estimated from Fig.3 and Fig.4a
p = 1.2
eta = 2.6
eta_e = eta / factor[500.0]
rows.append(["single_skutterudite", 500.0, p, eta, round(eta_e, 2)])

# serial_two_stage at 500 K – paper states 2.5 W and 3.4%
p = 2.5
eta = 3.4
eta_e = eta / factor[500.0]
rows.append(["serial_two_stage", 500.0, p, eta, round(eta_e, 2)])

# parallel_two_stage at 500 K – estimated from Fig.3 (~2.6 W) and Fig.4a (~3.6%)
p = 2.6
eta = 3.6
eta_e = eta / factor[500.0]
rows.append(["parallel_two_stage", 500.0, p, eta, round(eta_e, 2)])

# single_bi2te3 at 800 K – not applicable (material limit <600 K)
rows.append(["single_bi2te3", 800.0, None, None, None])

# single_skutterudite at 800 K – paper reports 17.18 W and 4.88%
p = 17.18
eta = 4.88
eta_e = eta / factor[800.0]
rows.append(["single_skutterudite", 800.0, p, eta, round(eta_e, 2)])

# serial_two_stage at 800 K – paper reports 19.02 W and 8.11%
p = 19.02
eta = 8.11
eta_e = eta / factor[800.0]
rows.append(["serial_two_stage", 800.0, p, eta, round(eta_e, 2)])

# parallel_two_stage at 800 K – paper reports 19.52 W and 8.34%
p = 19.52
eta = 8.34
eta_e = eta / factor[800.0]
rows.append(["parallel_two_stage", 800.0, p, eta, round(eta_e, 2)])

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["configuration", "T_h", "output_power", "conversion_efficiency", "exergy_efficiency"])
    for row in rows:
        writer.writerow(row)

print(f"Written {len(rows)} rows to {filename}")
PYEOF
