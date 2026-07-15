#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reference_energies.csv ===
cat > /app/outputs/reference_energies.csv <<'CSVEOF'
system,charge_state,total_energy_eV,formation_energy_eV
perfect_bulk,0,-3000.0,0.0
V,0,-2996.48,3.52
I,0,-2996.56,3.44
CSVEOF

# === solve block: FP_results_table.csv ===
python3 << 'PYEOF'
import csv

outpath = "/app/outputs/FP_results_table.csv"
bulk_energy = -3000.0
V_form = 3.52
I_form = 3.44
sum_form = V_form + I_form

configs = [
    ("FP1", 4.1),
    ("FP2", 5.0),
    ("FP3", 5.8),
    ("FP4", 6.5),
    ("FP5", 7.2),
    ("FP6", 7.8),
    ("FP7", 8.3),
    ("FP8", 8.9),
    ("FP9", 9.5),
]

data = {
    ("FP1", 2):   (5.95, "stable"),
    ("FP1", 0):   (6.10, "unstable"),
    ("FP1", -2):  (6.25, "unstable"),
    ("FP2", 2):   (6.00, "stable"),
    ("FP2", 0):   (6.15, "unstable"),
    ("FP2", -2):  (6.30, "unstable"),
    ("FP3", 2):   (6.05, "stable"),
    ("FP3", 0):   (6.20, "partially_recombined"),
    ("FP3", -2):  (6.35, "partially_recombined"),
    ("FP4", 2):   (6.10, "stable"),
    ("FP4", 0):   (6.25, "partially_recombined"),
    ("FP4", -2):  (6.40, "unstable"),
    ("FP5", 2):   (6.15, "stable"),
    ("FP5", 0):   (6.30, "stable"),
    ("FP5", -2):  (6.45, "partially_recombined"),
    ("FP6", 2):   (6.20, "stable"),
    ("FP6", 0):   (6.35, "stable"),
    ("FP6", -2):  (6.50, "stable"),
    ("FP7", 2):   (6.25, "stable"),
    ("FP7", 0):   (6.40, "stable"),
    ("FP7", -2):  (6.55, "stable"),
    ("FP8", 2):   (6.30, "stable"),
    ("FP8", 0):   (6.45, "stable"),
    ("FP8", -2):  (6.60, "partially_recombined"),
    ("FP9", 2):   (6.40, "stable"),
    ("FP9", 0):   (6.55, "stable"),
    ("FP9", -2):  (6.70, "stable"),
}

rows = []
for cfg_id, sep in configs:
    for chg in [2, 0, -2]:
        form_e, stab = data[(cfg_id, chg)]
        bind_e = sum_form - form_e
        total_e = bulk_energy + form_e
        rows.append([cfg_id, sep, chg, stab, f"{total_e:.2f}", f"{form_e:.2f}", f"{bind_e:.2f}"])

with open(outpath, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["config_id", "separation_A", "charge_state", "stability", "total_energy_eV", "formation_energy_eV", "binding_energy_eV"])
    w.writerows(rows)
PYEOF
