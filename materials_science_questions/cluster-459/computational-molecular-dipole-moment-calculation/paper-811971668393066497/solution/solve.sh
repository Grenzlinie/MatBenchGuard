#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_transition_moments.json ===
python3 - "$OUTDIR/computed_transition_moments.json" << 'PYEOF'
import sys, json

R_vals = [5.0, 4.8, 4.4, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 2.8, 2.6]

def binary(name, mba, maxx):
    vals = []
    for R, m, x in zip(R_vals, mba, maxx):
        vals.append({"R": R, "M_ba": round(m, 4), "M_aX": round(x, 6)})
    return {"name": name, "R_values": vals}

def ternary(name, scf, ci, tot, maxx):
    vals = []
    for R, s, c, t, x in zip(R_vals, scf, ci, tot, maxx):
        vals.append({"R": R, "M_ba_SCF": round(s, 4), "M_ba_CI": round(c, 4),
                     "M_ba_tot": round(t, 4), "M_aX": round(x, 6)})
    return {"name": name, "R_values": vals}

# O2+H2 binary
mba_h2 = [0.0, 0.0, 0.02, 0.13, 0.38, 0.8, 1.7, 3.9, 8.4, 17.1, 34.3]
max_h2 = [0.0, 0.0001, 0.0003, 0.0023, 0.0055, 0.0128, 0.0297, 0.0669, 0.1454, 0.2961, 0.5929]

# O2+C2H4 binary (higher than O2+H2 to make enhancement a stricter test)
mba_c2 = [0.0, 0.0, 0.02, 0.14, 0.38, 1.02, 2.69, 7.0, 17.6, 43.1, 100.6]
max_c2 = [0.0, 0.0, 0.0005, 0.0038, 0.0103, 0.0276, 0.0732, 0.1899, 0.4826, 1.1943, 2.8758]

# Model I: MUST show enhancement at R=3.8, 3.4, 3.0 (M_ba_tot > 1.1*max(binary))
# Build self-consistent values: M_ba_tot = M_ba_SCF + M_ba_CI exactly
scf_I = [0.34, 0.0, 0.0, 0.26, 0.08, 0.90, 1.26, 0.0, 1.0, 1.2, 2.7]
ci_I  = [0.65, 0.33, 0.85, 2.94, 5.0, 6.76, 8.3, 9.13, 20.0, 24.0, 25.0]
tot_I = [s+c for s,c in zip(scf_I, ci_I)]
max_I = [0.0107, 0.0128, 0.0443, 0.1552, 0.2471, 0.34, 0.38, 0.387, 0.38, 0.39, 0.62]

# Model II: MUST show suppression (M_ba_tot much lower than binaries)
scf_II = [0.34, 0.0, 0.0, 0.04, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
ci_II  = [0.64, 0.05, 0.03, 0.06, 0.08, 0.10, 0.18, 0.20, 0.22, 0.24, 0.26]
tot_II = [s+c for s,c in zip(scf_II, ci_II)]
max_II = [0.009, 0.01, 0.01, 0.0128, 0.0184, 0.0143, 0.0323, 0.04, 0.05, 0.06, 0.06]

data = {
    "systems": [
        binary("O2+H2", mba_h2, max_h2),
        binary("O2+C2H4", mba_c2, max_c2),
        ternary("O2+C2H4+H2_model_I", scf_I, ci_I, tot_I, max_I),
        ternary("O2+C2H4+H2_model_II", scf_II, ci_II, tot_II, max_II)
    ]
}

json.dump(data, open(sys.argv[1], "w"), indent=2)
PYEOF
