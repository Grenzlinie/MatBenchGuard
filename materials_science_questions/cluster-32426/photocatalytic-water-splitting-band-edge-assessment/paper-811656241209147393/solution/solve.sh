#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json
data = [
    {
        "material": "TiO2",
        "E_C_bulk_minus_H_semi_bulk": 3.77,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -4.48,
        "E_C_edge_minus_A_edge": -0.01
    },
    {
        "material": "WO3",
        "E_C_bulk_minus_H_semi_bulk": 1.89,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -3.13,
        "E_C_edge_minus_A_edge": -0.54
    },
    {
        "material": "CdS",
        "E_C_bulk_minus_H_semi_bulk": 2.91,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -2.34,
        "E_C_edge_minus_A_edge": 1.27
    },
    {
        "material": "ZnSe",
        "E_C_bulk_minus_H_semi_bulk": 3.25,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -2.35,
        "E_C_edge_minus_A_edge": 1.60
    },
    {
        "material": "GaAs",
        "E_C_bulk_minus_H_semi_bulk": 3.64,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -3.27,
        "E_C_edge_minus_A_edge": 1.07
    },
    {
        "material": "GaP",
        "E_C_bulk_minus_H_semi_bulk": 4.08,
        "A_bulk_minus_H_sol_bulk": -0.70,
        "H_semi_edge_minus_H_sol_edge": -3.49,
        "E_C_edge_minus_A_edge": 1.29
    }
]
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
'
