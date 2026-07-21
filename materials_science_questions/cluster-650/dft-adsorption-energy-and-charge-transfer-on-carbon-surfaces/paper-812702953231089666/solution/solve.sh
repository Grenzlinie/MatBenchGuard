#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json
data = [
    {"system": "coronene", "E_ads": None, "Eg": 7.36, "delta_Eg_percent": None, "QT": None, "HOMO": -7.20, "LUMO": 0.16, "d": None},
    {"system": "Al-coronene", "E_ads": None, "Eg": 6.85, "delta_Eg_percent": None, "QT": None, "HOMO": -6.86, "LUMO": -0.01, "d": None},
    {"system": "A1_EF0", "E_ads": -47.71, "Eg": 6.39, "delta_Eg_percent": -6.72, "QT": -0.22, "HOMO": -6.24, "LUMO": 0.15, "d": 1.99},
    {"system": "T1_EF0", "E_ads": -42.63, "Eg": 6.04, "delta_Eg_percent": -11.82, "QT": -0.32, "HOMO": -6.03, "LUMO": 0.01, "d": 1.91},
    {"system": "G1_EF0", "E_ads": -53.19, "Eg": 6.37, "delta_Eg_percent": -7.01, "QT": -0.22, "HOMO": -5.73, "LUMO": 0.64, "d": 1.88},
    {"system": "C1_EF0", "E_ads": -51.69, "Eg": 5.63, "delta_Eg_percent": -17.81, "QT": -0.33, "HOMO": -5.94, "LUMO": -0.31, "d": 1.89},
    {"system": "A1_EF1e-2", "E_ads": -63.39, "Eg": 6.30, "delta_Eg_percent": -3.82, "QT": -0.34, "HOMO": -6.28, "LUMO": 0.02, "d": 1.95},
    {"system": "T1_EF1e-2", "E_ads": -67.36, "Eg": 5.93, "delta_Eg_percent": -9.47, "QT": -0.39, "HOMO": -6.12, "LUMO": -0.19, "d": 1.86},
    {"system": "G1_EF1e-2", "E_ads": -68.98, "Eg": 6.23, "delta_Eg_percent": -4.89, "QT": -0.43, "HOMO": -5.85, "LUMO": 0.38, "d": 1.82},
    {"system": "C1_EF1e-2", "E_ads": -67.11, "Eg": 5.55, "delta_Eg_percent": -15.27, "QT": -0.39, "HOMO": -5.31, "LUMO": 0.24, "d": 1.85},
    {"system": "A1_EF2e-2", "E_ads": -87.79, "Eg": 5.15, "delta_Eg_percent": -19.15, "QT": -0.45, "HOMO": -6.05, "LUMO": -0.90, "d": 1.92},
    {"system": "T1_EF2e-2", "E_ads": -89.66, "Eg": 5.58, "delta_Eg_percent": -12.40, "QT": -0.42, "HOMO": -6.23, "LUMO": -0.65, "d": 1.82},
    {"system": "G1_EF2e-2", "E_ads": -89.08, "Eg": 5.20, "delta_Eg_percent": -18.37, "QT": -0.48, "HOMO": -4.71, "LUMO": -0.49, "d": 1.80},
    {"system": "C1_EF2e-2", "E_ads": -89.56, "Eg": 5.39, "delta_Eg_percent": -15.38, "QT": -0.47, "HOMO": -5.98, "LUMO": -0.59, "d": 1.81}
]
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
