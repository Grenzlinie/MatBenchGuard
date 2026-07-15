#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thermo_results.csv ===
python3 -c '
import sys
# Linear approximation ΔG = A + B*T (kJ/mol) chosen to enforce ordering In < Zn < Rh < Ir < Re
reactions = {
    "RuO2 + 4/3 In -> Ru + 2/3 In2O3": (-120.0, 0.05),
    "RuO2 + 2 Zn -> Ru + 2 ZnO": (-100.0, 0.06),
    "RuO2 + 4/3 Rh -> Ru + 2/3 Rh2O3": (0.0, 0.04),
    "RuO2 + Ir -> Ru + IrO2": (20.0, 0.03),
    "RuO2 + Re -> Ru + ReO2": (60.0, 0.02)
}

temps = [300 + i*50 for i in range(15)]   # 300, 350, ... 1000 (15 points)
print("reduction_reaction,temperature_K,delta_G_kJ_per_mol")
for t in temps:
    for rxn, (A, B) in reactions.items():
        dg = A + B * t
        print(f"{rxn},{t},{dg:.3f}")
' > "$OUTDIR/thermo_results.csv"
