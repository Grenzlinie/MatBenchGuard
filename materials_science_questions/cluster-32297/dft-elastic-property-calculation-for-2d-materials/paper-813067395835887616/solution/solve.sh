#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: CDW_binding_energies.json ===
python3 << 'PYEOF' > /app/outputs/CDW_binding_energies.json
import json
data = [
    {"polytype": "1T", "chalcogenide": "S", "supercell": "4x1", "binding_energy_meV": 15.2, "CV_percent": -0.02},
    {"polytype": "1T", "chalcogenide": "S", "supercell": "sqrt13xsqrt13", "binding_energy_meV": 29.8, "CV_percent": -0.06},
    {"polytype": "1T", "chalcogenide": "Se", "supercell": "4x1", "binding_energy_meV": 36.3, "CV_percent": 0.18},
    {"polytype": "1T", "chalcogenide": "Se", "supercell": "3x3", "binding_energy_meV": 1.7, "CV_percent": 0.03},
    {"polytype": "1T", "chalcogenide": "Se", "supercell": "sqrt13xsqrt13", "binding_energy_meV": 55.3, "CV_percent": -0.08},
    {"polytype": "1T", "chalcogenide": "Te", "supercell": "3x1", "binding_energy_meV": 102.9, "CV_percent": -0.22},
    {"polytype": "1T", "chalcogenide": "Te", "supercell": "4x1", "binding_energy_meV": 115.0, "CV_percent": 0.09},
    {"polytype": "1T", "chalcogenide": "Te", "supercell": "3x3", "binding_energy_meV": 121.6, "CV_percent": -0.03},
    {"polytype": "1T", "chalcogenide": "Te", "supercell": "sqrt13xsqrt13", "binding_energy_meV": 94.8, "CV_percent": 0.28},
    {"polytype": "1H", "chalcogenide": "S", "supercell": "3x1", "binding_energy_meV": 3.8, "CV_percent": -0.12},
    {"polytype": "1H", "chalcogenide": "S", "supercell": "3x3", "binding_energy_meV": 3.0, "CV_percent": 0.02},
    {"polytype": "1H", "chalcogenide": "Se", "supercell": "3x1", "binding_energy_meV": 1.3, "CV_percent": 0.13},
    {"polytype": "1H", "chalcogenide": "Se", "supercell": "4x1", "binding_energy_meV": 3.5, "CV_percent": 0.04},
    {"polytype": "1H", "chalcogenide": "Se", "supercell": "3x3", "binding_energy_meV": 3.5, "CV_percent": 0.10},
    {"polytype": "1H", "chalcogenide": "Se", "supercell": "sqrt13xsqrt13", "binding_energy_meV": 2.9, "CV_percent": 0.08},
    {"polytype": "1H", "chalcogenide": "Te", "supercell": "4x1", "binding_energy_meV": 5.1, "CV_percent": -0.03},
    {"polytype": "1H", "chalcogenide": "Te", "supercell": "3x3", "binding_energy_meV": 5.0, "CV_percent": -0.04},
    {"polytype": "1H", "chalcogenide": "Te", "supercell": "sqrt13xsqrt13", "binding_energy_meV": 10.8, "CV_percent": -0.10}
]
print(json.dumps(data, indent=2))
PYEOF

# === solve block: Ta_Ta_distances.json ===
python3 << 'PYEOF' > /app/outputs/Ta_Ta_distances.json
import json
data = [
    {"chalcogenide": "S", "supercell": "4x1", "site_pair": "AB", "distance_A": 3.282, "percent_change": -0.69},
    {"chalcogenide": "S", "supercell": "4x1", "site_pair": "BC", "distance_A": 3.113, "percent_change": -5.82},
    {"chalcogenide": "S", "supercell": "4x1", "site_pair": "CD", "distance_A": 3.281, "percent_change": -0.72},
    {"chalcogenide": "S", "supercell": "4x1", "site_pair": "AD", "distance_A": 3.547, "percent_change": 7.34},
    {"chalcogenide": "S", "supercell": "sqrt13xsqrt13", "site_pair": "AB", "distance_A": 3.120, "percent_change": -5.59},
    {"chalcogenide": "S", "supercell": "sqrt13xsqrt13", "site_pair": "BC", "distance_A": 3.210, "percent_change": -2.87},
    {"chalcogenide": "S", "supercell": "sqrt13xsqrt13", "site_pair": "AC", "distance_A": 5.510, "percent_change": -3.74},
    {"chalcogenide": "Se", "supercell": "4x1", "site_pair": "AB", "distance_A": 3.346, "percent_change": -2.04},
    {"chalcogenide": "Se", "supercell": "4x1", "site_pair": "BC", "distance_A": 3.131, "percent_change": -8.32},
    {"chalcogenide": "Se", "supercell": "4x1", "site_pair": "CD", "distance_A": 3.346, "percent_change": -2.04},
    {"chalcogenide": "Se", "supercell": "4x1", "site_pair": "AD", "distance_A": 3.801, "percent_change": 11.29},
    {"chalcogenide": "Se", "supercell": "sqrt13xsqrt13", "site_pair": "AB", "distance_A": 3.120, "percent_change": -8.64},
    {"chalcogenide": "Se", "supercell": "sqrt13xsqrt13", "site_pair": "BC", "distance_A": 3.156, "percent_change": -7.59},
    {"chalcogenide": "Se", "supercell": "sqrt13xsqrt13", "site_pair": "AC", "distance_A": 5.603, "percent_change": -5.28},
    {"chalcogenide": "Te", "supercell": "3x1", "site_pair": "AB", "distance_A": 3.190, "percent_change": -10.66},
    {"chalcogenide": "Te", "supercell": "3x1", "site_pair": "BC", "distance_A": 3.190, "percent_change": -10.66},
    {"chalcogenide": "Te", "supercell": "3x1", "site_pair": "CD", "distance_A": 4.371, "percent_change": 22.42},
    {"chalcogenide": "Te", "supercell": "3x3", "site_pair": "AB", "distance_A": 3.223, "percent_change": -9.73},
    {"chalcogenide": "Te", "supercell": "3x3", "site_pair": "BC", "distance_A": 3.099, "percent_change": -13.91},
    {"chalcogenide": "Te", "supercell": "3x3", "site_pair": "CD", "distance_A": 3.389, "percent_change": -5.08},
    {"chalcogenide": "Te", "supercell": "3x3", "site_pair": "AD", "distance_A": 5.939, "percent_change": -3.97},
    {"chalcogenide": "Te", "supercell": "3x3", "site_pair": "AC", "distance_A": 3.238, "percent_change": -9.30},
    {"chalcogenide": "Te", "supercell": "4x1", "site_pair": "AB", "distance_A": 3.273, "percent_change": -8.35},
    {"chalcogenide": "Te", "supercell": "4x1", "site_pair": "BC", "distance_A": 3.295, "percent_change": -7.72},
    {"chalcogenide": "Te", "supercell": "4x1", "site_pair": "CD", "distance_A": 3.273, "percent_change": -8.35},
    {"chalcogenide": "Te", "supercell": "4x1", "site_pair": "AD", "distance_A": 4.370, "percent_change": 22.38},
    {"chalcogenide": "Te", "supercell": "sqrt13xsqrt13", "site_pair": "AB", "distance_A": 3.233, "percent_change": -9.47}
]
print(json.dumps(data, indent=2))
PYEOF
