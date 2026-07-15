#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transition_enthalpy_entropy.json ===
cat > "$OUTDIR/transition_enthalpy_entropy.json" <<'FFEOF'
{
  "delta_H_kJ_per_mol": 5.209,
  "delta_S_J_per_K_per_mol": 19.16
}
FFEOF

# === solve block: glass_transition_deltaCp.json ===
cat > "$OUTDIR/glass_transition_deltaCp.json" <<'FFEOF'
{
  "T_g_K": 163,
  "delta_Cp_J_per_K_per_mol": 25
}
FFEOF

# === solve block: configurational_entropy.csv ===
python3 -c "
import csv
T_trs = 273.0
Tg = 163.0
S_residual = 2.7
S_trs = 19.16
path = '$OUTDIR/configurational_entropy.csv'
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'S_c'])
    for T in range(5, 274):
        if T < Tg:
            S = S_residual
        else:
            frac = (T - Tg) / (T_trs - Tg)
            S = S_residual + (S_trs - S_residual) * frac
        writer.writerow([T, round(S, 4)])
"

# === solve block: residual_configurational_entropy.json ===
cat > "$OUTDIR/residual_configurational_entropy.json" <<'FFEOF'
{
  "S_c_residual_J_per_K_per_mol": 2.7,
  "T_g_K": 163
}
FFEOF

# === solve finalize ===
echo "All oracle outputs written."
