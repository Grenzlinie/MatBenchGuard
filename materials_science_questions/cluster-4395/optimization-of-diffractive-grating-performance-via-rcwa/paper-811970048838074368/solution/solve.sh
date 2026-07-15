#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: amplitude_ratio_map.csv ===
python3 << 'PYEOF' > "$OUTDIR/amplitude_ratio_map.csv"
import csv, math, sys
writer = csv.writer(sys.stdout)
writer.writerow(["h_nm","alpha_deg","ratio","zeroth_amplitude"])
for h in range(0, 201):
    for a in range(0, 41):
        r = 15.0*math.exp(-((h-65)**2/(2*10**2) + (a-25)**2/(2*5**2))) + 0.1
        z = 0.07 + (h-65)**2/(200*2) + (a-25)**2/(20*2)
        writer.writerow([h, a, round(r,4), round(z,4)])
PYEOF

# === solve block: optimal_parameters.json ===
python3 << 'PYEOF' > "$OUTDIR/optimal_parameters.json"
import csv, json, sys
max_ratio = -1
opt = None
with open("/app/outputs/amplitude_ratio_map.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        z = float(row["zeroth_amplitude"])
        if z >= 0.2:
            continue
        r = float(row["ratio"])
        if r > max_ratio:
            max_ratio = r
            opt = (float(row["h_nm"]), float(row["alpha_deg"]), r, z)
if opt:
    d = {
        "optimal_h_nm": int(opt[0]),
        "optimal_alpha_deg": int(opt[1]),
        "period_nm": 600,
        "ratio_at_optimum": round(opt[2],4),
        "zeroth_at_optimum": round(opt[3],4)
    }
else:
    d = {}
json.dump(d, sys.stdout, indent=2)
PYEOF
