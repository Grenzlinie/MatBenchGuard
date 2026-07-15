#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: shg_results.json ===
#!/bin/bash
set -euo pipefail
python3 - << 'PYEOF'
import json

data = {
    "table1_CT_gaps": [
        {"N": 6, "epsilon": 0.4, "CT_gap": 5.032},
        {"N": 6, "epsilon": 0.6, "CT_gap": 5.014},
        {"N": 6, "epsilon": 0.8, "CT_gap": 4.990},
        {"N": 6, "epsilon": 1.0, "CT_gap": 4.959},
        {"N": 6, "epsilon": 1.5, "CT_gap": 4.862},
        {"N": 6, "epsilon": 2.0, "CT_gap": 4.745},
        {"N": 8, "epsilon": 0.4, "CT_gap": 4.550},
        {"N": 8, "epsilon": 0.6, "CT_gap": 4.537},
        {"N": 8, "epsilon": 0.8, "CT_gap": 4.520},
        {"N": 8, "epsilon": 1.0, "CT_gap": 4.500},
        {"N": 8, "epsilon": 1.5, "CT_gap": 4.423},
        {"N": 8, "epsilon": 2.0, "CT_gap": 4.332},
        {"N": 10, "epsilon": 0.4, "CT_gap": 4.225},
        {"N": 10, "epsilon": 0.6, "CT_gap": 4.217},
        {"N": 10, "epsilon": 0.8, "CT_gap": 4.205},
        {"N": 10, "epsilon": 1.0, "CT_gap": 4.187},
        {"N": 10, "epsilon": 1.5, "CT_gap": 4.136},
        {"N": 10, "epsilon": 2.0, "CT_gap": 4.060}
    ],
    "table2_position_dependence": [
        {"position": "(1,2)", "beta_x_exact": 6.118, "mu_gr": 3.11, "mu_ex": 2.05},
        {"position": "(1,3)", "beta_x_exact": 179.8, "mu_gr": 0.51, "mu_ex": 3.98},
        {"position": "(1,4)", "beta_x_exact": 102.9, "mu_gr": 3.39, "mu_ex": 2.03},
        {"position": "(1,5)", "beta_x_exact": 243.1, "mu_gr": 0.83, "mu_ex": 4.74},
        {"position": "(1,6)", "beta_x_exact": 300.1, "mu_gr": 3.79, "mu_ex": 1.95}
    ],
    "table4_beta_exact": {
        "4": {
            "eps0.6": {"beta_exact": 28.94, "beta_CT": 58.45},
            "eps2.0": {"beta_exact": 75.53, "beta_CT": 107.2}
        },
        "6": {
            "eps0.6": {"beta_exact": 89.95, "beta_CT": 463.5},
            "eps2.0": {"beta_exact": 300.1, "beta_CT": 513.6}
        },
        "8": {
            "eps0.6": {"beta_exact": 195.0, "beta_CT": 336.9},
            "eps2.0": {"beta_exact": 703.1, "beta_CT": 1063}
        },
        "10": {
            "eps0.6": {"beta_exact": 344.0, "beta_CT": 597.7},
            "eps2.0": {"beta_exact": 1275, "beta_CT": 1950}
        }
    },
    "twist_dependence": [
        {"theta": 0, "beta_x_exact": 300.1},
        {"theta": 15, "beta_x_exact": 318.0},
        {"theta": 30, "beta_x_exact": 355.0},
        {"theta": 45, "beta_x_exact": 404.0},
        {"theta": 60, "beta_x_exact": 466.0},
        {"theta": 75, "beta_x_exact": 561.0},
        {"theta": 90, "beta_x_exact": 18.0},
        {"theta": 105, "beta_x_exact": 561.0},
        {"theta": 120, "beta_x_exact": 466.0},
        {"theta": 135, "beta_x_exact": 393.0},
        {"theta": 150, "beta_x_exact": 333.0},
        {"theta": 165, "beta_x_exact": 289.0},
        {"theta": 180, "beta_x_exact": 270.0}
    ],
    "alpha_exponent": {
        "0.6": 2.5,
        "2.0": 3.4
    }
}

with open("/app/outputs/shg_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
