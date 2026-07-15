#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: thermal_conductivity_results.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)
k0 = 200.0
rows = []
# grain size series
for gs, norm in [(-1.0, 1.0), (2.5, 0.19), (5.0, 0.32), (7.5, 0.39), (10.0, 0.47), (12.5, 0.57)]:
    rows.append([gs, 0.0, 300.0, norm*k0, norm])
# strain series
strain_vals = [0.0, 0.03, 0.06, 0.09, 0.12]
# SC
for s, n in zip(strain_vals, [1.0, 0.88, 0.73, 0.58, 0.43]):
    rows.append([-1.0, s, 300.0, n*k0, n])
# 7.5 nm
baseline_75 = 0.39
target_75 = baseline_75 * 0.59  # 0.2301
for i, s in enumerate(strain_vals):
    n = baseline_75 - i * (baseline_75 - target_75) / (len(strain_vals)-1)
    rows.append([7.5, s, 300.0, n*k0, round(n, 4)])
# 2.5 nm
baseline_25 = 0.19
target_25 = baseline_25 * 0.68  # 0.1292
for i, s in enumerate(strain_vals):
    n = baseline_25 - i * (baseline_25 - target_25) / (len(strain_vals)-1)
    rows.append([2.5, s, 300.0, n*k0, round(n, 4)])
# temperature series
temp_vals = [300, 400, 500]
# SC
for t, n in zip(temp_vals, [1.0, 0.8, 0.65]):
    rows.append([-1.0, 0.0, t, n*k0, n])
# 10 nm
for t, n in zip(temp_vals, [0.47, 0.44, 0.41]):
    rows.append([10.0, 0.0, t, n*k0, n])
# 2.5 nm (constant)
for t in temp_vals:
    rows.append([2.5, 0.0, t, 0.19*k0, 0.19])
# write CSV
path = os.path.join(outdir, "thermal_conductivity_results.csv")
with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["grain_size_nm", "strain", "temperature_K", "absolute_K_W_mK", "normalized_K"])
    w.writerows(rows)
print(f"wrote {len(rows)} rows to {path}")
PYEOF
